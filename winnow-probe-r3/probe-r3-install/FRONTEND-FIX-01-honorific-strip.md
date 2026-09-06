# FRONTEND-FIX-01 — header honorific strip at render
Master thread 3, 2026-09-06. Operator ruling: yes. Display layer only.

## Why

Two of 48 E2 finals since v27.5 carried a gender token in the header line —
`Ms.Kittiya` (v27.5, via the confirm path) and `MR. PUPAT` (v27.6 run B, pass 2
did not strip it). The asset sentence works most of the time and is not
deterministic. Text has been tried in two forms. A third sentence is the v29
reflex. The header is the most visible line on the page. This closes it.

## Why this is allowed under the rules

`render.py` already strips the string `Second pass?` from the end of an
evaluation (render.py:129 per the record). This is the same class: removal of
a closed set of literal tokens from one known position. It parses no verdict,
gates nothing, changes no line but the header, and never touches the résumé
or any engine payload. It bends U1 "render verbatim" by one token on one line,
which the operator has ruled acceptable.

## Behavior — exact

Applies to **the header line only**: the line matching `^R\d+\s+(.+?)\s+-\s+(Advance|Advance – Verify|Do Not Advance)\s*$`.
No other line in `evaluation.txt` is touched.

From the captured name, strip **leading** tokens that match, case-insensitively,
any of:

```
MR  MRS  MS  MISS  DR  MX  KHUN  NAI  NANG  NANGSAO  ดร  นาย  นาง  นางสาว  คุณ
```

each optionally followed by `.`, and optionally followed by whitespace — so
`Ms.Kittiya`, `MR. PUPAT`, `Ms. Kittiya`, `นางสาวPimchanok`, `นางสาว Pimchanok`
all strip. Repeat until the leading token does not match (handles `Dr. Ms.`).
Also strip a leading `[` and trailing `]` around the name if both are present
(the template-bracket artifact: `[PUPAT CHATAMEENA]`).

Never strip a token that is not at the start of the name. Never strip if what
would remain is empty.

Log every strip: `rid`, original header, rendered header — to the existing
render log or audit, so the master thread can count how often it fires.

## Not in scope

Anything below the header. The `⚖️ [Achievement] →` placeholder. Any change
to `run.py`, `intake.py`, the assets, or the manifest.

## Test cases (must all pass before deploy)

| input header | rendered |
|---|---|
| `R1 [MR. PUPAT CHATAMEENA] - Advance` | `R1 PUPAT CHATAMEENA - Advance` |
| `R4 Ms.Kittiya Anantapatthamanond - Advance – Verify` | `R4 Kittiya Anantapatthamanond - Advance – Verify` |
| `R11 นางสาว Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` |
| `R2 Dr. Mrs. Somsri Boonmee - Do Not Advance` | `R2 Somsri Boonmee - Do Not Advance` |
| `R3 Msaki Tanaka - Advance` | unchanged (`Ms` not followed by `.` or space) |
| `R5 Drew Nakamura - Advance` | unchanged |
| `R6 PUPAT CHATAMEENA - Advance` | unchanged |
| any non-header line containing `Mr.` | unchanged |

Note the `Msaki` / `Drew` cases: the token must be followed by `.`, whitespace,
or end of the token boundary — never a bare prefix match.

## Ratification

Same shape as the pipeline fixes: diff against the deployed `render.py`,
tests listed above run and reported, sha256 of the result. The master thread
records it as FRONTEND-FIX-01.
