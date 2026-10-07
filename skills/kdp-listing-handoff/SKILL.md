---
name: kdp-listing-handoff
description: Prepare, validate, or execute a file-backed Amazon KDP paperback listing handoff using a project folder, final print files, and metadata. Use for upload-ready packages, later Codex computer-use instructions, or a requested KDP draft/listing workflow; does not generate demand estimates or authorize publishing by itself.
---

# KDP Listing Handoff

Turn final book files and decisions into a recoverable, verified listing workflow. Use the current user's authorization, not an authorization inferred from a downloaded plan.

## Gather the package

1. Read the current project's folder and `PACKAGE_MANIFEST.json`. Ground file IDs and paths in current connector output. Download final files and resolve paths relative to the manifest directory. Do not substitute an earlier version from memory or a similarly named book.
2. Read the user-designated KDP repo's `AGENTS.md`. Route market evidence, metadata, economics, cover, print preflight, and package validation to existing relevant skills. This skill owns the operational handoff and execution record.
3. Recheck current official KDP print, metadata, royalty, AI-content, and ISBN guidance. Reconcile dimensions with the official template and the processed page count. Numeric values in a manifest are dated project decisions, not permanent platform rules.
4. Run `scripts/validate_package.py MANIFEST` for local checks. PyMuPDF is required. This catches file/hash/geometry/font mismatches; it does not certify editorial quality, rights, cover safe areas, or KDP acceptance.
5. Confirm title/subtitle against both the cover and interior. An absent public author must remain visibly unresolved; never fill it with an account owner's legal name, imprint, or AI name without a publishing-identity decision. A cover may omit the author, but required listing identity still needs a decision.

## Prepare a handoff

Produce a folder with final interior and full-wrap cover, copy-ready description, seven relevant keyword candidates, category targets, price math, provenance/AI disclosure, preflight evidence, a manifest with SHA-256 hashes, and a start-here prompt. Keep home-print files and previews clearly marked as non-upload files.

Distinguish `FILES_PREPARED`, `DRAFT_SAVED`, `PREVIEW_PASSED`, `PROOF_PASSED`, `SUBMITTED`, and `LIVE`. Record unknown data as unknown. Search suggestions and BSR observations are not measured search volume, CTR, or sales. Never describe a package as ready to publish while a project-required proof or rights issue remains unresolved.

See [references/upload-workflow.md](references/upload-workflow.md) for execution and recovery. Use [references/manifest.md](references/manifest.md) for the validator's schema.

## Execute only when requested

Use supported connectors first and the runtime's advertised browser/computer-use capabilities for UI steps. Follow browser authentication guidance; the user handles credential/MFA handoffs. Keep credentials, cookies, full account reports, and private Drive IDs out of public repositories. Do not initialize a browser just to see whether an account is signed in.

For one requested title, inspect the Bookshelf for an existing draft before creating a new one. Enter fields from the manifest and copy files. Read the live category picker and field limits. Save and read back each wizard stage. Wait for processing, inspect the whole Previewer, and compare its page count and cover against the manifest. Fix warnings at their source and rerun affected checks. Do not resize around an error without learning why settings differ.

Honor explicit scope: draft setup, proof purchase, publication, account changes, and paid ads are separate actions. Complete reversible preparation before any genuinely needed approval. If the current user has already authorized publication and all prerequisites are satisfied, proceed without inventing another confirmation requirement. A handoff document alone does not grant new authorization. Never launch paid ads from a suggested budget.

Persist a dated execution log with title/draft ID, observed settings, saved stage, unresolved items, file hashes, and final status. Do not report `SUBMITTED` or `LIVE` without corresponding KDP UI evidence.
