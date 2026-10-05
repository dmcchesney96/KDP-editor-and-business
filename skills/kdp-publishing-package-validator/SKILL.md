---
name: kdp-publishing-package-validator
description: Perform the final cross-artifact KDP publishing audit across interior, cover, metadata, categories, pricing, rights, AI disclosure, and preflight evidence before upload or publication approval.
---

# KDP Publishing Package Validator

## Job
Own: `FINAL FILES + METADATA + POLICY CHECKS → PUBLISHING READINESS GATE`

This is a cross-package validator. It does not replace specialized print preflight, Bible/content QA, metadata, economics, or category skills; it verifies their outputs agree.

## Required checks
As applicable:
- final interior exists and passed `kdp-print-preflight`;
- final cover dimensions match trim/page-count/paper specs;
- title/subtitle/author/imprint metadata agree with cover/interior;
- book description matches actual features;
- keywords are relevant/compliant;
- selected categories accurately fit the book and are current;
- price/royalty assumptions were rechecked;
- copyright/permissions issues resolved;
- trademark/IP risks resolved;
- AI-generated-content disclosure decision made according to current KDP policy;
- age/grade claims match the actual product;
- no unresolved editorial or specialist blockers;
- proof-copy/previewer inspection status is explicit.

## Status
For each item use:
- `PASS`
- `FAIL`
- `WARNING`
- `PENDING HUMAN ACTION`
- `NOT APPLICABLE`

## Output
### PACKAGE VERDICT
`READY TO UPLOAD`, `READY AFTER HUMAN ACTION`, or `NOT READY`.

### COMPONENT INVENTORY
### CROSS-FILE CONSISTENCY
### POLICY / RIGHTS
### METADATA / DISCOVERABILITY
### ECONOMICS
### HUMAN ACTIONS REQUIRED
### FINAL UPLOAD CHECKLIST

## Gate
Do not say “ready to publish” until KDP Previewer/physical-proof requirements the project considers necessary are complete. A technically uploadable package may still require a proof copy.
