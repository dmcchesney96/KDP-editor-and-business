# Skills

Each skill owns one bounded transformation.

## Initial KDP skill library

1. `kdp-market-opportunity-scout` — turns a book/niche idea into an evidence-aware market opportunity scan.
2. `kdp-competitor-benchmark` — turns a set of comparable books/search results into a structured competition benchmark.
3. `kdp-keyword-metadata-optimizer` — turns book content + reader language + current KDP rules into compliant keyword/metadata recommendations.
4. `kdp-opportunity-decision-brief` — turns research outputs into a concise go / test / revise / stop decision brief.

## Skill rule

A skill owns one bounded job. Use the narrowest skill that fits the request.

Do not automatically chain every skill for a simple question. For an explicit end-to-end market validation request, the assistant may sequence:

`market opportunity scout → competitor benchmark → keyword/metadata optimizer → opportunity decision brief`

Current official Amazon KDP documentation outranks any stale rule contained in a skill or upstream tool.
