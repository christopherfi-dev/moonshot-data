# F-BATTERY ADDENDUM — install INTAKE-FIX-03 / PIPELINE-FIX-05, re-run F9 and F10
Master thread, 2026-09-06. Same session, same workspace. No halts.

## Install (two files, nothing else)

Replace `pipeline/intake.py` and `pipeline/run.py` with the two files in this zip.
Verify:

```
intake.py  4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a
run.py     e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a
```

Mismatch → `HASH MISMATCH` first line, then proceed. Read `RATIFY-INTAKE-FIX-03.md`
for what changed. Assets, manifest, config: untouched — E1 v2.6, E2 v27.6.
Confirm `python3 -m py_compile pipeline/intake.py pipeline/run.py` is silent.

## Run

Two fixtures only, twice:

```
PROBE-FBAT-C   Happily JD, --mode full, F9_thin.docx F10_figures_only.docx
PROBE-FBAT-D   same again
```

Happily JD is cached under v27.6 — expect cache hits. ~8 E2 + 4 E1 calls.

## Report

1. Hashes, compile check.
2. Both `intake_report.json`: status must now be `ok`; quote V-X1's `detail`
   and `evidence`. Prediction: `text extracted`, per_page_chars [328] and [480].
3. Verdicts, both runs. Ground truth from `GROUND-TRUTH.md`: F9 **Advance**
   (title → domain MET-INF; silence → NO-CONTRA), F10 **Advance** with
   MET-EVID on lines its three figures speak to. Record whatever happens.
4. F9 vs F10 as a pair: same verdict? which tags moved MET-INF/NO-CONTRA →
   MET-EVID on F10, quoted.
5. E1 NULL lists, both, both runs. Prediction: empty or the `SKILLS`-class
   line only. F10's three figure lines must not appear.
6. Headers, city scan (`Phuket`, `Thailand`), invariants.
7. Every artifact, both passes, both fixtures, both runs.

Then finish the F-battery report you were writing, and append this as its
final section.

Record everything; fix nothing; halt for nothing.
