# KDP Scout Adaptation Notes

## Source

Upstream project: https://github.com/rxpelle/kdp-scout

License: MIT

The upstream project is a Python CLI for KDP keyword research and competitor analysis. It includes:

- Amazon autocomplete mining;
- trending/bestseller discovery;
- competitor tracking;
- BSR-based sales estimates;
- review/price/rank snapshots;
- Amazon Ads CSV import;
- keyword scoring;
- niche opportunity scoring;
- reporting/export;
- recurring automation.

## What we adapted

We extracted the **methods**, not the entire application, into assistant skills:

- seed + long-tail search-language discovery;
- use of autocomplete as reader-language evidence;
- competitor snapshot thinking;
- competition signals from rank/reviews/price;
- opportunity scoring as a heuristic;
- explicit labeling of BSR-derived sales as estimates;
- longitudinal comparison;
- keyword redundancy/compliance checks.

## What we did not copy blindly

### 1. Keyword field limits

The upstream repository contains an internal inconsistency:

- its README describes backend keyword export as “7 x 50 bytes”;
- `keyword_validator.py` hard-codes `500` bytes per slot.

Current official KDP help instead says authors may use up to seven keywords/short phrases and should watch the character limit in the field.

Therefore this repository does not preserve either upstream numeric limit as an official rule.

### 2. BSR → sales

The upstream tool uses a power-law model calibrated to assumed data points.

That may be useful for rough comparisons, but Amazon does not publish an official universal BSR-to-sales conversion. Treat outputs as `TOOL_ESTIMATE`, preferably as ranges.

### 3. Opportunity score

The upstream score weights:

- average BSR / competition;
- average review count;
- estimated revenue;
- proportion of high-BSR results.

This is useful as a prioritization heuristic, not a validated predictor of book success.

### 4. Scraping stability

Amazon pages and selectors change. Search results can also be dynamic. A failed scrape is not evidence of no market.

## Current official references used when creating this adaptation

- https://kdp.amazon.com/en_US/help/topic/G201743260
- https://kdp.amazon.com/en_US/help/topic/G201298500
- https://kdp.amazon.com/en_US/help/topic/G201097560
- https://kdp.amazon.com/en_US/help/topic/G200652170

Re-check official KDP documentation for consequential or time-sensitive platform decisions.
