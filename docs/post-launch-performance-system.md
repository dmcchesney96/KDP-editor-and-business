# KDP Post-Launch Performance System

## Objective
Measure **real** outcomes, diagnose discoverability and conversion without inventing unavailable organic traffic, and make one testable improvement per review. New titles receive a launch baseline and a release-calendar entry immediately.

## Operating loop
1. **Capture catalog** — `kdp-portfolio-tracker` records each title *per format* with evidence of status, submitted/live date, market, ASIN, current price/metadata/cover version, and review trigger.
2. **Collect actual reports** — `kdp-report-ingestion` imports KDP Orders/royalties and optional Amazon Ads exports to **private storage**, preserving original report, marketplace, currency, date range and attribution window. No KDP general organic page-view data.
3. **Check discoverability** — `kdp-discovery-diagnostic` validates live listing quality and logs spot-check Amazon buyer searches with timestamps, locations and search context. Distinguish paid and organic placement; rankings are variable.
4. **Make one decision** — `kdp-growth-decision-review` provides `WAIT/COLLECT`, `FIX TECHNICAL`, `TEST DISCOVERABILITY`, `TEST LISTING`, `TEST ADS (OPTIONAL)`, `SCALE` or `PAUSE`. Prioritize expected reader value and economics, not vanity metrics.
5. **Run an experiment** — existing `kdp-listing-experiment-review` logs hypothesis, one changed variable, before/after snapshots, comparison window, sample sufficiency, stop/cost guardrail, measured outcome and next learning.

## Initial cadence
- Day 0: capture final listing/version and approval for distribution; only when actually live mark 'live'.
- Day 3: confirm retail discoverability; Amazon's standard search/metadata propagation window can be up to 72h.
- Day 14: early observation, **not** an automatic failure or success verdict.
- Day 30: decision review; use comparable report and test periods.
- Every month: portfolio review with book-by-book next actions, profit/royalty context, series cross-selling, competing priorities.

An edit changes the baseline and may restart the relevant observation window. Reports can lag; align windows.

## Publishing cadence
Source checked 2026-10-08: https://kdp.amazon.com/en_US/help/topic/G202172740

KDP limits **new title creation** to up to two titles per book format per week and **first-time submission** to up to two titles per book format per week. These are distinct; count each format separately. Both reset **Sunday 00:00 UTC**. Previously submitted updates do not count as first-time submissions; first submissions of saved drafts do. Always verify current KDP policy and owner account status before a new upload. During Eastern Daylight Time, Sunday 00:00 UTC is **Saturday 8:00 p.m. Eastern**; during Eastern Standard Time it is Saturday 7:00 p.m.

## Dashboard — private copy template, do not populate in public repo
```csv
book_id,title,series,format,marketplace,asin,first_submitted_at,live_at,status,status_source_date,price,currency,metadata_version,cover_version,last_report_end,last_review_at,next_review_at,next_action
```
```csv
experiment_id,book_id,start_date,end_date,changed_variable,version_before,version_after,hypothesis,measured_metric,baseline_window,test_window,result,confidence,next_action
```

Core private views:
- **Portfolio**: total live, pending review, blocked, next scheduled releases; per-format creation and submission slots.
- **Sales**: orders/units, refunds, estimated royalties, marketplace and period (do not interpret zero orders as zero visits).
- **Ads**, if authorized: impressions, clicks, CTR, CPC, spend, attributed orders, ad sales, ACoS and estimated royalty-after-ad contribution by consistent grain/attribution window.
- **Keywords**: current KDP metadata, market-observed phrases, paid search terms *with clicks*, test history, next query to verify.
- **Experiments**: a versioned test register with cost guardrails and named decisions.

## Baseline questions for a 0-sales launch
1. Is it truly live on Amazon in the intended marketplace and purchasable in the intended print format?
2. Have at least 72 hours passed since the product went live or metadata changed?
3. Does the title/cover/description clearly tell the intended reader what the actual book does?
4. What specific high-intent buyer searches are relevant, and what *repeatable observations* exist for them?
5. Are there paid campaign impressions/clicks? If **not running ads**, paid traffic is unknown/not applicable, while organic traffic is unmeasured.
6. Which **one** test (if any) is the most informative within a safe budget? What will count as a useful result?

No claim of 0 page views is supported by ordinary KDP royalty reports.

## Rules
- Do not commit real owner reports, passwords, detailed private revenue, tokens, spending, or confidential keyword strategies to public GitHub.
- The GitHub repo supplies instructions; Google Drive/Sheets can hold private raw exports and live dashboard, if authorized.
- Manual account data entry, report export, listing edits, ad launches, and spending require appropriate access/approval.
- Do not add attributed Ads orders to total KDP units (overlap); ad sales revenue is not royalty; organic conversion cannot be computed from KDP reports alone.
- Review official current KDP and Ads guidance before enforcing new numeric policy restrictions or attribution definitions.

## Official references
- KDP new title creation/submission limits: https://kdp.amazon.com/en_US/help/topic/G202172740
- KDP reporting: https://kdp.amazon.com/en_US/help/topic/GVTTXHKHVPAPBEDQ
- KDP live listing/update timelines: https://kdp.amazon.com/en_US/help/topic/G202173620
- KDP updating listing details: https://kdp.amazon.com/en_US/help/topic/G200736410
- Amazon Ads book reporting: https://advertising.amazon.com/en-us/library/guides/book-advertising-reporting/
