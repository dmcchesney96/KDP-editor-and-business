# Evidence and import contract

## Source hierarchy
1. KDP account export (processed print orders / royalties); 2. Amazon Ads account export (paid traffic/attributed orders); 3. dated live listing screenshot/observations; 4. owner self-report; 5. estimates and hypotheses. Do not confuse them.

## Normalized KDP Orders CSV (private)
Required header: `date,book_id,marketplace,paid_units,free_units`. Example data row (illustration only): `2026-10-08,foundations-1,Amazon.com,1,0`. `book_id` links to `portfolio/catalog.json`; `date` is marketplace-local shipment/processed order date for paperback and hardcover. Do NOT manufacture zero-rows. Build from the actual KDP Orders export, preserving the original private file and the mapping record.

If a complete **All Books** export includes zero orders (no data rows for certain titles), its coverage can only be asserted through **both** `--orders-complete` and `--orders-start/--orders-end`, and the operator must have checked that the export really covers all book IDs, formats and marketplaces shown in the catalog. Otherwise leave absent metrics unknown.

Do not combine order dates/processed units directly with royalty transaction dates or treat a lack of shipped units as proof of no checkout purchases.

## Normalized Sponsored Products report CSV (private)
Required header: `date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend`; optional `search_term` (for search terms report). Dates, identifiers, and currency must be present. `orders` is **ad-attributed orders**, not KDP orders or attributed units. `sales` is ads-attributed gross sales in currency, not royalty. Report types must be declared with `--ads-type advertised_product` or `--ads-type search_terms`, and attribution window with `--attribution-window` from source settings. Normalized figures should retain the source's time grain; if source is an aggregate window, do not fake daily dates. In that situation, use the existing listing-experiment-review skill/manual review until a valid daily export is prepared.

Never merge targeting, search-terms, and advertised-product rows and sum them; they overlap. Search-terms report only covers clicked search terms; displayed impressions there are not a complete traffic base.

## Reproducibility and safety
- Keep a private evidence manifest: `source_filename,downloaded_at,source_app,report_type,account,marketplace,format,currency,window_start,window_end,attribution_window,filters,normalization_notes,source_hash`.
- No account credentials or personal financial exports inside this public repository, commit history, or GitHub Issues.
- The script accepts only valid normalized CSV; reject nonnumeric/negative counts, invalid dates, unknown book IDs, wrong marketplaces, missing columns, and mixed currencies.
- The resulting JSON/Markdown report is a descriptive snapshot, not a claim of causal lift. Keep output outside the repo if it exposes private sales data.
- If the operator lacks a full export, return `unknown` and specify the missing report. Never print `0 impressions` merely because no ad export was provided.

## Metric definitions
- KDP processed paid units = sum `paid_units` (shipment-stage for print).
- Ads CTR = sum clicks / sum impressions, not average daily CTR.
- Ads CPC = sum spend / sum clicks.
- Ads attributed-order-per-click = sum attributed orders / sum clicks (may represent multiple orders per click); not organic conversion rate.
- Ads ACoS = sum spend / sum attributed sales.
- If denominator 0, metric = `null` (undefined); if no report, all corresponding totals and rates = `null` (unknown).
- Net royalty and contribution margin require actual cost/royalty evidence and should be analyzed with `kdp-listing-experiment-review`, not inferred from sales price.
