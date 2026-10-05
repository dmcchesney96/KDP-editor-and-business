---
name: kdp-review-gap-miner
description: Turn reviews and reader feedback from true comparable books into evidence-backed unmet needs, table stakes, and product opportunities without treating anecdotes as demand proof.
---

# KDP Review Gap Miner

## Job
Own: `COMPARABLE REVIEWS / FEEDBACK → READER-NEED GAP MAP`

## Inputs
Prefer direct comparables selected by `kdp-competitor-benchmark`. Adjacent products may be used but must be labeled.

## Method
1. Separate direct, adjacent, and irrelevant feedback.
2. Capture recurring praise, complaints, confusion, missing features, age/skill mismatch, usability issues, durability/print complaints, content concerns, and purchase/use context.
3. Cluster semantically similar feedback. Do not inflate frequency by counting duplicate/near-duplicate reviews.
4. Record frequency as exact counts only when the sample supports it; otherwise use `recurring`, `occasional`, or `isolated`.
5. Distinguish:
   - table stakes readers expect;
   - pain points worth fixing;
   - delight features worth preserving;
   - conflicting preferences requiring a product choice;
   - suspicious/noisy feedback.
6. Convert gaps into testable product implications, not automatic feature requests.

## Guardrails
- Reviews are a biased sample, not population research.
- One vivid complaint is not a market.
- Never copy competitor wording, proprietary activity pages, or distinctive expression.
- Do not infer child-development or theological truth from customer reviews; route those questions to specialist research/checking skills.
- When review access is partial, say so.

## Output
### SAMPLE
Products, review coverage, direct/adjacent status, limitations.

### READER JOBS
What buyers appear to be hiring the book to do.

### TABLE STAKES
Repeatedly valued or expected attributes.

### FRICTION / COMPLAINT CLUSTERS
Evidence and confidence.

### DELIGHT CLUSTERS
What readers repeatedly value.

### WHITE-SPACE HYPOTHESES
For each: evidence → proposed improvement → confidence → smallest validation test.

### PRODUCT IMPLICATIONS
Concrete consequences for positioning, architecture, content, design, or format.

## Handoff
Feed supported implications to `kdp-product-positioning-architect`; do not design the whole book here.
