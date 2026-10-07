# Manifest v1

`PACKAGE_MANIFEST.json` uses UTF-8 JSON. Minimum local-validation fields:

```json
{
  "schema_version": 1,
  "metadata": {"title": "Actual title", "subtitle": "", "author": null, "keywords": ["relevant phrase"]},
  "print": {"trim_inches": [8.5, 11], "interior_pages": 80, "cover_inches": [17.43016, 11.25]},
  "files": [
    {"role": "interior", "path": "Print_Files/interior.pdf", "sha256": "actual hash"},
    {"role": "cover", "path": "Print_Files/cover.pdf", "sha256": "actual hash"}
  ]
}
```

Additional recommended fields: date, ink/paper, spine, bleed, finish, formula sources, marketplace, price recommendation, description file, category targets with live-selection status, AI provenance, rights status, authorization scope, Previewer/proof status, Drive inventory, and repo revision. Resolve paths relative to the manifest. Keep private IDs out of public repos. `author: null` is deliberately permitted for preparation and reported as a publication blocker.

The validator checks hashes, roles, PDF page count and displayed page dimensions, embedded fonts, unencrypted PDFs, and keyword shape. Passing is a local file check, not a print-quality or publication verdict. Font presence does not prove glyph fidelity. Image resolution, margins, barcode placement, and full visual checks need separate preflight evidence.
