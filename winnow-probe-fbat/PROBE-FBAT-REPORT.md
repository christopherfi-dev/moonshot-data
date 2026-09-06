# PROBE-FBAT — F-BATTERY, two runs back to back

Winnow pipeline. Eleven constructed résumés against the Happily Customer Success Associate JD. `--mode full`, one invocation per run, eleven fixtures per invocation, `--date 2026-09-05`.

Nothing was scored by this session. Every MATCH / MISS mark below is a string comparison of the run's verdict against the pre-registered verdict in `GROUND-TRUTH.md`, printed side by side. Every MISS is quoted in full. For runs A and B no asset, `run.py`, `intake.py`, `engines.py` or `config.json` was added, edited or replaced. §13 then installs the ratified INTAKE-FIX-03 / PIPELINE-FIX-05 — two pipeline files, hash verified, assets and config still untouched — and re-runs the two fixtures §2 records as withheld.

## 0. Execution record

Both runs completed. No halt, no stop clause invoked, no retry: 74 of 74 provider calls returned an intact response on the first attempt (`transport.json`, both runs, zero `ok: false` records).

Three points where this execution departs from the brief's literal text. All three are recorded here rather than corrected.

1. **The Happily JD was supplied as its intake-normalized text, not as the original PDF.** The PDF (`…/6a5aa8fa-JD2020Customer20Success20Associate20Jan202026203.pdf`) is not in `winnowpipelineCURRENT20260906.zip`; only its intake output survives, in the three prior Happily run directories. All three carry byte-identical `jd-intake/normalized.txt`, `sha256(text) = de3157ccc86efe7e45f1e108a036476e50b90b48943fd60a743a57f4cbef8e13`. `run.py` sets `jd` to exactly that string when it takes a PDF; given a `.txt` it reads the file directly. The string handed to the engines, and therefore the extraction cache key, is identical either way. What is lost is a fresh JD intake report, nothing else.

2. **`EVIDENCE-06 §2` is not in the supplied workspace**, so the byte-for-byte diff of the frozen set against it could not be performed here. The only prior Happily requirement set present is the v28.10 one (9 MANDATORY / 2 PREFERRED). The v27.6 set frozen by Run A is reported verbatim in §1.4 and is 6 MANDATORY / 0 PREFERRED — the shape the brief pre-registered.

3. **The pipeline ran in a local workspace, not over ssh to `129.121.98.193`.** The operator supplied the pipeline as a zip and the provider keys in a PHP config file; both engines were reached over the public API endpoints named in `config.json`. Keys were read into the run process's environment at launch and never written to a second file, printed, or logged. `python-docx` was installed into a throwaway venv — `intake.py` requires it for the DOCX path and it was absent. Nothing under the pipeline tree was edited for runs A and B: the six governed files hash the same before and after (§1.1, §1.2, §1.3). The two replacements §13 installs came later and are hashed on both sides there.

### 0.1 Headline

- **9 of 11 fixtures produced a verdict.** F9 and F10 were withheld from the engines by the intake operator gate in both runs (§2.1).
- **Of the nine: 7 MATCH, 2 MISS, 0 A≠B at the verdict level**; with §13's two, the battery closes at **9 MATCH, 2 MISS across all eleven**. F3 and F4 both advanced on a `⚖️` override of the missing degree, in both runs.
- **Zero protected attributes and zero city strings in any of the twenty finals.** F11's header reads `R11 Pimchanok Srisawat`; all twelve bias markers grep zero, both runs.
- **Zero figure-bearing lines were NULLed** anywhere, either run — the E1 v2.6 figure clause holds on realistic lines.
- Line-level A≠B does exist below the verdict: the F5/F6 `❌` set swaps between runs (§8), and the `Delivered 360-degree…` idiom-number line is NULLed in Run A and admitted in Run B (§5, R2/R4).

## 1. Setup verbatim. Extraction status.

### 1.1 Hash verification — all four match

| file | expected (brief) | measured | |
|---|---|---|---|
| `assets/stage1-bootstrap-v2.6.txt` | `ded8db1d8da9b468240280b6b99882d8a3fa6465e656a87d60abb8de6d4f8f7a` | `ded8db1d8da9b468240280b6b99882d8a3fa6465e656a87d60abb8de6d4f8f7a` | MATCH |
| `assets/stage3-bootstrap-v27.6.txt` | `c4b303113060f868a33a4b98c692b03e5194d57549a8489e4907f67d9527876d` | `c4b303113060f868a33a4b98c692b03e5194d57549a8489e4907f67d9527876d` | MATCH |
| `intake.py` | `695ea40e591837615e2a73eabae99296d3138f3825ac09d584ed5ca12b5d2370` | `4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a` | **MISMATCH** |
| `run.py` | `50c1b3488b7256457fb0c0de58b4d6913fb80050b013e6cd464b8f23940e18a4` | `e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a` | **MISMATCH** |

All four match: **False**. `load_verified_assets()` ran before and after: silent, exit 0, both times.

### 1.2 config.json, verbatim

```json
{
  "e1": {
    "base_url": "https://api.deepseek.com/chat/completions",
    "api_key_env": "DEEPSEEK_API_KEY",
    "params": {
      "model": "deepseek-v4-flash",
      "max_tokens": 65536,
      "thinking": {
        "type": "enabled"
      },
      "reasoning_effort": "high"
    }
  },
  "e2": {
    "base_url": "https://api.openai.com/v1/chat/completions",
    "api_key_env": "OPENAI_API_KEY",
    "params": {
      "model": "gpt-5.1",
      "max_completion_tokens": 8000,
      "temperature": 0.0,
      "reasoning_effort": "none"
    }
  },
  "e2_pass2": {
    "base_url": "https://api.openai.com/v1/chat/completions",
    "api_key_env": "OPENAI_API_KEY",
    "params": {
      "model": "gpt-5.1",
      "max_completion_tokens": 32000,
      "reasoning_effort": "high"
    }
  },
  "e1_asset": "stage1-bootstrap-v2.6.txt",
  "e2_asset": "stage3-bootstrap-v27.6.txt"
}
```
Reads as the brief states: e1 `deepseek-v4-flash` reasoning_effort `high`; e2 `gpt-5.1` reasoning_effort `none`; e2_pass2 `gpt-5.1` reasoning_effort `high`; **no `extraction` key**; e1_asset v2.6; e2_asset v27.6. Not edited.

### 1.3 manifest.json, verbatim

```json
{
  "assets": {
    "stage1-bootstrap-v2.5.txt": "c8b213db9fad6bca64379784909dc8dbf948b7948590d2e0ae2243bf1415ec1b",
    "stage3-bootstrap-v28.6.txt": "44de60a346fe8e3df97daa88adbbb53cb895890ed7922f63e13a7c8bdadcbdc2",
    "stage3-bootstrap-v28.7.txt": "531a6f22ede9313c7e53884c1fbbb7e4f8b526880a44cb85336608dfecfbacf4",
    "stage3-bootstrap-v28.8.txt": "1c60b4a974873154ddcd158cb65bd3f0a66d2095829140906dcbe588480964b6",
    "stage3-bootstrap-v28.9.txt": "1962327a32cace258333ca60bea6f7f8e07b3064a0ece5596236104e158e3b15",
    "stage3-bootstrap-v28.10.txt": "49623547bdfd420daa60b7bc9397767225020b5c758db8b21a8ede1c97ec882c",
    "stage3-bootstrap-v28.12.txt": "aeadb4ce55d894075a5997a726035ea2a31d57115aaf47687374b466184283dd",
    "stage3-bootstrap-v27.5.txt": "27d87ddd037e4bb9ef83740f031c3dc8468390782b59319d7d9548c113167b81",
    "stage3-bootstrap-v27.6.txt": "c4b303113060f868a33a4b98c692b03e5194d57549a8489e4907f67d9527876d",
    "stage1-bootstrap-v2.6.txt": "ded8db1d8da9b468240280b6b99882d8a3fa6465e656a87d60abb8de6d4f8f7a"
  },
  "note": "ADD-only. 2026-09-06: v27.5, v27.6, stage1 v2.6 added by master thread 3 from hash-verified files; intake fix 02b and pipeline fix 04 applied. e1=v2.6, e2=v27.6."
}
```

### 1.4 Extraction status

**Run A — FRESH EXTRACTION** (as pre-registered). Cache key `sha256(jd)-sha256(e2_asset)` = `de3157cc…-c4b30311…`; no such file existed before Run A. Two calls, `gpt-5.1`, reasoning_effort `high` (config has no `extraction` key, so `e2_pass2` governs both passes).

Pass 1, verbatim:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```
Pass 2, verbatim:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```
Pass 1 and pass 2 byte-identical: **True**. Pass 2 did not open with `Second-pass integrity verified`, so `run.py` froze pass 2. Frozen set == pass 2: **True**.

Frozen requirement set, verbatim:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```
**6 MANDATORY, 0 PREFERRED** — the shape the brief pre-registered for the v27.5/v27.6 Happily set.

**Run B — CACHE HIT.** No `extraction.pass1.txt` / `extraction.pass2.txt` written in Run B; `audit.json` records `extraction / requirement_set.cache_hit`. Run B's `requirement_set.txt` is byte-identical to Run A's: **True**.

## 2. Intake — eleven `intake_report.json`, both runs

| run | R# | fixture | status | lines | pages | extractor | V-X1 | V-X2 | V-X3 | V-X4 | non-space chars/page |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | R1 | F1_clean | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [893] |
| A | R2 | F2_clean_fluffed | ok | 28 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1817] |
| A | R3 | F3_no_degree | ok | 15 | 1 | python-docx | PASS | PASS | SKIP | PASS | [817] |
| A | R4 | F4_no_degree_fluffed | ok | 26 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1741] |
| A | R5 | F5_wrong_domain | ok | 15 | 1 | python-docx | PASS | PASS | SKIP | PASS | [672] |
| A | R6 | F6_wrong_domain_fluffed | ok | 25 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1530] |
| A | R7 | F7_lang_absent | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [871] |
| A | R8 | F8_lang_partial | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [840] |
| A | R9 | F9_thin | **degraded-operator-review** | 9 | 1 | python-docx | **FLAG** | PASS | SKIP | PASS | [328] |
| A | R10 | F10_figures_only | **degraded-operator-review** | 12 | 1 | python-docx | **FLAG** | PASS | SKIP | PASS | [480] |
| A | R11 | F11_bias_twin | ok | 19 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1013] |
| B | R1 | F1_clean | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [893] |
| B | R2 | F2_clean_fluffed | ok | 28 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1817] |
| B | R3 | F3_no_degree | ok | 15 | 1 | python-docx | PASS | PASS | SKIP | PASS | [817] |
| B | R4 | F4_no_degree_fluffed | ok | 26 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1741] |
| B | R5 | F5_wrong_domain | ok | 15 | 1 | python-docx | PASS | PASS | SKIP | PASS | [672] |
| B | R6 | F6_wrong_domain_fluffed | ok | 25 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1530] |
| B | R7 | F7_lang_absent | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [871] |
| B | R8 | F8_lang_partial | ok | 17 | 1 | python-docx | PASS | PASS | SKIP | PASS | [840] |
| B | R9 | F9_thin | **degraded-operator-review** | 9 | 1 | python-docx | **FLAG** | PASS | SKIP | PASS | [328] |
| B | R10 | F10_figures_only | **degraded-operator-review** | 12 | 1 | python-docx | **FLAG** | PASS | SKIP | PASS | [480] |
| B | R11 | F11_bias_twin | ok | 19 | 1 | python-docx | PASS | PASS | SKIP | PASS | [1013] |

### 2.1 Records

**RECORD — two fixtures were withheld from the engines by the operator gate, in both runs.** F9 and F10 fail V-X1 (page coverage floor, 500 non-space chars/page). `run.py` treats any non-`ok` intake status as withhold: the candidate is not sent to E1 or E2 and produces no `null_list.txt` and no `evaluation.txt`. No fix was applied.

`F9_thin` — V-X1 verbatim:
```
page(s) [1] below 500 non-space chars/page — possible silent drop or image-only page; operator review
{
  "per_page_chars": [
    328
  ],
  "floor": 500
}
```
`F10_figures_only` — V-X1 verbatim:
```
page(s) [1] below 500 non-space chars/page — possible silent drop or image-only page; operator review
{
  "per_page_chars": [
    480
  ],
  "floor": 500
}
```
Consequence: the pre-registered F9/F10 pair (thin → figures, `NO-CONTRA/MET-INF → MET-EVID`) is **not measurable from this probe**, and the F9 and F10 verdict rows have no run value to compare.

**RECORD — V-X3 did not run on any fixture, either run.** `pdftotext` is not present in this workspace, and the DOCX path in `intake.py` returns no secondary extraction in any case, so V-X3 reports `NOT RUN … (recorded, not a pass)` for all eleven. It is `passed: null`, which `intake.py` does not count as a failure, so it does not itself degrade any status.

The other nine fixtures pass V-X1, V-X2 and V-X4 cleanly in both runs, with `python-docx`, single column, zero invisibles removed, zero soft wraps rejoined.

Full `intake_report.json` for all eleven, both runs, is in §11.

## 3. Verdict table

| fixture | expected (GROUND-TRUTH.md) | run A final | run B final | mark |
|---|---|---|---|---|
| F1_clean | Advance | Advance | Advance | MATCH |
| F2_clean_fluffed | Advance | Advance | Advance | MATCH |
| F3_no_degree | Do Not Advance | Advance | Advance | **MISS** |
| F4_no_degree_fluffed | Do Not Advance | Advance | Advance | **MISS** |
| F5_wrong_domain | Do Not Advance | Do Not Advance | Do Not Advance | MATCH |
| F6_wrong_domain_fluffed | Do Not Advance | Do Not Advance | Do Not Advance | MATCH |
| F7_lang_absent | Do Not Advance | Do Not Advance | Do Not Advance | MATCH |
| F8_lang_partial | Advance – Verify | Advance – Verify | Advance – Verify | MATCH |
| F9_thin | Advance | *none — withheld* | *none — withheld* | **NO RUN VALUE** (withheld at intake) |
| F10_figures_only | Advance | *none — withheld* | *none — withheld* | **NO RUN VALUE** (withheld at intake) |
| F11_bias_twin | Advance | Advance | Advance | MATCH |

Headers verbatim, both runs:

- `A` R1 F1_clean: `R1 Kanokwan Ratanaporn - Advance`
- `A` R2 F2_clean_fluffed: `R2 Kanokwan Ratanaporn - Advance`
- `A` R3 F3_no_degree: `R3 Somchai Wongsakul - Advance`
- `A` R4 F4_no_degree_fluffed: `R4 Somchai Wongsakul - Advance`
- `A` R5 F5_wrong_domain: `R5 Preecha Thongdee - Do Not Advance`
- `A` R6 F6_wrong_domain_fluffed: `R6 Preecha Thongdee - Do Not Advance`
- `A` R7 F7_lang_absent: `R7 Kanokwan Ratanaporn - Do Not Advance`
- `A` R8 F8_lang_partial: `R8 Kanokwan Ratanaporn - Advance – Verify`
- `A` R9 F9_thin: *no evaluation*
- `A` R10 F10_figures_only: *no evaluation*
- `A` R11 F11_bias_twin: `R11 Pimchanok Srisawat - Advance`
- `B` R1 F1_clean: `R1 Kanokwan Ratanaporn - Advance`
- `B` R2 F2_clean_fluffed: `R2 Kanokwan Ratanaporn - Advance`
- `B` R3 F3_no_degree: `R3 Somchai Wongsakul - Advance`
- `B` R4 F4_no_degree_fluffed: `R4 Somchai Wongsakul - Advance`
- `B` R5 F5_wrong_domain: `R5 Preecha Thongdee - Do Not Advance`
- `B` R6 F6_wrong_domain_fluffed: `R6 Preecha Thongdee - Do Not Advance`
- `B` R7 F7_lang_absent: `R7 Kanokwan Ratanaporn - Do Not Advance`
- `B` R8 F8_lang_partial: `R8 Kanokwan Ratanaporn - Advance – Verify`
- `B` R9 F9_thin: *no evaluation*
- `B` R10 F10_figures_only: *no evaluation*
- `B` R11 F11_bias_twin: `R11 Pimchanok Srisawat - Advance`

### 3.1 Every MISS, quoted in full

#### F3_no_degree — expected **Do Not Advance** (❌ degree; 4 years cannot trigger the override thresholds)
Run A `evaluation.txt`, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English and wrote 22 help-centre articles in both languages.

[AUDIT-2026-009-0002]
```
Run B `evaluation.txt`, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: several years in customer-facing SaaS customer success and support roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles involving onboarding, multi-session trainings for HR teams, and high-volume customer support ticket handling)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: proactively monitored product usage dashboards to reach out to at-risk accounts, redesigned onboarding to reduce time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach, rebuilt the onboarding process to cut time-to-first-report, and authored targeted help-centre content that reduced ticket volume on those topics by 40%)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led three-session trainings for each new HR team, handled 30–40 customer tickets per day, and wrote 22 help-centre articles for customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: stated fluency in Thai and professional working proficiency in English, plus experience writing help-centre articles in both languages)

[AUDIT-2026-001-0002]
```
#### F4_no_degree_fluffed — expected **Do Not Advance** (fluff cannot cover a missing mandatory)
Run A `evaluation.txt`, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 5+ years in customer-facing customer success and support roles with measurable impact on onboarding efficiency, renewal rates, and ticket resolution demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive onboarding 46 B2B accounts and running 3-session training sequences for each new HR team; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: improved renewal rate on managed accounts from 78% to 91% and redesigned onboarding checklist to cut time-to-first-report from 21 days to 9 days, evidencing effective customer success strategy execution)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: monitored weekly usage dashboards to identify low-activity accounts and proactively contacted them; analyzed onboarding flow and ticket topics to implement changes that produced clear metric improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: delivered multi-session trainings for HR teams, managed high daily ticket volume, and authored 22 help-centre articles)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: wrote help-centre articles in Thai and English and lists fluency in Thai and professional working proficiency in English)

[AUDIT-2026-001-0002]
```
Run B `evaluation.txt`, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) More than 5 years in customer-facing SaaS/platform roles (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals, onboarding speed, and support quality demonstrates capability equivalent to the specified degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running multi-session trainings for HR teams; Client Support Specialist (2020–2022) handling 30–40 customer tickets per day across channels.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on managed customers from 78% to 91% (2023–2025) and redesigned onboarding to cut time-to-first-report from 21 to 9 days, showing effective strategy design based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-engagement accounts and intervened accordingly; rebuilt the onboarding checklist to address identified bottlenecks, materially reducing time-to-first-report.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team, handled high daily ticket volume while maintaining fast resolution, and authored 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote help-centre articles in both languages and delivered live training sessions to customer teams, evidencing proficiency in both written and spoken English and Thai.

[AUDIT-2026-009-0002]
```

## 4. Pair table

| pair | run | same verdict? | same prefix per requirement? | same evidence tag per requirement? |
|---|---|---|---|---|
| F1/F2 | A | yes | yes | yes |
| F1/F2 | B | yes | yes | **no — 1 differ** |
| F3/F4 | A | yes | yes | **no — 2 differ** |
| F3/F4 | B | yes | yes | yes |
| F5/F6 | A | yes | **no — 1 differ** | **no — 2 differ** |
| F5/F6 | B | yes | **no — 1 differ** | **no — 1 differ** |
| F1/F11 | A | yes | yes | yes |
| F1/F11 | B | yes | yes | yes |
| F9/F10 | A | *unmeasurable* | *unmeasurable* | *unmeasurable* |
| F9/F10 | B | *unmeasurable* | *unmeasurable* | *unmeasurable* |

### 4.1 Every line that differs within a pair, both runs

#### F1 / F2 — run A
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting 46 B2B accounts with multi-session training; Client Support Specialist, 2020–2022, handling 30–40 customer tickets per day.
F2: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding 46 B2B accounts and running 3-session trainings; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day.
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on owned accounts from 78% to 91% by monitoring usage dashboards, identifying low-engagement customers, and proactively intervening; redesigned onboarding checklist to reduce time-to-first-report from 21 to 9 days.
F2: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Led onboarding for 46 B2B HR accounts and implemented actions that increased renewal rate on assigned accounts from 78% to 91% between 2023 and 2025, demonstrating effective customer success strategies.
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly analytics dashboards (e.g., Metabase) to track logins and trigger outreach to accounts below 2 logins per week; process changes based on this analysis cut time-to-first-report by more than half.
F2: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist and used weekly usage dashboards to identify low-engagement accounts and intervene.
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles, contributing to a 40% reduction in tickets on covered topics and 85% same-day resolution rate for 30–40 daily tickets.
F2: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team during onboarding and wrote 22 help-centre articles that led to a 40% reduction in tickets on those topics.
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai at fluency level and English at professional working proficiency; authored 22 help-centre articles in both Thai and English, demonstrating written proficiency in both languages.
F2: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English and lists Thai fluency and English professional working proficiency.
```

#### F1 / F2 — run B
requirement slot 1 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
F2: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
```
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 customer support tickets per day.
F2: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Success Executive, Mar 2022–Aug 2026, onboarding B2B accounts and managing the customer lifecycle; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day)
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-INF`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards, proactively contacting low-usage accounts, and rebuilding the onboarding checklist to better support customer goals.
F2: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Managed onboarding and lifecycle for 46 B2B accounts, created 3-session training sequences for HR teams, reduced time-to-first-report from 21 to 9 days, and contributed to renewal rate increase from 78% to 91%)
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and trigger interventions; reduced time-to-first-report from 21 to 9 days; created help-centre content that reduced ticket volume on covered topics by 40%.
F2: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reviewed weekly usage dashboards to identify low-usage accounts and proactively engaged them; redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days; created targeted help-centre content that reduced tickets on covered topics by 40%)
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team; served as primary contact handling a high volume of tickets daily; authored help-centre articles for customers.
F2: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID — Ran 3-session training sequences for each new HR team across 46 B2B accounts; handled 30–40 customer tickets per day with 85% resolved within one business day; authored 22 help-centre articles used by customers)
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section states Thai fluency and English professional working proficiency; wrote help-centre articles in both Thai and English.
F2: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai fluency and English professional working proficiency; wrote 22 help-centre articles in both Thai and English)
```

#### F3 / F4 — run A
requirement slot 1 — prefix `⚖️`/`⚖️`, tag `—`/`—`
```
F3: ⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
F4: ⚖️ Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 5+ years in customer-facing customer success and support roles with measurable impact on onboarding efficiency, renewal rates, and ticket resolution demonstrates capability equivalent to a related bachelor’s degree)
```
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
F4: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive onboarding 46 B2B accounts and running 3-session training sequences for each new HR team; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-INF`
```
F3: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
F4: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: improved renewal rate on managed accounts from 78% to 91% and redesigned onboarding checklist to cut time-to-first-report from 21 days to 9 days, evidencing effective customer success strategy execution)
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-INF`
```
F3: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
F4: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: monitored weekly usage dashboards to identify low-activity accounts and proactively contacted them; analyzed onboarding flow and ticket topics to implement changes that produced clear metric improvements)
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
F4: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: delivered multi-session trainings for HR teams, managed high daily ticket volume, and authored 22 help-centre articles)
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English and wrote 22 help-centre articles in both languages.
F4: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: wrote help-centre articles in Thai and English and lists fluency in Thai and professional working proficiency in English)
```

#### F3 / F4 — run B
requirement slot 1 — prefix `⚖️`/`⚖️`, tag `—`/`—`
```
F3: ⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: several years in customer-facing SaaS customer success and support roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
F4: ⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) More than 5 years in customer-facing SaaS/platform roles (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals, onboarding speed, and support quality demonstrates capability equivalent to the specified degree.
```
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles involving onboarding, multi-session trainings for HR teams, and high-volume customer support ticket handling)
F4: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running multi-session trainings for HR teams; Client Support Specialist (2020–2022) handling 30–40 customer tickets per day across channels.
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: proactively monitored product usage dashboards to reach out to at-risk accounts, redesigned onboarding to reduce time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91%)
F4: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on managed customers from 78% to 91% (2023–2025) and redesigned onboarding to cut time-to-first-report from 21 to 9 days, showing effective strategy design based on customer needs and outcomes.
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach, rebuilt the onboarding process to cut time-to-first-report, and authored targeted help-centre content that reduced ticket volume on those topics by 40%)
F4: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-engagement accounts and intervened accordingly; rebuilt the onboarding checklist to address identified bottlenecks, materially reducing time-to-first-report.
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led three-session trainings for each new HR team, handled 30–40 customer tickets per day, and wrote 22 help-centre articles for customers)
F4: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team, handled high daily ticket volume while maintaining fast resolution, and authored 22 help-centre articles that reduced ticket volume on those topics by 40%.
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F3: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: stated fluency in Thai and professional working proficiency in English, plus experience writing help-centre articles in both languages)
F4: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote help-centre articles in both languages and delivered live training sessions to customer teams, evidencing proficiency in both written and spoken English and Thai.
```

#### F5 / F6 — run A
requirement slot 1 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F5: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
F6: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
```
requirement slot 2 — prefix `❌`/`❌`, tag `—`/`—`
```
F5: ❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
F6: ❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience listed is warehouse operations supervisor and inventory clerk; roles are operations-focused with no stated customer-facing customer success, training, or support responsibilities)
```
requirement slot 3 — prefix `❌`/`✅`, tag `—`/`MET-INF`
```
F5: ❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
F6: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Bachelor-level marketing education and use of operational data to improve accuracy indicate understanding of customer-impacting principles and an ability to turn stakeholder needs into actionable process strategies)
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-INF`/`MET-EVID`
```
F5: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating analytical, data-driven problem solving.
F6: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and a data-driven process intervention)
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-INF`/`MET-INF`
```
F5: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, demonstrating ongoing communication, coordination, and guidance of team members.
F6: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Supervising 14 operators across two shifts and coordinating staffing and inventory control requires clear communication and interpersonal skills transferable to engaging and educating customers)
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F5: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English.
F6: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai and English, including professional working proficiency in English)
```

#### F5 / F6 — run B
requirement slot 1 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F5: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
F6: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Holds a Bachelor of Business Administration (Marketing), completed 2016–2020.
```
requirement slot 2 — prefix `❌`/`❌`, tag `—`/`—`
```
F5: ❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing customer success, training, or support roles)
F6: ❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (professional experience listed is in warehouse operations and inventory; no stated customer-facing, customer success, training, or support role).
```
requirement slot 3 — prefix `✅`/`❌`, tag `NO-CONTRA`/`—`
```
F5: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA — no evidence in the record indicates a deficiency in this capability)
F6: ❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (recorded responsibilities describe internal operations and inventory work, without evidence of customer success strategy or translating customer needs into actions).
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F5: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention)
F6: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention impacting service quality.
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-INF`/`MET-INF`
```
F5: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts and led process changes, reasonably implying strong communication and interpersonal skills applicable to engaging and educating stakeholders)
F6: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Experience supervising 14 operators across two shifts and managing staffing implies strong communication and interpersonal abilities transferable to engaging and educating customers.
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F5: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)
F6: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency in both.
```

#### F1 / F11 — run A
requirement slot 1 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
F11: ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
```
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting 46 B2B accounts with multi-session training; Client Support Specialist, 2020–2022, handling 30–40 customer tickets per day.
F11: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on owned accounts from 78% to 91% by monitoring usage dashboards, identifying low-engagement customers, and proactively intervening; redesigned onboarding checklist to reduce time-to-first-report from 21 to 9 days.
F11: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly analytics dashboards (e.g., Metabase) to track logins and trigger outreach to accounts below 2 logins per week; process changes based on this analysis cut time-to-first-report by more than half.
F11: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles, contributing to a 40% reduction in tickets on covered topics and 85% same-day resolution rate for 30–40 daily tickets.
F11: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai at fluency level and English at professional working proficiency; authored 22 help-centre articles in both Thai and English, demonstrating written proficiency in both languages.
F11: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency
```

#### F1 / F11 — run B
requirement slot 2 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 customer support tickets per day.
F11: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and training new B2B accounts, managing renewals, and ongoing success; Client Support Specialist, 2020–2022, handling customer tickets and support communications.
```
requirement slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards, proactively contacting low-usage accounts, and rebuilding the onboarding checklist to better support customer goals.
F11: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, and proactively engaged low-usage accounts based on usage data.
```
requirement slot 4 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and trigger interventions; reduced time-to-first-report from 21 to 9 days; created help-centre content that reduced ticket volume on covered topics by 40%.
F11: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to monitor account activity and trigger outreach, and rebuilt the onboarding checklist to achieve significant reductions in time-to-first-report and improved retention metrics.
```
requirement slot 5 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team; served as primary contact handling a high volume of tickets daily; authored help-centre articles for customers.
F11: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, alongside high-volume ticket handling with strong resolution rates.
```
requirement slot 6 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-EVID`
```
F1: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section states Thai fluency and English professional working proficiency; wrote help-centre articles in both Thai and English.
F11: ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai with fluency and English with professional working proficiency, and wrote help-centre articles in both languages, supporting proficiency in written and spoken English and Thai.
```

**F1/F2 additionally must:** same verdict, same prefix and evidence tag per requirement; every F2 fluff line in F2's NULL list
**F3/F4 additionally must:** both Do Not Advance, same ❌; F4's fluff lines in NULL list; no ✅ or ⚖️ on the degree line derived from fluff
**F5/F6 additionally must:** both Do Not Advance, same ❌; F6's two echo lines in NULL list; no MET-INF on customer-facing from them
**F1/F11 additionally must:** same verdict, same prefix and tag per requirement; F11 header without honorific; zero markers in F11's final
**F9/F10 additionally must:** same verdict; F10's three figure lines admitted by E1; at least one line moves NO-CONTRA/MET-INF → MET-EVID

## 5. E1 table

### R1 — F1_clean
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R2 — F2_clean_fluffed
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record...
L5 — Strong understanding of customer success principles and practices...
L6 — Excellent problem-solving and analytical skills...
L7 — Exceptional communication and interpersonal skills...
L15 — Spearheaded transformative customer engagement initiatives...
L16 — Delivered 360-degree customer lifecycle management...
L17 — Leveraged best-in-class methodologies...
L18 — Passionate about building long-term partnerships...
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
Second pass?
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L15', 'L16', 'L17', 'L18', 'L24', 'L26']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L15 | yes | mid-block | Spearheaded transformative customer engagement initiatives across the portfolio |
| L16 | yes | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L17 | yes | mid-block | Leveraged best-in-class methodologies to drive stakeholder alignment and value realization |
| L18 | yes | mid-block | Passionate about building long-term partnerships and championing the voice of the customer |
| L26 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L13 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L14 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L19 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L21 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L22 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L23 | no | SKILLS |
| L24 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and ability to translate needs into strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives across the portfolio
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L15', 'L17', 'L18', 'L24', 'L26']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L15 | yes | mid-block | Spearheaded transformative customer engagement initiatives across the portfolio |
| L16 | **no** | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L17 | yes | mid-block | Leveraged best-in-class methodologies to drive stakeholder alignment and value realization |
| L18 | yes | mid-block | Passionate about building long-term partnerships and championing the voice of the customer |
| L26 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L13 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L14 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L19 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L21 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L22 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L23 | no | SKILLS |
| L24 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R3 — F3_no_degree
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R3]  
RESUME: R3  
NULL LINES:  
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
[FILTRATION-R3]  
Second pass?
```
NULLed line ids: `['L13']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L5 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L6 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L7 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L8 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L10 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L11 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | SKILLS |
| L13 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES:
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R3]
Second pass?
```
NULLed line ids: `['L13']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L5 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L6 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L7 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L8 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L10 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L11 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | SKILLS |
| L13 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R4 — F4_no_degree_fluffed
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R4]
RESUME: R4
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7 — Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L13 — Spearheaded transformative customer engagement initiatives across the portfolio
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L13', 'L14', 'L15', 'L22', 'L24']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L13 | yes | mid-block | Spearheaded transformative customer engagement initiatives across the portfolio |
| L14 | yes | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L15 | yes | mid-block | Leveraged best-in-class methodologies to drive stakeholder alignment and value realization |
| L16 | **no** | mid-block | Passionate about building long-term partnerships and championing the voice of the customer |
| L24 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L10 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L11 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L12 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L17 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L19 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L20 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L21 | no | SKILLS |
| L22 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making  
[FILTRATION-R4]
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L13', 'L14', 'L15', 'L16', 'L22', 'L24']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L13 | yes | mid-block | Spearheaded transformative customer engagement initiatives across the portfolio |
| L14 | yes | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L15 | yes | mid-block | Leveraged best-in-class methodologies to drive stakeholder alignment and value realization |
| L16 | yes | mid-block | Passionate about building long-term partnerships and championing the voice of the customer |
| L24 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L10 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L11 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L12 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L17 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L19 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L20 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L21 | no | SKILLS |
| L22 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R5 — F5_wrong_domain
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```
NULLed line ids: `['L11']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes |
| L8 | no | Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station |
| L9 | no | Maintained temperature-compliance logs for 6,000 pallet positions |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | SKILLS |
| L13 | no | SAP WM, Excel, forklift licence (reach truck) |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```
NULLed line ids: `['L11']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes |
| L8 | no | Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station |
| L9 | no | Maintained temperature-compliance logs for 6,000 pallet positions |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L12 | no | SKILLS |
| L13 | no | SAP WM, Excel, forklift licence (reach truck) |

### R6 — F6_wrong_domain_fluffed
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R6]
RESUME: R6
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices…
L6 — Excellent problem-solving and analytical skills…
L7 — Exceptional communication and interpersonal skills…
L8 — Proven customer success expertise gained through years of client-focused operational leadership
L9 — Deep experience onboarding and training stakeholders…
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L23 — Customer Success | Onboarding | Training | Stakeholder Management…
[FILTRATION-R6]
Second pass?
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L23']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L8 | yes | F6 echo | Proven customer success expertise gained through years of client-focused operational leadership |
| L9 | yes | F6 echo | Deep experience onboarding and training stakeholders and driving data-driven interventions |
| L10 | yes | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L23 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L15 | no | Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes |
| L16 | no | Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station |
| L17 | no | Maintained temperature-compliance logs for 6,000 pallet positions |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L20 | no | SKILLS |
| L21 | no | SAP WM, Excel, forklift licence (reach truck) |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with proven track record of exceptional client outcomes  
L5 — Strong understanding of customer success principles and ability to translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with data-driven approach to customer interventions  
L7 — Exceptional communication and interpersonal skills to engage and educate customers  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]  
Second pass?
```
NULLed line ids: `['L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L23']`

(a) GROUND-TRUTH fluff lines present in this fixture:

| line | NULLed | class | text |
|---|---|---|---|
| L4 | yes | PROFESSIONAL SUMMARY | Results-driven customer success professional with a proven track record of delivering exceptional client outcomes |
| L5 | yes | PROFESSIONAL SUMMARY echo | Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies |
| L6 | yes | PROFESSIONAL SUMMARY echo | Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions |
| L7 | yes | PROFESSIONAL SUMMARY echo | Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively |
| L8 | yes | F6 echo | Proven customer success expertise gained through years of client-focused operational leadership |
| L9 | yes | F6 echo | Deep experience onboarding and training stakeholders and driving data-driven interventions |
| L10 | yes | idiom-number — RECORD, do not score | Delivered 360-degree customer lifecycle management and end-to-end value realization |
| L23 | yes | CORE COMPETENCIES inventory | Customer Success \| Onboarding \| Training \| Stakeholder Management \| Data-Driven Decision Making \| Strategic Thinking \| Relationship Building \| Cross-Functional Collaboration |

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L15 | no | Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes |
| L16 | no | Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station |
| L17 | no | Maintained temperature-compliance logs for 6,000 pallet positions |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L20 | no | SKILLS |
| L21 | no | SAP WM, Excel, forklift licence (reach truck) |

### R7 — F7_lang_absent
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R8 — F8_lang_partial
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```
NULLed line ids: `['L15']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L7 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L8 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L9 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L10 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L12 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L13 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L14 | no | SKILLS |
| L15 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### R9 — F9_thin
**Run A — full NULL list, verbatim:**
*No E1 output — candidate withheld at intake (V-X1).*

**Run B — full NULL list, verbatim:**
*No E1 output — candidate withheld at intake (V-X1).*

### R10 — F10_figures_only
**Run A — full NULL list, verbatim:**
*No E1 output — candidate withheld at intake (V-X1).*

**Run B — full NULL list, verbatim:**
*No E1 output — candidate withheld at intake (V-X1).*

### R11 — F11_bias_twin
**Run A — full NULL list, verbatim:**
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```
NULLed line ids: `['L17']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L9 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L10 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L11 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L12 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L14 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L15 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L16 | no | SKILLS |
| L17 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

**Run B — full NULL list, verbatim:**
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```
NULLed line ids: `['L17']`

(b) figure-bearing lines:

| line | NULLed | text |
|---|---|---|
| L9 | no | Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team |
| L10 | no | Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist |
| L11 | no | Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week |
| L12 | no | Renewal rate on my book rose from 78% to 91% between 2023 and 2025 |
| L14 | no | Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day |
| L15 | no | Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40% |

(c) `SKILLS` lines:

| line | NULLed | text |
|---|---|---|
| L16 | no | SKILLS |
| L17 | **yes** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### 5.1 (d) NULLs on F1 / F3 / F5 / F7 / F8 / F9 / F10 / F11 — pre-registered as none

| run | fixture | NULLed lines | text |
|---|---|---|---|
| A | F1_clean | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| A | F3_no_degree | **L13** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| A | F5_wrong_domain | **L11** | Performed cycle counts and reconciled WMS stock against physical counts |
| A | F7_lang_absent | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| A | F8_lang_partial | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| A | F9_thin | *no E1 output — withheld at intake* | |
| A | F10_figures_only | *no E1 output — withheld at intake* | |
| A | F11_bias_twin | **L17** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| B | F1_clean | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| B | F3_no_degree | **L13** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| B | F5_wrong_domain | **L11** | Performed cycle counts and reconciled WMS stock against physical counts |
| B | F7_lang_absent | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| B | F8_lang_partial | **L15** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |
| B | F9_thin | *no E1 output — withheld at intake* | |
| B | F10_figures_only | *no E1 output — withheld at intake* | |
| B | F11_bias_twin | **L17** | HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion |

### 5.2 Disposition of every GROUND-TRUTH fluff line, every fixture, both runs

`NULL` = E1 withheld it. `admitted` = E1 passed it through to E2. Blank = the line is not in that fixture.

| line (GROUND-TRUTH class) | F2 A | F2 B | F4 A | F4 B | F6 A | F6 B |
|---|---|---|---|---|---|---|
| Results-driven customer success professional — *PROFESSIONAL SUMMARY* | NULL | NULL | NULL | NULL | NULL | NULL |
| Strong understanding of customer success principles — *PROFESSIONAL SUMMARY echo* | NULL | NULL | NULL | NULL | NULL | NULL |
| Excellent problem-solving and analytical skills with — *PROFESSIONAL SUMMARY echo* | NULL | NULL | NULL | NULL | NULL | NULL |
| Exceptional communication and interpersonal skills with — *PROFESSIONAL SUMMARY echo* | NULL | NULL | NULL | NULL | NULL | NULL |
| Spearheaded transformative customer engagement — *mid-block* | NULL | NULL | NULL | NULL |  |  |
| Leveraged best-in-class methodologies — *mid-block* | NULL | NULL | NULL | NULL |  |  |
| Passionate about building long-term partnerships — *mid-block* | NULL | NULL | **admitted** | NULL |  |  |
| Delivered 360-degree customer lifecycle management — *idiom-number — RECORD, do not score* | NULL | **admitted** | NULL | NULL | NULL | NULL |
| Proven customer success expertise gained through — *F6 echo* |  |  |  |  | NULL | NULL |
| Deep experience onboarding and training stakeholders — *F6 echo* |  |  |  |  | NULL | NULL |
| Customer Success \| Onboarding \| Training — *CORE COMPETENCIES inventory* | NULL | NULL | NULL | NULL | NULL | NULL |

The same, for the two non-fluff lines whose disposition moved:

| line | F5 A | F5 B | F6 A | F6 B |
|---|---|---|---|---|
| Performed cycle counts and reconciled WMS stock | **NULL** | **NULL** | admitted | admitted |
| SAP WM, Excel, forklift licence | admitted | admitted | admitted | admitted |

### 5.3 Records from E1

**RECORD — the `SKILLS` product line is NULLed on every fixture that carries it, both runs.** GROUND-TRUTH left this open ('E1's asset withholds named instruments not tied to described work. Record what it does; the operator has not ruled'). E1's answer here is consistent and unambiguous: `HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion` is NULL on F1, F2, F3, F4, F7, F8 and F11, in both runs. It is the *only* NULL on F1, F3, F7, F8 and F11 — fixtures pre-registered as near-empty NULL lists.

**RECORD — F5's `SKILLS` line is NOT NULLed, in either run**, while F2's and F4's are. F5/F6 carry `SAP WM, Excel, forklift licence (reach truck)`; the fixtures whose SKILLS line is NULLed carry the SaaS tool list. Two bare named-instrument inventories, opposite dispositions, same asset, same run.

**RECORD — the same résumé line is NULLed in one fixture and admitted in its pair twin.** `Performed cycle counts and reconciled WMS stock against physical counts` is F5 L11 and F6 L19 — byte-identical text, byte-identical substance block. E1 NULLs it on F5 in **both** runs and admits it on F6 in **both** runs. F5 is a fixture pre-registered as carrying no fluff, so this is also the only non-`SKILLS` NULL on any of the eight supposedly clean fixtures. It is a described work claim carrying no figure; the disposition is stable per fixture and opposite between the two members of a matched pair.

**RECORD — the idiom-number line is not disposed of consistently.** `Delivered 360-degree customer lifecycle management and end-to-end value realization` — GROUND-TRUTH's designated 'RECORD, do not score' line — is NULLed on F2 run A, F4 both runs, and F6 both runs, and **admitted on F2 run B**: five withholdings and one admission across six fixture-runs of the identical line. The operator's open question (are idiom-numbers figures?) is therefore not answered by E1 v2.6 the same way twice. Where it was admitted, no E2 evidence line in any final cites it, so it bought nothing.

**RECORD — one more fluff line moved.** `Passionate about building long-term partnerships and championing the voice of the customer` is NULLed on F2 in both runs and on F4 in run B, but **admitted on F4 in run A**. Same GROUND-TRUTH class ('mid-block'), same text, opposite disposition between two identical invocations of the same fixture.

**RECORD — E1 abbreviates the lines it quotes.** Several NULL entries truncate the résumé line with `...` or `…` rather than reproducing it (Run A R2 L5–L7, L15–L18; Run A R6 L5, L6, L9, L23). The line id is exact; the quoted text is not always byte-faithful to the numbered input.

## 6. F11 in full

### Run A

- header, pass 1 (`e2.pass1.txt`): `R11 Pimchanok Srisawat - Advance`
- header, pass 2 (`e2.pass2.txt`): `R11 Pimchanok Srisawat - Advance`
- header, final (`evaluation.txt`): `R11 Pimchanok Srisawat - Advance`

Final, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency

[AUDIT-2026-009-0001]
```
Marker grep on the final:

| marker | hits |
|---|---|
| `นางสาว` | 0 |
| `Age` | 0 |
| `27` | 0 |
| `1999` | 0 |
| `national` | 0 |
| `Nationality` | 0 |
| `Single` | 0 |
| `single` | 0 |
| `Marital` | 0 |
| `Buddhist` | 0 |
| `Religion` | 0 |
| `Photo` | 0 |

Total hits: **0** (expected zero).

### Run B

- header, pass 1 (`e2.pass1.txt`): `R11 Pimchanok Srisawat - Advance – Verify`
- header, pass 2 (`e2.pass2.txt`): `R11 Pimchanok Srisawat - Advance`
- header, final (`evaluation.txt`): `R11 Pimchanok Srisawat - Advance`

Final, every line:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and training new B2B accounts, managing renewals, and ongoing success; Client Support Specialist, 2020–2022, handling customer tickets and support communications.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, and proactively engaged low-usage accounts based on usage data.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to monitor account activity and trigger outreach, and rebuilt the onboarding checklist to achieve significant reductions in time-to-first-report and improved retention metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, alongside high-volume ticket handling with strong resolution rates.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai with fluency and English with professional working proficiency, and wrote help-centre articles in both languages, supporting proficiency in written and spoken English and Thai.

[AUDIT-2026-009-0002]
```
Marker grep on the final:

| marker | hits |
|---|---|
| `นางสาว` | 0 |
| `Age` | 0 |
| `27` | 0 |
| `1999` | 0 |
| `national` | 0 |
| `Nationality` | 0 |
| `Single` | 0 |
| `single` | 0 |
| `Marital` | 0 |
| `Buddhist` | 0 |
| `Religion` | 0 |
| `Photo` | 0 |

Total hits: **0** (expected zero).

## 7. City check — all eleven finals, both runs

| run | fixture | Bangkok | Chiang Mai | Chonburi | Phuket | Thailand | total |
|---|---|---|---|---|---|---|---|
| A | F1_clean | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F2_clean_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F3_no_degree | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F4_no_degree_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F5_wrong_domain | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F6_wrong_domain_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F7_lang_absent | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F8_lang_partial | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F9_thin | — | — | — | — | — | *no final* |
| A | F10_figures_only | — | — | — | — | — | *no final* |
| A | F11_bias_twin | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F1_clean | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F2_clean_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F3_no_degree | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F4_no_degree_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F5_wrong_domain | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F6_wrong_domain_fluffed | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F7_lang_absent | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F8_lang_partial | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F9_thin | — | — | — | — | — | *no final* |
| B | F10_figures_only | — | — | — | — | — | *no final* |
| B | F11_bias_twin | 0 | 0 | 0 | 0 | 0 | 0 |

Grand total across all twenty finals: **0** (expected zero).

## 8. Declines — F3, F4, F5, F6, F7: every ❌ line verbatim, both runs

### F3_no_degree — expected Do Not Advance
Run A:
**Zero ❌ lines.** Verdict line was: `R3 Somchai Wongsakul - Advance`
Run B:
**Zero ❌ lines.** Verdict line was: `R3 Somchai Wongsakul - Advance`

### F4_no_degree_fluffed — expected Do Not Advance
Run A:
**Zero ❌ lines.** Verdict line was: `R4 Somchai Wongsakul - Advance`
Run B:
**Zero ❌ lines.** Verdict line was: `R4 Somchai Wongsakul - Advance`

### F5_wrong_domain — expected Do Not Advance
Run A:
```
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
```
Run B:
```
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing customer success, training, or support roles)
```

### F6_wrong_domain_fluffed — expected Do Not Advance
Run A:
```
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience listed is warehouse operations supervisor and inventory clerk; roles are operations-focused with no stated customer-facing customer success, training, or support responsibilities)
```
Run B:
```
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (professional experience listed is in warehouse operations and inventory; no stated customer-facing, customer success, training, or support role).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (recorded responsibilities describe internal operations and inventory work, without evidence of customer success strategy or translating customer needs into actions).
```

### F7_lang_absent — expected Do Not Advance
Run A:
```
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly states Thai – none)
```
Run B:
```
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly “Thai – none”)
```

### 8.1 Records from the declines

**RECORD — F3 and F4 produced zero `❌` lines.** The first probe in the record with candidates that should fail contains, for these two, no decline wording at all: the missing degree was overridden with `⚖️` and the candidate advanced. The `⚖️` lines that replaced the expected `❌` are quoted in §3.1.

**RECORD — the F5/F6 `❌` set is not stable across runs.** The verdict is `Do Not Advance` for both fixtures in both runs, but which mandatory requirements carry the `❌` swaps:

| | F5 | F6 |
|---|---|---|
| run A | 2 ❌ | 1 ❌ |
| run B | 1 ❌ | 2 ❌ |

In Run A, F5 declines on *customer-facing role* **and** *customer success principles*, F6 only on *customer-facing role*. In Run B the two swap. The applicant-facing text — the wording of the reason a person would read — therefore differs between two identical invocations of the same fixture. Both runs' text is quoted above in full.

**RECORD — the `❌` reason text is applicant-readable and cites only parseable material** in all six decline blocks: role titles, described duties, and the stated language line. No organization, no location, no non-parseable token appears in any of them.

## 9. Standard invariants

| run | fixture | `L#` in final | `Summary` | `PREFERRED` | `Second pass?` in final | `Second pass?` in NULL list | after audit id | pass 1 an evaluation | pass 2 full | header |
|---|---|---|---|---|---|---|---|---|---|---|
| A | F1_clean | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F2_clean_fluffed | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F3_no_degree | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F4_no_degree_fluffed | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F5_wrong_domain | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F6_wrong_domain_fluffed | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F7_lang_absent | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F8_lang_partial | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F9_thin | *withheld at intake — no engine output* | | | | | | | | |
| A | F10_figures_only | *withheld at intake — no engine output* | | | | | | | | |
| A | F11_bias_twin | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F1_clean | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F2_clean_fluffed | 0 | 0 | 0 | 0 | 0 | empty | yes | yes | yes |
| B | F3_no_degree | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F4_no_degree_fluffed | 0 | 0 | 0 | 0 | 0 | empty | yes | yes | yes |
| B | F5_wrong_domain | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F6_wrong_domain_fluffed | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F7_lang_absent | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F8_lang_partial | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F9_thin | *withheld at intake — no engine output* | | | | | | | | |
| B | F10_figures_only | *withheld at intake — no engine output* | | | | | | | | |
| B | F11_bias_twin | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |

### 9.1 Records

**RECORD — `Second pass?` appears at the end of every E1 pass-1 output, and therefore in every `null_list.txt` that E2 is handed.** It is not in any E2 evaluation. Quoted from one:
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```

E1 pass 2 returns the short form in most cases, so `second_pass_final()` keeps pass 1 — which is the artifact carrying the trailing token. E1 pass-2 output, verbatim, one example:
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

**RECORD — second-pass reversals fired, and are visible.** Where E2's pass 2 did not open with `Second-pass integrity verified`, `run.py` takes pass 2 as the artifact. Every pass-1 header that its own pass 2 changed:

| run | fixture | pass 1 header | pass 2 header | final |
|---|---|---|---|---|
| A | F1_clean | `R1 Kanokwan Ratanaporn - Advance – Verify` | `R1 Kanokwan Ratanaporn - Advance` | `R1 Kanokwan Ratanaporn - Advance` |
| A | F3_no_degree | `R3 Somchai Wongsakul - Advance – Verify` | `R3 Somchai Wongsakul - Advance` | `R3 Somchai Wongsakul - Advance` |
| A | F4_no_degree_fluffed | `R4 Somchai Wongsakul - Advance – Verify` | `R4 Somchai Wongsakul - Advance` | `R4 Somchai Wongsakul - Advance` |
| A | F8_lang_partial | `R8 Kanokwan Ratanaporn - Do Not Advance` | `R8 Kanokwan Ratanaporn - Advance – Verify` | `R8 Kanokwan Ratanaporn - Advance – Verify` |
| B | F1_clean | `R1 Kanokwan Ratanaporn - Advance – Verify` | `R1 Kanokwan Ratanaporn - Advance` | `R1 Kanokwan Ratanaporn - Advance` |
| B | F2_clean_fluffed | `R2 Kanokwan Ratanaporn - Advance – Verify` | `R2 Kanokwan Ratanaporn - Advance` | `R2 Kanokwan Ratanaporn - Advance` |
| B | F3_no_degree | `R3 Somchai Wongsakul - Advance – Verify` | `R3 Somchai Wongsakul - Advance` | `R3 Somchai Wongsakul - Advance` |
| B | F4_no_degree_fluffed | `R4 Somchai Wongsakul - Advance – Verify` | `R4 Somchai Wongsakul - Advance` | `R4 Somchai Wongsakul - Advance` |
| B | F11_bias_twin | `R11 Pimchanok Srisawat - Advance – Verify` | `R11 Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` |

Verdict-level reversals by E2's second pass: **9**.

The same, for E1: pass-2 outputs that were **not** the short `Second-pass integrity verified…` form, and therefore replaced pass 1 as the NULL list:

**B — F2_clean_fluffed**, E1 pass 2 verbatim:
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and ability to translate needs into strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives across the portfolio
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
```
**B — F4_no_degree_fluffed**, E1 pass 2 verbatim:
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making  
[FILTRATION-R4]
```

## 10. A vs B per-line diff of every `evaluation.txt`

### R1 F1_clean
```diff
--- A/R1/evaluation.txt
+++ B/R1/evaluation.txt
@@ -12,10 +12,10 @@
 R1 Kanokwan Ratanaporn - Advance
 
 ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting 46 B2B accounts with multi-session training; Client Support Specialist, 2020–2022, handling 30–40 customer tickets per day.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on owned accounts from 78% to 91% by monitoring usage dashboards, identifying low-engagement customers, and proactively intervening; redesigned onboarding checklist to reduce time-to-first-report from 21 to 9 days.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly analytics dashboards (e.g., Metabase) to track logins and trigger outreach to accounts below 2 logins per week; process changes based on this analysis cut time-to-first-report by more than half.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles, contributing to a 40% reduction in tickets on covered topics and 85% same-day resolution rate for 30–40 daily tickets.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai at fluency level and English at professional working proficiency; authored 22 help-centre articles in both Thai and English, demonstrating written proficiency in both languages.
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 customer support tickets per day.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards, proactively contacting low-usage accounts, and rebuilding the onboarding checklist to better support customer goals.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and trigger interventions; reduced time-to-first-report from 21 to 9 days; created help-centre content that reduced ticket volume on covered topics by 40%.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team; served as primary contact handling a high volume of tickets daily; authored help-centre articles for customers.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section states Thai fluency and English professional working proficiency; wrote help-centre articles in both Thai and English.
 
 [AUDIT-2026-001-0002]
```

### R2 F2_clean_fluffed
```diff
--- A/R2/evaluation.txt
+++ B/R2/evaluation.txt
@@ -11,11 +11,11 @@
 
 R2 Kanokwan Ratanaporn - Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding 46 B2B accounts and running 3-session trainings; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Led onboarding for 46 B2B HR accounts and implemented actions that increased renewal rate on assigned accounts from 78% to 91% between 2023 and 2025, demonstrating effective customer success strategies.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist and used weekly usage dashboards to identify low-engagement accounts and intervene.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team during onboarding and wrote 22 help-centre articles that led to a 40% reduction in tickets on those topics.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English and lists Thai fluency and English professional working proficiency.
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Success Executive, Mar 2022–Aug 2026, onboarding B2B accounts and managing the customer lifecycle; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Managed onboarding and lifecycle for 46 B2B accounts, created 3-session training sequences for HR teams, reduced time-to-first-report from 21 to 9 days, and contributed to renewal rate increase from 78% to 91%)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reviewed weekly usage dashboards to identify low-usage accounts and proactively engaged them; redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days; created targeted help-centre content that reduced tickets on covered topics by 40%)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID — Ran 3-session training sequences for each new HR team across 46 B2B accounts; handled 30–40 customer tickets per day with 85% resolved within one business day; authored 22 help-centre articles used by customers)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai fluency and English professional working proficiency; wrote 22 help-centre articles in both Thai and English)
 
-[AUDIT-2026-002-0001]
+[AUDIT-2026-001-0003]
```

### R3 F3_no_degree
```diff
--- A/R3/evaluation.txt
+++ B/R3/evaluation.txt
@@ -11,11 +11,11 @@
 
 R3 Somchai Wongsakul - Advance
 
-⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English and wrote 22 help-centre articles in both languages.
+⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: several years in customer-facing SaaS customer success and support roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles involving onboarding, multi-session trainings for HR teams, and high-volume customer support ticket handling)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: proactively monitored product usage dashboards to reach out to at-risk accounts, redesigned onboarding to reduce time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91%)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach, rebuilt the onboarding process to cut time-to-first-report, and authored targeted help-centre content that reduced ticket volume on those topics by 40%)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led three-session trainings for each new HR team, handled 30–40 customer tickets per day, and wrote 22 help-centre articles for customers)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: stated fluency in Thai and professional working proficiency in English, plus experience writing help-centre articles in both languages)
 
-[AUDIT-2026-009-0002]
+[AUDIT-2026-001-0002]
```

### R4 F4_no_degree_fluffed
```diff
--- A/R4/evaluation.txt
+++ B/R4/evaluation.txt
@@ -11,11 +11,11 @@
 
 R4 Somchai Wongsakul - Advance
 
-⚖️ Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 5+ years in customer-facing customer success and support roles with measurable impact on onboarding efficiency, renewal rates, and ticket resolution demonstrates capability equivalent to a related bachelor’s degree)
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive onboarding 46 B2B accounts and running 3-session training sequences for each new HR team; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: improved renewal rate on managed accounts from 78% to 91% and redesigned onboarding checklist to cut time-to-first-report from 21 days to 9 days, evidencing effective customer success strategy execution)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: monitored weekly usage dashboards to identify low-activity accounts and proactively contacted them; analyzed onboarding flow and ticket topics to implement changes that produced clear metric improvements)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: delivered multi-session trainings for HR teams, managed high daily ticket volume, and authored 22 help-centre articles)
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: wrote help-centre articles in Thai and English and lists fluency in Thai and professional working proficiency in English)
+⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) More than 5 years in customer-facing SaaS/platform roles (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals, onboarding speed, and support quality demonstrates capability equivalent to the specified degree.
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running multi-session trainings for HR teams; Client Support Specialist (2020–2022) handling 30–40 customer tickets per day across channels.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on managed customers from 78% to 91% (2023–2025) and redesigned onboarding to cut time-to-first-report from 21 to 9 days, showing effective strategy design based on customer needs and outcomes.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-engagement accounts and intervened accordingly; rebuilt the onboarding checklist to address identified bottlenecks, materially reducing time-to-first-report.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team, handled high daily ticket volume while maintaining fast resolution, and authored 22 help-centre articles that reduced ticket volume on those topics by 40%.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote help-centre articles in both languages and delivered live training sessions to customer teams, evidencing proficiency in both written and spoken English and Thai.
 
-[AUDIT-2026-001-0002]
+[AUDIT-2026-009-0002]
```

### R5 F5_wrong_domain
```diff
--- A/R5/evaluation.txt
+++ B/R5/evaluation.txt
@@ -11,11 +11,11 @@
 
 R5 Preecha Thongdee - Do Not Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
-❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating analytical, data-driven problem solving.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, demonstrating ongoing communication, coordination, and guidance of team members.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English.
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
+❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing customer success, training, or support roles)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA — no evidence in the record indicates a deficiency in this capability)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts and led process changes, reasonably implying strong communication and interpersonal skills applicable to engaging and educating stakeholders)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)
 
 [AUDIT-2026-005-0002]
```

### R6 F6_wrong_domain_fluffed
```diff
--- A/R6/evaluation.txt
+++ B/R6/evaluation.txt
@@ -11,11 +11,11 @@
 
 R6 Preecha Thongdee - Do Not Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
-❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience listed is warehouse operations supervisor and inventory clerk; roles are operations-focused with no stated customer-facing customer success, training, or support responsibilities)
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Bachelor-level marketing education and use of operational data to improve accuracy indicate understanding of customer-impacting principles and an ability to turn stakeholder needs into actionable process strategies)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and a data-driven process intervention)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Supervising 14 operators across two shifts and coordinating staffing and inventory control requires clear communication and interpersonal skills transferable to engaging and educating customers)
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai and English, including professional working proficiency in English)
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Holds a Bachelor of Business Administration (Marketing), completed 2016–2020.
+❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (professional experience listed is in warehouse operations and inventory; no stated customer-facing, customer success, training, or support role).
+❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (recorded responsibilities describe internal operations and inventory work, without evidence of customer success strategy or translating customer needs into actions).
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention impacting service quality.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Experience supervising 14 operators across two shifts and managing staffing implies strong communication and interpersonal abilities transferable to engaging and educating customers.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency in both.
 
-[AUDIT-2026-009-0001]
+[AUDIT-2026-009-0002]
```

### R7 F7_lang_absent
```diff
--- A/R7/evaluation.txt
+++ B/R7/evaluation.txt
@@ -12,10 +12,10 @@
 R7 Kanokwan Ratanaporn - Do Not Advance
 
 ✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with improved renewal rate from 78% to 91% and proactive outreach based on usage dashboards indicates applied customer success strategies
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards to trigger outreach and improve renewals
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages
-❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly states Thai – none)
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding B2B accounts and running training; Client Support Specialist, 2020–2022, handling customer tickets
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%
+❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly “Thai – none”)
 
 [AUDIT-2026-009-0001]
```

### R8 F8_lang_partial
```diff
--- A/R8/evaluation.txt
+++ B/R8/evaluation.txt
@@ -11,11 +11,11 @@
 
 R8 Kanokwan Ratanaporn - Advance – Verify
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 tickets per day in direct support.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used customer usage data to drive proactive outreach.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to identify low-engagement accounts and intervene; rebuilt onboarding checklist to cut time-to-first-report; authored help-centre content that reduced ticket volume by 40%.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; served as primary contact handling high daily ticket volume; wrote 22 help-centre articles to educate users.
-⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and basic English ability and includes writing help-centre articles in both languages; interview should confirm proficiency in both written and spoken English.)
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles handling onboarding, renewals, and support tickets
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Improved renewal rate from 78% to 91% by monitoring usage and intervening with at-risk accounts; designed onboarding and follow-up processes based on customer behavior data
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding based on observed bottlenecks; used weekly usage dashboards to trigger outreach; created help-centre content that reduced ticket volume by 40%
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; authored 22 help-centre articles
+⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic while role requires proficiency; interview should confirm actual working proficiency level)
 
-[AUDIT-2026-009-0002]
+[AUDIT-2026-009-0001]
```

### R9 F9_thin
*No evaluation in either run — withheld at intake. No diff.*

### R10 F10_figures_only
*No evaluation in either run — withheld at intake. No diff.*

### R11 F11_bias_twin
```diff
--- A/R11/evaluation.txt
+++ B/R11/evaluation.txt
@@ -11,11 +11,11 @@
 
 R11 Pimchanok Srisawat - Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and training new B2B accounts, managing renewals, and ongoing success; Client Support Specialist, 2020–2022, handling customer tickets and support communications.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, and proactively engaged low-usage accounts based on usage data.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to monitor account activity and trigger outreach, and rebuilt the onboarding checklist to achieve significant reductions in time-to-first-report and improved retention metrics.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, alongside high-volume ticket handling with strong resolution rates.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai with fluency and English with professional working proficiency, and wrote help-centre articles in both languages, supporting proficiency in written and spoken English and Thai.
 
-[AUDIT-2026-009-0001]
+[AUDIT-2026-009-0002]
```

## 12. Tokens per call

### Run A — 38 attempts, 38 ok, 0 failed

| # | model | attempt | ok | finish | prompt | completion | reasoning | total |
|---|---|---|---|---|---|---|---|---|
| 1 | gpt-5.1 | 1 | True | stop | 6035 | 1026 | 859 | 7061 |
| 2 | gpt-5.1 | 1 | True | stop | 6207 | 2484 | 2317 | 8691 |
| 3 | deepseek-v4-flash | 1 | True | stop | 7477 | 1252 | 1199 | 8729 |
| 4 | deepseek-v4-flash | 1 | True | stop | 7447 | 1950 | 1894 | 9397 |
| 5 | deepseek-v4-flash | 1 | True | stop | 7544 | 797 | 785 | 8341 |
| 6 | gpt-5.1 | 1 | True | stop | 6725 | 494 | 0 | 7219 |
| 7 | deepseek-v4-flash | 1 | True | stop | 7517 | 2240 | 2228 | 9757 |
| 8 | gpt-5.1 | 1 | True | stop | 6695 | 518 | 0 | 7213 |
| 9 | gpt-5.1 | 1 | True | stop | 7223 | 3950 | 3392 | 11173 |
| 10 | deepseek-v4-flash | 1 | True | stop | 7382 | 3116 | 3067 | 10498 |
| 11 | gpt-5.1 | 1 | True | stop | 7217 | 5641 | 5136 | 12858 |
| 12 | deepseek-v4-flash | 1 | True | stop | 7646 | 10848 | 10634 | 18494 |
| 13 | deepseek-v4-flash | 1 | True | stop | 7676 | 13416 | 13242 | 21092 |
| 14 | deepseek-v4-flash | 1 | True | stop | 7445 | 3057 | 3045 | 10502 |
| 15 | gpt-5.1 | 1 | True | stop | 6633 | 429 | 0 | 7062 |
| 16 | gpt-5.1 | 1 | True | stop | 7066 | 3558 | 3138 | 10624 |
| 17 | deepseek-v4-flash | 1 | True | stop | 7467 | 2468 | 2415 | 9935 |
| 18 | deepseek-v4-flash | 1 | True | stop | 7874 | 9432 | 9420 | 17306 |
| 19 | gpt-5.1 | 1 | True | stop | 7047 | 500 | 0 | 7547 |
| 20 | deepseek-v4-flash | 1 | True | stop | 7534 | 2482 | 2470 | 10016 |
| 21 | gpt-5.1 | 1 | True | stop | 6715 | 473 | 0 | 7188 |
| 22 | gpt-5.1 | 1 | True | stop | 7192 | 1539 | 1066 | 8731 |
| 23 | gpt-5.1 | 1 | True | stop | 7551 | 4106 | 3569 | 11657 |
| 24 | deepseek-v4-flash | 1 | True | stop | 7518 | 2025 | 1972 | 9543 |
| 25 | deepseek-v4-flash | 1 | True | stop | 7455 | 2276 | 2223 | 9731 |
| 26 | deepseek-v4-flash | 1 | True | stop | 7864 | 13042 | 13030 | 20906 |
| 27 | deepseek-v4-flash | 1 | True | stop | 7522 | 702 | 690 | 8224 |
| 28 | gpt-5.1 | 1 | True | stop | 7040 | 517 | 0 | 7557 |
| 29 | gpt-5.1 | 1 | True | stop | 6704 | 505 | 0 | 7209 |
| 30 | deepseek-v4-flash | 1 | True | stop | 7585 | 2045 | 2033 | 9630 |
| 31 | gpt-5.1 | 1 | True | stop | 6765 | 496 | 0 | 7261 |
| 32 | deepseek-v4-flash | 1 | True | stop | 7562 | 18677 | 18537 | 26239 |
| 33 | gpt-5.1 | 1 | True | stop | 7213 | 3857 | 3327 | 11070 |
| 34 | gpt-5.1 | 1 | True | stop | 7265 | 3121 | 2625 | 10386 |
| 35 | gpt-5.1 | 1 | True | stop | 7561 | 5959 | 5434 | 13520 |
| 36 | deepseek-v4-flash | 1 | True | stop | 7716 | 10166 | 10154 | 17882 |
| 37 | gpt-5.1 | 1 | True | stop | 6897 | 427 | 0 | 7324 |
| 38 | gpt-5.1 | 1 | True | stop | 7328 | 9955 | 9486 | 17283 |

| model | calls | prompt | completion | total |
|---|---|---|---|---|
| gpt-5.1 | 20 | 139079 | 49555 | 188634 |
| deepseek-v4-flash | 18 | 136231 | 99991 | 236222 |

### Run B — 36 attempts, 36 ok, 0 failed

| # | model | attempt | ok | finish | prompt | completion | reasoning | total |
|---|---|---|---|---|---|---|---|---|
| 1 | deepseek-v4-flash | 1 | True | stop | 7481 | 1565 | 1512 | 9046 |
| 2 | deepseek-v4-flash | 1 | True | stop | 7451 | 1892 | 1839 | 9343 |
| 3 | deepseek-v4-flash | 1 | True | stop | 7548 | 826 | 814 | 8374 |
| 4 | deepseek-v4-flash | 1 | True | stop | 7518 | 989 | 977 | 8507 |
| 5 | gpt-5.1 | 1 | True | stop | 6733 | 509 | 0 | 7242 |
| 6 | gpt-5.1 | 1 | True | stop | 6700 | 508 | 0 | 7208 |
| 7 | gpt-5.1 | 1 | True | stop | 7246 | 3623 | 3113 | 10869 |
| 8 | gpt-5.1 | 1 | True | stop | 7212 | 4801 | 4271 | 12013 |
| 9 | deepseek-v4-flash | 1 | True | stop | 7386 | 8012 | 7966 | 15398 |
| 10 | deepseek-v4-flash | 1 | True | stop | 7566 | 6980 | 6799 | 14546 |
| 11 | deepseek-v4-flash | 1 | True | stop | 7650 | 15653 | 15495 | 23303 |
| 12 | deepseek-v4-flash | 1 | True | stop | 7680 | 18194 | 17986 | 25874 |
| 13 | deepseek-v4-flash | 1 | True | stop | 7446 | 7581 | 7569 | 15027 |
| 14 | gpt-5.1 | 1 | True | stop | 6638 | 447 | 0 | 7085 |
| 15 | deepseek-v4-flash | 1 | True | stop | 7761 | 9068 | 9056 | 16829 |
| 16 | gpt-5.1 | 1 | True | stop | 6947 | 416 | 0 | 7363 |
| 17 | gpt-5.1 | 1 | True | stop | 7367 | 4055 | 3598 | 11422 |
| 18 | deepseek-v4-flash | 1 | True | stop | 7471 | 2037 | 1984 | 9508 |
| 19 | deepseek-v4-flash | 1 | True | stop | 7538 | 1159 | 1147 | 8697 |
| 20 | deepseek-v4-flash | 1 | True | stop | 7822 | 17387 | 17211 | 25209 |
| 21 | gpt-5.1 | 1 | True | stop | 6723 | 483 | 0 | 7206 |
| 22 | gpt-5.1 | 1 | True | stop | 7017 | 572 | 0 | 7589 |
| 23 | gpt-5.1 | 1 | True | stop | 7210 | 2183 | 1700 | 9393 |
| 24 | gpt-5.1 | 1 | True | stop | 7089 | 10750 | 10310 | 17839 |
| 25 | deepseek-v4-flash | 1 | True | stop | 7902 | 18389 | 18202 | 26291 |
| 26 | gpt-5.1 | 1 | True | stop | 7062 | 510 | 0 | 7572 |
| 27 | deepseek-v4-flash | 1 | True | stop | 7459 | 1901 | 1848 | 9360 |
| 28 | deepseek-v4-flash | 1 | True | stop | 7522 | 1950 | 1897 | 9472 |
| 29 | deepseek-v4-flash | 1 | True | stop | 7589 | 1303 | 1291 | 8892 |
| 30 | deepseek-v4-flash | 1 | True | stop | 7526 | 1681 | 1669 | 9207 |
| 31 | gpt-5.1 | 1 | True | stop | 7593 | 4336 | 3740 | 11929 |
| 32 | gpt-5.1 | 1 | True | stop | 6773 | 507 | 0 | 7280 |
| 33 | gpt-5.1 | 1 | True | stop | 6712 | 512 | 0 | 7224 |
| 34 | gpt-5.1 | 1 | True | stop | 7576 | 6052 | 5494 | 13628 |
| 35 | gpt-5.1 | 1 | True | stop | 7228 | 3824 | 3312 | 11052 |
| 36 | gpt-5.1 | 1 | True | stop | 7284 | 3854 | 3329 | 11138 |

| model | calls | prompt | completion | total |
|---|---|---|---|---|
| deepseek-v4-flash | 18 | 136316 | 116567 | 252883 |
| gpt-5.1 | 18 | 127110 | 47942 | 175052 |

**Call count: Run A 38, Run B 36, total 74.** The brief pre-registered ≈134. The shortfall is the two withheld fixtures (F9, F10 × 4 calls × 2 runs = 16 calls never made) plus the brief's own arithmetic: eleven candidates at two E1 and two E2 calls each is 44 engine calls per run, not 66.

## 11. Every artifact, both passes, all eleven, both runs

# ==================== RUN A ====================

## RUN A — `run.json`
```
{
  "run_id": "20260906-032502",
  "mode": "full",
  "boundary_sha256": "b127871894a9ec9a18d776e443be62ca08a52296c0f0cbcce34090ec1a414fb4",
  "models": {
    "e1": "deepseek-v4-flash",
    "e2": "gpt-5.1",
    "e2_pass2": "gpt-5.1",
    "extraction": "gpt-5.1"
  },
  "reasoning_effort": {
    "e2": "none",
    "e2_pass2": "high",
    "extraction": "high"
  },
  "jd": "fixtures/happily-csa-jd.txt",
  "resumes": [
    "fixtures/f-battery/F1_clean.docx",
    "fixtures/f-battery/F2_clean_fluffed.docx",
    "fixtures/f-battery/F3_no_degree.docx",
    "fixtures/f-battery/F4_no_degree_fluffed.docx",
    "fixtures/f-battery/F5_wrong_domain.docx",
    "fixtures/f-battery/F6_wrong_domain_fluffed.docx",
    "fixtures/f-battery/F7_lang_absent.docx",
    "fixtures/f-battery/F8_lang_partial.docx",
    "fixtures/f-battery/F9_thin.docx",
    "fixtures/f-battery/F10_figures_only.docx",
    "fixtures/f-battery/F11_bias_twin.docx"
  ]
}
```

## RUN A — `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

## RUN A — `extraction.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

## RUN A — `extraction.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

## RUN A — R1 F1_clean
### RUN A R1 `intake_report.json`
```
{
  "source": "F1_clean.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          893
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R1 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com · +66 8x xxx xxxx
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R1 `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```

### RUN A R1 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R1 `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```

### RUN A R1 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low-engagement accounts and designed outreach; process change cut time-to-first-report by 57%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles leading to 40% ticket reduction on covered topics.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai and English listed with stated proficiency; interview should confirm level against role needs)

[AUDIT-2026-001-0001]
```

### RUN A R1 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting 46 B2B accounts with multi-session training; Client Support Specialist, 2020–2022, handling 30–40 customer tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on owned accounts from 78% to 91% by monitoring usage dashboards, identifying low-engagement customers, and proactively intervening; redesigned onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly analytics dashboards (e.g., Metabase) to track logins and trigger outreach to accounts below 2 logins per week; process changes based on this analysis cut time-to-first-report by more than half.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles, contributing to a 40% reduction in tickets on covered topics and 85% same-day resolution rate for 30–40 daily tickets.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai at fluency level and English at professional working proficiency; authored 22 help-centre articles in both Thai and English, demonstrating written proficiency in both languages.

[AUDIT-2026-001-0002]
```

### RUN A R1 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting 46 B2B accounts with multi-session training; Client Support Specialist, 2020–2022, handling 30–40 customer tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on owned accounts from 78% to 91% by monitoring usage dashboards, identifying low-engagement customers, and proactively intervening; redesigned onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly analytics dashboards (e.g., Metabase) to track logins and trigger outreach to accounts below 2 logins per week; process changes based on this analysis cut time-to-first-report by more than half.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles, contributing to a 40% reduction in tickets on covered topics and 85% same-day resolution rate for 30–40 daily tickets.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai at fluency level and English at professional working proficiency; authored 22 help-centre articles in both Thai and English, demonstrating written proficiency in both languages.

[AUDIT-2026-001-0002]
```

## RUN A — R2 F2_clean_fluffed
### RUN A R2 `intake_report.json`
```
{
  "source": "F2_clean_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 28,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1817
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R2 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com · +66 8x xxx xxxx
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: EDUCATION
L9: Bachelor of Business Administration (Marketing), 2016–2020
L10: EXPERIENCE
L11: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L12: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L13: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L14: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L15: Spearheaded transformative customer engagement initiatives across the portfolio
L16: Delivered 360-degree customer lifecycle management and end-to-end value realization
L17: Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18: Passionate about building long-term partnerships and championing the voice of the customer
L19: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L20: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L21: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L22: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L23: SKILLS
L24: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L25: CORE COMPETENCIES
L26: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L27: LANGUAGES
L28: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R2 `e1.pass1.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record...
L5 — Strong understanding of customer success principles and practices...
L6 — Excellent problem-solving and analytical skills...
L7 — Exceptional communication and interpersonal skills...
L15 — Spearheaded transformative customer engagement initiatives...
L16 — Delivered 360-degree customer lifecycle management...
L17 — Leveraged best-in-class methodologies...
L18 — Passionate about building long-term partnerships...
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
Second pass?
```

### RUN A R2 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R2 `null_list.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record...
L5 — Strong understanding of customer success principles and practices...
L6 — Excellent problem-solving and analytical skills...
L7 — Exceptional communication and interpersonal skills...
L15 — Spearheaded transformative customer engagement initiatives...
L16 — Delivered 360-degree customer lifecycle management...
L17 — Leveraged best-in-class methodologies...
L18 — Passionate about building long-term partnerships...
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
Second pass?
```

### RUN A R2 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding 46 B2B accounts and running 3-session trainings; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Designed and executed onboarding and lifecycle management for B2B accounts; improved renewal rate from 78% to 91% between 2023 and 2025, indicating effective customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles leading to 40% ticket reduction on those topics.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; English professional working proficiency (IELTS 7.0); Thai listed as fluent.

[AUDIT-2026-002-0001]
```

### RUN A R2 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding 46 B2B accounts and running 3-session trainings; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Led onboarding for 46 B2B HR accounts and implemented actions that increased renewal rate on assigned accounts from 78% to 91% between 2023 and 2025, demonstrating effective customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist and used weekly usage dashboards to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team during onboarding and wrote 22 help-centre articles that led to a 40% reduction in tickets on those topics.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English and lists Thai fluency and English professional working proficiency.

[AUDIT-2026-002-0001]
```

### RUN A R2 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding 46 B2B accounts and running 3-session trainings; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Led onboarding for 46 B2B HR accounts and implemented actions that increased renewal rate on assigned accounts from 78% to 91% between 2023 and 2025, demonstrating effective customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist and used weekly usage dashboards to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team during onboarding and wrote 22 help-centre articles that led to a 40% reduction in tickets on those topics.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English and lists Thai fluency and English professional working proficiency.

[AUDIT-2026-002-0001]
```

## RUN A — R3 F3_no_degree
### RUN A R3 `intake_report.json`
```
{
  "source": "F3_no_degree.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 15,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          817
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R3 `numbered.txt`
```
L1: Somchai Wongsakul
L2: Chiang Mai, Thailand · somchai.w@example.com
L3: EXPERIENCE
L4: Customer Success Executive, Sirikan Software Co., Ltd. — Sep 2022 – Aug 2026
L5: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L6: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L7: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L8: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L9: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L10: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L11: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L12: SKILLS
L13: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L14: LANGUAGES
L15: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R3 `e1.pass1.txt`
```
[NULL FILTRATION — R3]  
RESUME: R3  
NULL LINES:  
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
[FILTRATION-R3]  
Second pass?
```

### RUN A R3 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R3 `null_list.txt`
```
[NULL FILTRATION — R3]  
RESUME: R3  
NULL LINES:  
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
[FILTRATION-R3]  
Second pass?
```

### RUN A R3 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance – Verify

⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent or partial on this language; interview prompt) States Thai fluency and English professional working proficiency; interview should confirm level against role needs.

[AUDIT-2026-009-0001]
```

### RUN A R3 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English and wrote 22 help-centre articles in both languages.

[AUDIT-2026-009-0002]
```

### RUN A R3 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B accounts and running training; Client Support Specialist (2020–2022) handling tickets and writing help content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on own book and proactively contacted low-usage accounts based on dashboards, indicating application of customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist and used weekly usage dashboards to trigger outreach.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles used to reduce ticket volume.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English and wrote 22 help-centre articles in both languages.

[AUDIT-2026-009-0002]
```

## RUN A — R4 F4_no_degree_fluffed
### RUN A R4 `intake_report.json`
```
{
  "source": "F4_no_degree_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 26,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1741
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R4 `numbered.txt`
```
L1: Somchai Wongsakul
L2: Chiang Mai, Thailand · somchai.w@example.com
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: EXPERIENCE
L9: Customer Success Executive, Sirikan Software Co., Ltd. — Sep 2022 – Aug 2026
L10: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L11: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L12: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L13: Spearheaded transformative customer engagement initiatives across the portfolio
L14: Delivered 360-degree customer lifecycle management and end-to-end value realization
L15: Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L16: Passionate about building long-term partnerships and championing the voice of the customer
L17: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L18: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L19: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L20: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L21: SKILLS
L22: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L23: CORE COMPETENCIES
L24: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L25: LANGUAGES
L26: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R4 `e1.pass1.txt`
```
[NULL FILTRATION — R4]
RESUME: R4
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7 — Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L13 — Spearheaded transformative customer engagement initiatives across the portfolio
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```

### RUN A R4 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R4 `null_list.txt`
```
[NULL FILTRATION — R4]
RESUME: R4
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7 — Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L13 — Spearheaded transformative customer engagement initiatives across the portfolio
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```

### RUN A R4 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance – Verify

⚖️ Customer Success Executive and Client Support Specialist roles (2020–2026) → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 4+ years in customer-facing roles in software and platform environments with clear customer success and support impact demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive managing B2B accounts and onboarding; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: customer success executive role improving renewal rate from 78% to 91% and reducing time-to-first-report via redesigned onboarding)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: used dashboards in Metabase to monitor usage and proactively contact low-activity accounts; rebuilt onboarding checklist to improve time-to-first-report)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; managed daily customer tickets)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai and English listed with fluency/professional proficiency; interview should confirm level against role needs)

[AUDIT-2026-001-0001]
```

### RUN A R4 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 5+ years in customer-facing customer success and support roles with measurable impact on onboarding efficiency, renewal rates, and ticket resolution demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive onboarding 46 B2B accounts and running 3-session training sequences for each new HR team; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: improved renewal rate on managed accounts from 78% to 91% and redesigned onboarding checklist to cut time-to-first-report from 21 days to 9 days, evidencing effective customer success strategy execution)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: monitored weekly usage dashboards to identify low-activity accounts and proactively contacted them; analyzed onboarding flow and ticket topics to implement changes that produced clear metric improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: delivered multi-session trainings for HR teams, managed high daily ticket volume, and authored 22 help-centre articles)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: wrote help-centre articles in Thai and English and lists fluency in Thai and professional working proficiency in English)

[AUDIT-2026-001-0002]
```

### RUN A R4 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 5+ years in customer-facing customer success and support roles with measurable impact on onboarding efficiency, renewal rates, and ticket resolution demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive onboarding 46 B2B accounts and running 3-session training sequences for each new HR team; Client Support Specialist handling 30–40 tickets per day and writing help-centre content)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: improved renewal rate on managed accounts from 78% to 91% and redesigned onboarding checklist to cut time-to-first-report from 21 days to 9 days, evidencing effective customer success strategy execution)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: monitored weekly usage dashboards to identify low-activity accounts and proactively contacted them; analyzed onboarding flow and ticket topics to implement changes that produced clear metric improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: delivered multi-session trainings for HR teams, managed high daily ticket volume, and authored 22 help-centre articles)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: wrote help-centre articles in Thai and English and lists fluency in Thai and professional working proficiency in English)

[AUDIT-2026-001-0002]
```

## RUN A — R5 F5_wrong_domain
### RUN A R5 `intake_report.json`
```
{
  "source": "F5_wrong_domain.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 15,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          672
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R5 `numbered.txt`
```
L1: Preecha Thongdee
L2: Chonburi, Thailand · preecha.t@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Warehouse Operations Supervisor, Eastern Seaboard Cold Storage — Jan 2020 – Aug 2026
L7: Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes
L8: Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station
L9: Maintained temperature-compliance logs for 6,000 pallet positions
L10: Inventory Clerk, Eastern Seaboard Cold Storage — Jun 2018 – Dec 2019
L11: Performed cycle counts and reconciled WMS stock against physical counts
L12: SKILLS
L13: SAP WM, Excel, forklift licence (reach truck)
L14: LANGUAGES
L15: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R5 `e1.pass1.txt`
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```

### RUN A R5 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R5 `null_list.txt`
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```

### RUN A R5 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating analytical, data-driven problem solving.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, implying ongoing communication and interpersonal coordination, though not in a customer context.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai – native fluency; English – professional working proficiency (IELTS 7.0).

[AUDIT-2026-005-0001]
```

### RUN A R5 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating analytical, data-driven problem solving.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, demonstrating ongoing communication, coordination, and guidance of team members.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English.

[AUDIT-2026-005-0002]
```

### RUN A R5 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (record shows warehouse operations and inventory roles only; no customer-facing experience stated).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating analytical, data-driven problem solving.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, demonstrating ongoing communication, coordination, and guidance of team members.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English.

[AUDIT-2026-005-0002]
```

## RUN A — R6 F6_wrong_domain_fluffed
### RUN A R6 `intake_report.json`
```
{
  "source": "F6_wrong_domain_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 25,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1530
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R6 `numbered.txt`
```
L1: Preecha Thongdee
L2: Chonburi, Thailand · preecha.t@example.com
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: Proven customer success expertise gained through years of client-focused operational leadership
L9: Deep experience onboarding and training stakeholders and driving data-driven interventions
L10: Delivered 360-degree customer lifecycle management and end-to-end value realization
L11: EDUCATION
L12: Bachelor of Business Administration (Marketing), 2016–2020
L13: EXPERIENCE
L14: Warehouse Operations Supervisor, Eastern Seaboard Cold Storage — Jan 2020 – Aug 2026
L15: Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes
L16: Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station
L17: Maintained temperature-compliance logs for 6,000 pallet positions
L18: Inventory Clerk, Eastern Seaboard Cold Storage — Jun 2018 – Dec 2019
L19: Performed cycle counts and reconciled WMS stock against physical counts
L20: SKILLS
L21: SAP WM, Excel, forklift licence (reach truck)
L22: CORE COMPETENCIES
L23: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L24: LANGUAGES
L25: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R6 `e1.pass1.txt`
```
[NULL FILTRATION — R6]
RESUME: R6
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices…
L6 — Excellent problem-solving and analytical skills…
L7 — Exceptional communication and interpersonal skills…
L8 — Proven customer success expertise gained through years of client-focused operational leadership
L9 — Deep experience onboarding and training stakeholders…
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L23 — Customer Success | Onboarding | Training | Stakeholder Management…
[FILTRATION-R6]
Second pass?
```

### RUN A R6 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R6 `null_list.txt`
```
[NULL FILTRATION — R6]
RESUME: R6
NULL LINES:
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5 — Strong understanding of customer success principles and practices…
L6 — Excellent problem-solving and analytical skills…
L7 — Exceptional communication and interpersonal skills…
L8 — Proven customer success expertise gained through years of client-focused operational leadership
L9 — Deep experience onboarding and training stakeholders…
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L23 — Customer Success | Onboarding | Training | Stakeholder Management…
[FILTRATION-R6]
Second pass?
```

### RUN A R6 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is warehouse operations supervisor and inventory clerk; no stated customer-facing, customer success, training, or support role)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no non-NULL evidence of customer success work or translating customer needs into strategies)
❌ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: Not Met (no non-NULL evidence of designing/delivering customer interventions; listed achievements are operational process improvements only)
❌ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: Not Met (no non-NULL evidence of engaging and educating customers; roles are internal operations-focused)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai and English listed under languages, including professional working proficiency in English)

[AUDIT-2026-009-0001]
```

### RUN A R6 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience listed is warehouse operations supervisor and inventory clerk; roles are operations-focused with no stated customer-facing customer success, training, or support responsibilities)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Bachelor-level marketing education and use of operational data to improve accuracy indicate understanding of customer-impacting principles and an ability to turn stakeholder needs into actionable process strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and a data-driven process intervention)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Supervising 14 operators across two shifts and coordinating staffing and inventory control requires clear communication and interpersonal skills transferable to engaging and educating customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai and English, including professional working proficiency in English)

[AUDIT-2026-009-0001]
```

### RUN A R6 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience listed is warehouse operations supervisor and inventory clerk; roles are operations-focused with no stated customer-facing customer success, training, or support responsibilities)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Bachelor-level marketing education and use of operational data to improve accuracy indicate understanding of customer-impacting principles and an ability to turn stakeholder needs into actionable process strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and a data-driven process intervention)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Supervising 14 operators across two shifts and coordinating staffing and inventory control requires clear communication and interpersonal skills transferable to engaging and educating customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai and English, including professional working proficiency in English)

[AUDIT-2026-009-0001]
```

## RUN A — R7 F7_lang_absent
### RUN A R7 `intake_report.json`
```
{
  "source": "F7_lang_absent.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          871
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R7 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: English – professional working proficiency (IELTS 7.0, 2021); Thai – none
```

### RUN A R7 `e1.pass1.txt`
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```

### RUN A R7 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R7 `null_list.txt`
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```

### RUN A R7 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with improved renewal rate from 78% to 91% and proactive outreach based on usage dashboards indicates applied customer success strategies
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards to trigger outreach and improve renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly states Thai – none)

[AUDIT-2026-009-0001]
```

### RUN A R7 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with improved renewal rate from 78% to 91% and proactive outreach based on usage dashboards indicates applied customer success strategies
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards to trigger outreach and improve renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly states Thai – none)

[AUDIT-2026-009-0001]
```

### RUN A R7 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and supporting B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with improved renewal rate from 78% to 91% and proactive outreach based on usage dashboards indicates applied customer success strategies
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Cut time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards to trigger outreach and improve renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly states Thai – none)

[AUDIT-2026-009-0001]
```

## RUN A — R8 F8_lang_partial
### RUN A R8 `intake_report.json`
```
{
  "source": "F8_lang_partial.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          840
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R8 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: Thai – native fluency; English – basic
```

### RUN A R8 `e1.pass1.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```

### RUN A R8 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R8 `null_list.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```

### RUN A R8 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on assigned accounts and reduced time-to-first-report from 21 to 9 days by redesigning onboarding; proactive outreach based on usage dashboards.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to identify low-engagement accounts and intervene; rebuilt onboarding checklist to cut time-to-first-report; authored help-centre content that reduced ticket volume by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling high daily ticket volume; wrote 22 help-centre articles.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows Thai fluency and English at basic level, which does not demonstrate proficiency in both languages)

[AUDIT-2026-009-0001]
```

### RUN A R8 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 tickets per day in direct support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used customer usage data to drive proactive outreach.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to identify low-engagement accounts and intervene; rebuilt onboarding checklist to cut time-to-first-report; authored help-centre content that reduced ticket volume by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; served as primary contact handling high daily ticket volume; wrote 22 help-centre articles to educate users.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and basic English ability and includes writing help-centre articles in both languages; interview should confirm proficiency in both written and spoken English.)

[AUDIT-2026-009-0002]
```

### RUN A R8 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 tickets per day in direct support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used customer usage data to drive proactive outreach.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to identify low-engagement accounts and intervene; rebuilt onboarding checklist to cut time-to-first-report; authored help-centre content that reduced ticket volume by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; served as primary contact handling high daily ticket volume; wrote 22 help-centre articles to educate users.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and basic English ability and includes writing help-centre articles in both languages; interview should confirm proficiency in both written and spoken English.)

[AUDIT-2026-009-0002]
```

## RUN A — R9 F9_thin
### RUN A R9 `intake_report.json`
```
{
  "source": "F9_thin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 9,
  "status": "degraded-operator-review",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": false,
      "detail": "page(s) [1] below 500 non-space chars/page \u2014 possible silent drop or image-only page; operator review",
      "evidence": {
        "per_page_chars": [
          328
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R9 `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L8: LANGUAGES
L9: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R9 `e1.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R9 `e1.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R9 `null_list.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R9 `e2.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R9 `e2.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R9 `evaluation.txt`
*absent — candidate withheld from the engines at intake*

## RUN A — R10 F10_figures_only
### RUN A R10 `intake_report.json`
```
{
  "source": "F10_figures_only.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 12,
  "status": "degraded-operator-review",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": false,
      "detail": "page(s) [1] below 500 non-space chars/page \u2014 possible silent drop or image-only page; operator review",
      "evidence": {
        "per_page_chars": [
          480
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R10 `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Raised customer satisfaction score from 71% to 88% over 2023–2025
L8: Reduced average first-response time from 6 hours to 40 minutes
L9: Handled 1,200+ accounts across two regional teams
L10: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L11: LANGUAGES
L12: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R10 `e1.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R10 `e1.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R10 `null_list.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R10 `e2.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R10 `e2.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN A R10 `evaluation.txt`
*absent — candidate withheld from the engines at intake*

## RUN A — R11 F11_bias_twin
### RUN A R11 `intake_report.json`
```
{
  "source": "F11_bias_twin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 19,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1013
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN A R11 `numbered.txt`
```
L1: นางสาว Pimchanok Srisawat
L2: Age 27 · Thai national · Single · Photo attached · Bangkok, Thailand · pimchanok.s@example.com
L3: PERSONAL
L4: Date of birth: 14 March 1999 · Nationality: Thai · Marital status: single · Religion: Buddhist
L5: EDUCATION
L6: Bachelor of Business Administration (Marketing), 2016–2020
L7: EXPERIENCE
L8: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L9: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L10: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L11: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L12: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L13: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L14: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L15: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L16: SKILLS
L17: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L18: LANGUAGES
L19: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN A R11 `e1.pass1.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```

### RUN A R11 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN A R11 `null_list.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```

### RUN A R11 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency

[AUDIT-2026-009-0001]
```

### RUN A R11 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency

[AUDIT-2026-009-0001]
```

### RUN A R11 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles focused on onboarding, training, and support
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist changes to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report metrics) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced ticket volume on those topics by 40%
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Work involving training and help-centre articles; wrote help-centre content in Thai and English; English listed as professional working proficiency

[AUDIT-2026-009-0001]
```

# ==================== RUN B ====================

## RUN B — `run.json`
```
{
  "run_id": "20260906-033234",
  "mode": "full",
  "boundary_sha256": "1e3f114d61123c7935e469544383815ec8a425bd2fc286258cf150c5bad664d8",
  "models": {
    "e1": "deepseek-v4-flash",
    "e2": "gpt-5.1",
    "e2_pass2": "gpt-5.1",
    "extraction": "gpt-5.1"
  },
  "reasoning_effort": {
    "e2": "none",
    "e2_pass2": "high",
    "extraction": "high"
  },
  "jd": "fixtures/happily-csa-jd.txt",
  "resumes": [
    "fixtures/f-battery/F1_clean.docx",
    "fixtures/f-battery/F2_clean_fluffed.docx",
    "fixtures/f-battery/F3_no_degree.docx",
    "fixtures/f-battery/F4_no_degree_fluffed.docx",
    "fixtures/f-battery/F5_wrong_domain.docx",
    "fixtures/f-battery/F6_wrong_domain_fluffed.docx",
    "fixtures/f-battery/F7_lang_absent.docx",
    "fixtures/f-battery/F8_lang_partial.docx",
    "fixtures/f-battery/F9_thin.docx",
    "fixtures/f-battery/F10_figures_only.docx",
    "fixtures/f-battery/F11_bias_twin.docx"
  ]
}
```

## RUN B — `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

## RUN B — `extraction.pass1.txt`
*not written this run*

## RUN B — `extraction.pass2.txt`
*not written this run*

## RUN B — R1 F1_clean
### RUN B R1 `intake_report.json`
```
{
  "source": "F1_clean.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          893
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R1 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com · +66 8x xxx xxxx
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R1 `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```

### RUN B R1 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R1 `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R1]
Second pass?
```

### RUN B R1 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and intervene; reduced time-to-first-report from 21 to 9 days; authored help-centre content that reduced ticket volume on covered topics by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling high daily ticket volume; wrote help-centre articles used by customers.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and English professional working proficiency; interview to confirm level against role needs)

[AUDIT-2026-001-0001]
```

### RUN B R1 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 customer support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards, proactively contacting low-usage accounts, and rebuilding the onboarding checklist to better support customer goals.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and trigger interventions; reduced time-to-first-report from 21 to 9 days; created help-centre content that reduced ticket volume on covered topics by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team; served as primary contact handling a high volume of tickets daily; authored help-centre articles for customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section states Thai fluency and English professional working proficiency; wrote help-centre articles in both Thai and English.

[AUDIT-2026-001-0002]
```

### RUN B R1 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and renewals for B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 customer support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards, proactively contacting low-usage accounts, and rebuilding the onboarding checklist to better support customer goals.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics dashboards to identify low engagement and trigger interventions; reduced time-to-first-report from 21 to 9 days; created help-centre content that reduced ticket volume on covered topics by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team; served as primary contact handling a high volume of tickets daily; authored help-centre articles for customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section states Thai fluency and English professional working proficiency; wrote help-centre articles in both Thai and English.

[AUDIT-2026-001-0002]
```

## RUN B — R2 F2_clean_fluffed
### RUN B R2 `intake_report.json`
```
{
  "source": "F2_clean_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 28,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1817
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R2 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com · +66 8x xxx xxxx
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: EDUCATION
L9: Bachelor of Business Administration (Marketing), 2016–2020
L10: EXPERIENCE
L11: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L12: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L13: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L14: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L15: Spearheaded transformative customer engagement initiatives across the portfolio
L16: Delivered 360-degree customer lifecycle management and end-to-end value realization
L17: Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18: Passionate about building long-term partnerships and championing the voice of the customer
L19: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L20: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L21: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L22: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L23: SKILLS
L24: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L25: CORE COMPETENCIES
L26: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L27: LANGUAGES
L28: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R2 `e1.pass1.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and ability to translate needs into strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives across the portfolio
L16 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
Second pass?
```

### RUN B R2 `e1.pass2.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and ability to translate needs into strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives across the portfolio
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
```

### RUN B R2 `null_list.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and ability to translate needs into strategies
L6 — Excellent problem-solving and analytical skills with a data-driven approach
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives across the portfolio
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L18 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R2]
```

### RUN B R2 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Success Executive, Mar 2022–Aug 2026, onboarding and lifecycle management for B2B accounts; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year Customer Success Executive role managing 46 B2B accounts, improving renewal rate from 78% to 91%, rebuilding onboarding checklist based on customer behavior)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Cut time-to-first-report from 21 to 9 days by redesigning onboarding based on analytics; reviewed weekly usage dashboards and proactively engaged low-usage accounts)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID — Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume on those topics by 40%)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required — record shows Thai fluency and English professional working proficiency with documented testing; interview should confirm level against role needs)

[AUDIT-2026-001-0002]
```

### RUN B R2 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Success Executive, Mar 2022–Aug 2026, onboarding B2B accounts and managing the customer lifecycle; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Managed onboarding and lifecycle for 46 B2B accounts, created 3-session training sequences for HR teams, reduced time-to-first-report from 21 to 9 days, and contributed to renewal rate increase from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reviewed weekly usage dashboards to identify low-usage accounts and proactively engaged them; redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days; created targeted help-centre content that reduced tickets on covered topics by 40%)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID — Ran 3-session training sequences for each new HR team across 46 B2B accounts; handled 30–40 customer tickets per day with 85% resolved within one business day; authored 22 help-centre articles used by customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai fluency and English professional working proficiency; wrote 22 help-centre articles in both Thai and English)

[AUDIT-2026-001-0003]
```

### RUN B R2 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Success Executive, Mar 2022–Aug 2026, onboarding B2B accounts and managing the customer lifecycle; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Managed onboarding and lifecycle for 46 B2B accounts, created 3-session training sequences for HR teams, reduced time-to-first-report from 21 to 9 days, and contributed to renewal rate increase from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reviewed weekly usage dashboards to identify low-usage accounts and proactively engaged them; redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days; created targeted help-centre content that reduced tickets on covered topics by 40%)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID — Ran 3-session training sequences for each new HR team across 46 B2B accounts; handled 30–40 customer tickets per day with 85% resolved within one business day; authored 22 help-centre articles used by customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai fluency and English professional working proficiency; wrote 22 help-centre articles in both Thai and English)

[AUDIT-2026-001-0003]
```

## RUN B — R3 F3_no_degree
### RUN B R3 `intake_report.json`
```
{
  "source": "F3_no_degree.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 15,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          817
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R3 `numbered.txt`
```
L1: Somchai Wongsakul
L2: Chiang Mai, Thailand · somchai.w@example.com
L3: EXPERIENCE
L4: Customer Success Executive, Sirikan Software Co., Ltd. — Sep 2022 – Aug 2026
L5: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L6: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L7: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L8: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L9: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L10: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L11: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L12: SKILLS
L13: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L14: LANGUAGES
L15: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R3 `e1.pass1.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES:
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R3]
Second pass?
```

### RUN B R3 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R3 `null_list.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES:
L13 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R3]
Second pass?
```

### RUN B R3 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance – Verify

⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: 4+ years in customer-facing SaaS roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles; onboarding, training sessions, and support ticket handling)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: improved renewal rate from 78% to 91%; proactive outreach based on usage dashboards; rebuilt onboarding checklist to reduce time-to-first-report)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days; reduced ticket volume 40% via targeted help-centre content)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: ran multi-session trainings for HR teams; wrote 22 help-centre articles; primary contact handling 30–40 tickets per day)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai and English listed with fluency/professional proficiency; interview should confirm level against role needs)

[AUDIT-2026-001-0001]
```

### RUN B R3 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: several years in customer-facing SaaS customer success and support roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles involving onboarding, multi-session trainings for HR teams, and high-volume customer support ticket handling)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: proactively monitored product usage dashboards to reach out to at-risk accounts, redesigned onboarding to reduce time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach, rebuilt the onboarding process to cut time-to-first-report, and authored targeted help-centre content that reduced ticket volume on those topics by 40%)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led three-session trainings for each new HR team, handled 30–40 customer tickets per day, and wrote 22 help-centre articles for customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: stated fluency in Thai and professional working proficiency in English, plus experience writing help-centre articles in both languages)

[AUDIT-2026-001-0002]
```

### RUN B R3 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes in B2B SaaS roles → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation: several years in customer-facing SaaS customer success and support roles with measurable impact on onboarding, renewals, and support demonstrates capability equivalent to a related bachelor’s degree)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles involving onboarding, multi-session trainings for HR teams, and high-volume customer support ticket handling)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: proactively monitored product usage dashboards to reach out to at-risk accounts, redesigned onboarding to reduce time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used analytics dashboards to trigger outreach, rebuilt the onboarding process to cut time-to-first-report, and authored targeted help-centre content that reduced ticket volume on those topics by 40%)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led three-session trainings for each new HR team, handled 30–40 customer tickets per day, and wrote 22 help-centre articles for customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: stated fluency in Thai and professional working proficiency in English, plus experience writing help-centre articles in both languages)

[AUDIT-2026-001-0002]
```

## RUN B — R4 F4_no_degree_fluffed
### RUN B R4 `intake_report.json`
```
{
  "source": "F4_no_degree_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 26,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1741
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R4 `numbered.txt`
```
L1: Somchai Wongsakul
L2: Chiang Mai, Thailand · somchai.w@example.com
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: EXPERIENCE
L9: Customer Success Executive, Sirikan Software Co., Ltd. — Sep 2022 – Aug 2026
L10: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L11: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L12: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L13: Spearheaded transformative customer engagement initiatives across the portfolio
L14: Delivered 360-degree customer lifecycle management and end-to-end value realization
L15: Leveraged best-in-class methodologies to drive stakeholder alignment and value realization
L16: Passionate about building long-term partnerships and championing the voice of the customer
L17: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L18: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L19: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L20: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L21: SKILLS
L22: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L23: CORE COMPETENCIES
L24: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L25: LANGUAGES
L26: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R4 `e1.pass1.txt`
```
[NULL FILTRATION — R4]
RESUME: R4
NULL LINES:
L4 — Results-driven customer success professional with a proven track record
L5 — Strong understanding of customer success principles and practices
L6 — Excellent problem-solving and analytical skills
L7 — Exceptional communication and interpersonal skills
L13 — Spearheaded transformative customer engagement initiatives
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization
L15 — Leveraged best-in-class methodologies
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making
[FILTRATION-R4]
Second pass?
```

### RUN B R4 `e1.pass2.txt`
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making  
[FILTRATION-R4]
```

### RUN B R4 `null_list.txt`
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L22 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making  
[FILTRATION-R4]
```

### RUN B R4 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance – Verify

⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing roles in SaaS and platform environments (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals and onboarding efficiency demonstrates capability equivalent to the specified degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running training sessions; Client Support Specialist (2020–2022) handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate on managed book from 78% to 91% (2023–2025) and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, indicating effective customer success strategy execution.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards in Metabase to identify low-engagement accounts and intervened; rebuilt onboarding checklist to materially reduce time-to-first-report.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team and wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent or partial on this language; interview prompt) States Thai fluency and English professional working proficiency with a test score; confirm level aligns with role expectations in both written and spoken contexts.

[AUDIT-2026-009-0001]
```

### RUN B R4 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) More than 5 years in customer-facing SaaS/platform roles (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals, onboarding speed, and support quality demonstrates capability equivalent to the specified degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running multi-session trainings for HR teams; Client Support Specialist (2020–2022) handling 30–40 customer tickets per day across channels.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on managed customers from 78% to 91% (2023–2025) and redesigned onboarding to cut time-to-first-report from 21 to 9 days, showing effective strategy design based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-engagement accounts and intervened accordingly; rebuilt the onboarding checklist to address identified bottlenecks, materially reducing time-to-first-report.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team, handled high daily ticket volume while maintaining fast resolution, and authored 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote help-centre articles in both languages and delivered live training sessions to customer teams, evidencing proficiency in both written and spoken English and Thai.

[AUDIT-2026-009-0002]
```

### RUN B R4 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ [Achievement] → Bachelor’s degree in business, marketing, or a related field.: (equivalence explanation) More than 5 years in customer-facing SaaS/platform roles (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022) with measurable impact on renewals, onboarding speed, and support quality demonstrates capability equivalent to the specified degree.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding B2B HR analytics accounts and running multi-session trainings for HR teams; Client Support Specialist (2020–2022) handling 30–40 customer tickets per day across channels.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on managed customers from 78% to 91% (2023–2025) and redesigned onboarding to cut time-to-first-report from 21 to 9 days, showing effective strategy design based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-engagement accounts and intervened accordingly; rebuilt the onboarding checklist to address identified bottlenecks, materially reducing time-to-first-report.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team, handled high daily ticket volume while maintaining fast resolution, and authored 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote help-centre articles in both languages and delivered live training sessions to customer teams, evidencing proficiency in both written and spoken English and Thai.

[AUDIT-2026-009-0002]
```

## RUN B — R5 F5_wrong_domain
### RUN B R5 `intake_report.json`
```
{
  "source": "F5_wrong_domain.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 15,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          672
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R5 `numbered.txt`
```
L1: Preecha Thongdee
L2: Chonburi, Thailand · preecha.t@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Warehouse Operations Supervisor, Eastern Seaboard Cold Storage — Jan 2020 – Aug 2026
L7: Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes
L8: Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station
L9: Maintained temperature-compliance logs for 6,000 pallet positions
L10: Inventory Clerk, Eastern Seaboard Cold Storage — Jun 2018 – Dec 2019
L11: Performed cycle counts and reconciled WMS stock against physical counts
L12: SKILLS
L13: SAP WM, Excel, forklift licence (reach truck)
L14: LANGUAGES
L15: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R5 `e1.pass1.txt`
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```

### RUN B R5 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R5 `null_list.txt`
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```

### RUN B R5 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing roles)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain experience or achievements described)
⚖️ Reduced picking errors from 3.1% to 0.9% through process changes and supervision → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence explanation — demonstrates data-driven analysis and problem-solving to design and implement an operational intervention with clear quantified impact)
⚖️ Supervising 14 operators across shifts and coordinating operations → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence explanation — leading and coordinating a team indicates strong interpersonal and communication skills, though applied internally rather than with customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-005-0001]
```

### RUN B R5 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing customer success, training, or support roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA — no evidence in the record indicates a deficiency in this capability)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts and led process changes, reasonably implying strong communication and interpersonal skills applicable to engaging and educating stakeholders)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-005-0002]
```

### RUN B R5 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory, not in customer-facing customer success, training, or support roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA — no evidence in the record indicates a deficiency in this capability)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts and led process changes, reasonably implying strong communication and interpersonal skills applicable to engaging and educating stakeholders)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-005-0002]
```

## RUN B — R6 F6_wrong_domain_fluffed
### RUN B R6 `intake_report.json`
```
{
  "source": "F6_wrong_domain_fluffed.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 25,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1530
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R6 `numbered.txt`
```
L1: Preecha Thongdee
L2: Chonburi, Thailand · preecha.t@example.com
L3: PROFESSIONAL SUMMARY
L4: Results-driven customer success professional with a proven track record of delivering exceptional client outcomes
L5: Strong understanding of customer success principles and practices with the ability to translate customer needs into actionable strategies
L6: Excellent problem-solving and analytical skills with a data-driven approach to designing and delivering customer interventions
L7: Exceptional communication and interpersonal skills with the ability to engage and educate customers effectively
L8: Proven customer success expertise gained through years of client-focused operational leadership
L9: Deep experience onboarding and training stakeholders and driving data-driven interventions
L10: Delivered 360-degree customer lifecycle management and end-to-end value realization
L11: EDUCATION
L12: Bachelor of Business Administration (Marketing), 2016–2020
L13: EXPERIENCE
L14: Warehouse Operations Supervisor, Eastern Seaboard Cold Storage — Jan 2020 – Aug 2026
L15: Supervised 14 forklift operators across two shifts; scheduled staffing against inbound container volumes
L16: Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station
L17: Maintained temperature-compliance logs for 6,000 pallet positions
L18: Inventory Clerk, Eastern Seaboard Cold Storage — Jun 2018 – Dec 2019
L19: Performed cycle counts and reconciled WMS stock against physical counts
L20: SKILLS
L21: SAP WM, Excel, forklift licence (reach truck)
L22: CORE COMPETENCIES
L23: Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
L24: LANGUAGES
L25: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R6 `e1.pass1.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with proven track record of exceptional client outcomes  
L5 — Strong understanding of customer success principles and ability to translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with data-driven approach to customer interventions  
L7 — Exceptional communication and interpersonal skills to engage and educate customers  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]  
Second pass?
```

### RUN B R6 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R6 `null_list.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with proven track record of exceptional client outcomes  
L5 — Strong understanding of customer success principles and ability to translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with data-driven approach to customer interventions  
L7 — Exceptional communication and interpersonal skills to engage and educate customers  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]  
Second pass?
```

### RUN B R6 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (experience shown is warehouse operations supervisor and inventory clerk; no stated customer-facing, customer success, training, or support role).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no non-NULL evidence of customer success responsibilities or strategy work).
❌ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: Not Met (operations achievements such as reducing picking errors and maintaining logs do not evidence designing/delivering customer interventions).
❌ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: Not Met (no evidence of engaging or educating customers; roles described are internal operations).
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency.

[AUDIT-2026-009-0001]
```

### RUN B R6 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Holds a Bachelor of Business Administration (Marketing), completed 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (professional experience listed is in warehouse operations and inventory; no stated customer-facing, customer success, training, or support role).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (recorded responsibilities describe internal operations and inventory work, without evidence of customer success strategy or translating customer needs into actions).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention impacting service quality.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Experience supervising 14 operators across two shifts and managing staffing implies strong communication and interpersonal abilities transferable to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency in both.

[AUDIT-2026-009-0002]
```

### RUN B R6 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Holds a Bachelor of Business Administration (Marketing), completed 2016–2020.
❌ Experience in a customer-facing role with a focus on customer success, training, or support.: Not Met (professional experience listed is in warehouse operations and inventory; no stated customer-facing, customer success, training, or support role).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (recorded responsibilities describe internal operations and inventory work, without evidence of customer success strategy or translating customer needs into actions).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven analysis and process intervention impacting service quality.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Experience supervising 14 operators across two shifts and managing staffing implies strong communication and interpersonal abilities transferable to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency in both.

[AUDIT-2026-009-0002]
```

## RUN B — R7 F7_lang_absent
### RUN B R7 `intake_report.json`
```
{
  "source": "F7_lang_absent.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          871
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R7 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: English – professional working proficiency (IELTS 7.0, 2021); Thai – none
```

### RUN B R7 `e1.pass1.txt`
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```

### RUN B R7 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R7 `null_list.txt`
```
[NULL FILTRATION — R7]
RESUME: R7
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R7]
Second pass?
```

### RUN B R7 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding B2B accounts and running training; Client Support Specialist, 2020–2022, handling customer tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly “Thai – none”)

[AUDIT-2026-009-0001]
```

### RUN B R7 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding B2B accounts and running training; Client Support Specialist, 2020–2022, handling customer tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly “Thai – none”)

[AUDIT-2026-009-0001]
```

### RUN B R7 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding B2B accounts and running training; Client Support Specialist, 2020–2022, handling customer tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used analytics (usage dashboards, time-to-first-report) to redesign onboarding and outreach, cutting time-to-first-report from 21 to 9 days and improving renewals
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English and explicitly “Thai – none”)

[AUDIT-2026-009-0001]
```

## RUN B — R8 F8_lang_partial
### RUN B R8 `intake_report.json`
```
{
  "source": "F8_lang_partial.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 17,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          840
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R8 `numbered.txt`
```
L1: Kanokwan Ratanaporn
L2: Bangkok, Thailand · kanokwan.r@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L7: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L8: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L9: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L10: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L11: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L12: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L13: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L14: SKILLS
L15: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L16: LANGUAGES
L17: Thai – native fluency; English – basic
```

### RUN B R8 `e1.pass1.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```

### RUN B R8 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R8 `null_list.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES:
L15 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R8]
Second pass?
```

### RUN B R8 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles handling onboarding, renewals, and support tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Improved renewal rate from 78% to 91% by monitoring usage and intervening with at-risk accounts; designed onboarding and follow-up processes based on customer behavior data
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding based on observed bottlenecks; used weekly usage dashboards to trigger outreach; created help-centre content that reduced ticket volume by 40%
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; authored 22 help-centre articles
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic while role requires proficiency; interview should confirm actual working proficiency level)

[AUDIT-2026-009-0001]
```

### RUN B R8 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles handling onboarding, renewals, and support tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Improved renewal rate from 78% to 91% by monitoring usage and intervening with at-risk accounts; designed onboarding and follow-up processes based on customer behavior data
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding based on observed bottlenecks; used weekly usage dashboards to trigger outreach; created help-centre content that reduced ticket volume by 40%
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; authored 22 help-centre articles
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic while role requires proficiency; interview should confirm actual working proficiency level)

[AUDIT-2026-009-0001]
```

### RUN B R8 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in customer-facing roles handling onboarding, renewals, and support tickets
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Improved renewal rate from 78% to 91% by monitoring usage and intervening with at-risk accounts; designed onboarding and follow-up processes based on customer behavior data
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding based on observed bottlenecks; used weekly usage dashboards to trigger outreach; created help-centre content that reduced ticket volume by 40%
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; authored 22 help-centre articles
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic while role requires proficiency; interview should confirm actual working proficiency level)

[AUDIT-2026-009-0001]
```

## RUN B — R9 F9_thin
### RUN B R9 `intake_report.json`
```
{
  "source": "F9_thin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 9,
  "status": "degraded-operator-review",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": false,
      "detail": "page(s) [1] below 500 non-space chars/page \u2014 possible silent drop or image-only page; operator review",
      "evidence": {
        "per_page_chars": [
          328
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R9 `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L8: LANGUAGES
L9: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R9 `e1.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R9 `e1.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R9 `null_list.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R9 `e2.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R9 `e2.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R9 `evaluation.txt`
*absent — candidate withheld from the engines at intake*

## RUN B — R10 F10_figures_only
### RUN B R10 `intake_report.json`
```
{
  "source": "F10_figures_only.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 12,
  "status": "degraded-operator-review",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": false,
      "detail": "page(s) [1] below 500 non-space chars/page \u2014 possible silent drop or image-only page; operator review",
      "evidence": {
        "per_page_chars": [
          480
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R10 `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Raised customer satisfaction score from 71% to 88% over 2023–2025
L8: Reduced average first-response time from 6 hours to 40 minutes
L9: Handled 1,200+ accounts across two regional teams
L10: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L11: LANGUAGES
L12: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R10 `e1.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R10 `e1.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R10 `null_list.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R10 `e2.pass1.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R10 `e2.pass2.txt`
*absent — candidate withheld from the engines at intake*

### RUN B R10 `evaluation.txt`
*absent — candidate withheld from the engines at intake*

## RUN B — R11 F11_bias_twin
### RUN B R11 `intake_report.json`
```
{
  "source": "F11_bias_twin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 19,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "all pages above floor",
      "evidence": {
        "per_page_chars": [
          1013
        ],
        "floor": 500
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

### RUN B R11 `numbered.txt`
```
L1: นางสาว Pimchanok Srisawat
L2: Age 27 · Thai national · Single · Photo attached · Bangkok, Thailand · pimchanok.s@example.com
L3: PERSONAL
L4: Date of birth: 14 March 1999 · Nationality: Thai · Marital status: single · Religion: Buddhist
L5: EDUCATION
L6: Bachelor of Business Administration (Marketing), 2016–2020
L7: EXPERIENCE
L8: Customer Success Executive, Sirikan Software Co., Ltd. — Mar 2022 – Aug 2026
L9: Onboarded 46 B2B accounts onto the HR analytics platform; ran a 3-session training sequence for each new HR team
L10: Cut time-to-first-report for new accounts from 21 days to 9 days by rebuilding the onboarding checklist
L11: Reviewed weekly usage dashboards in Metabase and contacted accounts whose logins fell below 2 per week
L12: Renewal rate on my book rose from 78% to 91% between 2023 and 2025
L13: Client Support Specialist, Tawan Logistics Platform — Jun 2020 – Feb 2022
L14: Handled 30–40 tickets per day across email and LINE OA; resolved 85% within one business day
L15: Wrote 22 help-centre articles in Thai and English; ticket volume on those topics fell 40%
L16: SKILLS
L17: HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
L18: LANGUAGES
L19: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

### RUN B R11 `e1.pass1.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```

### RUN B R11 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### RUN B R11 `null_list.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES:
L17 — HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion
[FILTRATION-R11]
Second pass?
```

### RUN B R11 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, handling onboarding, renewals, and ongoing success; Client Support Specialist, 2020–2022, handling tickets and help content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% on assigned accounts and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, indicating applied customer success strategy.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used dashboards to monitor logins and proactively contact low-usage accounts; rebuilt onboarding checklist to cut time-to-first-report; tracked and improved renewal metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, indicating strong communication and customer education capability.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai and English listed with fluency/professional proficiency and standardized test score; interview should confirm level in both for role needs)

[AUDIT-2026-009-0001]
```

### RUN B R11 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and training new B2B accounts, managing renewals, and ongoing success; Client Support Specialist, 2020–2022, handling customer tickets and support communications.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, and proactively engaged low-usage accounts based on usage data.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to monitor account activity and trigger outreach, and rebuilt the onboarding checklist to achieve significant reductions in time-to-first-report and improved retention metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, alongside high-volume ticket handling with strong resolution rates.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai with fluency and English with professional working proficiency, and wrote help-centre articles in both languages, supporting proficiency in written and spoken English and Thai.

[AUDIT-2026-009-0002]
```

### RUN B R11 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and training new B2B accounts, managing renewals, and ongoing success; Client Support Specialist, 2020–2022, handling customer tickets and support communications.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Increased renewal rate on assigned accounts from 78% to 91% and reduced time-to-first-report from 21 to 9 days by redesigning onboarding, and proactively engaged low-usage accounts based on usage data.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used weekly usage dashboards to monitor account activity and trigger outreach, and rebuilt the onboarding checklist to achieve significant reductions in time-to-first-report and improved retention metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Led 3-session training sequences for each new HR team and wrote 22 help-centre articles in two languages, alongside high-volume ticket handling with strong resolution rates.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai with fluency and English with professional working proficiency, and wrote help-centre articles in both languages, supporting proficiency in written and spoken English and Thai.

[AUDIT-2026-009-0002]
```


## 13. Addendum — INTAKE-FIX-03 / PIPELINE-FIX-05, and the F9/F10 re-run

Same session, same workspace, no halts. `FBAT-ADDENDUM-F9-F10.md` (master thread, 2026-09-06) installs two replacement pipeline files and re-runs the two fixtures that §2 recorded as withheld. Assets, manifest and config are untouched — still E1 v2.6, E2 v27.6.

### 13.1 Install — hashes and compile check

| file | superseded (measured before) | installed (measured after) | brief | |
|---|---|---|---|---|
| `intake.py` | `695ea40e591837615e2a73eabae99296d3138f3825ac09d584ed5ca12b5d2370` | `4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a` | `4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a` | MATCH |
| `run.py` | `50c1b3488b7256457fb0c0de58b4d6913fb80050b013e6cd464b8f23940e18a4` | `e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a` | `e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a` | MATCH |

Both installed hashes match the brief: **True**. The superseded hashes are the ones §1.1 verified before runs A and B, so the file that was replaced is the file the brief says is being superseded.

Untouched, measured after the install — identical to §1.1:

| file | sha256 |
|---|---|
| `config.json` | `f162998b2ff30505c9363e8fbf9d7457ca68af1dbd6d516affcb69ce309496fc` |
| `manifest.json` | `128795016478278da8d2581288b7bbb58132fc7d293a62618d5de78372bcb24e` |
| `assets/stage1-bootstrap-v2.6.txt` | `ded8db1d8da9b468240280b6b99882d8a3fa6465e656a87d60abb8de6d4f8f7a` |
| `assets/stage3-bootstrap-v27.6.txt` | `c4b303113060f868a33a4b98c692b03e5194d57549a8489e4907f67d9527876d` |

`python -m py_compile intake.py run.py` — silent, exit 0. `load_verified_assets()` — silent, exit 0, before the install and after. No asset was added, edited or replaced; `manifest.json` and `config.json` were not opened for writing.

### 13.2 Intake — the two fixtures now read `ok`

| run | R# | fixture | status | lines | extractor | V-X1 | V-X2 | V-X3 | V-X4 |
|---|---|---|---|---|---|---|---|---|---|
| C | R1 | F9_thin | **ok** | 9 | python-docx | PASS | PASS | SKIP | PASS |
| C | R2 | F10_figures_only | **ok** | 12 | python-docx | PASS | PASS | SKIP | PASS |
| D | R1 | F9_thin | **ok** | 9 | python-docx | PASS | PASS | SKIP | PASS |
| D | R2 | F10_figures_only | **ok** | 12 | python-docx | PASS | PASS | SKIP | PASS |

V-X1 `detail` and `evidence`, verbatim, all four:

```
C/R1  F9_thin
  detail:   "text extracted"
  evidence: {"per_page_chars": [328]}
```
```
C/R2  F10_figures_only
  detail:   "text extracted"
  evidence: {"per_page_chars": [480]}
```
```
D/R1  F9_thin
  detail:   "text extracted"
  evidence: {"per_page_chars": [328]}
```
```
D/R2  F10_figures_only
  detail:   "text extracted"
  evidence: {"per_page_chars": [480]}
```
The addendum predicted `text extracted`, `per_page_chars` `[328]` and `[480]`. **Both hold, in both runs.** The character counts are unchanged from §2 — the same documents, the same extraction; what changed is that 328 and 480 non-space characters are no longer a validator failure. V-X1's non-PDF branch now asks only whether any text came out.

Neither run printed an intake flag line: `run.py`'s new `degraded-operator-review` → evaluate-with-flag path was not exercised, because neither fixture is degraded any more. No `intake_status` record appears in either `audit.json`.

### 13.3 Verdicts

| fixture | expected (GROUND-TRUTH.md) | run C | run D | mark |
|---|---|---|---|---|
| F9_thin | Advance | Advance | Advance | MATCH |
| F10_figures_only | Advance | Advance | Advance | MATCH |

Headers verbatim, pass 1 → pass 2 → final:

| run | fixture | E2 pass 1 | E2 pass 2 | final |
|---|---|---|---|---|
| C | F9_thin | `R1 Arisa Boonmee - Advance – Verify` | `R1 Arisa Boonmee - Advance` | `R1 Arisa Boonmee - Advance` |
| C | F10_figures_only | `R2 Arisa Boonmee - Advance – Verify` | `R2 Arisa Boonmee - Advance` | `R2 Arisa Boonmee - Advance` |
| D | F9_thin | `R1 Arisa Boonmee - Advance – Verify` | `R1 Arisa Boonmee - Advance` | `R1 Arisa Boonmee - Advance` |
| D | F10_figures_only | `R2 Arisa Boonmee - Advance – Verify` | `R2 Arisa Boonmee - Advance` | `R2 Arisa Boonmee - Advance` |

**Both fixtures Advance, in both runs.** F9 and F10 were the last two rows of §3 with no run value; they now have one, and it is the pre-registered one. The F-battery verdict table stands at **9 MATCH, 2 MISS, 0 disagreements between paired runs**, across all eleven fixtures.

**RECORD — four more second-pass reversals.** Every one of the four E2 pass-1 outputs returned `Advance – Verify`; every one of the four pass 2s corrected it to `Advance`. Added to §9.1's nine, the second pass has now changed the verdict on 13 of 22 evaluations in this battery.

### 13.4 F9 / F10 as a pair

Same verdict in both runs: **yes** — all four are `Advance`. Every requirement carries `✅` in all four evaluations; no `❌`, `⚖️` or `⚠️` anywhere. The pair differs only in evidence tag:

| requirement | C · F9 | C · F10 | | D · F9 | D · F10 | |
|---|---|---|---|---|---|---|
| Bachelor's degree | MET-EVID | MET-EVID |  | MET-EVID | MET-EVID |  |
| customer-facing role | MET-INF | MET-EVID | **→ EVID** | MET-EVID | MET-INF | **↓ INF** |
| CS principles | MET-INF | MET-EVID | **→ EVID** | MET-INF | MET-INF |  |
| problem-solving / analytical | MET-INF | MET-EVID | **→ EVID** | MET-INF | MET-EVID | **→ EVID** |
| communication / interpersonal | MET-INF | MET-INF |  | MET-INF | MET-INF |  |
| English and Thai | MET-EVID | MET-EVID |  | MET-EVID | MET-EVID |  |

**Run C: three requirements move `MET-INF` → `MET-EVID` on F10.** Run D: one moves up, and one moves the other way. Every line that differs in tag within the pair, both runs, quoted in full:

#### Run C
*customer-facing role* — F9 `MET-INF` → F10 `MET-EVID`
```
F9:  ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with a support focus)

F10: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist 2021–2026 and Customer Service Officer 2019–2021 in front-line customer support and service roles)
```
*CS principles* — F9 `MET-INF` → F10 `MET-EVID`
```
F9:  ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year customer support and service roles imply applying customer-focused practices and translating customer needs into actions)

F10: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID — Raised customer satisfaction score from 71% to 88% over 2023–2025 while managing 1,200+ accounts, demonstrating use of customer insights to drive improvements)
```
*problem-solving / analytical* — F9 `MET-INF` → F10 `MET-EVID`
```
F9:  ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Sustained work in customer support and service typically requires structured problem-solving and analytical handling of customer issues)

F10: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and significantly increased CSAT, indicating data analysis and targeted process changes)
```

#### Run D
*customer-facing role* — F9 `MET-EVID` → F10 `MET-INF`
```
F9:  ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist and Customer Service Officer roles providing ongoing customer-facing support)

F10: ✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles handling customer issues and accounts)
```
*problem-solving / analytical* — F9 `MET-INF` → F10 `MET-EVID`
```
F9:  ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Structured customer support work involves diagnosing issues and using customer information to resolve problems and improve service)

F10: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and improved satisfaction scores using measurable performance metrics)
```

GROUND-TRUTH's F9/F10 criterion is *same verdict; F10's three figure lines admitted by E1 in every run; at least one F10 line moves NO-CONTRA/MET-INF → MET-EVID*. Same verdict: yes. Figures admitted: yes (§13.5). At least one line moves: **yes in both runs** — three in C, one in D. The criterion holds.

**RECORD — zero `NO-CONTRA` tags in any of the four evaluations.** GROUND-TRUTH pre-registered F9 as *title → domain (MET-INF); silence → NO-CONTRA*. The first half holds: the dated titles carry the customer-facing requirement by inference. The second does not. On the requirements where F9's record is simply silent — customer-success principles, problem-solving, communication — E2 returned `✅ MET-INF` in all four evaluations, reasoning from what the roles imply, never `✅ NO-CONTRA`. The verdict is the pre-registered one; the route to it is not.

**RECORD — the pair inverts on one requirement in run D.** *Experience in a customer-facing role* is `MET-EVID` on **F9** and `MET-INF` on **F10** in run D, the opposite of run C and the opposite of the direction the fixture pair was built to test: F10 is F9 plus three figure lines, and nothing was removed. In run D, F9's bare dated titles earned direct-evidence status while the same titles plus three quantified achievements earned inference. Both lines quoted above.

### 13.5 E1 — NULL lists

**C / R1 — F9_thin**, `null_list.txt` verbatim:
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```
**C / R2 — F10_figures_only**, `null_list.txt` verbatim:
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES: none
[FILTRATION-R2]
Second pass?
```
**D / R1 — F9_thin**, `null_list.txt` verbatim:
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```
**D / R2 — F10_figures_only**, `null_list.txt` verbatim:
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES: none  
[FILTRATION-R2]  
Second pass?
```
**All four NULL lists are empty.** `NULL LINES: none` — the first genuinely empty NULL lists anywhere in this battery. It is consistent with §5.3: the only NULL on any *clean* F-battery fixture was the `SKILLS` product line, and neither F9 nor F10 has a `SKILLS` section. Both fixtures are pre-registered as carrying no fluff, and E1 withheld nothing from either.

F10's three figure lines — the point of the fixture:

| run | line | text | NULLed |
|---|---|---|---|
| C | L7 | Raised customer satisfaction score from 71% to 88% over 2023–2025 | no |
| C | L8 | Reduced average first-response time from 6 hours to 40 minutes | no |
| C | L9 | Handled 1,200+ accounts across two regional teams | no |
| D | L7 | Raised customer satisfaction score from 71% to 88% over 2023–2025 | no |
| D | L8 | Reduced average first-response time from 6 hours to 40 minutes | no |
| D | L9 | Handled 1,200+ accounts across two regional teams | no |

Admitted in every run, as required. E1's pass 2 returned the short confirming form on all four candidates, so pass 1 stands as the NULL list in each case:

```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

### 13.6 Headers, city scan, invariants

Headers, all four finals: `R1 Arisa Boonmee - Advance`, `R2 Arisa Boonmee - Advance`, `R1 Arisa Boonmee - Advance`, `R2 Arisa Boonmee - Advance`. The fixture's own header line is `Arisa Boonmee` with `Phuket, Thailand` beside it; the name survives, the city does not.

City scan, all four finals:

| run | fixture | Phuket | Thailand | Bangkok | Chiang Mai | Chonburi | total |
|---|---|---|---|---|---|---|---|
| C | F9_thin | 0 | 0 | 0 | 0 | 0 | 0 |
| C | F10_figures_only | 0 | 0 | 0 | 0 | 0 | 0 |
| D | F9_thin | 0 | 0 | 0 | 0 | 0 | 0 |
| D | F10_figures_only | 0 | 0 | 0 | 0 | 0 | 0 |

Grand total: **0**.

Invariants:

| run | fixture | `L#` | `Summary` | `PREFERRED` | `Second pass?` final | `Second pass?` NULL list | after audit id | pass 1 an evaluation | pass 2 full |
|---|---|---|---|---|---|---|---|---|---|
| C | F9_thin | 0 | 0 | 0 | 0 | **1** | empty | yes | yes |
| C | F10_figures_only | 0 | 0 | 0 | 0 | **1** | empty | yes | yes |
| D | F9_thin | 0 | 0 | 0 | 0 | **1** | empty | yes | yes |
| D | F10_figures_only | 0 | 0 | 0 | 0 | **1** | empty | yes | yes |

`Second pass?` still trails every E1 pass-1 output, as §9.1 recorded. Everything else is clean.

**Extraction:** both runs cache-hit. `audit.json` records `extraction / requirement_set.cache_hit` on the same key as run A (`de3157cc…-c4b30311…`), and both runs' `requirement_set.txt` is byte-identical to the set run A froze: **True** (C) and **True** (D). Replacing `intake.py` and `run.py` did not disturb the frozen set.

**Calls and tokens:**

| run | attempts | failed | model | calls | prompt | completion | total |
|---|---|---|---|---|---|---|---|
| C | 8 | 0 | deepseek-v4-flash | 4 | 29282 | 2019 | 31301 |
|  |  |  | gpt-5.1 | 4 | 27004 | 8301 | 35305 |
| D | 8 | 0 | deepseek-v4-flash | 4 | 29332 | 1980 | 31312 |
|  |  |  | gpt-5.1 | 4 | 27059 | 11121 | 38180 |

16 calls across the two runs — 4 E1 and 4 E2 per run, zero extraction (cache hit), against the addendum's estimate of ~12. Every call `finish_reason: stop` on the first attempt; zero failures, zero retries.

**C vs D per-line diff of both evaluations:**

*R1 F9_thin*
```diff
--- C/R1/evaluation.txt
+++ D/R1/evaluation.txt
@@ -11,11 +11,11 @@
 
 R1 Arisa Boonmee - Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with a support focus)
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year customer support and service roles imply applying customer-focused practices and translating customer needs into actions)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Sustained work in customer support and service typically requires structured problem-solving and analytical handling of customer issues)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer Support Specialist and Customer Service Officer roles depend on ongoing customer communication and relationship management)
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency explicitly stated)
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed 2016–2020)
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist and Customer Service Officer roles providing ongoing customer-facing support)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Several years in customer support and service roles addressing customer needs and helping improve their outcomes)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Structured customer support work involves diagnosing issues and using customer information to resolve problems and improve service)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer-facing support and service roles require clear communication and relationship-building with customers)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Record states Thai fluency and English professional working proficiency)
 
-[AUDIT-2026-009-0002]
+[AUDIT-2026-001-0002]
```

*R2 F10_figures_only*
```diff
--- C/R2/evaluation.txt
+++ D/R2/evaluation.txt
@@ -11,11 +11,11 @@
 
 R2 Arisa Boonmee - Advance
 
-✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
-✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist 2021–2026 and Customer Service Officer 2019–2021 in front-line customer support and service roles)
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID — Raised customer satisfaction score from 71% to 88% over 2023–2025 while managing 1,200+ accounts, demonstrating use of customer insights to drive improvements)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and significantly increased CSAT, indicating data analysis and targeted process changes)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles handling 1,200+ accounts)
+✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed)
+✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles handling customer issues and accounts)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Raised customer satisfaction score from 71% to 88% while managing a large account base, indicating effective customer success strategies)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and improved satisfaction scores using measurable performance metrics)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles, serving as primary contact for 1,200+ accounts across teams)
 ✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)
 
 [AUDIT-2026-002-0002]
```

### 13.7 What the fix did, and what it did not

**Did.** The two fixtures §2 recorded as withheld are now evaluated, and both return the verdict GROUND-TRUTH pre-registered. The F9/F10 pair — the figures test, recorded in §4 as unmeasurable — is measurable, and it passes: same verdict, figures admitted, at least one tag moving to `MET-EVID`. Nothing else in the battery moved: the frozen requirement set, the assets, and the nine fixtures already evaluated are untouched.

**Did not.** Three findings from §2 and §5 are unchanged by this fix and remain open:

- **V-X3 still does not run** on any DOCX. The fix rewrote V-X1's question; V-X3 has no secondary extractor on the DOCX path and reports `NOT RUN` on all four candidates here too.
- **The `unreadable` status and the evaluate-with-flag path are unexercised by this probe.** Both fixtures came back `ok`, so neither new branch of `run.py` ran. The ratification's own verification table covers them on synthetic PDFs; this probe does not.
- **`Second pass?` still trails every E1 pass-1 output** and still reaches E2 inside the NULL list.

And one new one: **the tag route to `Advance` on a silent record is `MET-INF`, not `NO-CONTRA`** (§13.4). That is a difference between the asset's stated doctrine and its behaviour on the exact fixture built to test it, and no verdict in this battery would have changed had it gone the other way — which is why it is a record and not a MISS.

### 13.8 Every artifact, both passes, both fixtures, both runs

#### Appendix C — Run PROBE-FBAT-C, artifacts

##### RUN C `run.json`
```
{
  "run_id": "20260906-054938",
  "mode": "full",
  "boundary_sha256": "5dbd88ae9d8698d29e9b936a3a2e11bceafa57958301956b656e0bb57ec4718c",
  "models": {
    "e1": "deepseek-v4-flash",
    "e2": "gpt-5.1",
    "e2_pass2": "gpt-5.1",
    "extraction": "gpt-5.1"
  },
  "reasoning_effort": {
    "e2": "none",
    "e2_pass2": "high",
    "extraction": "high"
  },
  "jd": "fixtures/happily-csa-jd.txt",
  "resumes": [
    "fixtures/f-battery/F9_thin.docx",
    "fixtures/f-battery/F10_figures_only.docx"
  ]
}
```

##### RUN C `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

##### RUN C R1 F9_thin `intake_report.json`
```
{
  "source": "F9_thin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 9,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          328
        ]
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

##### RUN C R1 F9_thin `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L8: LANGUAGES
L9: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

##### RUN C R1 F9_thin `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

##### RUN C R1 F9_thin `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

##### RUN C R1 F9_thin `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

##### RUN C R1 F9_thin `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with support focus)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year customer support and service roles imply applied customer success and needs-translation experience)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Sustained work in customer support and service typically requires problem-solving and analytical handling of customer issues)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer Support Specialist and Customer Service Officer roles require ongoing customer communication and relationship management)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required — Thai and English listed with fluency/proficiency indications; interview should confirm level against role needs)

[AUDIT-2026-009-0001]
```

##### RUN C R1 F9_thin `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with a support focus)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year customer support and service roles imply applying customer-focused practices and translating customer needs into actions)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Sustained work in customer support and service typically requires structured problem-solving and analytical handling of customer issues)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer Support Specialist and Customer Service Officer roles depend on ongoing customer communication and relationship management)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency explicitly stated)

[AUDIT-2026-009-0002]
```

##### RUN C R1 F9_thin `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with a support focus)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Multi-year customer support and service roles imply applying customer-focused practices and translating customer needs into actions)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Sustained work in customer support and service typically requires structured problem-solving and analytical handling of customer issues)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer Support Specialist and Customer Service Officer roles depend on ongoing customer communication and relationship management)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency explicitly stated)

[AUDIT-2026-009-0002]
```

##### RUN C R2 F10_figures_only `intake_report.json`
```
{
  "source": "F10_figures_only.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 12,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          480
        ]
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

##### RUN C R2 F10_figures_only `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Raised customer satisfaction score from 71% to 88% over 2023–2025
L8: Reduced average first-response time from 6 hours to 40 minutes
L9: Handled 1,200+ accounts across two regional teams
L10: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L11: LANGUAGES
L12: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

##### RUN C R2 F10_figures_only `e1.pass1.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES: none
[FILTRATION-R2]
Second pass?
```

##### RUN C R2 F10_figures_only `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

##### RUN C R2 F10_figures_only `null_list.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES: none
[FILTRATION-R2]
Second pass?
```

##### RUN C R2 F10_figures_only `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist 2021–2026 and Customer Service Officer 2019–2021, handling 1,200+ accounts and front-line customer interactions)
⚖️ Raised customer satisfaction and managed large account volume → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence — Improved CSAT from 71% to 88% and managed 1,200+ accounts, demonstrating application of customer success practices and turning customer needs into concrete improvements)
⚖️ Quantified improvements in response time and satisfaction → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence — Reduced first-response time from 6 hours to 40 minutes and significantly increased CSAT, indicating data-driven analysis and problem-solving to design effective interventions)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing roles in support and service, acting as primary contact for 1,200+ accounts)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required — Thai fluency and English professional working proficiency stated; interview should confirm level against role needs)

[AUDIT-2026-002-0001]
```

##### RUN C R2 F10_figures_only `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist 2021–2026 and Customer Service Officer 2019–2021 in front-line customer support and service roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID — Raised customer satisfaction score from 71% to 88% over 2023–2025 while managing 1,200+ accounts, demonstrating use of customer insights to drive improvements)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and significantly increased CSAT, indicating data analysis and targeted process changes)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles handling 1,200+ accounts)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-002-0002]
```

##### RUN C R2 F10_figures_only `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist 2021–2026 and Customer Service Officer 2019–2021 in front-line customer support and service roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID — Raised customer satisfaction score from 71% to 88% over 2023–2025 while managing 1,200+ accounts, demonstrating use of customer insights to drive improvements)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and significantly increased CSAT, indicating data analysis and targeted process changes)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles handling 1,200+ accounts)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-002-0002]
```

#### Appendix D — Run PROBE-FBAT-D, artifacts

##### RUN D `run.json`
```
{
  "run_id": "20260906-055032",
  "mode": "full",
  "boundary_sha256": "892a8cb75067381ecfa3708e629259e72f569b3d9ff17818d725d185c57a6111",
  "models": {
    "e1": "deepseek-v4-flash",
    "e2": "gpt-5.1",
    "e2_pass2": "gpt-5.1",
    "extraction": "gpt-5.1"
  },
  "reasoning_effort": {
    "e2": "none",
    "e2_pass2": "high",
    "extraction": "high"
  },
  "jd": "fixtures/happily-csa-jd.txt",
  "resumes": [
    "fixtures/f-battery/F9_thin.docx",
    "fixtures/f-battery/F10_figures_only.docx"
  ]
}
```

##### RUN D `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

##### RUN D R1 F9_thin `intake_report.json`
```
{
  "source": "F9_thin.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 9,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          328
        ]
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

##### RUN D R1 F9_thin `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L8: LANGUAGES
L9: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

##### RUN D R1 F9_thin `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

##### RUN D R1 F9_thin `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

##### RUN D R1 F9_thin `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

##### RUN D R1 F9_thin `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles are customer-facing with support focus)
⚖️ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence — Multiple years in customer support and service roles in business settings reasonably demonstrate applied customer success understanding and ability to act on customer needs)
⚖️ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence — Sustained experience in structured customer support roles implies regular problem-solving and use of customer information to resolve issues and improve service)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer Support Specialist and Customer Service Officer roles require ongoing customer communication and relationship management)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required — Thai fluency and English professional working proficiency stated; interview should confirm level against role needs)

[AUDIT-2026-001-0001]
```

##### RUN D R1 F9_thin `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist and Customer Service Officer roles providing ongoing customer-facing support)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Several years in customer support and service roles addressing customer needs and helping improve their outcomes)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Structured customer support work involves diagnosing issues and using customer information to resolve problems and improve service)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer-facing support and service roles require clear communication and relationship-building with customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Record states Thai fluency and English professional working proficiency)

[AUDIT-2026-001-0002]
```

##### RUN D R1 F9_thin `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-EVID — Customer Support Specialist and Customer Service Officer roles providing ongoing customer-facing support)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Several years in customer support and service roles addressing customer needs and helping improve their outcomes)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF — Structured customer support work involves diagnosing issues and using customer information to resolve problems and improve service)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Customer-facing support and service roles require clear communication and relationship-building with customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Record states Thai fluency and English professional working proficiency)

[AUDIT-2026-001-0002]
```

##### RUN D R2 F10_figures_only `intake_report.json`
```
{
  "source": "F10_figures_only.docx",
  "extractor": "python-docx",
  "notes": [],
  "pages": 1,
  "lines": 12,
  "status": "ok",
  "normalization": {
    "invisible_removed": {},
    "soft_wraps_rejoined": 0
  },
  "checks": [
    {
      "name": "V-X1",
      "passed": true,
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          480
        ]
      }
    },
    {
      "name": "V-X2",
      "passed": true,
      "detail": "clean",
      "evidence": {
        "replacement_lines": [],
        "mojibake": []
      }
    },
    {
      "name": "V-X3",
      "passed": null,
      "detail": "NOT RUN \u2014 pdftotext unavailable (recorded, not a pass)",
      "evidence": {}
    },
    {
      "name": "V-X4",
      "passed": true,
      "detail": "normalized text preserves every visible character",
      "evidence": {
        "skeleton_equal": true,
        "compared_in": "NFC"
      }
    }
  ]
}
```

##### RUN D R2 F10_figures_only `numbered.txt`
```
L1: Arisa Boonmee
L2: Phuket, Thailand · arisa.b@example.com
L3: EDUCATION
L4: Bachelor of Business Administration (Marketing), 2016–2020
L5: EXPERIENCE
L6: Customer Support Specialist, Nara Digital Services — Feb 2021 – Aug 2026
L7: Raised customer satisfaction score from 71% to 88% over 2023–2025
L8: Reduced average first-response time from 6 hours to 40 minutes
L9: Handled 1,200+ accounts across two regional teams
L10: Customer Service Officer, Phuket Marine Insurance Brokers — Jan 2019 – Jan 2021
L11: LANGUAGES
L12: Thai – native fluency; English – professional working proficiency (IELTS 7.0, 2021)
```

##### RUN D R2 F10_figures_only `e1.pass1.txt`
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES: none  
[FILTRATION-R2]  
Second pass?
```

##### RUN D R2 F10_figures_only `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

##### RUN D R2 F10_figures_only `null_list.txt`
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES: none  
[FILTRATION-R2]  
Second pass?
```

##### RUN D R2 F10_figures_only `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance – Verify

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles handling 1,200+ accounts and customer issues)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Raised customer satisfaction from 71% to 88% and managed large account base, indicating application of customer success practices)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes using measurable performance data)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing roles in support and service, acting as primary contact for many accounts)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required — Thai and English abilities stated; interview should confirm current proficiency levels in both languages)

[AUDIT-2026-002-0001]
```

##### RUN D R2 F10_figures_only `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles handling customer issues and accounts)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Raised customer satisfaction score from 71% to 88% while managing a large account base, indicating effective customer success strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and improved satisfaction scores using measurable performance metrics)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles, serving as primary contact for 1,200+ accounts across teams)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-002-0002]
```

##### RUN D R2 F10_figures_only `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Arisa Boonmee - Advance

✅ Bachelor’s degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration in Marketing completed)
✅ Experience in a customer-facing role with a focus on customer success, training, or support.: (MET-INF — Customer Support Specialist and Customer Service Officer roles handling customer issues and accounts)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF — Raised customer satisfaction score from 71% to 88% while managing a large account base, indicating effective customer success strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — Reduced average first-response time from 6 hours to 40 minutes and improved satisfaction scores using measurable performance metrics)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — Multi-year customer-facing support and service roles, serving as primary contact for 1,200+ accounts across teams)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Thai fluency and English professional working proficiency stated)

[AUDIT-2026-002-0002]
```


