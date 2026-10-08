#!/usr/bin/env python3
"""Evidence-aware KDP portfolio review. Only standard-library dependencies."""
import argparse
import csv
import datetime as dt
import json
import math
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ORDER_FIELDS = {"date", "book_id", "marketplace", "paid_units", "free_units"}
AD_FIELDS = {"date", "book_id", "marketplace", "currency", "impressions", "clicks", "orders", "sales", "spend"}
STATUSES = {"draft", "in_review", "publishing", "live", "blocked", "unpublished"}


class DataError(ValueError):
    pass


def date_value(value, label):
    try:
        return dt.date.fromisoformat(str(value))
    except (ValueError, TypeError):
        raise DataError(f"{label}: expected YYYY-MM-DD; got {value!r}")


def nonnegative(value, label, integer=False):
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        raise DataError(f"{label}: invalid number {value!r}")
    if not result.is_finite() or result < 0 or (integer and result != result.to_integral_value()):
        raise DataError(f"{label}: expected nonnegative {'integer' if integer else 'number'}; got {value!r}")
    return int(result) if integer else result


def read_csv(path, fields):
    try:
        with open(path, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or not fields.issubset(set(reader.fieldnames)):
                raise DataError(f"{path}: required columns missing: {sorted(fields - set(reader.fieldnames or []))}")
            result = []
            for i, row in enumerate(reader, 2):
                if None in row:
                    raise DataError(f"{path}:{i}: unexpected extra columns")
                if any(v is None for v in row.values()):
                    raise DataError(f"{path}:{i}: missing cell")
                result.append((i, row))
            return result
    except OSError as e:
        raise DataError(f"{path}: {e}")


def load_catalog(path):
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise DataError(f"{path}: {e}")
    books = payload.get("books")
    if not isinstance(books, list) or not books:
        raise DataError("catalog must have nonempty 'books' array")
    found = {}
    for b in books:
        for f in ("id", "working_title", "format", "marketplace", "status"):
            if not isinstance(b.get(f), str) or not b[f].strip():
                raise DataError(f"catalog entry missing {f}")
        if b["id"] in found:
            raise DataError(f"duplicate catalog book_id: {b['id']}")
        if b["status"] not in STATUSES:
            raise DataError(f"{b['id']}: unknown status {b['status']}")
        if b.get("first_live_date") is not None:
            date_value(b["first_live_date"], f"{b['id']} first_live_date")
        found[b["id"]] = b
    return found


def rate(num, den):
    return round(float(num / den), 6) if den else None


def analyze(catalog_path, as_of, orders_path=None, orders_start=None, orders_end=None,
            orders_complete=False, orders_marketplace=None, orders_format=None,
            ads_path=None, ads_type=None, attribution_window=None):
    today = date_value(as_of, "as_of")
    books = load_catalog(catalog_path)

    if orders_complete and not (orders_path and orders_start and orders_end and orders_marketplace and orders_format):
        raise DataError("--orders-complete needs --orders, start, end, marketplace and format")
    if any((orders_start, orders_end, orders_marketplace, orders_format)) and not orders_path:
        raise DataError("order coverage options require --orders")
    if orders_path and not (orders_start and orders_end):
        raise DataError("--orders needs --orders-start and --orders-end to bound data")
    if orders_path and (bool(orders_marketplace) != bool(orders_format)):
        raise DataError("provide both --orders-marketplace and --orders-format or neither")
    if bool(ads_path) != bool(ads_type):
        raise DataError("--ads requires --ads-type (and vice versa)")
    if ads_path and not attribution_window:
        raise DataError("--ads requires --attribution-window from the source export")

    start = date_value(orders_start, "orders_start") if orders_start else None
    end = date_value(orders_end, "orders_end") if orders_end else None
    if start and (start > end or end > today):
        raise DataError("order coverage interval must be ordered and not in the future")

    processed = defaultdict(lambda: {"paid_units": 0, "free_units": 0, "rows": 0})
    if orders_path:
        for line, row in read_csv(orders_path, ORDER_FIELDS):
            context = f"{orders_path}:{line}"
            bid = row["book_id"].strip()
            if bid not in books:
                raise DataError(f"{context}: unknown book_id {bid!r}")
            if row["marketplace"] != books[bid]["marketplace"]:
                raise DataError(f"{context}: marketplace mismatches catalog for {bid}")
            if orders_marketplace and row["marketplace"] != orders_marketplace:
                raise DataError(f"{context}: marketplace outside declared export scope")
            if orders_format and books[bid]["format"] != orders_format:
                raise DataError(f"{context}: format outside declared export scope")
            when = date_value(row["date"], context)
            if not start <= when <= end:
                raise DataError(f"{context}: date outside declared orders window")
            for col in ("paid_units", "free_units"):
                processed[bid][col] += nonnegative(row[col], f"{context} {col}", True)
            processed[bid]["rows"] += 1

    paid = defaultdict(lambda: {
        "impressions": 0, "clicks": 0, "orders": 0,
        "sales": Decimal(0), "spend": Decimal(0), "currency": None,
        "rows": 0, "term_clicks": defaultdict(int)
    })
    if ads_path:
        for line, row in read_csv(ads_path, AD_FIELDS):
            context = f"{ads_path}:{line}"
            bid = row["book_id"].strip()
            if bid not in books:
                raise DataError(f"{context}: unknown book_id {bid!r}")
            if row["marketplace"] != books[bid]["marketplace"]:
                raise DataError(f"{context}: marketplace mismatches catalog for {bid}")
            when = date_value(row["date"], context)
            if when > today:
                raise DataError(f"{context}: future ad report date")
            currency = row["currency"].strip().upper()
            if len(currency) != 3 or not currency.isalpha():
                raise DataError(f"{context}: invalid currency")
            p = paid[bid]
            if p["currency"] and p["currency"] != currency:
                raise DataError(f"{context}: mixed currencies for {bid}")
            p["currency"] = currency
            numbers = {k: nonnegative(row[k], f"{context} {k}", k in ("impressions", "clicks", "orders"))
                       for k in ("impressions", "clicks", "orders", "sales", "spend")}
            if numbers["clicks"] > numbers["impressions"]:
                raise DataError(f"{context}: clicks exceed impressions")
            for key, value in numbers.items():
                p[key] += value
            p["rows"] += 1
            if ads_type == "search_terms":
                term = (row.get("search_term") or "").strip()
                if not term:
                    raise DataError(f"{context}: search_terms report requires search_term")
                p["term_clicks"][term] += numbers["clicks"]

    results = []
    for bid, b in books.items():
        o = processed[bid]
        in_scope = bool(orders_complete and b["marketplace"] == orders_marketplace and b["format"] == orders_format)
        observed = o["rows"] > 0
        units = o["paid_units"] if observed or in_scope else None
        free = o["free_units"] if observed or in_scope else None
        p = paid[bid]
        has_ads = p["rows"] > 0
        ads = None
        if has_ads:
            ads = {
                "report_type": ads_type,
                "attribution_window": attribution_window,
                "currency": p["currency"],
                "impressions": p["impressions"],
                "clicks": p["clicks"],
                "attributed_orders": p["orders"],
                "attributed_sales": str(p["sales"]),
                "spend": str(p["spend"]),
                "ad_ctr": rate(p["clicks"], p["impressions"]),
                "ad_cpc": rate(p["spend"], p["clicks"]),
                "ad_order_per_click": rate(p["orders"], p["clicks"]),
                "ad_acos": rate(p["spend"], p["sales"]),
                "top_clicked_terms": sorted(
                    [{"term": term, "clicks": clicks} for term, clicks in p["term_clicks"].items()],
                    key=lambda x: (-x["clicks"], x["term"]))[:10] if ads_type == "search_terms" else []
            }

        if b["status"] != "live":
            diagnosis = "PENDING_REVIEW" if b["status"] in ("in_review", "publishing") else "NOT_LIVE"
            action = "Verify status and ASIN when available; do not diagnose conversion yet."
        elif units is None:
            diagnosis = "INSUFFICIENT_ACCOUNT_DATA"
            action = "Get a complete covered KDP Orders export and inspect the live listing; organic views are unavailable."
        elif units > 0:
            diagnosis = "MEASURABLE_TRACTION"
            action = "Reconcile royalties by marketplace, then review qualified traffic and contribution after any ad spend."
        elif ads and ads_type == "advertised_product" and ads["impressions"] >= 1000 and ads["clicks"] == 0:
            diagnosis = "AD_ENGAGEMENT_WEAK"
            action = "Review targeting relevance, mobile cover thumbnail and title before a one-variable test."
        elif ads and ads_type == "advertised_product" and ads["clicks"] >= 20 and ads["attributed_orders"] == 0:
            diagnosis = "AD_CONVERSION_UNCERTAIN"
            action = "Audit price, sample, description, targeting and attribution lag; not enough to prove causality."
        elif ads and ads_type == "advertised_product" and ads["impressions"] < 100:
            diagnosis = "AD_DISCOVERY_WEAK"
            action = "Check campaign eligibility, bidding, budget and relevance; low ad delivery is not an organic reach measure."
        else:
            diagnosis = "NO_CONFIRMED_PRINT_SHIPMENTS"
            action = "Verify indexing and listing completeness. Discovery remains unknown without suitable ad evidence."
        results.append({
            "book_id": bid, "title": b["working_title"], "format": b["format"],
            "marketplace": b["marketplace"], "status": b["status"],
            "asin": b.get("asin"), "first_live_date": b.get("first_live_date"),
            "kdp_paid_processed_units": units, "kdp_free_processed_units": free,
            "kdp_source": ("complete_scope_export" if in_scope else "observed_rows_only" if observed else "not_measured"),
            "ads": ads, "diagnosis": diagnosis, "next_action": action
        })
    return {
        "as_of": str(today), "catalog_source": str(catalog_path),
        "orders_source": str(orders_path) if orders_path else None,
        "orders_coverage": {"start": str(start), "end": str(end), "complete": orders_complete,
                            "marketplace": orders_marketplace, "format": orders_format} if orders_path else None,
        "ads_source": str(ads_path) if ads_path else None,
        "ads_type": ads_type,
        "caveats": [
            "KDP processed print orders generally appear after shipment, not at checkout.",
            "Organic page views, impressions and conversion rates are not provided by ordinary KDP reports.",
            "Amazon Ads orders may overlap KDP units; do not add them together.",
            "Amazon Ads search-terms reports include click-associated terms only; not full campaign impression coverage.",
            "A before-after listing change is not a controlled causal experiment."
        ], "books": results
    }


def render_markdown(data):
    def show(v):
        return "unknown" if v is None else str(v)
    lines = [f"# KDP portfolio review — {data['as_of']}", "",
             "| Book | Status | Processed paid units | Ad impressions | Ad clicks | Diagnosis |",
             "|---|---|---:|---:|---:|---|"]
    for b in data["books"]:
        a = b["ads"]
        lines.append(f"| {b['title'].replace('|', '/')} | {b['status']} | "
                     f"{show(b['kdp_paid_processed_units'])} | "
                     f"{show(a['impressions'] if a else None)} | "
                     f"{show(a['clicks'] if a else None)} | {b['diagnosis']} |")
    lines.extend(["", "## Recommended next steps", ""])
    for b in data["books"]:
        lines.extend([f"**{b['title']}** — {b['next_action']}",
                      f"Source: KDP {b['kdp_source']}; Ads {'reported' if b['ads'] else 'not measured'}.", ""])
    lines.extend(["## Evidence limitations", ""])
    lines.extend([f"- {c}" for c in data["caveats"]])
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--as-of", required=True, help="YYYY-MM-DD")
    parser.add_argument("--orders", help="Private normalized KDP Orders CSV")
    parser.add_argument("--orders-start")
    parser.add_argument("--orders-end")
    parser.add_argument("--orders-complete", action="store_true", help="Affirm complete book/format/marketplace coverage")
    parser.add_argument("--orders-marketplace")
    parser.add_argument("--orders-format")
    parser.add_argument("--ads", help="Private normalized Ads CSV")
    parser.add_argument("--ads-type", choices=("advertised_product", "search_terms"))
    parser.add_argument("--attribution-window", help="Verbatim attribution window from Ads source")
    parser.add_argument("--json-out", help="Optional path outside public repository")
    parser.add_argument("--markdown-out", help="Optional path outside public repository")
    args = parser.parse_args(argv)
    try:
        result = analyze(args.catalog, args.as_of, args.orders, args.orders_start, args.orders_end,
                         args.orders_complete, args.orders_marketplace, args.orders_format,
                         args.ads, args.ads_type, args.attribution_window)
        markdown = render_markdown(result)
        if args.json_out:
            Path(args.json_out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        if args.markdown_out:
            Path(args.markdown_out).write_text(markdown, encoding="utf-8")
        print(markdown)
        return 0
    except (DataError, OSError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
