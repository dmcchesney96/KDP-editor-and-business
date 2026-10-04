---
name: kdp-market-opportunity-scout
description: Evaluate a KDP book idea or niche using reader demand signals, search language, competition, differentiation, and production fit while clearly separating observation from estimates.
---

# KDP Market Opportunity Scout

## Job

Own the bounded transformation:

`BOOK IDEA / NICHE → MARKET OPPORTUNITY SCAN`

Do not claim that an opportunity score predicts sales.

## Inputs

Use the smallest useful set available:

- proposed reader/audience;
- book type and format;
- topic or niche;
- seed search phrases;
- marketplace;
- comparable books;
- known production constraints;
- project goals.

## Method

### 1. Reader/job definition

State:

- target reader;
- problem, desire, entertainment need, or use case;
- expected buying/search context;
- what the book must genuinely deliver.

### 2. Search-language discovery

Use multiple signals when available:

- Amazon search/autocomplete suggestions;
- related long-tail phrases;
- relevant bestseller/new-release/movers patterns;
- current web search trends;
- language used in comparable product titles/descriptions/reviews.

Treat autocomplete as `MARKET_OBSERVATION`, not exact search volume.

The upstream KDP Scout approach expands seed phrases with alphabetic variations and deduplicates suggestions. This is a useful discovery pattern, not a demand measurement.

### 3. Demand signals

Look for converging evidence such as:

- repeated relevant search suggestions;
- multiple commercially active comparable books;
- recent/recurrent titles in the niche;
- meaningful review activity;
- observable ranking activity;
- external interest/trend signals where relevant.

If using BSR-derived sales estimates, label them `TOOL_ESTIMATE` and present a range.

### 4. Competition signals

Assess:

- number and strength of close comparables;
- review-count barrier;
- brand/author dominance;
- cover/interior quality expectations;
- pricing range;
- recency;
- exactness of fit between search intent and current products;
- whether weak competitors exist because the niche is underserved or because demand is weak.

### 5. Differentiation

Require substantive differentiation:

- better reader outcome;
- clearer audience;
- stronger format;
- more useful activities/prompts/tools;
- better age/skill fit;
- stronger visual design;
- improved organization;
- unique point of view or content.

Keyword wording alone does not count.

### 6. Production fit

Assess whether the opportunity fits realistic capability:

- page count;
- illustration/design burden;
- trim/bleed/color needs;
- content expertise;
- editing burden;
- copyright/trademark risk;
- update frequency;
- cost and time burden.

## Upstream heuristic

`rxpelle/kdp-scout` uses a niche score weighting competition BSR, review counts, estimated revenue, and an underserved ratio. Preserve this only as an `UPSTREAM_HEURISTIC`.

Do not treat fixed thresholds such as “average BSR > X means good niche” as universal truth. Marketplace, format, category, price, seasonality, ads, release timing, and scraping quality all matter.

## Output

Return:

### OPPORTUNITY SUMMARY
One paragraph.

### TARGET READER + JOB
Who the book is for and what it must deliver.

### DEMAND SIGNALS
Observed evidence, with confidence.

### COMPETITION SIGNALS
Observed evidence, with confidence.

### DIFFERENTIATION GAP
What existing books appear not to do well enough.

### PRODUCTION / POLICY RISKS
Important constraints.

### OPPORTUNITY RATING
Use one: `STRONG`, `PROMISING`, `MIXED`, `WEAK`, `INSUFFICIENT EVIDENCE`.

### NEXT BEST TEST
The smallest useful next research or prototype action.

## Stop rules

Stop and say evidence is insufficient when:

- results are too sparse or unstable;
- the niche is ambiguous;
- scraping/search data is blocked;
- a major conclusion depends on a guessed sales estimate;
- current KDP rules materially affect the recommendation but have not been verified.
