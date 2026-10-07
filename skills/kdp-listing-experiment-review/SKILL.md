---
name: kdp-listing-experiment-review
description: Review actual KDP and Amazon Ads exports to distinguish discovery, clicks, purchases, and contribution margin, then propose a measured listing experiment. Use for post-launch keyword, cover, price, or ad-performance reviews; never invent traffic, search volume, or conversion rates from sales rank or royalty reports.
---

# KDP Listing Experiment Review

Use real account exports to decide what to test next. A repo of instructions is not a source of account analytics.

## Gather and reconcile

Request or retrieve only reports authorized for the named title. Ground ASIN/draft, marketplace, currency, report type, date range, and attribution window. Keep exports in a private project folder. Read current official Amazon Ads reporting definitions and KDP royalty rules before interpreting changing metrics.

KDP unit/royalty reports measure sales and royalties. They do not supply organic impressions, detail-page visits, or an organic conversion denominator. Amazon Ads reports can measure ad impressions, clicks, attributed orders/sales, and spend for their stated window. Autocomplete gives language; BSR gives a rank snapshot. Neither provides measured keyword demand or this book's CTR.

Use `scripts/summarize_ads.py NORMALIZED.csv --currency USD --royalty-per-unit 3.578` after mapping columns into the canonical schema in [references/report-schema.md](references/report-schema.md). The supplied unit royalty is an estimate for chosen print options/marketplace, not a cost supplied by the Ads report. Preserve the original export and mapping note. Do not combine marketplaces, currencies, attribution windows, or unlike periods.

## Evaluate

Report denominators and unknowns. Aggregate CTR and conversion from sums, not averages of row percentages. Calculate cost per attributed order and estimated royalty contribution after ads. ACoS is spend/ad-attributed revenue, not profit; book-ad break-even depends on royalty. Account for refunds, taxes, lagged attribution, and unallocated business costs when they matter. Do not add ad orders to KDP units: they overlap.

Diagnose cautiously: poor discovery may involve relevance/indexing; low ad CTR may involve targeting, placements, cover, or title; clicks with few attributed orders may involve price, preview, description, product fit, or small samples. Reports rarely isolate cover causality. Present inferences as hypotheses.

## Recommend one experiment

Define observation, proposed cause, one changed variable, baseline period, comparable test period, success measure, cost guardrail, and stop/continue rule. Preserve other major listing variables where practical. Note seasonality and concurrent targeting changes. If data is sparse, recommend gathering more data or user feedback; do not claim a winner or statistical confidence without a defensible comparison.

Favor real converting search terms that match the book. Do not put competitor names, unauthorized brands, unrelated traffic, or promotional claims in KDP keywords. Keep observed search terms separate from approved metadata.

A review does not authorize listing writes, price changes, ad spending, or contacting customers. Complete a concrete recommendation and act within current requested scope. Save report provenance and decisions so the next review distinguishes new results from an earlier hypothesis.
