---
name: kdp-keyword-metadata-optimizer
description: Build reader-centered, current-policy-compliant KDP keyword and metadata recommendations from the actual book content, market language, and official Amazon guidance.
---

# KDP Keyword & Metadata Optimizer

## Job

Own the bounded transformation:

`BOOK CONTENT + READER LANGUAGE + CURRENT KDP RULES → METADATA RECOMMENDATION`

## Authority rule

Before hard-coding or asserting a KDP metadata limit/rule, verify current official Amazon KDP guidance when the answer is time-sensitive.

Do not inherit a third-party limit merely because a tool encodes it.

## Current baseline

At the time this skill was created, official KDP guidance says authors may use **up to seven keywords or short phrases** and should watch the character limit in the KDP field.

Amazon recommends relevant reader-centered terms and warns against misleading or promotional metadata.

Because interface limits can change, do not encode a permanent numeric per-box character/byte limit here unless current official KDP documentation supports it.

## Keyword discovery

Generate candidate phrases from:

- reader search language;
- Amazon autocomplete/search suggestions;
- setting;
- audience;
- problem/use case;
- character type/role where applicable;
- theme;
- tone;
- format/activity type;
- age/skill level when accurate;
- niche-specific terminology.

Prefer accurate search intent over keyword stuffing.

## Avoid

Do not recommend:

- unrelated terms;
- competitor author names or book titles;
- unauthorized brands/trademarks;
- sales-rank claims;
- promotional terms such as free/on sale;
- misleading category terms;
- HTML;
- metadata already adequately represented elsewhere when it wastes limited space.

Use current official KDP guidance for the final compliance pass.

## Optimization logic

1. Preserve relevance first.
2. Remove unnecessary duplication.
3. Prefer natural reader phrases.
4. Cover distinct semantic/search-intent dimensions.
5. Test candidate phrases in Amazon search when useful.
6. Keep metadata consistent with what the book actually delivers.
7. Separate discovery experiments from final compliant metadata.

## Important upstream correction

The upstream `rxpelle/kdp-scout` project contains useful keyword-discovery and redundancy-checking concepts, but one implementation hard-codes a 500-byte per-slot limit while other project text references a different limit.

Do **not** carry that conflict forward as truth.

## Output

### READER SEARCH INTENTS
Grouped by intent.

### CANDIDATE KEYWORDS
Ranked candidates with rationale.

### RECOMMENDED KDP KEYWORDS
Up to seven relevant phrases, subject to current KDP field validation.

### TITLE / SUBTITLE CHECK
Only if requested or relevant; ensure metadata truthfully matches the cover/book.

### COMPLIANCE CHECK
Flag risky or prohibited wording.

### EXPERIMENTS
Optional alternate keyword sets worth testing after publication.
