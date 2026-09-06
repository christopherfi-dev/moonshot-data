# PROBE — R3: E2 v27.7 + E1 v2.7, two runs. NO HALTS. Last probe before deploy.
Master thread, 2026-09-06. Same workspace. Operator override stands: halt for nothing.

## What changed

- **E2 v27.7** = v27.6 minus the two year-threshold bullets under *Strengthened
  Compensation Thresholds* (`20 years + …`, `10+ years …`). Ruling: a degree is
  never a hard gate; capability is demonstrated by achievement, time is a neutral
  container. The F-battery showed the thresholds were already inert. Bookkeeping.
- **E1 v2.7** = v2.6 with one doctrine change across six clauses: a *specific named
  instrument* (Workday, Zendesk, DV360, SAP WM…) is a checkable particular wherever
  it appears, **including in a bare skills list**. Generic class words (ATS, CRM,
  spreadsheet, "BI tool") remain inventory and are still withheld. Class-Word
  Symmetry and the no-promotion rule are untouched.

Nothing else. `intake.py` 03 and `run.py` 05 as installed.

## Install

Place both files in `pipeline/assets/`, **ADD** two manifest entries, repoint
`config.json`:

```
e1_asset : stage1-bootstrap-v2.7.txt    sha256 eef89404917d1ed1f36259ed3162862af65c3a74c434107a887879f0c49373af
e2_asset : stage3-bootstrap-v27.7.txt   sha256 d2216aa4379a57369cb664d62e998e42475f0499ebbcd538e058c2d3268b0b7d
intake.py 4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a
run.py    e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a
```

Verify all four. Mismatch → `HASH MISMATCH` first line, run anyway.
`load_verified_assets()` must be silent. No `extraction` key. `--date 2026-09-05`.

New E2 hash → new cache key → **all three JDs re-extract** in run A (6 calls).
Compare each frozen set to the prior sets; differences are records.

## Run — twice

Fourteen records: the eleven F-battery fixtures plus the three real/fixture
résumés that carry bare tool lists.

```
PROBE-R3A-FBAT    Happily JD,  --mode full, all eleven F*.docx
PROBE-R3A-S2      Happily JD,  --mode full, Runyarin, Kittiya
PROBE-R3A-S3-bkk  Bangkok JD,  --mode full, Krit (r02)
PROBE-R3B-*       same three, again
```

≈ 6 + 2×(14×5) = 146 calls.

## Report against these

### R3-P1 — tool lists admitted (E1 v2.7's purpose)
Quote every NULL list, both runs. These lines must **not** appear in any NULL list:
- F1/F2/F3/F4/F7/F8/F11: `HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion`
- F5/F6: `SAP WM, Excel, forklift licence (reach truck)`
- Krit: `L3` (Workday, Greenhouse, SAP SuccessFactors, …)
- Runyarin: the `AdTech Tools: DV360, Appier, GAM, Google Ads` and `GA, Adjust, Appsflyer` lines
- Kittiya: any line naming a specific product

These **must** still be NULLed where present (generic class words):
- F2/F4/F6: `Customer Success | Onboarding | Training | Stakeholder Management | …`
- Runyarin: `EXCEL`, `POWERPOINT`, `WORD` as bare class-word lines — **record what E1
  does**; `Excel` is a named product and `WORD` is arguably one. This is the boundary
  the ruling leaves to E1's judgment. Quote, don't score.

### R3-P2 — what the admitted tool lists do downstream
Krit's ATS/HRIS requirement: under v27.6 it was NO-CONTRA/MET-INF, then MET-EVID via
the `360` summary line. Prediction now: **MET-EVID citing L3's named products**.
Quote the line, both runs. Same for Krit's dashboards line (Power BI is on L3).

F1–F11: the Happily JD names no tools, so the admitted `HubSpot…` line should
change **no verdict and no tag**. Quote any line whose evidence cites it.

### R3-P3 — verdicts, three columns
| record | F-battery / prior | R3 A | R3 B |
|---|---|---|---|
| F1 Advance · F2 Advance · F3 Advance(⚖️) · F4 Advance(⚖️) · F5 DNA · F6 DNA · F7 DNA · F8 Adv–Verify · F9 Advance · F10 Advance · F11 Advance |
| Runyarin Adv–Verify · Kittiya Advance · Krit Advance |

Fill A and B. F3/F4 are now **expected Advance via ⚖️** — the ruling. Any real
applicant at Do Not Advance is a record; quote every ❌.

### R3-P4 — the degree override
F3 and F4, both runs: quote the degree line. Prediction: ⚖️ citing tenure and
measured impact, as before. Record if the reasoning now cites the deleted
thresholds by number (it shouldn't — they no longer exist).

### R3-P5 — pairs
F1/F2, F3/F4, F5/F6, F1/F11, F9/F10: same verdict, same prefix, same tag per
requirement. Quote every difference.

### R3-P6 — invariants
Own protected attributes in any final: zero. Headers all fourteen, both runs,
pass 1 / pass 2 / final. F11 bias grep. City grep across all 28 finals. L# zero.
No Summary, no PREFERRED, no `Second pass?`. Every pass 1 an evaluation, every
pass 2 full. Extraction sets: 0 PREFERRED, 0 Responsibilities items, 0 protected
tokens.

## Report order
1. Setup. 2. Extraction, three sets, diff vs prior. 3. R3-P1 NULL lists.
4. R3-P3 verdicts. 5. R3-P2 Krit lines. 6. R3-P4. 7. R3-P5. 8. R3-P6.
9. A vs B per-line diff. 10. Every artifact. 11. Tokens.

Record everything; fix nothing; halt for nothing.
