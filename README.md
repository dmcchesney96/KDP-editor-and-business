# KDP Editor & Business Assistant

An operating repository for AI-assisted Amazon KDP work: book ideation, market research, metadata, editing, production planning, KDP readiness, and post-launch learning.

## Purpose

This repository is the assistant's operating system for KDP projects. It stores instructions, reusable skills, research methods, governance, and integrations. Project manuscripts, covers, print-ready PDFs, and other large publishing artifacts should live in the appropriate project workspace/Drive rather than being duplicated here unless there is a clear reason.

## Core principle

Build books that are genuinely useful to readers first, then use market evidence to improve positioning and discoverability.

Market data is decision support, not a promise of sales.

## Initial skill library

- `kdp-market-opportunity-scout` — explores reader demand, search language, competition, and opportunity.
- `kdp-competitor-benchmark` — analyzes comparable books and separates observed facts from estimated performance.
- `kdp-keyword-metadata-optimizer` — develops compliant, relevant KDP keywords and metadata using current Amazon guidance.
- `kdp-opportunity-decision-brief` — turns market research into a go / test / revise / stop recommendation.

## Upstream inspiration

The initial market-research skills were adapted from ideas in [rxpelle/kdp-scout](https://github.com/rxpelle/kdp-scout), an MIT-licensed open-source KDP keyword and competitor research tool.

We intentionally do **not** copy every upstream assumption. KDP rules change, and some upstream implementation details can become stale or conflict with current Amazon guidance. Official current KDP documentation outranks copied heuristics.

See:
- `docs/kdp-scout-adaptation.md`
- `THIRD_PARTY_NOTICES.md`

## Source hierarchy

For KDP policy, metadata limits, file requirements, content rules, and publishing requirements:

1. Current official Amazon KDP documentation
2. Current KDP interface behavior / validation
3. Verified Amazon marketplace observations
4. Reputable publishing-industry sources
5. Open-source tools and practitioner heuristics
6. Anecdotes and unverified claims

Never present an estimate, scraped metric, or heuristic as an Amazon-confirmed fact.

## Project playbooks

Project-specific strategy can live under `projects/` without changing the reusable KDP skills.

- `projects/slow-with-jesus/market-launch-playbook.md` — approved positioning, keyword architecture, Amazon listing strategy, ad experiments, product-targeting seeds, and series reuse rules for the Slow With Jesus Gospel journals.


## File-backed listing handoffs

- `skills/kdp-listing-handoff/` — verified file roles/hashes, recoverable draft/upload checkpoints, and live KDP/proof gates.
- `skills/kdp-listing-experiment-review/` — actual report normalization, weighted Ads metrics, and measured listing experiments.
- `projects/abc-of-the-bible/launch-handoff.md` — current activity-book positioning, print spec, metadata hypotheses, and pending launch gates.

Large project print files remain in the owner’s project folder. Repository instructions and public observations are not account analytics.

## Portfolio performance and experimentation

- `skills/kdp-portfolio-optimization/` — launch health checks, evidence rules, safe KDP Orders/Ads report comparison, reproducible CLI and regression tests.
- `portfolio/catalog.json` — owner-reported four-book working inventory; unknown ASINs/dates explicitly null.
- `portfolio/README.md` — weekly workflow, report schemas, private export safety, experiment/observation templates.

This public repo contains **no** live KDP account views or private reports. Organic page views and keyword search volumes must not be fabricated. Publishing capacity and editable fields follow current KDP help guidance; validate before posting or updating.
