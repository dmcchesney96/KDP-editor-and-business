---
name: kdp-portfolio-tracker
description: Maintain a verified, private KDP catalog of book formats, ASINs, launch states, prices, metadata versions, and weekly release capacity; route individual launches into regular reviews.
---

# KDP Portfolio Tracker

## Purpose
Maintain one reliable portfolio inventory: `BOOKS + FORMATS + STATUS + METADATA HISTORY + RELEASE CAPACITY -> PORTFOLIO STATE`. Use this skill for portfolio status checks, publishing cadence, or to establish the baseline for an optimization review.

## Required inputs
Retrieve the latest owner-authorized Bookshelf/export/screenshots and existing private catalog. Track one row per **title + format + marketplace** (never confuse a manuscript, book, and format). Suggested fields:
- internal book ID (stable, not an ASIN); title, series, audience, format, marketplace
- KDP ASIN/ISBN if known; Amazon listing URL; first-publication/submission dates if verified
- status with source timestamp (draft / in review / live / blocked / unpublished; do not assume review completion)
- list price, estimated royalty per unit and calculation date
- current category IDs/labels, seven KDP keyword fields (private when commercially sensitive), description/cover version
- source links to final interior/cover and owner-approved listing package, not duplicate binary files in repo
- last indexing check, last report period, last experiment ID, next review date
- evidence/provenance and UNKNOWN for unverified values.

## Weekly submission gate
Verify current official KDP rules before scheduling. As documented on 2026-10-08, KDP allows up to two new **created** titles and two first-time **submitted** titles per format per week (separate limits; eBook, paperback, hardcover distinct), reset **Sunday 00:00 UTC**. Updates to titles already submitted do not consume first-submission capacity. Translate reset to local time with correct daylight saving. A draft creation can use creation capacity without using submission capacity; previously saved drafts first submitted this week do count against submission capacity. Do not claim eligibility without checking live KDP state.

Plan a queue with dependencies: KDP-ready final files, proof/preview, rights and AI disclosure, selected format, compliance, budget, and publication/review status. Publishing or changing an account is a separate explicit authorization.

## Procedure
1. Reconcile existing catalog against current owner-authorized sources. Preserve former values and dates in a private change log; never silently overwrite.
2. Summarize: live / review / blocked / ready; new-creation and new-submission capacity by format; titles needing indexing, QA, or performance reviews.
3. For live titles, route to `kdp-report-ingestion` and `kdp-discovery-diagnostic`. For testing, route to `kdp-growth-decision-review` and the existing `kdp-listing-experiment-review`.
4. Prefer a compact decision-focused portfolio dashboard over a fabricated performance score.

## Privacy and truth
This repository is public. **Never commit** raw account reports, private revenue totals, ad spend, passwords, account identifiers, private commercial keyword sets, or confidential catalog URLs without explicit review. Keep account data in private Drive/Sheets or another owner-authorized secure workspace. A user-reported count of zero units is not independently verified traffic data.

## Output contract
`PORTFOLIO SNAPSHOT` (as-of date, verified/user-reported distinctions);
`TITLE STATUS TABLE` (per format, next action);
`WEEKLY RELEASE SLOTS` (creation vs first submission);
`REVIEW QUEUE` (evidence needed, owner, due/trigger);
`UNKNOWN / NEEDS ACCESS` (do not fill with estimates).
