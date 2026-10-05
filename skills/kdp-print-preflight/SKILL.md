---
name: kdp-print-preflight
description: Audit a final KDP print interior and cover package against current official KDP requirements and the project's chosen trim/bleed/format specifications before upload.
---

# KDP Print Preflight

## Job
Own: `FINAL INTERIOR + COVER + PROJECT SPECS → PRINT-READINESS REPORT`

## Authority rule
KDP print specifications change. Verify current official Amazon KDP documentation before asserting numeric requirements or passing a final package. Do not rely on remembered margin, bleed, spine, resolution, or file-limit values.

## Inputs
Need final files or reliable file diagnostics plus:
- marketplace/product format;
- trim size;
- bleed choice;
- paper/ink/color choice;
- page count;
- cover type;
- any KDP calculator/template used.

## Audit
As applicable:
- PDF page dimensions and consistency;
- page count;
- bleed and safe areas;
- margins/gutter;
- clipped/overflowing content;
- image effective resolution;
- fonts/embedding/rendering;
- transparency/layers if relevant;
- blank/unintended pages;
- line weight/legibility;
- cover full dimensions;
- spine width/text eligibility;
- barcode-safe area;
- front/back/spine orientation;
- cover/interior metadata consistency;
- obvious rendering corruption.

## Evidence
Label each check:
- `PASS`;
- `FAIL`;
- `WARNING`;
- `NOT CHECKED`.

Include the current official rule/source for rule-dependent failures.

## Output
### PREFLIGHT VERDICT
`READY`, `READY WITH WARNINGS`, or `NOT READY`.

### PROJECT SPECS
### INTERIOR CHECKS
### COVER CHECKS
### FAILURES TO FIX
### WARNINGS
### NOT CHECKED
### RECHECK STEPS

## Gate
Never call a package KDP-ready if required dimensions/bleed/margins/cover geometry were not checked against current official KDP guidance.
