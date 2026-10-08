---
name: kdp-portfolio-optimization
description: Run a grounded post-publication health check across KDP titles, reconcile real KDP Orders and Amazon Ads reports, audit keyword/listing discoverability, and recommend reversible one-variable experiments. Activate for "how are my books doing", zero sales, KDP portfolio analytics, listing health checks, keyword effectiveness, launch monitoring, and next listing tests.
---

# KDP Portfolio Performance & Optimization

## Goal and operating rules
Turn **observed account exports + verifiable listing evidence + product intent** into a small, ranked action plan. This is the post-launch orchestrator, **not** a replacement for `kdp-listing-experiment-review`, `kdp-keyword-metadata-optimizer`, `kdp-competitor-benchmark`, `kdp-category-positioning`, `kdp-cover-strategy`, `kdp-product-economics-planner`, or `kdp-listing-copywriter`. Call those specialist skills for a concrete subtask.

- Treat GitHub as reusable instructions/source-controlled public catalog; **never** claim it has direct access to private KDP/Ads analytics.
- Never infer organic impressions, page views, organic CTR, or organic conversion from KDP sales, BSR, keyword suggestions, or Amazon public listings.
- Do not treat "zero sales after a week" as proof of bad keywords. Print orders are reported after shipment, and launch/indexing timing varies.
- Never equate ads-attributed sales/orders with incremental sales; do not add ad orders to KDP units (overlap).
- Ads search-term report is **click-associated only**, so it is not a complete record of search impressions or campaign discovery.
- Separate evidence classes: `KDP_EXPORT`, `ADS_EXPORT`, `LIVE_PAGE_OBSERVATION`, `OFFICIAL_RULE`, `OWNER_REPORT`, `HYPOTHESIS`, and `RECOMMENDATION`.
- Never launch ads, change live listings, publish titles, purchase services, or make budget commitments without explicit permission for that action. Recommend a test first, then request approval.
- Keep account exports, transaction data and spending private (Drive/private local workspace); this repository is **public**.
- Do not solicit artificial reviews or guaranteed sales; observe Amazon content/Ads policies.

## Workflow

### 1. Inventory and source lock
Read `portfolio/catalog.json` as a *working*, owner-reported registry, not a live KDP mirror. Verify each book's exact live title, format, ASIN/ISBN, marketplace, status, first-live date, price, royalty estimate, and Amazon URL when evidence is available. Preserve unknown values as `null`. Different formats have different identifiers and should be separate catalog rows. Never silently guess publication dates or ASINs.

Create an evidence ledger for each run: timestamp; snapshot/export time; report title, marketplace, currency, format, date range, report type, attribution window; filters and file location; which findings are owner-reported or directly observed. Do **not** add rows of fake zero sales to represent missing reports.

### 2. Data capture
Follow [report-contract.md](references/report-contract.md). Ask for/download (when authorized) a KDP **Orders** report for the selected marketplace/book/format window and an Amazon Ads **advertised-product** report if ads are active. For search-term analysis also get **search-term** and **targeting** reports separately, without summing them together.

Use `scripts/review_portfolio.py` on normalized exports; it validates identifiers, dates, nonnegative numbers, currencies and coverage claims. The script reports *missing* until an actual complete report and covered interval are affirmed; exports are never fabricated. KDP orders are processed/shipped print books, not real-time purchases. Compare royalty reports separately, matching currency, marketplace, units, and shipment periods. For ad effectiveness hand the report to `kdp-listing-experiment-review` and its existing `summarize_ads.py` if appropriate.

### 3. Pre-change listing health review (independent of sales)
For each live title, record in a dated private observation log:
- exact ASIN/product URL and marketplace, whether buyable, price, format, cover thumbnail legibility on mobile;
- whether exact title / ASIN is findable, whether reader-intent search results look relevant, whether categories/age are accurate; note personalization, search location and snapshot time;
- visible description, subtitle, samples/Look Inside where eligible and available, A+ content status, reviews and customer objections when legitimate;
- 3–5 relevant competitor examples with verified prices, positioning, visual differentiation, evidence date;
- user-benefit fit with actual interior content, not just algorithm optimization.

Amazon autocomplete reflects suggested phrases, **not numeric keyword search volume**. A search result position is an unstable observational snapshot, **not measured rank performance**. Missing Look Inside is not always a listing error (special limitations can apply to low-content books).

### 4. Diagnose without overclaiming
Use [experiment-playbook.md](references/experiment-playbook.md) and report one of:
- `PENDING_REVIEW`: title not live; no conversion diagnosis.
- `INSUFFICIENT_ACCOUNT_DATA`: missing exported or covered sales data.
- `NO_CONFIRMED_PRINT_SHIPMENTS`: complete report says zero processed units; discovery still unknown.
- `AD_DISCOVERY_WEAK`: *ad data* show weak delivery/impressions; check relevance, bids, eligibility, budget.
- `AD_ENGAGEMENT_WEAK`: adequate *ad impressions* but little click activity; investigate audience, thumbnail, positioning.
- `AD_CONVERSION_UNCERTAIN`: clicks and few/no ad-attributed orders; consider listing, offer, samples, price, attribution delay; never pronounce a cause from a small sample.
- `MEASURABLE_TRACTION`: orders or attributed ad conversions exist; inspect profitability and avoid overreaction.

Thresholds such as 1,000 ad impressions or 20 clicks can prompt an *investigation*, never a statistical confidence claim. No precise traffic metric implies `unknown`, not `0`.

### 5. Select the next action
Prioritize a broken listing/eligibility issue first, measurement gap second, irrelevant targeting third, thumbnail/offer mismatch next, then carefully scoped metadata experiments. Before recommending a specific change, invoke the specialist skill: e.g. keyword intent review → `kdp-keyword-metadata-optimizer`, cover analysis → `kdp-cover-strategy`, categories → `kdp-category-positioning`, ads/royalty economics → `kdp-listing-experiment-review`.

Use an experiment record with: `experiment_id`, `book_id`, hypothesis, baseline dates, evidence link, **one changed factor**, hold-constant factors, approval, implementation timestamp, stabilization window, evaluation date, primary metric, guardrail, result and decision. Label before/after changes as observational, not randomized causality. Keep an archive of old metadata/cover/price before edits.

KDP keywords, categories, description and price generally are editable after publication; paperback title/subtitle generally lock 72 hours after first publication (check conditions). An update sends the title through review. Account for update propagation and print reporting lag; avoid repeated reactive edits in one week. KDP creation and first-submission cap is **two titles per format per UTC week** each, separately, reset Sundays 00:00 UTC; **updates** do not consume first-submission slots. Reconfirm these rules before every publishing workflow.

### 6. Deliver an actionable review
Output a short portfolio matrix with `ASIN/format/status/first-live/processed units/ad metrics/source dates`, blanks as `unknown`. Then, per live book: evidence, diagnosis/confidence, highest-value next action, experiment details if warranted, and stop/pause/spend guardrails. Identify a **single highest-priority test** and the exact missing data. Do not invent an experiment winner. At 7 days emphasize technical QA and baseline; at approximately 14+ days consider ads or metadata hypotheses *only if evidence warrants*; at 30+ days reassess positioning and economics. These review milestones are operating heuristics, not KDP guarantees.

## First run for this catalog
As of owner report on 2026-10-08: Gospel Foundations Parts 1 and 2 are live around one week with no reported purchases; Slow With Jesus Luke and Matthew are submitted/in review. This is **not** a verified KDP export, and no page-view metric has been supplied. First action: verify ASINs and live dates and take baseline marketplace listing snapshots before editing anything. If there are no ads, ad impressions/clicks are **not measured**.

## Official sources to recheck
- KDP Reports https://kdp.amazon.com/en_US/help/topic/GVTTXHKHVPAPBEDQ
- KDP Orders https://kdp.amazon.com/en_US/help/topic/GNT7B2H74F5NJZW3
- KDP title caps https://kdp.amazon.com/en_US/help/topic/G202172740
- KDP editable details https://kdp.amazon.com/en_US/help/topic/G200736410
- KDP timelines https://kdp.amazon.com/en_US/help/topic/G202173620
- KDP discoverability https://kdp.amazon.com/en_US/help/topic/G201298500
- Amazon Ads reports https://advertising.amazon.com/en-us/library/guides/book-advertising-reporting/
- Amazon Ads search-term constraints https://advertising.amazon.com/help/G3HEFZYWZF84NPS9

## Executable check
```sh
python3 skills/kdp-portfolio-optimization/scripts/review_portfolio.py --catalog portfolio/catalog.json --as-of 2026-10-08
python3 -m unittest discover -s skills/kdp-portfolio-optimization/tests -v
```
See `portfolio/README.md` for private report imports and a repeatable weekly workflow.
