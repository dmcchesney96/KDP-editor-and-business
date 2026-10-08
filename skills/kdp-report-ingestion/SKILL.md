---
name: kdp-report-ingestion
description: Import owner-provided KDP Reports and Amazon Ads exports into a private, provenance-preserving book performance dataset; validate fields without confusing organic traffic with ad metrics.
---

# KDP Report Ingestion

## Purpose
Turn real, authorized data into a dependable review package. This skill handles `EXPORTS -> VALIDATED TABLES + METRIC DEFINITIONS + DATA-QUALITY FLAGS`, not account login or analysis of winning experiments.

## Inputs and collection
Accept KDP Orders/royalty/KENP reports, Amazon Ads Sponsored Products campaign/targeting/search term/advertised-product reports, and owner-recorded promotion links or manual search observations. First capture title/ASIN/format, marketplace, currency, period boundaries, export generated-at timestamp, ad attribution window, and data as-of timestamp. Never infer page views or search impressions from KDP order or royalty reports.

Retrieve only reports the owner authorizes and can access. If direct account access is not available, request an export and return a precise missing-data list. Do not imply an automatic KDP analytics API is connected.

## Canonical private datasets
1. `catalog`: stable book ID, ASIN, format, marketplace, version and publication state (see `kdp-portfolio-tracker`).
2. `kdp_daily`: date, book ID, marketplace, format, ordered units, refunded units if reported, KENP if applicable, royalties, currency, source report/filters. If a report provides only a period total, retain period granularity instead of inventing daily rows.
3. `ads_daily`: date/range, book ID, campaign, ad group, target/search term (depending on report grain), impressions, clicks, spend, attributed orders, attributed sales, currency, attribution window, source.
4. `listing_change_log`: book, change ID, variable, before and after, dates submitted and visible, hypothesis, baseline/test windows.
5. `observations`: manually logged Amazon search query and position, marketplace, timestamp, device/incognito state, method; marked `MARKET_OBSERVATION`.

Never sum ads campaign, targeting, and search-term exports together: these can report **the same traffic at different aggregations**. Deduplicate overlapping time windows, avoid double-counting ad-attributed orders with total KDP units, separate royalties from ad-attributed gross sales, and reject mixed currencies/markets or mismatched attribution windows. Data should include missingness flags; absent metric means `null/unknown`, not zero.

## Validations
- Source and date range named; unique stable identifiers and listing ownership reconciled.
- Numeric amounts nonnegative unless an explicit refund/adjustment column; ad impressions >= clicks (check source anomalies).
- Totals reconciled to source where feasible; snapshots append rather than overwrite.
- Aggregate rates use total numerators / total denominators. Zero denominators -> undefined, not 0%.
- Retain exported originals privately with hashes where feasible. Never fabricate historical report rows.
- Explain order timing, print reporting delays, refunds, and ad attribution lag where material.

## Existing code and handoff
Reuse `skills/kdp-listing-experiment-review/references/report-schema.md` and `scripts/summarize_ads.py` for a validated **single-grain** normalized Ads CSV; do not build a competing calculator. Route interpretation to `kdp-growth-decision-review`, controlled tests to `kdp-listing-experiment-review`.

## Output contract
`SOURCES/PROVENANCE`, `VALIDATION RESULTS`, `RECONCILED METRICS`, `MISSING DATA`, `PRIVATE STORAGE DESTINATIONS`, `READY FOR ANALYSIS?`. This skill does not authorize bids, budget increases, listing edits, or ad creation.
