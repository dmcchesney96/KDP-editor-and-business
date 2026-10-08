# KDP portfolio — repeatable launch measurement

`catalog.json` contains **owner-reported working records** for four current titles, not KDP account exports. Update the exact title, ASIN, public detail page, actual marketplace, and first-live date only after verifying. Use a separate row per format, e.g. paperback vs Kindle.

**Do not commit reports containing royalties, account data, campaign spending or private observations into this public GitHub repo.** Place private exports in Google Drive with restricted access or `portfolio/private/` locally (gitignored). Reported "zero views" is not a KDP metric; only recorded ad impressions/clicks can support a paid-traffic claim.

## Weekly review SOP
1. Check KDP Bookshelf: status, live date, ASIN, public Amazon detail page, corrections needed. Preserve a screenshot and the last-known title/description/cover/categories/price/keyword set privately.
2. Confirm indexing/availability by exact ASIN/title, then research 3–5 **relevant** shopper queries and comparable competing books. Save marketplace, query, date, result position if observed, and caveats that search is personalized; do not claim search volumes.
3. Download current **KDP Orders** report (not just royalty totals) filtered to the same marketplace/format/time window. For paperback/hardcover it records orders after shipment. Keep original export private; map into the normalized CSV described in `../skills/kdp-portfolio-optimization/references/report-contract.md`.
4. If advertising and authorized, download Sponsored Products **advertised product** report to measure impression/click/order funnel. Separately download clicked search-terms report for intent discovery. Keep report types separate; record attribution window, period, marketplace, currency.
5. Run the CLI with the exact coverage of the exports. Do not mark an incomplete filtered report as complete. If no report exists, run in no-data mode first and act on its measurement checklist.
6. Compare to last verified baseline only after changes have propagated and attribution/shipping delay makes the windows meaningful. Open one experimental hypothesis with evidence, one changed variable, goal, spend cap, approval, next review.
7. Monthly: review series cross-selling, reviews/reader feedback, title quality and economics. Log `continue/test/revise/pause` with evidence, never an invented "winner".

## Commands

No account reports yet (honest no-data review):
```bash
python3 skills/kdp-portfolio-optimization/scripts/review_portfolio.py \
  --catalog portfolio/catalog.json --as-of 2026-10-08
```

After you have privately normalized a **complete** all-books paperback Orders export for Amazon.com during October 1–8:
```bash
python3 skills/kdp-portfolio-optimization/scripts/review_portfolio.py \
  --catalog portfolio/catalog.json --as-of 2026-10-08 \
  --orders portfolio/private/orders-normalized.csv \
  --orders-start 2026-10-01 --orders-end 2026-10-08 \
  --orders-complete --orders-marketplace Amazon.com --orders-format paperback \
  --markdown-out portfolio/private/week1.md \
  --json-out portfolio/private/week1.json
```
`--orders-complete` is an **explicit operator attestation**: the source covers all relevant tracked books in that exact time frame/marketplace/format. The script cannot independently prove it by looking at nonzero rows. Without the flag, empty export ≠ zero.

For one consistent Amazon Ads advertised-product report (when ads exist):
```bash
python3 skills/kdp-portfolio-optimization/scripts/review_portfolio.py \
  --catalog portfolio/catalog.json --as-of 2026-10-08 \
  --ads portfolio/private/ads-products-normalized.csv \
  --ads-type advertised_product --attribution-window 'source-value-14-days'
```
Replace the window label with the **actual** exported reporting horizon. Do not combine search-term and advertised-product reports: the same attributed orders may appear in both. If the Ads report is not daily, use a manual review or prepare a valid correctly dated daily normalization rather than assigning a fake single date.

## Catalog fields and launch states
- `status`: `draft | in_review | publishing | live | blocked | unpublished`.
- `first_live_date`: verified ISO date or null; never estimated from "about a week."
- `asin` / `amazon_url`: null until confirmed.
- `notes`: source and any uncertainty; user statements do not become Amazon report numbers.
- Current owner-reported state on 2026-10-08: Gospel Foundations 1/2 live about a week, no purchases reported; Slow With Jesus Luke and Matthew in review.

## Operational decisions
- First week: investigate structural problems / listing completeness, record baseline; avoid changing multiple fields.
- After ~2 weeks: compare real measured outcomes, consider one reasonable discovery or conversion test only with clear exposure/evidence.
- After ~4 weeks: evaluate weak positioning and ROI; no arbitrary requirement to advertise.
- Post-publication KDP keywords, categories, description and price may be updated; title/subtitle have stricter rules. KDP generally allows two new created and two first-submitted titles per *format* per UTC week, with Sunday 00:00 UTC reset. Updates to existing submitted books are separate. Verify current rules.

## Source-of-truth documentation
- [Portfolio skill](../skills/kdp-portfolio-optimization/SKILL.md)
- [Normalized report contract](../skills/kdp-portfolio-optimization/references/report-contract.md)
- [Experiment specification](../skills/kdp-portfolio-optimization/references/experiment-playbook.md)
- [Existing Ads experiment analysis](../skills/kdp-listing-experiment-review/SKILL.md)

Run automated safety checks with:
```bash
python3 -m unittest discover -s skills/kdp-portfolio-optimization/tests -v
```
