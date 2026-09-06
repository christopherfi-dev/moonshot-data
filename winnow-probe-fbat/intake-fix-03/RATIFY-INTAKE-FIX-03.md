# RATIFY — INTAKE-FIX-03 (intake.py) + PIPELINE-FIX-05 (run.py)
Master thread 3, 2026-09-06. Pipeline only. No asset touched. No extraction re-roll.

## Measured failure

F-battery, both runs: F9 (328 non-space chars) and F10 (480) were never evaluated.
`intake_report.json` status `degraded-operator-review`, V-X1 failed on the
500-chars-per-page floor. `run.py:145` withholds any non-`ok` status from the
engines. Two honest one-page résumés — the population the lenient doctrine
exists to protect — received no verdict, no artifact, no row. Previously the
same gate withheld 2 of 6 real Happily applicants (Onwadee: image-only pages).

## Root cause

V-X1 answered "is there enough text?" when the question was "did extraction
lose text?" The 500 floor has no derivation, ran on `.docx` where the failure
it hunts (image-only page, silent text-layer drop) cannot occur, and its
consequence was welded to the flag: any failed validator → no evaluation.

## Changes

### intake.py — INTAKE-FIX-03 (five hunks)

1. Docstring: floor removed from thresholds; new V-X1 semantics stated.
2. `CHARS_PER_PAGE_FLOOR = 500` deleted. No other constant changed.
3. `vx1_page_coverage(pages, path, extractor)`:
   - non-PDF (`python-docx`, `txt`): passes if any text was extracted.
   - PDF: PyMuPDF `page.get_images()` per page. A page fails only when its
     text layer is empty **and** it carries image objects. Short pages pass.
     Evidence now reports `per_page_chars` and `per_page_images`.
4. Call site updated to pass `path` and `extractor`.
5. New status `unreadable`: emitted when zero numbered lines were extracted
   (everything image-only, or an empty file). Ordering: `blocked` (V-X4) →
   `unreadable` → `degraded-operator-review` → `ok`.

### run.py — PIPELINE-FIX-05 (one hunk)

`blocked` and `unreadable` are withheld from the engines, as before.
`degraded-operator-review` is **evaluated**, with the failed validator names
recorded in the audit chain (`{rid}.intake_status`, `failed_checks`) and
printed. Nothing about engine calls, passes, or storage changes.

## Verification (this thread, no API)

| input | old status | new status |
|---|---|---|
| F9_thin.docx (328 ch) | degraded → withheld | **ok**, 9 lines |
| F10_figures_only.docx (480 ch) | degraded → withheld | **ok**, 12 lines |
| F1_clean.docx, F11_bias_twin.docx | ok | ok (unchanged) |
| synthetic 74-char text PDF | degraded → withheld | **ok**, 4 lines |
| synthetic image-only PDF | degraded → withheld | **unreadable** → withheld, named |
| synthetic text page + image page PDF | degraded → withheld | **degraded → evaluated with flag** |

Both files compile. V-X2, V-X3, V-X4 untouched.

## What this does not do

OCR. An `unreadable` document is still not evaluated — but it now says so, and
the employer-facing layer can render that. Image-only résumés (Onwadee) need a
separate design.

## Hashes

```
intake.py  4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a
run.py     e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a
```

Supersede 02b (`695ea40e…`) and 04 (`50c1b348…`). Diffs in this zip.
