---
name: kdp-discovery-diagnostic
description: Diagnose whether a published book is visible and relevant for intended Amazon searches using verified listing checks, current metadata, and labeled search observations rather than invented organic traffic.
---

# KDP Discoverability Diagnostic

## Purpose
Distinguish `NOT YET LIVE/INDEXED` from `WEAK SEARCH FIT` from `NO MEASURED TRAFFIC`. Perform a buyer-centered discoverability audit on a named book without claiming to know Amazon's organic impressions.

## Required context
Get exact marketplace, format and live status, ASIN/listing URL, publication/update dates, seven active backend KDP phrases if owner-provided, live categories, title/subtitle/description, cover image, positioning brief, and closest reader search intents. Use the current `kdp-keyword-metadata-optimizer` and `kdp-category-positioning` skills for proposed fixes.

## Verification protocol
1. Confirm the product detail page is live, title/format/price/cover/description are accurate, and category placements and sample (when available) match the published product. Log observed vs expected.
2. If the title or metadata just went live/changed, check official KDP display/search propagation guidance; allow up to the documented delay (commonly up to 72 hours) before diagnosing indexing issues.
3. Build a *small* list of relevant buyer phrases organized by problem, audience, product format, topic and method. Prefer the buyer's language. Do not turn unrelated high-traffic phrases into metadata.
4. Manually and reproducibly spot-check Amazon retail search for exact title and selected buyer phrases. Record marketplace, date/time, query exact spelling, page/approximate placement, device/session, sponsored-vs-organic distinction and uncertainty. Rankings vary by shopper, location and time; one observation is not a stable keyword rank.
5. Compare each phrase to close truthful competitor product pages and actual reader use case. Distinguish search-language evidence from search-volume estimates. Review title/cover clarity at thumbnail scale as a qualitative fit check.
6. If Ads data exists, use measured paid impressions/clicks by keyword separately from these organic observations; a paid impression does not establish organic indexing.

## Diagnose with explicit confidence
Possible classifications:
- `PUBLICATION/PROPAGATION`: newly live/in review or recent update.
- `LISTING/FORMAT ISSUE`: missing/broken/mismatched cover, subtitle, price, sample or availability.
- `RELEVANCE HYPOTHESIS`: intended queries do not closely reflect the book or competitor/buyer language.
- `LOW OBSERVED SEARCH PLACEMENT`: grounded to logged queries only; not proof of zero organic impressions.
- `TRAFFIC UNKNOWN`: no organic page-view telemetry available.
- `INSUFFICIENT EVIDENCE`: not enough repeat or report observations.

Do not claim an Amazon backend "indexing score," keyword volume, daily page views, or true organic conversion unless such measurements are provided by an authorized source. Avoid high-rate scraping, automated rank queries that violate site rules, or false certainty.

## Output contract
`LISTING HEALTH CHECK`; `SEARCH-INTENT OBSERVATION TABLE` with timestamps and observed placement; `EVIDENCE vs HYPOTHESES`; `TOP 1-3 FIXES`; `NEXT CHECK DATE / EVIDENCE REQUEST`. Any suggested account edit requires separate approval.
