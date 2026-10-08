# Listing experiment playbook

## Before a hypothesis
Inspect actual product page, metadata currently entered, current indexing/search availability, delivery/eligibility and competitive set. Record title, format, ASIN, country, screenshot time, reader job, price, cover size on mobile, description, categories, A+ presence, and sample availability. Verify current official KDP policies. Owners may estimate traffic via ads, but the public book page cannot show organic views.

## Diagnostic ladder (noncausal)
1. Not live / in review → verify status, don't optimize conversions.
2. Missing complete KDP export → collect it; don't call 0 sales confirmed.
3. Zero confirmed paid shipments with no ads → distinguish unmeasured discovery from verified lack of sales; check exact-title availability and relevant search intent.
4. Ads impressions very limited → delivery/eligibility/bids/target relevance, **not** a cover verdict.
5. Ads impressions but few clicks → audience/positioning/cover hypothesis, not demonstrated causality.
6. Ads clicks but no attributed orders → pricing, sample, description, promise, competition, targeting and attribution timing hypotheses; no false certainty.
7. Conversions and positive orders → evaluate royalty-after-ad costs, not only ACoS.

## Controlled experiment specification
```yaml
experiment_id: exp-0001
book_id: foundations-1
marketplace: Amazon.com
hypothesis: "More accurate reader-intent keyword phrases may improve qualified ad discovery"
evidence: "<private source manifest and dated observations>"
status: proposed # proposed/approved/implemented/observing/completed/abandoned
approval: not_granted
variable: "KDP backend keyword set" # one changed factor; do not change cover and price together
baseline_start: null
baseline_end: null
implemented_at: null
stabilization_rule: "Review KDP update timeline; allow up to 72 hours as relevant"
comparison_start: null
comparison_end: null
primary_metric: "Comparable qualified ad impressions and ad-attributed orders, if campaigns held constant"
hold_constant: ["cover", "price", "description", "ad budget", "targeting"]
guardrail: "No ad spend without separate approval; stop if spend exceeds approved cap"
evaluation: "Require matching marketplace, attribution settings, observation windows and exposure"
decision: pending
```
This is an **example experiment**, not proof that keyword changes cause ad impressions to rise. On Amazon, delivery, seasonality, auctions, ad bid/budget or other factors can change the observable result. For sparse data, report inconclusive and continue observing, rather than declare a winner.

## Priority and cadence
- Launch (first 7 days): listing technically complete? cover legible? correct category/age, sample eligibility, ASIN findability? Capture baseline once searchable; do not churn metadata.
- ~14 days: inspect KDP processed units, competitive positioning and any authorized ad report; propose exactly one narrow test if evidence is suitable.
- ~30 days: test reader promise/positioning and evaluate economics, discovery channel, potential marketing distribution beyond Amazon.
- Weekly after: compare snapshots with the last known stable state. Stagger related changes to isolate hypotheses; do not treat weekly churn as a growth strategy.
- Re-evaluate earlier conclusions if delayed reports or attribution move the denominator.

## Targeting and compliance
Use relevant, accurate Amazon search language and current KDP keyword rules (up to seven backend keyword slots). Don't pack descriptions with repeated search terms, misleading categories, unauthorized trademarks, or competitors' names. When analyzing competitors, keep source and date and distinguish directly observed prices and rankings from tool forecasts. Ads activation/budget changes and listing modifications require separate authorization.
