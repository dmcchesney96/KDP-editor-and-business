---
name: kdp-growth-decision-review
description: Run a recurring evidence-gated portfolio and single-book performance review to choose whether to wait, fix discoverability, improve a listing, run a small ad learning test, scale, or stop.
---

# KDP Growth Decision Review

## Purpose
Turn catalog status, validated KDP/Ads reports, discoverability observations, and listing history into a single prioritized **next decision**. Coordinate existing `kdp-listing-experiment-review`; do not duplicate its ad calculator or claim observational data proves causality.

## Rhythm (suggested, not universal rules)
- `D+0`: capture listing baseline, metadata/cover versions, audience/job and planned evaluation.
- `D+3`: check live discoverability after official propagation window; fix technical/availability issues.
- `D+14`: initial review with clear caveat when units or clicks are sparse; avoid interpreting zero sales as a proven failed cover/keyword.
- `D+30`: compare consistent windows and decide whether one useful controlled test is warranted.
- `Monthly/quarterly`: portfolio prioritization, series effects, cumulative royalty contribution and production capacity.
Use alternative dates if ads launch later, propagation is delayed, reports lag or a major listing change resets the comparison. No automatic waiting period proves success or failure.

## Inputs
- Current per-format catalog and actual launch/change timestamps (`kdp-portfolio-tracker`).
- Validated report package with grains/attribution identified (`kdp-report-ingestion`).
- Public listing/search checks and buyer-intent map (`kdp-discovery-diagnostic`).
- Existing hypotheses, previous changes and comparison windows (`kdp-listing-experiment-review`).
- Current print royalty estimate and spending guardrail if considering ads (`kdp-product-economics-planner`).

## Diagnostic tree
1. `Not live / recent update`: address publication, compliance, availability and 72-hour propagation before sales conclusions.
2. `Live; no paid data; no orders`: label organic exposure unknown. Verify search relevance, cover clarity and competitor positioning; recommend evidence collection before large revisions.
3. `Paid impressions low`: review query targeting, bids, eligibility and relevance; no CTR conclusion with virtually no impressions.
4. `Paid impressions present, few clicks`: test audience match/cover/title/targeting. CTR = sum(clicks)/sum(impressions).
5. `Paid clicks present, few attributed orders`: consider price, detail-page promise, sample, product fit or weak samples. Order rate = sum(attributed orders)/sum(clicks).
6. `Sales but poor contribution`: compare estimated per-unit royalties and ad cost; ACoS is not profit and ad-attributed sales are not KDP royalty dollars.
7. `Positive trend`: prioritize evidence-backed incremental changes and series cross-sell, without extrapolating from one week.

Each branch must state a `MEASURED`, `OBSERVED`, or `HYPOTHESIS` tag, sample/time window, confidence, next evidence step, and possible confounders. No arbitrary fixed CTR/ACoS pass/fail benchmark is universal.

## Decision options
`WAIT/COLLECT`, `FIX TECHNICAL`, `TEST DISCOVERABILITY`, `TEST LISTING`, `TEST ADS (OPTIONAL)`, `SCALE WITH GUARDRAIL`, `PAUSE`. Recommend **one primary action per title**, bounded cost and a review date. Route one-variable experimental design to `kdp-listing-experiment-review`; keep prior metadata and screenshots so reversions are possible. Do not change multiple major listing variables simultaneously without marking attribution lost.

## Authorization
Reading reports does not authorize spending money, starting advertising, publishing titles, editing public listings or changing prices. Present proposed changes and expected observable outcomes; request explicit approval before account mutations.

## Output contract
`EXECUTIVE DECISION`; `MEASUREMENTS + UNKNOWNS`; `PRIMARY HYPOTHESIS`; `ONE NEXT TEST/ACTION`; `SUCCESS / STOP / SPEND GUARDRAIL`; `RECHECK DATE`; `LEARNINGS TO RETAIN`. Protect confidential sales data in a private owner workspace, not this public repo.
