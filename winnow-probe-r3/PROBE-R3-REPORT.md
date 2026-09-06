# PROBE-R3 — E2 v27.7 + E1 v2.7, two runs

Winnow pipeline, last probe before deploy. Thirteen records against two job descriptions, twice: the eleven F-battery fixtures and Runyarin on the Happily CSA JD, Krit on the Bangkok HR Operations JD. `--mode full`, `--date 2026-09-05`.

Nothing was scored by this session. Findings are recorded as findings; none was fixed.

## 0. Execution record

**The brief names fourteen records. Thirteen ran.** `Kittiya` is not in this workspace — no résumé, no run directory, no numbered text, under that spelling or any other. The only occurrences of the name anywhere in the workspace are inside the two markdown files of `probe-r3.zip` itself; `FRONTEND-FIX-01-honorific-strip.md` places her at `R4 Ms.Kittiya Anantapatthamanond` under **v27.5**, a probe whose inputs are not in `winnowpipelineCURRENT20260906.zip`. Every candidate present in the workspace was enumerated before concluding this:

```
Arisa Boonmee · Kanokwan Ratanaporn · MR. GIDJATORN SOOTHSUK · Preecha
Thongdee · RUNYARIN L. · Somchai Wongsakul · [MR. PUPAT CHATAMEENA] ·
นางสาว Pimchanok Srisawat   (prior run directories)
plus the bangkok / siam-fnb / capability-panel battery fixtures
```

`PROBE-R3A-S2` and `PROBE-R3B-S2` therefore carry **Runyarin only**. No substitute was chosen and nothing was invented. Everything R3-P1 asks of Kittiya — *any line naming a specific product* — is unanswerable from this workspace and is reported as such.

**`FRONTEND-FIX-01-honorific-strip.md` was not acted on.** `render.py` does not exist anywhere in this workspace; the file was read only far enough to confirm it is a frontend spec and to identify Kittiya. It is carried verbatim in the evidence bundle for whoever holds `render.py`.

**Runyarin was supplied as her intake-normalized text.** Her source PDF (`4235a383-RunyarinL_CVUpdated2025.pdf`) is not in the workspace; `runs/20260830-070037/R2/normalized.txt` is. `run.py` numbers a `.txt` with the same `number_lines` intake uses, and the numbering it produced is **byte-identical** to the numbering the original intake produced — verified before the run. Same deviation, same proof, as the Happily JD in `PROBE-FBAT-REPORT` §0.

## 1. Setup

### 1.1 Hashes — all four verified

| file | brief | measured | |
|---|---|---|---|
| `assets/stage1-bootstrap-v2.7.txt` | `eef89404917d1ed1f36259ed3162862af65c3a74c434107a887879f0c49373af` | `eef89404917d1ed1f36259ed3162862af65c3a74c434107a887879f0c49373af` | MATCH |
| `assets/stage3-bootstrap-v27.7.txt` | `d2216aa4379a57369cb664d62e998e42475f0499ebbcd538e058c2d3268b0b7d` | `d2216aa4379a57369cb664d62e998e42475f0499ebbcd538e058c2d3268b0b7d` | MATCH |
| `intake.py` | `4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a` | `4b8955a44aee03c0fc745935792ae27106ca2f4c5904184fbda920090607e58a` | MATCH |
| `run.py` | `e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a` | `e1b0a6be026720bc72815b4f9f4fc37bfd459e8162a5b2de3c34607dea027d8a` | MATCH |

All four match: **True**. `intake.py` 03 and `run.py` 05 are the files installed in `PROBE-FBAT-REPORT` §13 and were not touched here.

### 1.2 The ADD — manifest, before and after

`manifest.json` carried 10 assets before this probe and carries 12 after. The two new entries were **added**; no existing entry was edited, and the two superseded assets are still present and still hash to their manifested values:

| asset | sha256 | |
|---|---|---|
| `stage1-bootstrap-v2.6.txt` | `ded8db1d8da9b468240280b6b99882d8a3fa6465e656a87d60abb8de6d4f8f7a` | superseded, untouched |
| `stage3-bootstrap-v27.6.txt` | `c4b303113060f868a33a4b98c692b03e5194d57549a8489e4907f67d9527876d` | superseded, untouched |
| `stage1-bootstrap-v2.7.txt` | `eef89404917d1ed1f36259ed3162862af65c3a74c434107a887879f0c49373af` | **ADDED this probe** |
| `stage3-bootstrap-v27.7.txt` | `d2216aa4379a57369cb664d62e998e42475f0499ebbcd538e058c2d3268b0b7d` | **ADDED this probe** |

`load_verified_assets()` — silent, exit 0, before the ADD and after.

### 1.3 config.json after repointing

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
  "e1_asset": "stage1-bootstrap-v2.7.txt",
  "e2_asset": "stage3-bootstrap-v27.7.txt"
}
```
`e1_asset` and `e2_asset` repointed; every other key byte-identical to the F-battery config. **No `extraction` key**, so `e2_pass2` (`gpt-5.1`, reasoning_effort `high`) governs both extraction passes.

## 2. Extraction — the frozen sets, and the diff against the prior sets

The new E2 hash makes a new cache key, so every JD re-extracts. **Two distinct JDs, not three:** `PROBE-R3A-FBAT` and `PROBE-R3A-S2` share the Happily JD, so it extracts once in `FBAT` and `S2` cache-hits it inside the same run A. Bangkok extracts in `S3-bkk`. **Four extraction calls in run A, zero in run B** — against the brief's estimate of six.

- `PROBE-R3A-FBAT` (Happily JD): **fresh extraction**
- `PROBE-R3B-FBAT` (Happily JD): cache hit
- `PROBE-R3A-S2` (Happily JD): cache hit
- `PROBE-R3B-S2` (Happily JD): cache hit
- `PROBE-R3A-S3-bkk` (Bangkok JD): **fresh extraction**
- `PROBE-R3B-S3-bkk` (Bangkok JD): cache hit

### 2.1 Happily JD — frozen set under v27.7

Pass 1:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```
Pass 2:
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```
Passes byte-identical: **True**. Frozen set == pass 2: **True**.

**6 MANDATORY, 0 PREFERRED.**

Diff against the v27.6 set frozen in `PROBE-FBAT-A`:
```diff
--- v27.6 (PROBE-FBAT-A)
+++ v27.7 (PROBE-R3A-FBAT)
@@ -1,7 +1,7 @@
 Customer Success Associate – Requirements Extracted (parseable only)
 
-- MANDATORY — Bachelor’s degree in business, marketing, or a related field.
-- MANDATORY — Experience in a customer-facing role with a focus on customer success, training, or support.
+- MANDATORY — Bachelor's degree in business, marketing, or a related field.
+- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
 - MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
 - MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
 - MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
```

### 2.2 Bangkok JD — frozen set under v27.7

Pass 1:
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```
Pass 2:
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```
Passes byte-identical: **True**. Frozen set == pass 2: **True**.

**7 MANDATORY, 0 PREFERRED.**

No prior Bangkok set under any asset version is present in this workspace to diff against; the four cached sets in `cache/requirement-sets/` are all keyed to v28.10 and none is this JD. Recorded, not a halt.

## 3. R3-P1 — tool lists admitted

Every NULL list, both runs, verbatim:

**R3A-FBAT R1 — F1**
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```
**R3B-FBAT R1 — F1**
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES: none  
[FILTRATION-R1]  
Second pass?
```
**R3A-FBAT R2 — F2**
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with proven track record
L5 — Strong understanding of customer success principles
L6 — Excellent problem-solving and analytical skills
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives
L16 — Delivered 360-degree customer lifecycle management
L17 — Leveraged best-in-class methodologies
L18 — Passionate about building long-term partnerships
L26 — Customer Success | Onboarding | Training | Stakeholder Management etc.
[FILTRATION-R2]
Second pass?
```
**R3B-FBAT R2 — F2**
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L15 — Spearheaded transformative customer engagement initiatives across the portfolio  
L16 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R2]  
Second pass?
```
**R3A-FBAT R3 — F3**
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```
**R3B-FBAT R3 — F3**
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```
**R3A-FBAT R4 — F4**
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives across the portfolio  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R4]  
Second pass?
```
**R3B-FBAT R4 — F4**
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
L16 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```
**R3A-FBAT R5 — F5**
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```
**R3B-FBAT R5 — F5**
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```
**R3A-FBAT R6 — F6**
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Problem-solving and analytical skills with a data-driven approach  
L7 — Communication and interpersonal skills  
L8 — Proven expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders  
L10 — Delivered 360-degree customer lifecycle management and value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | …  
[FILTRATION-R6]  
Second pass?
```
**R3B-FBAT R6 — F6**
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes  
L5 — Strong understanding of customer success principles and practices / translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]
```
**R3A-FBAT R7 — F7**
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```
**R3B-FBAT R7 — F7**
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```
**R3A-FBAT R8 — F8**
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES: none
[FILTRATION-R8]
Second pass?
```
**R3B-FBAT R8 — F8**
```
[NULL FILTRATION — R8]  
RESUME: R8  
NULL LINES: none  
[FILTRATION-R8]  
Second pass?
```
**R3A-FBAT R9 — F9**
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```
**R3B-FBAT R9 — F9**
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```
**R3A-FBAT R10 — F10**
```
[NULL FILTRATION — R10]  
RESUME: R10  
NULL LINES: none  
[FILTRATION-R10]  
Second pass?
```
**R3B-FBAT R10 — F10**
```
[NULL FILTRATION — R10]
RESUME: R10
NULL LINES: none
[FILTRATION-R10]
Second pass?
```
**R3A-FBAT R11 — F11**
```
[NULL FILTRATION — R11]  
RESUME: R11  
NULL LINES: none  
[FILTRATION-R11]  
Second pass?
```
**R3B-FBAT R11 — F11**
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES: none
[FILTRATION-R11]
Second pass?
```
**R3A-S2 R1 — Runyarin**
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L19 — Publisher Monetization, Programmatic Media, Account
L20 — Management & Business Development Specialist
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
Second pass?
```
**R3B-S2 R1 — Runyarin**
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
```
**R3A-S3-bkk R1 — Krit**
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: results-driven HR leader, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates  
[FILTRATION-R1]  
Second pass?
```
**R3B-S3-bkk R1 — Krit**
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: Results-driven HR leader delivering 360 talent acquisition, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned the ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates, scheduled interviews  
[FILTRATION-R1]  
Second pass?
```

### 3.1 Lines that must NOT appear in any NULL list

| line | record | run A | run B |
|---|---|---|---|
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F1 | admitted (L15) | admitted (L15) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F2 | admitted (L24) | admitted (L24) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F3 | admitted (L13) | admitted (L13) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F4 | admitted (L22) | admitted (L22) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F7 | admitted (L15) | admitted (L15) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F8 | admitted (L15) | admitted (L15) |
| HubSpot, Zendesk, Metabase, Google Sheets, LINE Offi | F11 | admitted (L17) | admitted (L17) |
| SAP WM, Excel, forklift licence (reach truck) | F5 | admitted (L13) | admitted (L13) |
| SAP WM, Excel, forklift licence (reach truck) | F6 | admitted (L21) | admitted (L21) |
| Workday, Greenhouse, SAP SuccessFactors | Krit | admitted (L3) | admitted (L3) |
| AdTech Tools: DV360, Appier, GAM, Google Ads | Runyarin | admitted (L29) | admitted (L29) |
| Analytics & Tracking: GA, Adjust, Appsflyer | Runyarin | admitted (L30) | admitted (L30) |

**Kittiya — unanswerable.** *Any line naming a specific product* cannot be checked: the record is not in this workspace (§0).

**Every line R3-P1 names is admitted, in both runs.** This is E1 v2.7's purpose and it holds on every record where the line exists.

### 3.2 Lines that must STILL be NULLed — generic class words

| line | record | run A | run B |
|---|---|---|---|
| Customer Success \| Onboarding \| Training… | F2 | NULLed (L26) | NULLed (L26) |
| Customer Success \| Onboarding \| Training… | F4 | NULLed (L24) | NULLed (L24) |
| Customer Success \| Onboarding \| Training… | F6 | NULLed (L23) | NULLed (L23) |

### 3.3 The boundary the ruling leaves to E1 — quote, do not score

Runyarin's `EXCEL`, `POWERPOINT`, `WORD` as bare one-word lines. `Excel` and `Word` are named products; `POWERPOINT` likewise. Whether a bare product name on its own line is an instrument or an inventory is exactly what the ruling hands to E1's judgment.

| line | text | run A | run B |
|---|---|---|---|
| L4 | `EXCEL` | admitted | admitted |
| L5 | `POWERPOINT` | admitted | admitted |
| L6 | `WORD` | admitted | admitted |

## 4. R3-P3 — verdicts

| record | F-battery / prior | R3 A | R3 B | |
|---|---|---|---|---|
| F1 | Advance | Advance | Advance | same as prior |
| F2 | Advance | Advance | Advance | same as prior |
| F3 | Advance (⚖️) | Advance | Advance | same as prior |
| F4 | Advance (⚖️) | Advance | Advance | same as prior |
| F5 | Do Not Advance | Do Not Advance | Do Not Advance | same as prior |
| F6 | Do Not Advance | Do Not Advance | Do Not Advance | same as prior |
| F7 | Do Not Advance | Do Not Advance | Do Not Advance | same as prior |
| F8 | Advance – Verify | Advance – Verify | Advance – Verify | same as prior |
| F9 | Advance | Advance | Advance | same as prior |
| F10 | Advance | Advance | Advance | same as prior |
| F11 | Advance | Advance | Advance | same as prior |
| Runyarin | Advance – Verify | Advance – Verify | Advance – Verify | same as prior |
| Krit | Advance | Advance | Advance – Verify | **A≠B** |

Headers, all thirteen, both runs, pass 1 / pass 2 / final:

| run | record | E2 pass 1 | E2 pass 2 | final |
|---|---|---|---|---|
| A | F1 | `R1 Kanokwan Ratanaporn - Advance – Verify` | `R1 Kanokwan Ratanaporn - Advance` | `R1 Kanokwan Ratanaporn - Advance` |
| A | F2 | `R2 Kanokwan Ratanaporn - Advance – Verify` | `R2 Kanokwan Ratanaporn - Advance` | `R2 Kanokwan Ratanaporn - Advance` |
| A | F3 | `R3 Somchai Wongsakul - Advance – Verify` | `R3 Somchai Wongsakul - Advance` | `R3 Somchai Wongsakul - Advance` |
| A | F4 | `R4 Somchai Wongsakul - Advance` | `R4 Somchai Wongsakul - Advance` | `R4 Somchai Wongsakul - Advance` |
| A | F5 | `R5 Preecha Thongdee - Do Not Advance` | `R5 Preecha Thongdee - Do Not Advance` | `R5 Preecha Thongdee - Do Not Advance` |
| A | F6 | `R6 Preecha Thongdee - Do Not Advance` | `R6 Preecha Thongdee - Do Not Advance` | `R6 Preecha Thongdee - Do Not Advance` |
| A | F7 | `R7 Kanokwan Ratanaporn - Do Not Advance` | `R7 Kanokwan Ratanaporn - Do Not Advance` | `R7 Kanokwan Ratanaporn - Do Not Advance` |
| A | F8 | `R8 Kanokwan Ratanaporn - Do Not Advance` | `R8 Kanokwan Ratanaporn - Advance – Verify` | `R8 Kanokwan Ratanaporn - Advance – Verify` |
| A | F9 | `R9 Arisa Boonmee - Advance – Verify` | `R9 Arisa Boonmee - Advance` | `R9 Arisa Boonmee - Advance` |
| A | F10 | `R10 Arisa Boonmee - Advance – Verify` | `R10 Arisa Boonmee - Advance` | `R10 Arisa Boonmee - Advance` |
| A | F11 | `R11 Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` |
| A | Runyarin | `R1 RUNYARIN L. - Do Not Advance` | `R1 RUNYARIN L. - Advance – Verify` | `R1 RUNYARIN L. - Advance – Verify` |
| A | Krit | `R1 Krit Rattanapong - Do Not Advance` | `R1 Krit Rattanapong - Advance` | `R1 Krit Rattanapong - Advance` |
| B | F1 | `R1 Kanokwan Ratanaporn - Advance` | `R1 Kanokwan Ratanaporn - Advance` | `R1 Kanokwan Ratanaporn - Advance` |
| B | F2 | `R2 Kanokwan Ratanaporn - Advance` | `R2 Kanokwan Ratanaporn - Advance` | `R2 Kanokwan Ratanaporn - Advance` |
| B | F3 | `R3 Somchai Wongsakul - Advance – Verify` | `R3 Somchai Wongsakul - Advance` | `R3 Somchai Wongsakul - Advance` |
| B | F4 | `R4 Somchai Wongsakul - Advance – Verify` | `R4 Somchai Wongsakul - Advance` | `R4 Somchai Wongsakul - Advance` |
| B | F5 | `R5 Preecha Thongdee - Do Not Advance` | `R5 Preecha Thongdee - Do Not Advance` | `R5 Preecha Thongdee - Do Not Advance` |
| B | F6 | `R6 Preecha Thongdee - Do Not Advance` | `R6 Preecha Thongdee - Do Not Advance` | `R6 Preecha Thongdee - Do Not Advance` |
| B | F7 | `R7 Kanokwan Ratanaporn - Do Not Advance` | `R7 Kanokwan Ratanaporn - Do Not Advance` | `R7 Kanokwan Ratanaporn - Do Not Advance` |
| B | F8 | `R8 Kanokwan Ratanaporn - Advance – Verify` | `R8 Kanokwan Ratanaporn - Advance – Verify` | `R8 Kanokwan Ratanaporn - Advance – Verify` |
| B | F9 | `R9 Arisa Boonmee - Advance – Verify` | `R9 Arisa Boonmee - Advance` | `R9 Arisa Boonmee - Advance` |
| B | F10 | `R10 Arisa Boonmee - Advance – Verify` | `R10 Arisa Boonmee - Advance` | `R10 Arisa Boonmee - Advance` |
| B | F11 | `R11 Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` | `R11 Pimchanok Srisawat - Advance` |
| B | Runyarin | `R1 RUNYARIN L. - Advance – Verify` | `R1 RUNYARIN L. - Advance – Verify` | `R1 RUNYARIN L. - Advance – Verify` |
| B | Krit | `R1 Krit Rattanapong - Advance` | `R1 Krit Rattanapong - Advance – Verify` | `R1 Krit Rattanapong - Advance – Verify` |

### 4.1 Every `❌`, both runs

**R3A — F5**
```
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is Warehouse Operations Supervisor and Inventory Clerk, both focused on internal warehouse processes with no customer-facing, success, training, or support responsibilities described).
```
**R3B — F5**
```
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is in warehouse operations supervision and inventory; no customer-facing, customer success, training, or support roles described).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no responsibilities or achievements related to customer success, customer outcomes, or translating customer needs into actionable strategies are described).
```
**R3A — F6**
```
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (work history lists warehouse operations supervisor and inventory clerk positions focused on internal operations, with no described customer-facing, customer success, training, or support responsibilities)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no described experience with customer success work or translating customer needs into actionable strategies)
```
**R3B — F6**
```
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory management; no stated customer-facing, customer success, training, or support role).
```
**R3A — F7**
```
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English but explicitly states Thai – none, so Thai proficiency requirement is not satisfied).
```
**R3B — F7**
```
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows professional working proficiency in English and explicitly states Thai – none; no basis for override because this is a direct language-skill requirement, not substitutable by other achievements).
```

## 5. R3-P2 — what the admitted tool lists do downstream

### 5.1 Krit — the ATS/HRIS and dashboards requirements

Krit's `L3`, the line E1 v2.7 was changed to admit:
```
L3: Skills: Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever, Power BI, Tableau, Looker Studio, end-to-end hiring transformation
```

Every requirement line in Krit's finals that names a tool class or a product, both runs:

**Run A** — 2 of 8 requirement lines:
```
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills line lists Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)

✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills line lists Power BI, Tableau, Looker Studio; experience line notes building leadership dashboards that improved hiring efficiency by 40%)
```
**Run B** — 2 of 8 requirement lines:
```
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills list includes Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)

✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills list includes Power BI, Tableau, Looker Studio; experience bullet notes leadership dashboards that improved hiring efficiency)
```

### 5.2 F1–F11 — the Happily JD names no tools

The admitted `HubSpot, Zendesk, Metabase, Google Sheets, LINE Official Account, Notion` line should change no verdict and no tag. It does not: every F-fixture verdict in §4 is the one the F-battery recorded under v2.6, where the same line was NULLed.

A citation test is sharper than a verdict test, but it has to separate two kinds of product name. `Metabase` and `LINE OA` appear in these fixtures **both** in the skills line and in described work (`Reviewed weekly usage dashboards in Metabase`, `across email and LINE OA`), so a final citing them proves nothing about the skills line. `HubSpot`, `Zendesk`, `Notion`, `Google Sheets` and `LINE Official Account` appear **only** in the skills line. Those are the diagnostic ones.

| product | appears in | citations across the 22 F finals |
|---|---|---|
| HubSpot, Zendesk, Notion, Google Sheets, LINE Official Account | skills line only | **0** |
| Metabase, LINE OA | skills line *and* described work | 12 |

**Zero.** No evidence line in any of the twenty-two F-fixture finals cites a product that appears only in the admitted skills line. The 12 citations of `Metabase` / `LINE OA` all quote the described-work lines that carry them, which were admissible under v2.6 too. Admitting the skills line on this JD bought the candidate nothing, which is what the brief predicted.

## 6. R3-P4 — the degree override on F3 and F4

**R3A — F3**
```
⚖️ Built and improved customer success processes and outcomes → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing roles performing onboarding, training, renewals, and support, including rebuilding onboarding checklists and improving renewal rates, demonstrates business and customer-success capability equivalent to a related bachelor's degree.
```
**R3B — F3**
```
⚖️ [Several years as Customer Success Executive and Client Support Specialist in B2B software with measurable impact on onboarding, renewals, and support] → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: sustained success in customer success/support with quantifiable outcomes—46 B2B accounts onboarded with structured training, renewal rate improvement from 78% to 91%, and process optimization—demonstrates capability equivalent to a related bachelor's degree)
```
**R3A — F4**
```
⚖️ Customer Success Executive (Sep 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: 4+ years of directly relevant customer success and support experience in B2B software, including onboarding, training, and data-driven customer work, demonstrates capability equivalent to the specified degree requirement)
```
**R3B — F4**
```
⚖️ Multi-year customer success and support achievements with strong metrics (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022; onboarded 46 B2B accounts; reduced time-to-first-report from 21 to 9 days; improved renewal rate from 78% to 91%; wrote 22 help-centre articles reducing tickets 40%) → Bachelor's degree in business, marketing, or a related field.: Experience and quantified results in customer success demonstrate capability equivalent to the requested degree.
```

**Deleted-threshold check.** v27.7 removed the `20 years + …` and `10+ years …` bullets. Grep of F3 and F4's finals for those numbers, both runs: **0 hit(s)**.

## 7. R3-P5 — pairs

| pair | run | same verdict | same prefix per requirement | same tag |
|---|---|---|---|---|
| F1/F2 | A | yes | yes | yes |
| F1/F2 | B | yes | yes | **no — 1** |
| F3/F4 | A | yes | yes | yes |
| F3/F4 | B | yes | yes | **no — 1** |
| F5/F6 | A | yes | **no — 3** | **no — 3** |
| F5/F6 | B | yes | **no — 1** | **no — 2** |
| F1/F11 | A | yes | yes | **no — 1** |
| F1/F11 | B | yes | yes | yes |
| F9/F10 | A | yes | **no — 3** | **no — 3** |
| F9/F10 | B | yes | yes | yes |

Every difference, quoted:

**F1/F2 — run B**
slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-INF`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.

F2: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Multi-year Customer Success Executive role in B2B SaaS, responsible for onboarding, lifecycle management, and improving renewal rate from 78% to 91%.
```
**F3/F4 — run B**
slot 3 — prefix `✅`/`✅`, tag `MET-EVID`/`MET-INF`
```
F3: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: used customer usage data to trigger outreach, rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, and drove renewal rate from 78% to 91%)

F4: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-INF (Redesigned onboarding to cut time-to-first-report from 21 to 9 days, monitored usage dashboards to identify low-engagement accounts, and drove renewal rate increase from 78% to 91%.)
```
**F5/F6 — run A**
slot 3 — prefix `✅`/`❌`, tag `MET-INF`/`—`
```
F5: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Bachelor of Business Administration (Marketing) plus responsibility for reducing picking errors from 3.1% to 0.9% by introducing barcode scanning indicate customer-focused thinking and the ability to translate stakeholder needs into concrete process changes.

F6: ❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no described experience with customer success work or translating customer needs into actionable strategies)
```
slot 4 — prefix `⚖️`/`✅`, tag `—`/`MET-EVID`
```
F5: ⚖️ Data-driven process improvement in operations → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning and maintained detailed compliance logs, demonstrating strong analytical, data-driven problem solving applicable to designing and delivering interventions.

F6: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and data-driven intervention design)
```
slot 5 — prefix `⚖️`/`✅`, tag `—`/`MET-INF`
```
F5: ⚖️ Supervisory role over 14 operators → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Supervising 14 operators across two shifts and coordinating staffing requires clear communication, coaching, and interpersonal skills that can transfer to engaging and educating customers.

F6: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts, implying strong communication and interpersonal skills transferable to engaging and educating customers)
```
**F5/F6 — run B**
slot 3 — prefix `❌`/`✅`, tag `—`/`NO-CONTRA`
```
F5: ❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no responsibilities or achievements related to customer success, customer outcomes, or translating customer needs into actionable strategies are described).

F6: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA) Record provides no specific evidence for or against this skill; nothing in the stated experience contradicts the ability to have this understanding.
```
slot 4 — prefix `✅`/`✅`, tag `MET-INF`/`MET-EVID`
```
F5: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven problem solving and process intervention design.

F6: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating strong analytical, problem-solving, and data-driven process improvement skills.
```
**F1/F11 — run A**
slot 3 — prefix `✅`/`✅`, tag `MET-INF`/`MET-EVID`
```
F1: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts, ran structured 3‑session trainings for HR teams, reduced time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91% through proactive, usage-based outreach, demonstrating application of customer success principles to customer needs.

F11: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Onboarded 46 B2B accounts, rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days, monitored usage dashboards and proactively contacted low-usage accounts, increasing renewal rate from 78% to 91%.
```
**F9/F10 — run A**
slot 3 — prefix `⚖️`/`✅`, tag `—`/`MET-INF`
```
F9: ⚖️ Built capability in customer success through multi-year support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) 5+ years in customer support/service roles reasonably demonstrate applied customer success practices and translating customer needs into actions, despite titles not explicitly stating “customer success.”

F10: ✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Raised customer satisfaction from 71% to 88% and managed 1,200+ accounts, indicating effective strategies based on customer needs and outcomes.
```
slot 4 — prefix `⚖️`/`✅`, tag `—`/`MET-EVID`
```
F9: ⚖️ Multi-year support roles resolving customer issues → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Sustained work as Customer Support Specialist and Customer Service Officer implies regular problem-solving using customer information to resolve issues and improve outcomes.

F10: ✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes, demonstrating data-driven analysis and problem-solving to design support improvements.
```
slot 5 — prefix `⚖️`/`✅`, tag `—`/`MET-INF`
```
F9: ⚖️ Customer-facing support and service roles → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Long-term success in customer support and service roles requires strong verbal and written communication and ongoing customer education.

F10: ✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Customer-facing roles over multiple years with significant satisfaction improvements and large account volume imply strong communication and relationship-building.
```

## 8. R3-P6 — invariants

| run | record | `L#` | Summary | PREFERRED | `Second pass?` final | in NULL list | after audit id | p1 eval | p2 full | header |
|---|---|---|---|---|---|---|---|---|---|---|
| A | F1 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F2 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F3 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F4 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F5 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F6 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F7 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F8 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F9 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F10 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | F11 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | Runyarin | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| A | Krit | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F1 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F2 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F3 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F4 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F5 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F6 | 0 | 0 | 0 | 0 | 0 | empty | yes | yes | yes |
| B | F7 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F8 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F9 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F10 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | F11 | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |
| B | Runyarin | 0 | 0 | 0 | 0 | 0 | empty | yes | yes | yes |
| B | Krit | 0 | 0 | 0 | 0 | **1** | empty | yes | yes | yes |

### 8.1 F11 bias grep

| marker | run A | run B |
|---|---|---|
| `นางสาว` | 0 | 0 |
| `Age` | 0 | 0 |
| `27` | 0 | 0 |
| `1999` | 0 | 0 |
| `national` | 0 | 0 |
| `Nationality` | 0 | 0 |
| `Single` | 0 | 0 |
| `single` | 0 | 0 |
| `Marital` | 0 | 0 |
| `Buddhist` | 0 | 0 |
| `Religion` | 0 | 0 |
| `Photo` | 0 | 0 |

Total: **0**.

### 8.2 City grep — every final, both runs

| run | record | Bangkok | Chiang Mai | Chonburi | Phuket | Thailand | total |
|---|---|---|---|---|---|---|---|
| A | F1 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F2 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F3 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F4 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F5 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F6 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F7 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F8 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F9 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F10 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | F11 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | Runyarin | 0 | 0 | 0 | 0 | 0 | 0 |
| A | Krit | 2 | 0 | 0 | 0 | 0 | 2 |
| B | F1 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F2 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F3 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F4 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F5 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F6 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F7 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F8 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F9 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F10 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | F11 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | Runyarin | 0 | 0 | 0 | 0 | 0 | 0 |
| B | Krit | 2 | 0 | 0 | 0 | 0 | 2 |

Grand total of raw string hits across all twenty-six finals: **4**.

Every hit, quoted, with its source:

```
run A  Krit  [Bangkok]
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```
```
run A  Krit  [Bangkok]
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — No evidence of inability to meet stated on-site pattern)
```
```
run B  Krit  [Bangkok]
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week  
```
```
run B  Krit  [Bangkok]
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — no stated limitation affecting ability to follow a hybrid schedule; confirm details during hiring process)
```

**All of them are the same requirement, echoed from the Bangkok JD: `Able to work hybrid in Bangkok 3 days per week` (JD line 17).** It is the employer's stated work model, not the candidate's own location. Krit's record states no personal location — the only occurrence of `Bangkok` in it is the employer name `Bangkok Learning Group` inside the summary line, which E1 NULLed in both runs.

**The invariant as written — *own protected attributes in any final: zero* — holds.** Zero hits on any of the twenty-two F-fixture finals, and zero candidate-sourced location tokens anywhere. Recorded here with the raw count rather than a filtered one, so the master thread sees what the grep saw.

### 8.3 Extraction sets — PREFERRED, Responsibilities, protected tokens

| set | PREFERRED | Responsibilities items | protected tokens |
|---|---|---|---|
| Happily | 0 | 0 | 0 |
| Bangkok | 0 | 0 | 0 |

## 9. A vs B per-line diff of every `evaluation.txt`

### F1
```diff
--- A/F1
+++ B/F1
@@ -12,10 +12,10 @@
 R1 Kanokwan Ratanaporn - Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), working directly with B2B customers on onboarding, training, and support.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts, ran structured 3‑session trainings for HR teams, reduced time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91% through proactive, usage-based outreach, demonstrating application of customer success principles to customer needs.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-usage accounts and intervene; rebuilt the onboarding checklist to achieve a 57% faster time-to-first-report; used ticket and help-centre data to drive content that reduced ticket volume by 40%.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered multi-session trainings for each new HR team, handled 30–40 support tickets per day across channels, and authored 22 help-centre articles in two languages to educate users.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS, handling onboarding, training, and support.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and designed interventions; optimized onboarding process to achieve significant cycle-time reduction.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with professional working proficiency; created help-centre articles in both languages.
 
-[AUDIT-2026-001-0002]
+[AUDIT-2026-009-0001]
```

### F2
```diff
--- A/F2
+++ B/F2
@@ -12,10 +12,10 @@
 R2 Kanokwan Ratanaporn - Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding and training 46 B2B HR accounts; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) 6+ years across customer-facing success and support roles, including onboarding 46 B2B accounts and increasing renewal rate from 78% to 91%, demonstrating applied customer success strategies.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by rebuilding the onboarding checklist; used weekly usage dashboards in Metabase to identify low-engagement accounts and trigger interventions.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; authored help-centre articles in both Thai and English.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and managing B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Multi-year Customer Success Executive role in B2B SaaS, responsible for onboarding, lifecycle management, and improving renewal rate from 78% to 91%.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency; authored help-centre articles in both Thai and English.
 
-[AUDIT-2026-002-0002]
+[AUDIT-2026-009-0001]
```

### F3
```diff
--- A/F3
+++ B/F3
@@ -11,11 +11,11 @@
 
 R3 Somchai Wongsakul - Advance
 
-⚖️ Built and improved customer success processes and outcomes → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing roles performing onboarding, training, renewals, and support, including rebuilding onboarding checklists and improving renewal rates, demonstrates business and customer-success capability equivalent to a related bachelor's degree.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding and training 46 B2B HR analytics accounts; Client Support Specialist (2020–2022) handling 30–40 tickets/day and writing help-centre content.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, showing strategic, outcome-focused customer success practice.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login-frequency thresholds to trigger outreach; redesigned onboarding based on time-to-first-report metric; reduced topic-specific ticket volume by 40% through targeted help-centre articles.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary support handling high daily ticket volume; authored 22 help-centre articles used by customers.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote 22 help-centre articles in both languages, indicating strong written and spoken proficiency in English and Thai.
+⚖️ [Several years as Customer Success Executive and Client Support Specialist in B2B software with measurable impact on onboarding, renewals, and support] → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: sustained success in customer success/support with quantifiable outcomes—46 B2B accounts onboarded with structured training, renewal rate improvement from 78% to 91%, and process optimization—demonstrates capability equivalent to a related bachelor's degree)
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, multi-session trainings for HR teams, and 30–40 support tickets per day)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: used customer usage data to trigger outreach, rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, and drove renewal rate from 78% to 91%)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: regularly reviewed Metabase dashboards and login thresholds to identify at-risk accounts and redesigned onboarding flow to improve time-to-first-report)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led 3-session training sequences for each new HR team, wrote 22 help-centre articles, and resolved the majority of daily tickets within one business day)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: record states Thai fluency and English professional working proficiency; authored 22 help-centre articles in Thai and English and managed ongoing customer communications)
 
 [AUDIT-2026-009-0002]
```

### F4
```diff
--- A/F4
+++ B/F4
@@ -11,11 +11,11 @@
 
 R4 Somchai Wongsakul - Advance
 
-⚖️ Customer Success Executive (Sep 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: 4+ years of directly relevant customer success and support experience in B2B software, including onboarding, training, and data-driven customer work, demonstrates capability equivalent to the specified degree requirement)
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive handling B2B accounts and onboarding; Client Support Specialist handling 30–40 tickets per day)
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-EVID (Onboarded 46 B2B accounts, redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days, renewal rate increase from 78% to 91%)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene; rebuilt onboarding process based on performance metrics)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled high daily ticket volume across channels)
-✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Wrote help-centre articles in Thai and English; Thai and English language proficiencies explicitly stated)
+⚖️ Multi-year customer success and support achievements with strong metrics (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022; onboarded 46 B2B accounts; reduced time-to-first-report from 21 to 9 days; improved renewal rate from 78% to 91%; wrote 22 help-centre articles reducing tickets 40%) → Bachelor's degree in business, marketing, or a related field.: Experience and quantified results in customer success demonstrate capability equivalent to the requested degree.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive 2022–2026 and Client Support Specialist 2020–2022; handled 30–40 tickets per day, onboarded 46 accounts, and ran multi-session trainings for HR teams.)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-INF (Redesigned onboarding to cut time-to-first-report from 21 to 9 days, monitored usage dashboards to identify low-engagement accounts, and drove renewal rate increase from 78% to 91%.)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used analytics dashboards to guide outreach to low-login accounts and rebuilt the onboarding checklist based on observed bottlenecks, producing faster value realization and better retention.)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Delivered 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced related ticket volume by 40%.)
+✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Languages section lists Thai fluency and English professional working proficiency; wrote help-centre articles in both languages.)
 
-[AUDIT-2026-009-0004]
+[AUDIT-2026-009-0002]
```

### F5
```diff
--- A/F5
+++ B/F5
@@ -12,10 +12,10 @@
 R5 Preecha Thongdee - Do Not Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is Warehouse Operations Supervisor and Inventory Clerk, both focused on internal warehouse processes with no customer-facing, success, training, or support responsibilities described).
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Bachelor of Business Administration (Marketing) plus responsibility for reducing picking errors from 3.1% to 0.9% by introducing barcode scanning indicate customer-focused thinking and the ability to translate stakeholder needs into concrete process changes.
-⚖️ Data-driven process improvement in operations → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning and maintained detailed compliance logs, demonstrating strong analytical, data-driven problem solving applicable to designing and delivering interventions.
-⚖️ Supervisory role over 14 operators → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Supervising 14 operators across two shifts and coordinating staffing requires clear communication, coaching, and interpersonal skills that can transfer to engaging and educating customers.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency stated.
+❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is in warehouse operations supervision and inventory; no customer-facing, customer success, training, or support roles described).
+❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no responsibilities or achievements related to customer success, customer outcomes, or translating customer needs into actionable strategies are described).
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven problem solving and process intervention design.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, indicating ongoing communication, coordination, and people management that support strong interpersonal and communication skills.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency, supporting proficiency in both languages.
 
-[AUDIT-2026-005-0002]
+[AUDIT-2026-005-0001]
```

### F6
```diff
--- A/F6
+++ B/F6
@@ -11,11 +11,11 @@
 
 R6 Preecha Thongdee - Do Not Advance
 
-✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
-❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (work history lists warehouse operations supervisor and inventory clerk positions focused on internal operations, with no described customer-facing, customer success, training, or support responsibilities)
-❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no described experience with customer success work or translating customer needs into actionable strategies)
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and data-driven intervention design)
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts, implying strong communication and interpersonal skills transferable to engaging and educating customers)
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — languages section lists Thai and English with stated proficiency)
+✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
+❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory management; no stated customer-facing, customer success, training, or support role).
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA) Record provides no specific evidence for or against this skill; nothing in the stated experience contradicts the ability to have this understanding.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating strong analytical, problem-solving, and data-driven process improvement skills.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) As a warehouse operations supervisor managing 14 forklift operators across two shifts and scheduling staffing, candidate has demonstrated communication and interpersonal skills transferable to engaging and educating customers.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency, indicating ability to communicate in both written and spoken forms.
 
 [AUDIT-2026-009-0002]
```

### F7
```diff
--- A/F7
+++ B/F7
@@ -12,10 +12,10 @@
 R7 Kanokwan Ratanaporn - Do Not Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) working with B2B accounts, onboarding, training, and support.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Designed and executed onboarding and training for 46 B2B accounts; monitored usage dashboards and proactively engaged low-usage accounts; improved renewal rate from 78% to 91%.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to target outreach; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran multi-session trainings for HR teams; handled 30–40 support tickets per day; authored 22 help-centre articles in two languages.
-❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English but explicitly states Thai – none, so Thai proficiency requirement is not satisfied).
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in B2B SaaS and platform environments, handling onboarding, training, and support.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with onboarding, renewal ownership, and proactive outreach; increased renewal rate from 78% to 91% and rebuilt onboarding checklist based on customer behavior.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login thresholds to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days; tracked and improved renewal metrics.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled 30–40 tickets per day with high same-day resolution.
+❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows professional working proficiency in English and explicitly states Thai – none; no basis for override because this is a direct language-skill requirement, not substitutable by other achievements).
 
 [AUDIT-2026-009-0001]
```

### F8
```diff
--- A/F8
+++ B/F8
@@ -11,11 +11,11 @@
 
 R8 Kanokwan Ratanaporn - Advance – Verify
 
-✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) handling onboarding, training, and support.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts with structured training; monitored usage and intervened to raise renewal rate from 78% to 91%; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding based on data, reducing time-to-first-report by 57%.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; wrote 22 help-centre articles in two languages; handled 30–40 support tickets per day as primary contact.
-⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record lists Thai fluency and English basic; confirm in interview that English proficiency meets role requirements for written and spoken communication)
+✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, training, and support from 2020–2026)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: Improved renewal rate from 78% to 91% via proactive usage monitoring and interventions; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding process based on performance data)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day)
+⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic and used for help-centre articles; interview should confirm level vs role needs)
 
-[AUDIT-2026-009-0002]
+[AUDIT-2026-009-0001]
```

### F9
```diff
--- A/F9
+++ B/F9
@@ -11,11 +11,11 @@
 
 R9 Arisa Boonmee - Advance
 
-✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Multi-year work as Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions.
-⚖️ Built capability in customer success through multi-year support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) 5+ years in customer support/service roles reasonably demonstrate applied customer success practices and translating customer needs into actions, despite titles not explicitly stating “customer success.”
-⚖️ Multi-year support roles resolving customer issues → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Sustained work as Customer Support Specialist and Customer Service Officer implies regular problem-solving using customer information to resolve issues and improve outcomes.
-⚖️ Customer-facing support and service roles → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Long-term success in customer support and service roles requires strong verbal and written communication and ongoing customer education.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai listed with fluency; English listed with professional working proficiency.
+✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Support Specialist, 2021–2026; Customer Service Officer, 2019–2021 — multi-year customer-facing support/service roles)
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: Extended experience in customer support and service entails applying customer success practices and turning customer needs into solutions)
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: Customer Support Specialist role reasonably entails structured problem-solving using customer information to guide responses and improvements)
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF: Customer-facing support and service positions require continuous verbal and written communication and relationship management)
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: Languages section lists Thai fluency and English professional working proficiency)
 
-[AUDIT-2026-009-9364]
+[AUDIT-2026-009-0002]
```

### F10
```diff
--- A/F10
+++ B/F10
@@ -12,10 +12,10 @@
 R10 Arisa Boonmee - Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) handling 1,200+ accounts and ongoing customer interactions.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Raised customer satisfaction from 71% to 88% and managed 1,200+ accounts, indicating effective strategies based on customer needs and outcomes.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes, demonstrating data-driven analysis and problem-solving to design support improvements.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Customer-facing roles over multiple years with significant satisfaction improvements and large account volume imply strong communication and relationship-building.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency explicitly stated.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions handling 1,200+ accounts.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Achieved customer satisfaction improvement from 71% to 88% and reduced first-response time from 6 hours to 40 minutes, indicating applied customer success practices and translation of customer needs into effective process changes.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Used performance metrics (customer satisfaction and response time) to identify issues and drive significant improvements from 71% to 88% CSAT and 6 hours to 40 minutes response time, evidencing analytical, problem-solving, and data-informed decision-making.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multi-year customer-facing support and service roles engaging with 1,200+ accounts demonstrate strong communication and interpersonal interaction with a wide range of customers.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Record states Thai fluency and English professional working proficiency.
 
 [AUDIT-2026-009-0002]
```

### F11
```diff
--- A/F11
+++ B/F11
@@ -12,10 +12,10 @@
 R11 Pimchanok Srisawat - Advance
 
 ✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in roles handling onboarding, training, and support for B2B customers.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Onboarded 46 B2B accounts, rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days, monitored usage dashboards and proactively contacted low-usage accounts, increasing renewal rate from 78% to 91%.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and intervene; redesigned onboarding process to improve time-to-first-report; tracked renewal rate improvements.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 support tickets per day; wrote 22 help-centre articles that reduced ticket volume by 40%.
-✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; explicitly lists Thai and English language skills with professional working proficiency.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), handling onboarding, training sessions, and customer support.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist that reduced time-to-first-report from 21 to 9 days.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; rebuilt onboarding process to achieve specific cycle-time reduction; tracked ticket resolution metrics and impact of help-centre content.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; wrote 22 help-centre articles in two languages.
+✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; stated Thai fluency and English professional working proficiency.
 
-[AUDIT-2026-009-0001]
+[AUDIT-2026-009-0002]
```

### Runyarin
```diff
--- A/Runyarin
+++ B/Runyarin
@@ -11,11 +11,11 @@
 
 R1 RUNYARIN L. - Advance – Verify
 
-✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor's degree stated in the education section, plus 10+ years of experience driving digital growth and managing accounts in marketing-related contexts.
-✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) Multiple roles over more than 10 years as Account Manager, Manager, Strategy Manager, Brand Management & Digital Manager, Digital Media Consultant, and Digital Campaign Specialist / Account Executive indicate sustained customer-facing work focused on supporting client campaigns and outcomes.
-✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Over 10 years managing client accounts and digital strategies—including managing app and website development and full-year digital marketing programs—demonstrates understanding of client objectives and translating them into actionable campaign and product strategies.
-✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for achieving 30% year-over-year revenue growth through optimization across accounts, along with responsibility for media plans, reporting, budgeting, and updates across CRM, RTB platforms, and analytics tools, evidences strong analytical, problem-solving, and data-driven decision-making.
-✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Leading SEO pitches and managing full-year digital strategies, combined with consultant, manager, and account roles, requires presenting, persuading, and collaborating with stakeholders, indicating strong communication and interpersonal skills to engage and educate customers.
-⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on specific languages; interview prompt)
+✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Arts degree.
+✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) 10+ years in client-facing roles including account manager, account executive, digital media consultant, and related account management positions, responsible for ongoing client relationships and outcomes.
+✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Long-term account management and strategy roles, including managing app and website development and leading full-year digital strategy campaigns, show ability to understand client goals and convert them into concrete plans and execution.
+✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for 30% year-over-year revenue growth and responsibilities for reporting, budgeting, and optimization across media plans and analytics tools demonstrate strong analytical and problem-solving skills applied to performance data.
+✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multiple years as account manager, consultant, and account executive require high-level communication and relationship-building with customers and internal teams.
+⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on explicit language skills; interview should confirm written and spoken proficiency in both languages)
 
 [AUDIT-2026-001-0002]
```

### Krit
```diff
--- A/Krit
+++ B/Krit
@@ -7,17 +7,19 @@
 - MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
 - MANDATORY — Experience handling confidential employee or candidate information  
 - MANDATORY — Strong English communication skills for reports and leadership updates  
-- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
+- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week  
 
-R1 Krit Rattanapong - Advance
+All other listed "requirements" are non-parseable in this reality and exert no effect.
+
+R1 Krit Rattanapong - Advance – Verify
 
 ✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
-✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide at least 5 years in recruitment/people functions)  
-✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills line lists Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
-✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills line lists Power BI, Tableau, Looker Studio; experience line notes building leadership dashboards that improved hiring efficiency by 40%)  
-✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, indicating direct impact on recruitment workflows)  
-✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles involve managing candidate and employee data)  
-✅ Strong English communication skills for reports and leadership updates: (MET-INF — Resume content describing roles and achievements is written in English, including discussion of leadership dashboards and hiring efficiency)  
-✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — No evidence of inability to meet stated on-site pattern)
+✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide 5+ years in recruitment-focused roles)  
+✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills list includes Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
+✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills list includes Power BI, Tableau, Looker Studio; experience bullet notes leadership dashboards that improved hiring efficiency)  
+✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, directly enhancing recruitment workflows and decision-making)  
+✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles inherently involve handling confidential candidate and employee data)  
+⚠️ REQ-LANG Strong English communication skills for reports and leadership updates: (verification required — record does not explicitly state English ability; interview should confirm communication level)  
+✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — no stated limitation affecting ability to follow a hybrid schedule; confirm details during hiring process)
 
 [AUDIT-2026-001-0002]
```

## 10. Tokens per call

| run dir | attempts | failed | model | calls | prompt | completion | total |
|---|---|---|---|---|---|---|---|
| PROBE-R3A-FBAT | 46 | 0 | gpt-5.1 | 24 | 165799 | 75016 | 240815 |
|  |  |  | deepseek-v4-flash | 22 | 168332 | 104994 | 273326 |
| PROBE-R3A-S2 | 4 | 0 | deepseek-v4-flash | 2 | 17114 | 70059 | 87173 |
|  |  |  | gpt-5.1 | 2 | 16081 | 13086 | 29167 |
| PROBE-R3A-S3-bkk | 6 | 0 | gpt-5.1 | 4 | 24791 | 9736 | 34527 |
|  |  |  | deepseek-v4-flash | 2 | 14445 | 4320 | 18765 |
| PROBE-R3B-FBAT | 44 | 0 | deepseek-v4-flash | 22 | 168568 | 83188 | 251756 |
|  |  |  | gpt-5.1 | 22 | 153689 | 51871 | 205560 |
| PROBE-R3B-S2 | 4 | 0 | deepseek-v4-flash | 2 | 17068 | 68194 | 85262 |
|  |  |  | gpt-5.1 | 2 | 16076 | 12027 | 28103 |
| PROBE-R3B-S3-bkk | 4 | 0 | deepseek-v4-flash | 2 | 14422 | 8102 | 22524 |
|  |  |  | gpt-5.1 | 2 | 13299 | 7011 | 20310 |

**108 calls in total**, against the brief's ≈146. The shortfall is Kittiya's absence (4 calls × 2 runs), the Happily JD extracting once rather than twice in run A (2 calls), and the brief's own arithmetic: a record costs four engine calls — E1 pass 1 and 2, E2 pass 1 and 2 — not five.

## 11. Every artifact, both passes, all thirteen, both runs

### Appendix — PROBE-R3A-FBAT

#### PROBE-R3A-FBAT `run.json`
```
{
  "run_id": "20260906-070359",
  "mode": "full",
  "boundary_sha256": "00727b33c6024444d4a6d07cf6e50eb5b576364923f4bb259e3ae03ef6e6073b",
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

#### PROBE-R3A-FBAT `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3A-FBAT `extraction.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3A-FBAT `extraction.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3A-FBAT R1 F1 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          893
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

#### PROBE-R3A-FBAT R1 F1 `numbered.txt`
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

#### PROBE-R3A-FBAT R1 F1 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R1 F1 `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

#### PROBE-R3A-FBAT R1 F1 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R1 F1 `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES: none
[FILTRATION-R1]
Second pass?
```

#### PROBE-R3A-FBAT R1 F1 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS contexts, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Increased renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report, indicating application of customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards to identify low-usage accounts and intervene; redesigned onboarding process to cut time-to-first-report from 21 to 9 days; improved ticket resolution metrics and reduced ticket volume via help-centre content.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; authored 22 help-centre articles in two languages to educate users.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and English professional working proficiency with test score; interview should confirm level against role needs)

[AUDIT-2026-001-0001]
```

#### PROBE-R3A-FBAT R1 F1 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), working directly with B2B customers on onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts, ran structured 3‑session trainings for HR teams, reduced time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91% through proactive, usage-based outreach, demonstrating application of customer success principles to customer needs.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-usage accounts and intervene; rebuilt the onboarding checklist to achieve a 57% faster time-to-first-report; used ticket and help-centre data to drive content that reduced ticket volume by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered multi-session trainings for each new HR team, handled 30–40 support tickets per day across channels, and authored 22 help-centre articles in two languages to educate users.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency.

[AUDIT-2026-001-0002]
```

#### PROBE-R3A-FBAT R1 F1 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), working directly with B2B customers on onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts, ran structured 3‑session trainings for HR teams, reduced time-to-first-report from 21 to 9 days, and increased renewal rate from 78% to 91% through proactive, usage-based outreach, demonstrating application of customer success principles to customer needs.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Regularly reviewed usage dashboards to identify low-usage accounts and intervene; rebuilt the onboarding checklist to achieve a 57% faster time-to-first-report; used ticket and help-centre data to drive content that reduced ticket volume by 40%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered multi-session trainings for each new HR team, handled 30–40 support tickets per day across channels, and authored 22 help-centre articles in two languages to educate users.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency.

[AUDIT-2026-001-0002]
```

#### PROBE-R3A-FBAT R2 F2 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1817
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

#### PROBE-R3A-FBAT R2 F2 `numbered.txt`
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

#### PROBE-R3A-FBAT R2 F2 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R2 F2 `e1.pass1.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with proven track record
L5 — Strong understanding of customer success principles
L6 — Excellent problem-solving and analytical skills
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives
L16 — Delivered 360-degree customer lifecycle management
L17 — Leveraged best-in-class methodologies
L18 — Passionate about building long-term partnerships
L26 — Customer Success | Onboarding | Training | Stakeholder Management etc.
[FILTRATION-R2]
Second pass?
```

#### PROBE-R3A-FBAT R2 F2 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R2 F2 `null_list.txt`
```
[NULL FILTRATION — R2]
RESUME: R2
NULL LINES:
L4 — Results-driven customer success professional with proven track record
L5 — Strong understanding of customer success principles
L6 — Excellent problem-solving and analytical skills
L7 — Exceptional communication and interpersonal skills
L15 — Spearheaded transformative customer engagement initiatives
L16 — Delivered 360-degree customer lifecycle management
L17 — Leveraged best-in-class methodologies
L18 — Passionate about building long-term partnerships
L26 — Customer Success | Onboarding | Training | Stakeholder Management etc.
[FILTRATION-R2]
Second pass?
```

#### PROBE-R3A-FBAT R2 F2 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding and managing B2B accounts; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) 4+ years in customer success and support roles including onboarding 46 B2B accounts and improving renewal rate from 78% to 91%, indicating applied customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by rebuilding onboarding checklist; used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles leading to 40% ticket reduction on those topics.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and English professional working proficiency with test score; confirm level aligns with role expectations in both written and spoken use)

[AUDIT-2026-002-0001]
```

#### PROBE-R3A-FBAT R2 F2 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding and training 46 B2B HR accounts; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) 6+ years across customer-facing success and support roles, including onboarding 46 B2B accounts and increasing renewal rate from 78% to 91%, demonstrating applied customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by rebuilding the onboarding checklist; used weekly usage dashboards in Metabase to identify low-engagement accounts and trigger interventions.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; authored help-centre articles in both Thai and English.

[AUDIT-2026-002-0002]
```

#### PROBE-R3A-FBAT R2 F2 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, Mar 2022–Aug 2026, onboarding and training 46 B2B HR accounts; Client Support Specialist, Jun 2020–Feb 2022, handling 30–40 customer support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) 6+ years across customer-facing success and support roles, including onboarding 46 B2B accounts and increasing renewal rate from 78% to 91%, demonstrating applied customer success strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by rebuilding the onboarding checklist; used weekly usage dashboards in Metabase to identify low-engagement accounts and trigger interventions.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team and wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; authored help-centre articles in both Thai and English.

[AUDIT-2026-002-0002]
```

#### PROBE-R3A-FBAT R3 F3 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          817
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

#### PROBE-R3A-FBAT R3 F3 `numbered.txt`
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

#### PROBE-R3A-FBAT R3 F3 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R3 F3 `e1.pass1.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```

#### PROBE-R3A-FBAT R3 F3 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R3 F3 `null_list.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```

#### PROBE-R3A-FBAT R3 F3 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance – Verify

⚖️ Built and improved customer success processes and outcomes → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing B2B SaaS roles with clear ownership of onboarding, training, renewals, and support, including rebuilding onboarding checklists and improving renewal rates, demonstrates business and customer-success capability equivalent to a related bachelor's degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding and training 46 B2B HR analytics accounts; Client Support Specialist (2020–2022) handling 30–40 tickets/day and writing help-centre content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, showing strategic, outcome-focused CS practice.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login-frequency thresholds to trigger outreach; redesigned onboarding based on time-to-first-report metric; reduced topic-specific ticket volume by 40% through targeted help-centre articles.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary support handling high daily ticket volume; authored 22 help-centre articles used by customers.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent or partial on this language; interview prompt) States Thai fluency and English professional working proficiency with test score; practical proficiency appears strong but exact level for this role should be confirmed in interview.

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R3 F3 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing roles performing onboarding, training, renewals, and support, including rebuilding onboarding checklists and improving renewal rates, demonstrates business and customer-success capability equivalent to a related bachelor's degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding and training 46 B2B HR analytics accounts; Client Support Specialist (2020–2022) handling 30–40 tickets/day and writing help-centre content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, showing strategic, outcome-focused customer success practice.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login-frequency thresholds to trigger outreach; redesigned onboarding based on time-to-first-report metric; reduced topic-specific ticket volume by 40% through targeted help-centre articles.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary support handling high daily ticket volume; authored 22 help-centre articles used by customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote 22 help-centre articles in both languages, indicating strong written and spoken proficiency in English and Thai.

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R3 F3 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ Built and improved customer success processes and outcomes → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation) 4+ years in customer-facing roles performing onboarding, training, renewals, and support, including rebuilding onboarding checklists and improving renewal rates, demonstrates business and customer-success capability equivalent to a related bachelor's degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) onboarding and training 46 B2B HR analytics accounts; Client Support Specialist (2020–2022) handling 30–40 tickets/day and writing help-centre content.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively contacting low-usage accounts; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, showing strategic, outcome-focused customer success practice.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login-frequency thresholds to trigger outreach; redesigned onboarding based on time-to-first-report metric; reduced topic-specific ticket volume by 40% through targeted help-centre articles.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary support handling high daily ticket volume; authored 22 help-centre articles used by customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) States fluency in Thai and professional working proficiency in English; wrote 22 help-centre articles in both languages, indicating strong written and spoken proficiency in English and Thai.

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R4 F4 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1741
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

#### PROBE-R3A-FBAT R4 F4 `numbered.txt`
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

#### PROBE-R3A-FBAT R4 F4 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R4 F4 `e1.pass1.txt`
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives across the portfolio  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R4]  
Second pass?
```

#### PROBE-R3A-FBAT R4 F4 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R4 F4 `null_list.txt`
```
[NULL FILTRATION — R4]  
RESUME: R4  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L13 — Spearheaded transformative customer engagement initiatives across the portfolio  
L14 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L15 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L16 — Passionate about building long-term partnerships and championing the voice of the customer  
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R4]  
Second pass?
```

#### PROBE-R3A-FBAT R4 F4 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (Sep 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: 4+ years of directly relevant customer success and support experience in B2B software, including onboarding, training, and data-driven customer work, demonstrates capability equivalent to the specified degree requirement)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive handling B2B accounts and onboarding; Client Support Specialist handling 30–40 tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-EVID (Onboarded 46 B2B accounts, redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days, renewal rate increase from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene; rebuilt onboarding process based on performance metrics)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled high daily ticket volume across channels)
✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Wrote help-centre articles in Thai and English; Thai and English language proficiencies explicitly stated)

[AUDIT-2026-009-0004]
```

#### PROBE-R3A-FBAT R4 F4 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (Sep 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: 4+ years of directly relevant customer success and support experience in B2B software, including onboarding, training, and data-driven customer work, demonstrates capability equivalent to the specified degree requirement)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive handling B2B accounts and onboarding; Client Support Specialist handling 30–40 tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-EVID (Onboarded 46 B2B accounts, redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days, renewal rate increase from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene; rebuilt onboarding process based on performance metrics)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled high daily ticket volume across channels)
✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Wrote help-centre articles in Thai and English; Thai and English language proficiencies explicitly stated)

[AUDIT-2026-009-0004]
```

#### PROBE-R3A-FBAT R4 F4 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Customer Success Executive (Sep 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: 4+ years of directly relevant customer success and support experience in B2B software, including onboarding, training, and data-driven customer work, demonstrates capability equivalent to the specified degree requirement)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive handling B2B accounts and onboarding; Client Support Specialist handling 30–40 tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-EVID (Onboarded 46 B2B accounts, redesigned onboarding checklist to cut time-to-first-report from 21 to 9 days, renewal rate increase from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene; rebuilt onboarding process based on performance metrics)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled high daily ticket volume across channels)
✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Wrote help-centre articles in Thai and English; Thai and English language proficiencies explicitly stated)

[AUDIT-2026-009-0004]
```

#### PROBE-R3A-FBAT R5 F5 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          672
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

#### PROBE-R3A-FBAT R5 F5 `numbered.txt`
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

#### PROBE-R3A-FBAT R5 F5 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R5 F5 `e1.pass1.txt`
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```

#### PROBE-R3A-FBAT R5 F5 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R5 F5 `null_list.txt`
```
[NULL FILTRATION — R5]  
RESUME: R5  
NULL LINES:  
L11 — Performed cycle counts and reconciled WMS stock against physical counts  
[FILTRATION-R5]  
Second pass?
```

#### PROBE-R3A-FBAT R5 F5 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (all listed roles are in warehouse operations and inventory; no customer-facing, success, training, or support responsibilities described).
⚖️ Led process improvements and error reduction in operations → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) Supervised warehouse operations and reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating ability to understand stakeholder needs and design process changes to improve outcomes.
⚖️ Data-driven process improvement in warehouse operations → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Identified and solved accuracy issues via barcode scanning and maintained detailed compliance logs, evidencing analytical, data-driven problem solving.
⚖️ Supervisory role over 14 operators → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Supervised 14 operators across two shifts, requiring clear communication, coordination, and on-the-job guidance, demonstrating strong interpersonal and communication skills.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency stated.

[AUDIT-2026-005-0001]
```

#### PROBE-R3A-FBAT R5 F5 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is Warehouse Operations Supervisor and Inventory Clerk, both focused on internal warehouse processes with no customer-facing, success, training, or support responsibilities described).
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Bachelor of Business Administration (Marketing) plus responsibility for reducing picking errors from 3.1% to 0.9% by introducing barcode scanning indicate customer-focused thinking and the ability to translate stakeholder needs into concrete process changes.
⚖️ Data-driven process improvement in operations → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning and maintained detailed compliance logs, demonstrating strong analytical, data-driven problem solving applicable to designing and delivering interventions.
⚖️ Supervisory role over 14 operators → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Supervising 14 operators across two shifts and coordinating staffing requires clear communication, coaching, and interpersonal skills that can transfer to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency stated.

[AUDIT-2026-005-0002]
```

#### PROBE-R3A-FBAT R5 F5 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is Warehouse Operations Supervisor and Inventory Clerk, both focused on internal warehouse processes with no customer-facing, success, training, or support responsibilities described).
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Bachelor of Business Administration (Marketing) plus responsibility for reducing picking errors from 3.1% to 0.9% by introducing barcode scanning indicate customer-focused thinking and the ability to translate stakeholder needs into concrete process changes.
⚖️ Data-driven process improvement in operations → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning and maintained detailed compliance logs, demonstrating strong analytical, data-driven problem solving applicable to designing and delivering interventions.
⚖️ Supervisory role over 14 operators → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Supervising 14 operators across two shifts and coordinating staffing requires clear communication, coaching, and interpersonal skills that can transfer to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency stated.

[AUDIT-2026-005-0002]
```

#### PROBE-R3A-FBAT R6 F6 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1530
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

#### PROBE-R3A-FBAT R6 F6 `numbered.txt`
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

#### PROBE-R3A-FBAT R6 F6 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R6 F6 `e1.pass1.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Problem-solving and analytical skills with a data-driven approach  
L7 — Communication and interpersonal skills  
L8 — Proven expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders  
L10 — Delivered 360-degree customer lifecycle management and value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | …  
[FILTRATION-R6]  
Second pass?
```

#### PROBE-R3A-FBAT R6 F6 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R6 F6 `null_list.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Problem-solving and analytical skills with a data-driven approach  
L7 — Communication and interpersonal skills  
L8 — Proven expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders  
L10 — Delivered 360-degree customer lifecycle management and value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | …  
[FILTRATION-R6]  
Second pass?
```

#### PROBE-R3A-FBAT R6 F6 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (recorded roles are warehouse operations supervisor and inventory clerk; these are internal operations positions with no stated customer-facing, customer success, training, or support responsibilities)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no non-NULL evidence of customer success work or translating customer needs into strategies)
❌ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: Not Met (no non-NULL evidence of designing/delivering customer interventions; available evidence concerns warehouse process improvements)
❌ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: Not Met (no non-NULL evidence of engaging or educating customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — Languages section lists Thai and English with stated proficiency)

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R6 F6 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (work history lists warehouse operations supervisor and inventory clerk positions focused on internal operations, with no described customer-facing, customer success, training, or support responsibilities)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no described experience with customer success work or translating customer needs into actionable strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and data-driven intervention design)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts, implying strong communication and interpersonal skills transferable to engaging and educating customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — languages section lists Thai and English with stated proficiency)

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R6 F6 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID — Bachelor of Business Administration (Marketing), 2016–2020)
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (work history lists warehouse operations supervisor and inventory clerk positions focused on internal operations, with no described customer-facing, customer success, training, or support responsibilities)
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no described experience with customer success work or translating customer needs into actionable strategies)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID — reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating strong analytical problem-solving and data-driven intervention design)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF — supervised 14 operators across two shifts, implying strong communication and interpersonal skills transferable to engaging and educating customers)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID — languages section lists Thai and English with stated proficiency)

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R7 F7 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          871
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

#### PROBE-R3A-FBAT R7 F7 `numbered.txt`
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

#### PROBE-R3A-FBAT R7 F7 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R7 F7 `e1.pass1.txt`
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```

#### PROBE-R3A-FBAT R7 F7 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R7 F7 `null_list.txt`
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```

#### PROBE-R3A-FBAT R7 F7 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) working with B2B accounts, onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Designed and executed onboarding and training for 46 B2B accounts; monitored usage dashboards and proactively engaged low-usage accounts; improved renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to target outreach; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran multi-session trainings for HR teams; handled 30–40 support tickets per day; authored 22 help-centre articles in two languages.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English but explicitly states Thai – none, so Thai proficiency requirement is not satisfied).

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R7 F7 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) working with B2B accounts, onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Designed and executed onboarding and training for 46 B2B accounts; monitored usage dashboards and proactively engaged low-usage accounts; improved renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to target outreach; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran multi-session trainings for HR teams; handled 30–40 support tickets per day; authored 22 help-centre articles in two languages.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English but explicitly states Thai – none, so Thai proficiency requirement is not satisfied).

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R7 F7 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) working with B2B accounts, onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Designed and executed onboarding and training for 46 B2B accounts; monitored usage dashboards and proactively engaged low-usage accounts; improved renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to target outreach; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran multi-session trainings for HR teams; handled 30–40 support tickets per day; authored 22 help-centre articles in two languages.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record states professional working proficiency in English but explicitly states Thai – none, so Thai proficiency requirement is not satisfied).

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R8 F8 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          840
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

#### PROBE-R3A-FBAT R8 F8 `numbered.txt`
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

#### PROBE-R3A-FBAT R8 F8 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R8 F8 `e1.pass1.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES: none
[FILTRATION-R8]
Second pass?
```

#### PROBE-R3A-FBAT R8 F8 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R8 F8 `null_list.txt`
```
[NULL FILTRATION — R8]
RESUME: R8
NULL LINES: none
[FILTRATION-R8]
Second pass?
```

#### PROBE-R3A-FBAT R8 F8 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Improved renewal rate from 78% to 91% by monitoring usage and intervening; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding process based on data, cutting time-to-first-report by 57%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles in two languages; primary contact for 30–40 tickets per day.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows Thai fluency but only basic English; role requires proficiency in both languages and no overriding achievement in English-language work is evidenced).

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R8 F8 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts with structured training; monitored usage and intervened to raise renewal rate from 78% to 91%; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding based on data, reducing time-to-first-report by 57%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; wrote 22 help-centre articles in two languages; handled 30–40 support tickets per day as primary contact.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record lists Thai fluency and English basic; confirm in interview that English proficiency meets role requirements for written and spoken communication)

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R8 F8 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Onboarded 46 B2B accounts with structured training; monitored usage and intervened to raise renewal rate from 78% to 91%; rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding based on data, reducing time-to-first-report by 57%.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Delivered 3-session training sequences for each new HR team; wrote 22 help-centre articles in two languages; handled 30–40 support tickets per day as primary contact.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record lists Thai fluency and English basic; confirm in interview that English proficiency meets role requirements for written and spoken communication)

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R9 F9 `intake_report.json`
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

#### PROBE-R3A-FBAT R9 F9 `numbered.txt`
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

#### PROBE-R3A-FBAT R9 F9 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R9 F9 `e1.pass1.txt`
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```

#### PROBE-R3A-FBAT R9 F9 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R9 F9 `null_list.txt`
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```

#### PROBE-R3A-FBAT R9 F9 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) — continuous customer-facing support roles.
⚖️ Built capability in customer success through multi-year support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) 5+ years in customer support/service roles in business settings reasonably demonstrates applied customer success principles and translating customer needs into actions, despite the title not explicitly stating “customer success.”
⚖️ Multi-year support roles resolving customer issues → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Sustained experience as Customer Support Specialist and Customer Service Officer implies regular problem-solving and use of customer information to resolve issues and improve outcomes.
⚖️ Customer-facing support and service roles → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Long-term success in customer support and service roles requires strong communication and interpersonal engagement with customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai listed with full fluency; English listed with professional working proficiency and standardized test score.

⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - confirm current proficiency level in both languages in conversation and written exercises.)

[AUDIT-2026-009-8291]
```

#### PROBE-R3A-FBAT R9 F9 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Multi-year work as Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions.
⚖️ Built capability in customer success through multi-year support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) 5+ years in customer support/service roles reasonably demonstrate applied customer success practices and translating customer needs into actions, despite titles not explicitly stating “customer success.”
⚖️ Multi-year support roles resolving customer issues → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Sustained work as Customer Support Specialist and Customer Service Officer implies regular problem-solving using customer information to resolve issues and improve outcomes.
⚖️ Customer-facing support and service roles → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Long-term success in customer support and service roles requires strong verbal and written communication and ongoing customer education.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai listed with fluency; English listed with professional working proficiency.

[AUDIT-2026-009-9364]
```

#### PROBE-R3A-FBAT R9 F9 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Multi-year work as Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions.
⚖️ Built capability in customer success through multi-year support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) 5+ years in customer support/service roles reasonably demonstrate applied customer success practices and translating customer needs into actions, despite titles not explicitly stating “customer success.”
⚖️ Multi-year support roles resolving customer issues → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Sustained work as Customer Support Specialist and Customer Service Officer implies regular problem-solving using customer information to resolve issues and improve outcomes.
⚖️ Customer-facing support and service roles → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence) Long-term success in customer support and service roles requires strong verbal and written communication and ongoing customer education.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai listed with fluency; English listed with professional working proficiency.

[AUDIT-2026-009-9364]
```

#### PROBE-R3A-FBAT R10 F10 `intake_report.json`
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

#### PROBE-R3A-FBAT R10 F10 `numbered.txt`
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

#### PROBE-R3A-FBAT R10 F10 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R10 F10 `e1.pass1.txt`
```
[NULL FILTRATION — R10]  
RESUME: R10  
NULL LINES: none  
[FILTRATION-R10]  
Second pass?
```

#### PROBE-R3A-FBAT R10 F10 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R10 F10 `null_list.txt`
```
[NULL FILTRATION — R10]  
RESUME: R10  
NULL LINES: none  
[FILTRATION-R10]  
Second pass?
```

#### PROBE-R3A-FBAT R10 F10 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) handling 1,200+ accounts and ongoing customer interactions.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Raised customer satisfaction from 71% to 88% and managed 1,200+ accounts, indicating effective strategies based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes, demonstrating data-driven analysis and problem-solving to design support improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Customer-facing roles over multiple years with significant satisfaction improvements and large account volume imply strong communication and relationship-building.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency and English professional working proficiency stated; interview should confirm level against role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R10 F10 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) handling 1,200+ accounts and ongoing customer interactions.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Raised customer satisfaction from 71% to 88% and managed 1,200+ accounts, indicating effective strategies based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes, demonstrating data-driven analysis and problem-solving to design support improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Customer-facing roles over multiple years with significant satisfaction improvements and large account volume imply strong communication and relationship-building.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency explicitly stated.

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R10 F10 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) handling 1,200+ accounts and ongoing customer interactions.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Raised customer satisfaction from 71% to 88% and managed 1,200+ accounts, indicating effective strategies based on customer needs and outcomes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Improved satisfaction scores and reduced first-response time from 6 hours to 40 minutes, demonstrating data-driven analysis and problem-solving to design support improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Customer-facing roles over multiple years with significant satisfaction improvements and large account volume imply strong communication and relationship-building.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai fluency and English professional working proficiency explicitly stated.

[AUDIT-2026-009-0002]
```

#### PROBE-R3A-FBAT R11 F11 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1013
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

#### PROBE-R3A-FBAT R11 F11 `numbered.txt`
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

#### PROBE-R3A-FBAT R11 F11 `resume.numbered.txt`
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

#### PROBE-R3A-FBAT R11 F11 `e1.pass1.txt`
```
[NULL FILTRATION — R11]  
RESUME: R11  
NULL LINES: none  
[FILTRATION-R11]  
Second pass?
```

#### PROBE-R3A-FBAT R11 F11 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-FBAT R11 F11 `null_list.txt`
```
[NULL FILTRATION — R11]  
RESUME: R11  
NULL LINES: none  
[FILTRATION-R11]  
Second pass?
```

#### PROBE-R3A-FBAT R11 F11 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in roles handling onboarding, training, and support for B2B customers.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Onboarded 46 B2B accounts, rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days, monitored usage dashboards and proactively contacted low-usage accounts, increasing renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and intervene; redesigned onboarding process to improve time-to-first-report; tracked renewal rate improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 support tickets per day; wrote 22 help-centre articles that reduced ticket volume by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; explicitly lists Thai and English language skills with professional working proficiency.

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R11 F11 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in roles handling onboarding, training, and support for B2B customers.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Onboarded 46 B2B accounts, rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days, monitored usage dashboards and proactively contacted low-usage accounts, increasing renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and intervene; redesigned onboarding process to improve time-to-first-report; tracked renewal rate improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 support tickets per day; wrote 22 help-centre articles that reduced ticket volume by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; explicitly lists Thai and English language skills with professional working proficiency.

[AUDIT-2026-009-0001]
```

#### PROBE-R3A-FBAT R11 F11 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in roles handling onboarding, training, and support for B2B customers.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Onboarded 46 B2B accounts, rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days, monitored usage dashboards and proactively contacted low-usage accounts, increasing renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and intervene; redesigned onboarding process to improve time-to-first-report; tracked renewal rate improvements.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 support tickets per day; wrote 22 help-centre articles that reduced ticket volume by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; explicitly lists Thai and English language skills with professional working proficiency.

[AUDIT-2026-009-0001]
```

### Appendix — PROBE-R3A-S2

#### PROBE-R3A-S2 `run.json`
```
{
  "run_id": "20260906-071144",
  "mode": "full",
  "boundary_sha256": "1140e5a26767e68ba390bafb7906016e6851d3eeeb09396fd7095c8f78c2ceb4",
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
    "fixtures/runyarin.txt"
  ]
}
```

#### PROBE-R3A-S2 `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3A-S2 `extraction.pass1.txt`
*not written this run*

#### PROBE-R3A-S2 `extraction.pass2.txt`
*not written this run*

#### PROBE-R3A-S2 R1 Runyarin `resume.numbered.txt`
```
L1: RUNYARIN L.
L2: (Belar)
L3: SKILLS
L4: EXCEL
L5: POWERPOINT
L6: WORD
L7: PHOTOSHOP
L8: HOBBIES
L9: TRAVEL
L10: MUSIC
L11: MOVIE
L12: SPORT
L13: CONTACT
L14: +66953648941
L15: Samut Prakan, Thailand
L16: Runyarin.lertchai@gmail.com
L17: ABOUT ME
L18: Open to freelance, full-time, and contract roles across APAC or remote
L19: Publisher Monetization, Programmatic Media, Account
L20: Management & Business Development Specialist
L21: With 10+ years of experience across Southeast Asia driving digital growth through ad tech, publisher strategy, and cross- platform execution.
L22: Key Skills:
L23: •
L24: Publisher Monetization & Yield Optimization
L25: •
L26: Programmatic Media Buying (RTB, Header Bidding)
L27: •
L28: SSPs, Ad Servers, Pixel & SDK Integration
L29: •    AdTech Tools: DV360, Appier, GAM, Google Ads, Facebook Ads
L30: • Analytics & Tracking: GA, Adjust, Appsflyer
L31: • Client Relations & Cross-Functional Team Leadership
L32: EDUCATION
L33: BACHELOR OF ARTS IN
L34: COMMUNICATION ARTS
L35: 2007-2011
L36: BANGKOK UNIVERSITY
L37: INTERNATIONAL COLLEGE
L38: NZQA NATIONAL CERTIFICATE
L39: CRAIGHEAD DIOCESAN SCHOOL,
L40: NEW  ZEALAND
L41: 2002-2007
L42: EXPERIENCES
L43: Appier Inc.(2021–Present): SEA Lead
L44: Account Manager
L45: •
L46: Led full-funnel programmatic campaigns for
L47: SEA advertisers
L48: •
L49: Supported yield improvement through strategic bidding and inventory insights
L50: •
L51: Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L52: Recognized for 30% YoY revenue growth and successful SSP optimization across accounts
L53:  Certificate of Achievement
L54: Havas Riverorchid(2021): Hybrid Media
L55: Manager
L56: •
L57: Crafted integrated media strategies for luxury and auto clients
L58: •
L59: Delivered performance-based media plans with measurable KPIs
L60: •
L61: Supervised cross-functional teams ensuring timely and accurate campaign execution
L62: Fivestones(2021): Account & Business
L63: Strategy Manager
L64: •
L65: Handled programmatic campaign setup via ad servers and SEM tools
L66: •
L67: Troubleshot pixel integrations and improved web analytics configurations
L68: •
L69: Acted as liaison between tech and business teams to enhance delivery
L70: Dentsu One(2018-2019): Account Manager
L71: • Managed Honda Connect app and website development, including CDP system integration and partner features (e.g., Major Cineplex)
L72: • Led successful SEO pitch for UmayPlus and managed full-year digital strategy including
L73: Facebook Ads, content, and search campaigns
L74: Martini Group(2017-2018):
L75: Brand Management & Digital Junior
L76: Manager
L77: • Managed end-to-end marketing campaigns from ideation to impact analysis
L78: • Executed SEO, social media content, and digital outreach (SMS, Email)
L79: • Developed brand assets and visuals to support creative marketing strategies
L80: • Contributed to brand building with hands-on design and content creation
L81: PHAR Partnerships, Air Asia[2014-2016):
L82: Digital Media Consultant
L83: • Supported go-to-market strategy development and secured internal alignment
L84: • Presented digital platforms to C-level stakeholders and partners
L85: • Planned and executed cross-channel marketing campaigns, including website and social media content
L86: - Reference Letter
L87: Innity Digital Media Co., Ltd.(2011-2013):
L88: Digital Campaign Specialist / Account Executive
L89: •
L90: Gained deep product knowledge to support client pitches and campaign execution
L91: •
L92: Provided technical guidance for pixel setup and campaign implementation
L93: •
L94: Collaborated with Sales, Business
L95: Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
L96: •
L97: Maintained media plans and managed reporting, budgeting, and updates across
L98: CRM, RTB platforms, and analytics tools (e.g., DoubleClick, ComScore, Google Dev)
```

#### PROBE-R3A-S2 R1 Runyarin `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L19 — Publisher Monetization, Programmatic Media, Account
L20 — Management & Business Development Specialist
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
Second pass?
```

#### PROBE-R3A-S2 R1 Runyarin `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-S2 R1 Runyarin `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L19 — Publisher Monetization, Programmatic Media, Account
L20 — Management & Business Development Specialist
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
Second pass?
```

#### PROBE-R3A-S2 R1 Runyarin `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Arts degree stated in education section.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (record shows roles in media, advertising, and digital campaign management; no explicit customer success, training, or support focus is stated in the non-NULL content).
⚖️ Built and managed multiple advertising and digital campaign accounts over 10+ years → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence explanation) Long-term account management and digital campaign responsibilities imply understanding of client objectives and translating them into strategic execution.
⚖️ 10+ years managing campaigns with measurable KPIs and impact analysis → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence explanation) Experience with analytics tools and KPI-driven campaigns demonstrates data-based problem solving and intervention design.
⚖️ Multiple account manager and consultant roles involving presentations to stakeholders → Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (equivalence explanation) Roles that include consulting and presenting to stakeholders indicate strong communication and interpersonal engagement.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on specific languages; interview prompt)

[AUDIT-2026-001-0001]
```

#### PROBE-R3A-S2 R1 Runyarin `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor's degree stated in the education section, plus 10+ years of experience driving digital growth and managing accounts in marketing-related contexts.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) Multiple roles over more than 10 years as Account Manager, Manager, Strategy Manager, Brand Management & Digital Manager, Digital Media Consultant, and Digital Campaign Specialist / Account Executive indicate sustained customer-facing work focused on supporting client campaigns and outcomes.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Over 10 years managing client accounts and digital strategies—including managing app and website development and full-year digital marketing programs—demonstrates understanding of client objectives and translating them into actionable campaign and product strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for achieving 30% year-over-year revenue growth through optimization across accounts, along with responsibility for media plans, reporting, budgeting, and updates across CRM, RTB platforms, and analytics tools, evidences strong analytical, problem-solving, and data-driven decision-making.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Leading SEO pitches and managing full-year digital strategies, combined with consultant, manager, and account roles, requires presenting, persuading, and collaborating with stakeholders, indicating strong communication and interpersonal skills to engage and educate customers.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on specific languages; interview prompt)

[AUDIT-2026-001-0002]
```

#### PROBE-R3A-S2 R1 Runyarin `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor's degree stated in the education section, plus 10+ years of experience driving digital growth and managing accounts in marketing-related contexts.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) Multiple roles over more than 10 years as Account Manager, Manager, Strategy Manager, Brand Management & Digital Manager, Digital Media Consultant, and Digital Campaign Specialist / Account Executive indicate sustained customer-facing work focused on supporting client campaigns and outcomes.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Over 10 years managing client accounts and digital strategies—including managing app and website development and full-year digital marketing programs—demonstrates understanding of client objectives and translating them into actionable campaign and product strategies.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for achieving 30% year-over-year revenue growth through optimization across accounts, along with responsibility for media plans, reporting, budgeting, and updates across CRM, RTB platforms, and analytics tools, evidences strong analytical, problem-solving, and data-driven decision-making.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Leading SEO pitches and managing full-year digital strategies, combined with consultant, manager, and account roles, requires presenting, persuading, and collaborating with stakeholders, indicating strong communication and interpersonal skills to engage and educate customers.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on specific languages; interview prompt)

[AUDIT-2026-001-0002]
```

### Appendix — PROBE-R3A-S3-bkk

#### PROBE-R3A-S3-bkk `run.json`
```
{
  "run_id": "20260906-072305",
  "mode": "full",
  "boundary_sha256": "3ce25225e02cfce542db9079e77cbb308ff9a8e4da33ac3908dcd6795690950f",
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
  "jd": "battery/bangkok/jd.txt",
  "resumes": [
    "battery/bangkok/r02.txt"
  ]
}
```

#### PROBE-R3A-S3-bkk `requirement_set.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```

#### PROBE-R3A-S3-bkk `extraction.pass1.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```

#### PROBE-R3A-S3-bkk `extraction.pass2.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```

#### PROBE-R3A-S3-bkk R1 Krit `resume.numbered.txt`
```
L1: Krit Rattanapong
L2: Summary: Results-driven HR leader delivering 360 talent acquisition, ATS transformation, HRIS excellence, dashboard ownership, and strategic workforce planning - tailored to Bangkok Learning Group's hybrid growth model.
L3: Skills: Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever, Power BI, Tableau, Looker Studio, end-to-end hiring transformation
L4: Experience:
L5: Senior Talent Acquisition Executive - Hospitality group, 2021-present
L6: - Spearheaded end-to-end hiring transformation and owned the ATS strategy across the talent function.
L7: - Built leadership dashboards that improved hiring efficiency by 40% and elevated data-driven decision-making.
L8: - Drove HRIS excellence and optimized the full employee lifecycle.
L9: Recruitment Officer - Retail company, 2019-2021
L10: - Managed full-cycle recruitment, posted roles, screened candidates, scheduled interviews, and partnered with hiring managers on workforce planning.
L11: Education: BBA, Thammasat University
L12: Other: Thai national. Lives near Asok BTS. References describe him as polished and client-facing. No career gaps.
```

#### PROBE-R3A-S3-bkk R1 Krit `e1.pass1.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: results-driven HR leader, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3A-S3-bkk R1 Krit `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3A-S3-bkk R1 Krit `null_list.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: results-driven HR leader, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3A-S3-bkk R1 Krit `e2.pass1.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week

R1 Krit Rattanapong - Do Not Advance

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
❌ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: Not Met (only two roles listed: Senior Talent Acquisition Executive 2021–present and Recruitment Officer 2019–2021, totaling approximately 5 years at most with no exceptional quantified achievements available in non-NULL lines to justify an override)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills line lists Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills line lists Power BI, Tableau, Looker Studio)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-INF — Roles as Senior Talent Acquisition Executive and Recruitment Officer in HR/recruitment functions imply process work in recruitment and employee lifecycle)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles necessarily involve handling candidate and employee information)  
✅ Strong English communication skills for reports and leadership updates: (MET-INF — Use of English throughout résumé, including skills and role descriptions, supports English communication capability)  
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — No evidence of inability to meet stated on-site pattern)

[AUDIT-2026-001-0001]
```

#### PROBE-R3A-S3-bkk R1 Krit `e2.pass2.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week

R1 Krit Rattanapong - Advance

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide at least 5 years in recruitment/people functions)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills line lists Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills line lists Power BI, Tableau, Looker Studio; experience line notes building leadership dashboards that improved hiring efficiency by 40%)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, indicating direct impact on recruitment workflows)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles involve managing candidate and employee data)  
✅ Strong English communication skills for reports and leadership updates: (MET-INF — Resume content describing roles and achievements is written in English, including discussion of leadership dashboards and hiring efficiency)  
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — No evidence of inability to meet stated on-site pattern)

[AUDIT-2026-001-0002]
```

#### PROBE-R3A-S3-bkk R1 Krit `evaluation.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week

R1 Krit Rattanapong - Advance

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide at least 5 years in recruitment/people functions)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills line lists Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills line lists Power BI, Tableau, Looker Studio; experience line notes building leadership dashboards that improved hiring efficiency by 40%)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, indicating direct impact on recruitment workflows)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles involve managing candidate and employee data)  
✅ Strong English communication skills for reports and leadership updates: (MET-INF — Resume content describing roles and achievements is written in English, including discussion of leadership dashboards and hiring efficiency)  
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — No evidence of inability to meet stated on-site pattern)

[AUDIT-2026-001-0002]
```

### Appendix — PROBE-R3B-FBAT

#### PROBE-R3B-FBAT `run.json`
```
{
  "run_id": "20260906-072514",
  "mode": "full",
  "boundary_sha256": "43a6416f28dc121c7ea6cba5f88ddd916f26b0b3015129256ad2ec0f152e7525",
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

#### PROBE-R3B-FBAT `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3B-FBAT `extraction.pass1.txt`
*not written this run*

#### PROBE-R3B-FBAT `extraction.pass2.txt`
*not written this run*

#### PROBE-R3B-FBAT R1 F1 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          893
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

#### PROBE-R3B-FBAT R1 F1 `numbered.txt`
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

#### PROBE-R3B-FBAT R1 F1 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R1 F1 `e1.pass1.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES: none  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3B-FBAT R1 F1 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R1 F1 `null_list.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES: none  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3B-FBAT R1 F1 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and designed interventions; optimized onboarding process to achieve significant cycle-time reduction.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with professional working proficiency; created help-centre articles in both languages.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R1 F1 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and designed interventions; optimized onboarding process to achieve significant cycle-time reduction.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with professional working proficiency; created help-centre articles in both languages.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R1 F1 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to identify at-risk accounts and designed interventions; optimized onboarding process to achieve significant cycle-time reduction.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with professional working proficiency; created help-centre articles in both languages.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R2 F2 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1817
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

#### PROBE-R3B-FBAT R2 F2 `numbered.txt`
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

#### PROBE-R3B-FBAT R2 F2 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R2 F2 `e1.pass1.txt`
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L15 — Spearheaded transformative customer engagement initiatives across the portfolio  
L16 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R2]  
Second pass?
```

#### PROBE-R3B-FBAT R2 F2 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R2 F2 `null_list.txt`
```
[NULL FILTRATION — R2]  
RESUME: R2  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record  
L5 — Strong understanding of customer success principles and practices  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L15 — Spearheaded transformative customer engagement initiatives across the portfolio  
L16 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L17 — Leveraged best-in-class methodologies to drive stakeholder alignment and value realization  
L26 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R2]  
Second pass?
```

#### PROBE-R3B-FBAT R2 F2 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and managing B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Multi-year Customer Success Executive role in B2B SaaS, responsible for onboarding, lifecycle management, and improving renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency; authored help-centre articles in both Thai and English.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R2 F2 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and managing B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Multi-year Customer Success Executive role in B2B SaaS, responsible for onboarding, lifecycle management, and improving renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency; authored help-centre articles in both Thai and English.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R2 F2 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R2 Kanokwan Ratanaporn - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive, 2022–2026, onboarding and managing B2B accounts; Client Support Specialist, 2020–2022, handling 30–40 support tickets per day.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Multi-year Customer Success Executive role in B2B SaaS, responsible for onboarding, lifecycle management, and improving renewal rate from 78% to 91%.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced time-to-first-report from 21 to 9 days by redesigning onboarding; used weekly usage dashboards in Metabase to identify low-engagement accounts and intervene.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Conducted 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume on those topics by 40%.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency; authored help-centre articles in both Thai and English.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R3 F3 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          817
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

#### PROBE-R3B-FBAT R3 F3 `numbered.txt`
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

#### PROBE-R3B-FBAT R3 F3 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R3 F3 `e1.pass1.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```

#### PROBE-R3B-FBAT R3 F3 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R3 F3 `null_list.txt`
```
[NULL FILTRATION — R3]
RESUME: R3
NULL LINES: none
[FILTRATION-R3]
Second pass?
```

#### PROBE-R3B-FBAT R3 F3 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance – Verify

⚖️ [Customer Success Executive and Client Support Specialist roles with measurable impact in B2B SaaS and support] → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: multiple years in customer success/support with quantifiable outcomes in onboarding, renewals, and support demonstrate capability equivalent to a related bachelor's degree)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles; onboarding, training sessions, and daily ticket handling)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: improved renewal rate from 78% to 91%, proactive outreach based on usage dashboards, rebuilt onboarding checklist to reduce time-to-first-report)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: used Metabase dashboards and login thresholds to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled 30–40 tickets per day with high same-day resolution)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and English professional working proficiency; interview to confirm level against role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R3 F3 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ [Several years as Customer Success Executive and Client Support Specialist in B2B software with measurable impact on onboarding, renewals, and support] → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: sustained success in customer success/support with quantifiable outcomes—46 B2B accounts onboarded with structured training, renewal rate improvement from 78% to 91%, and process optimization—demonstrates capability equivalent to a related bachelor's degree)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, multi-session trainings for HR teams, and 30–40 support tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: used customer usage data to trigger outreach, rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, and drove renewal rate from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: regularly reviewed Metabase dashboards and login thresholds to identify at-risk accounts and redesigned onboarding flow to improve time-to-first-report)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led 3-session training sequences for each new HR team, wrote 22 help-centre articles, and resolved the majority of daily tickets within one business day)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: record states Thai fluency and English professional working proficiency; authored 22 help-centre articles in Thai and English and managed ongoing customer communications)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R3 F3 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R3 Somchai Wongsakul - Advance

⚖️ [Several years as Customer Success Executive and Client Support Specialist in B2B software with measurable impact on onboarding, renewals, and support] → Bachelor's degree in business, marketing, or a related field.: (equivalence explanation: sustained success in customer success/support with quantifiable outcomes—46 B2B accounts onboarded with structured training, renewal rate improvement from 78% to 91%, and process optimization—demonstrates capability equivalent to a related bachelor's degree)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, multi-session trainings for HR teams, and 30–40 support tickets per day)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: used customer usage data to trigger outreach, rebuilt onboarding checklist to cut time-to-first-report from 21 to 9 days, and drove renewal rate from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: regularly reviewed Metabase dashboards and login thresholds to identify at-risk accounts and redesigned onboarding flow to improve time-to-first-report)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: led 3-session training sequences for each new HR team, wrote 22 help-centre articles, and resolved the majority of daily tickets within one business day)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: record states Thai fluency and English professional working proficiency; authored 22 help-centre articles in Thai and English and managed ongoing customer communications)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R4 F4 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1741
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

#### PROBE-R3B-FBAT R4 F4 `numbered.txt`
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

#### PROBE-R3B-FBAT R4 F4 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R4 F4 `e1.pass1.txt`
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
L16 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```

#### PROBE-R3B-FBAT R4 F4 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R4 F4 `null_list.txt`
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
L16 — Passionate about building long-term partnerships and championing the voice of the customer
L24 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration
[FILTRATION-R4]
Second pass?
```

#### PROBE-R3B-FBAT R4 F4 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance – Verify

❌ Bachelor's degree in business, marketing, or a related field.: Not Met (no degree stated)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive, 2022–2026; Client Support Specialist, 2020–2022, handling tickets, onboarding, and training)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-INF (multi-year Customer Success Executive role with onboarding, lifecycle management, and renewal improvement from 78% to 91%)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (used Metabase dashboards, reduced time-to-first-report from 21 to 9 days, monitored usage and intervened based on data)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (ran 3-session training sequences for each new HR team; wrote 22 help-centre articles)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (Thai fluency and English professional working proficiency stated; verification required at interview)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R4 F4 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Multi-year customer success and support achievements with strong metrics (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022; onboarded 46 B2B accounts; reduced time-to-first-report from 21 to 9 days; improved renewal rate from 78% to 91%; wrote 22 help-centre articles reducing tickets 40%) → Bachelor's degree in business, marketing, or a related field.: Experience and quantified results in customer success demonstrate capability equivalent to the requested degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive 2022–2026 and Client Support Specialist 2020–2022; handled 30–40 tickets per day, onboarded 46 accounts, and ran multi-session trainings for HR teams.)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-INF (Redesigned onboarding to cut time-to-first-report from 21 to 9 days, monitored usage dashboards to identify low-engagement accounts, and drove renewal rate increase from 78% to 91%.)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used analytics dashboards to guide outreach to low-login accounts and rebuilt the onboarding checklist based on observed bottlenecks, producing faster value realization and better retention.)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Delivered 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced related ticket volume by 40%.)
✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Languages section lists Thai fluency and English professional working proficiency; wrote help-centre articles in both languages.)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R4 F4 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R4 Somchai Wongsakul - Advance

⚖️ Multi-year customer success and support achievements with strong metrics (Customer Success Executive 2022–2026; Client Support Specialist 2020–2022; onboarded 46 B2B accounts; reduced time-to-first-report from 21 to 9 days; improved renewal rate from 78% to 91%; wrote 22 help-centre articles reducing tickets 40%) → Bachelor's degree in business, marketing, or a related field.: Experience and quantified results in customer success demonstrate capability equivalent to the requested degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: MET-EVID (Customer Success Executive 2022–2026 and Client Support Specialist 2020–2022; handled 30–40 tickets per day, onboarded 46 accounts, and ran multi-session trainings for HR teams.)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: MET-INF (Redesigned onboarding to cut time-to-first-report from 21 to 9 days, monitored usage dashboards to identify low-engagement accounts, and drove renewal rate increase from 78% to 91%.)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: MET-EVID (Used analytics dashboards to guide outreach to low-login accounts and rebuilt the onboarding checklist based on observed bottlenecks, producing faster value realization and better retention.)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: MET-EVID (Delivered 3-session training sequences for each new HR team and authored 22 help-centre articles that reduced related ticket volume by 40%.)
✅ Proficiency in both written and spoken English and Thai.: MET-EVID (Languages section lists Thai fluency and English professional working proficiency; wrote help-centre articles in both languages.)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R5 F5 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          672
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

#### PROBE-R3B-FBAT R5 F5 `numbered.txt`
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

#### PROBE-R3B-FBAT R5 F5 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R5 F5 `e1.pass1.txt`
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```

#### PROBE-R3B-FBAT R5 F5 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R5 F5 `null_list.txt`
```
[NULL FILTRATION — R5]
RESUME: R5
NULL LINES:
L11 — Performed cycle counts and reconciled WMS stock against physical counts
[FILTRATION-R5]
Second pass?
```

#### PROBE-R3B-FBAT R5 F5 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (all listed experience is in warehouse operations and inventory; no customer-facing, customer success, training, or support role described).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no customer success domain work or customer-strategy responsibilities described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning, demonstrating data-driven problem solving and intervention design in operations.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, implying ongoing communication, coordination, and people management; however, this is internal rather than customer-facing.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Thai and English listed with professional working proficiency and standardized test score.

[AUDIT-2026-005-0001]
```

#### PROBE-R3B-FBAT R5 F5 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is in warehouse operations supervision and inventory; no customer-facing, customer success, training, or support roles described).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no responsibilities or achievements related to customer success, customer outcomes, or translating customer needs into actionable strategies are described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven problem solving and process intervention design.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, indicating ongoing communication, coordination, and people management that support strong interpersonal and communication skills.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency, supporting proficiency in both languages.

[AUDIT-2026-005-0001]
```

#### PROBE-R3B-FBAT R5 F5 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R5 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience listed is in warehouse operations supervision and inventory; no customer-facing, customer success, training, or support roles described).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no responsibilities or achievements related to customer success, customer outcomes, or translating customer needs into actionable strategies are described).
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating data-driven problem solving and process intervention design.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Supervised 14 operators across two shifts, indicating ongoing communication, coordination, and people management that support strong interpersonal and communication skills.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai fluency and English professional working proficiency, supporting proficiency in both languages.

[AUDIT-2026-005-0001]
```

#### PROBE-R3B-FBAT R6 F6 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1530
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

#### PROBE-R3B-FBAT R6 F6 `numbered.txt`
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

#### PROBE-R3B-FBAT R6 F6 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R6 F6 `e1.pass1.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — proven track record of delivering exceptional client outcomes  
L5 — understanding of customer success principles and practices  
L6 — problem-solving/analytical skills with data-driven approach  
L7 — communication/interpersonal skills to engage and educate customers  
L8 — proven customer success expertise through client-focused operational leadership  
L9 — experience onboarding/training stakeholders and driving data-driven interventions  
L10 — delivered 360-degree customer lifecycle management and end-to-end value realization  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]  
Second pass?
```

#### PROBE-R3B-FBAT R6 F6 `e1.pass2.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes  
L5 — Strong understanding of customer success principles and practices / translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]
```

#### PROBE-R3B-FBAT R6 F6 `null_list.txt`
```
[NULL FILTRATION — R6]  
RESUME: R6  
NULL LINES:  
L4 — Results-driven customer success professional with a proven track record of delivering exceptional client outcomes  
L5 — Strong understanding of customer success principles and practices / translate customer needs into actionable strategies  
L6 — Excellent problem-solving and analytical skills with a data-driven approach  
L7 — Exceptional communication and interpersonal skills  
L8 — Proven customer success expertise gained through years of client-focused operational leadership  
L9 — Deep experience onboarding and training stakeholders and driving data-driven interventions  
L10 — Delivered 360-degree customer lifecycle management and end-to-end value realization  
L19 — Performed cycle counts and reconciled WMS stock against physical counts  
L23 — Customer Success | Onboarding | Training | Stakeholder Management | Data-Driven Decision Making | Strategic Thinking | Relationship Building | Cross-Functional Collaboration  
[FILTRATION-R6]
```

#### PROBE-R3B-FBAT R6 F6 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience shown is warehouse operations supervisor and inventory clerk; no stated customer-facing, customer success, training, or support role).
❌ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: Not Met (no non-NULL evidence of customer success work or translating customer needs into strategies).
❌ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: Not Met (no non-NULL evidence of data-driven customer interventions; listed achievements are operational/warehouse focused).
❌ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: Not Met (no non-NULL evidence of engaging and educating customers; roles described are internal operations).
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R6 F6 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory management; no stated customer-facing, customer success, training, or support role).
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA) Record provides no specific evidence for or against this skill; nothing in the stated experience contradicts the ability to have this understanding.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating strong analytical, problem-solving, and data-driven process improvement skills.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) As a warehouse operations supervisor managing 14 forklift operators across two shifts and scheduling staffing, candidate has demonstrated communication and interpersonal skills transferable to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency, indicating ability to communicate in both written and spoken forms.

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R6 F6 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R6 Preecha Thongdee - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
❌ Experience in a customer-facing role, with a focus on customer success, training, or support.: Not Met (experience shown is in warehouse operations supervision and inventory management; no stated customer-facing, customer success, training, or support role).
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (NO-CONTRA) Record provides no specific evidence for or against this skill; nothing in the stated experience contradicts the ability to have this understanding.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Reduced picking errors from 3.1% to 0.9% by introducing barcode scanning at the pack station, demonstrating strong analytical, problem-solving, and data-driven process improvement skills.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) As a warehouse operations supervisor managing 14 forklift operators across two shifts and scheduling staffing, candidate has demonstrated communication and interpersonal skills transferable to engaging and educating customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Languages section lists Thai and English with stated proficiency, indicating ability to communicate in both written and spoken forms.

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R7 F7 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          871
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

#### PROBE-R3B-FBAT R7 F7 `numbered.txt`
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

#### PROBE-R3B-FBAT R7 F7 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R7 F7 `e1.pass1.txt`
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```

#### PROBE-R3B-FBAT R7 F7 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R7 F7 `null_list.txt`
```
[NULL FILTRATION — R7]  
RESUME: R7  
NULL LINES: none  
[FILTRATION-R7]  
Second pass?
```

#### PROBE-R3B-FBAT R7 F7 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in B2B SaaS and platform environments, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with onboarding, renewal ownership, and proactive outreach; increased renewal rate from 78% to 91% and rebuilt onboarding checklist based on customer behavior.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login thresholds to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days; tracked and improved renewal metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled 30–40 tickets per day with high same-day resolution.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows professional working proficiency in English and explicitly states Thai – none; no basis for override because this is a direct language-skill requirement, not substitutable by other achievements).

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R7 F7 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in B2B SaaS and platform environments, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with onboarding, renewal ownership, and proactive outreach; increased renewal rate from 78% to 91% and rebuilt onboarding checklist based on customer behavior.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login thresholds to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days; tracked and improved renewal metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled 30–40 tickets per day with high same-day resolution.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows professional working proficiency in English and explicitly states Thai – none; no basis for override because this is a direct language-skill requirement, not substitutable by other achievements).

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R7 F7 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R7 Kanokwan Ratanaporn - Do Not Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (2022–2026) and Client Support Specialist (2020–2022) in B2B SaaS and platform environments, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Customer Success Executive role with onboarding, renewal ownership, and proactive outreach; increased renewal rate from 78% to 91% and rebuilt onboarding checklist based on customer behavior.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login thresholds to trigger outreach; redesigned onboarding to cut time-to-first-report from 21 to 9 days; tracked and improved renewal metrics.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles; handled 30–40 tickets per day with high same-day resolution.
❌ Proficiency in both written and spoken English and Thai.: Not Met (record shows professional working proficiency in English and explicitly states Thai – none; no basis for override because this is a direct language-skill requirement, not substitutable by other achievements).

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R8 F8 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          840
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

#### PROBE-R3B-FBAT R8 F8 `numbered.txt`
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

#### PROBE-R3B-FBAT R8 F8 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R8 F8 `e1.pass1.txt`
```
[NULL FILTRATION — R8]  
RESUME: R8  
NULL LINES: none  
[FILTRATION-R8]  
Second pass?
```

#### PROBE-R3B-FBAT R8 F8 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R8 F8 `null_list.txt`
```
[NULL FILTRATION — R8]  
RESUME: R8  
NULL LINES: none  
[FILTRATION-R8]  
Second pass?
```

#### PROBE-R3B-FBAT R8 F8 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, training, and support from 2020–2026)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: Improved renewal rate from 78% to 91% via proactive usage monitoring and interventions; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding process based on performance data)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic and used for help-centre articles; interview should confirm level vs role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R8 F8 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, training, and support from 2020–2026)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: Improved renewal rate from 78% to 91% via proactive usage monitoring and interventions; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding process based on performance data)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic and used for help-centre articles; interview should confirm level vs role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R8 F8 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R8 Kanokwan Ratanaporn - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Success Executive and Client Support Specialist roles handling onboarding, training, and support from 2020–2026)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID: Improved renewal rate from 78% to 91% via proactive usage monitoring and interventions; rebuilt onboarding checklist to reduce time-to-first-report from 21 to 9 days)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID: Used Metabase dashboards and login metrics to trigger outreach; redesigned onboarding process based on performance data)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID: Ran 3-session training sequences for each new HR team; wrote 22 help-centre articles that reduced ticket volume by 40%; handled 30–40 tickets per day with 85% resolved within one business day)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai fluency stated; English listed as basic and used for help-centre articles; interview should confirm level vs role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R9 F9 `intake_report.json`
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

#### PROBE-R3B-FBAT R9 F9 `numbered.txt`
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

#### PROBE-R3B-FBAT R9 F9 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R9 F9 `e1.pass1.txt`
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```

#### PROBE-R3B-FBAT R9 F9 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R9 F9 `null_list.txt`
```
[NULL FILTRATION — R9]
RESUME: R9
NULL LINES: none
[FILTRATION-R9]
Second pass?
```

#### PROBE-R3B-FBAT R9 F9 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Support Specialist, 2021–2026; Customer Service Officer, 2019–2021 — continuous customer-facing support/service roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: Multi-year customer support and service roles in business contexts imply applied customer success practices and translating customer needs into solutions)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: Customer Support Specialist role reasonably entails problem-solving and using information about customer issues to guide responses and improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF: Customer Support Specialist and Customer Service Officer roles require ongoing customer communication and relationship handling)
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - Thai and English listed with stated proficiency; interview should confirm level against role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R9 F9 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Support Specialist, 2021–2026; Customer Service Officer, 2019–2021 — multi-year customer-facing support/service roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: Extended experience in customer support and service entails applying customer success practices and turning customer needs into solutions)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: Customer Support Specialist role reasonably entails structured problem-solving using customer information to guide responses and improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF: Customer-facing support and service positions require continuous verbal and written communication and relationship management)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: Languages section lists Thai fluency and English professional working proficiency)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R9 F9 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R9 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID: Bachelor of Business Administration (Marketing), 2016–2020)
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID: Customer Support Specialist, 2021–2026; Customer Service Officer, 2019–2021 — multi-year customer-facing support/service roles)
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF: Extended experience in customer support and service entails applying customer success practices and turning customer needs into solutions)
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF: Customer Support Specialist role reasonably entails structured problem-solving using customer information to guide responses and improvements)
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF: Customer-facing support and service positions require continuous verbal and written communication and relationship management)
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID: Languages section lists Thai fluency and English professional working proficiency)

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R10 F10 `intake_report.json`
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

#### PROBE-R3B-FBAT R10 F10 `numbered.txt`
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

#### PROBE-R3B-FBAT R10 F10 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R10 F10 `e1.pass1.txt`
```
[NULL FILTRATION — R10]
RESUME: R10
NULL LINES: none
[FILTRATION-R10]
Second pass?
```

#### PROBE-R3B-FBAT R10 F10 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R10 F10 `null_list.txt`
```
[NULL FILTRATION — R10]
RESUME: R10
NULL LINES: none
[FILTRATION-R10]
Second pass?
```

#### PROBE-R3B-FBAT R10 F10 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) handling 1,200+ accounts and customer issues.
⚖️ Raised customer satisfaction and improved response times in support roles → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence) Demonstrated customer success outcomes: increased satisfaction from 71% to 88%, reduced first-response time from 6 hours to 40 minutes while managing large account volume, indicating applied customer success principles and translation of needs into strategies.
⚖️ Measurable improvements in satisfaction and response time → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence) Used metrics (CSAT, response time) to diagnose issues and implement changes that significantly improved performance, evidencing analytical, problem-solving, and data-driven intervention design.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multi-year customer-facing support and service roles engaging with 1,200+ accounts indicate strong communication and interpersonal engagement with customers.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record states Thai fluency and English professional working proficiency; interview to confirm level against role needs)

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R10 F10 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions handling 1,200+ accounts.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Achieved customer satisfaction improvement from 71% to 88% and reduced first-response time from 6 hours to 40 minutes, indicating applied customer success practices and translation of customer needs into effective process changes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Used performance metrics (customer satisfaction and response time) to identify issues and drive significant improvements from 71% to 88% CSAT and 6 hours to 40 minutes response time, evidencing analytical, problem-solving, and data-informed decision-making.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multi-year customer-facing support and service roles engaging with 1,200+ accounts demonstrate strong communication and interpersonal interaction with a wide range of customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Record states Thai fluency and English professional working proficiency.

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R10 F10 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R10 Arisa Boonmee - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Support Specialist (2021–2026) and Customer Service Officer (2019–2021) in customer-facing support/service positions handling 1,200+ accounts.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Achieved customer satisfaction improvement from 71% to 88% and reduced first-response time from 6 hours to 40 minutes, indicating applied customer success practices and translation of customer needs into effective process changes.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-INF) Used performance metrics (customer satisfaction and response time) to identify issues and drive significant improvements from 71% to 88% CSAT and 6 hours to 40 minutes response time, evidencing analytical, problem-solving, and data-informed decision-making.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multi-year customer-facing support and service roles engaging with 1,200+ accounts demonstrate strong communication and interpersonal interaction with a wide range of customers.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Record states Thai fluency and English professional working proficiency.

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R11 F11 `intake_report.json`
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
      "detail": "text extracted",
      "evidence": {
        "per_page_chars": [
          1013
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

#### PROBE-R3B-FBAT R11 F11 `numbered.txt`
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

#### PROBE-R3B-FBAT R11 F11 `resume.numbered.txt`
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

#### PROBE-R3B-FBAT R11 F11 `e1.pass1.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES: none
[FILTRATION-R11]
Second pass?
```

#### PROBE-R3B-FBAT R11 F11 `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-FBAT R11 F11 `null_list.txt`
```
[NULL FILTRATION — R11]
RESUME: R11
NULL LINES: none
[FILTRATION-R11]
Second pass?
```

#### PROBE-R3B-FBAT R11 F11 `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022) in B2B SaaS, handling onboarding, training, and support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist that reduced time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; rebuilt onboarding process to achieve specific cycle-time reduction; tracked ticket resolution metrics and impact of help-centre content.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; wrote 22 help-centre articles in two languages.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; stated Thai fluency and English professional working proficiency with standardized test score.

[AUDIT-2026-009-0001]
```

#### PROBE-R3B-FBAT R11 F11 `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), handling onboarding, training sessions, and customer support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist that reduced time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; rebuilt onboarding process to achieve specific cycle-time reduction; tracked ticket resolution metrics and impact of help-centre content.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; wrote 22 help-centre articles in two languages.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; stated Thai fluency and English professional working proficiency.

[AUDIT-2026-009-0002]
```

#### PROBE-R3B-FBAT R11 F11 `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R11 Pimchanok Srisawat - Advance

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Business Administration (Marketing), 2016–2020.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-EVID) Customer Success Executive (Mar 2022–Aug 2026) and Client Support Specialist (Jun 2020–Feb 2022), handling onboarding, training sessions, and customer support.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-EVID) Improved renewal rate from 78% to 91% by monitoring usage dashboards and proactively engaging low-usage accounts; designed onboarding checklist that reduced time-to-first-report from 21 to 9 days.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Used Metabase dashboards and login metrics to trigger outreach; rebuilt onboarding process to achieve specific cycle-time reduction; tracked ticket resolution metrics and impact of help-centre content.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-EVID) Ran 3-session training sequences for each new HR team; served as primary contact handling 30–40 tickets per day; wrote 22 help-centre articles in two languages.
✅ Proficiency in both written and spoken English and Thai.: (MET-EVID) Wrote help-centre articles in Thai and English; stated Thai fluency and English professional working proficiency.

[AUDIT-2026-009-0002]
```

### Appendix — PROBE-R3B-S2

#### PROBE-R3B-S2 `run.json`
```
{
  "run_id": "20260906-073019",
  "mode": "full",
  "boundary_sha256": "05bac5c9897c9dc298b1d925a5478d11afa76b3416082d78aaaf1671272d5bb5",
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
    "fixtures/runyarin.txt"
  ]
}
```

#### PROBE-R3B-S2 `requirement_set.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.
```

#### PROBE-R3B-S2 `extraction.pass1.txt`
*not written this run*

#### PROBE-R3B-S2 `extraction.pass2.txt`
*not written this run*

#### PROBE-R3B-S2 R1 Runyarin `resume.numbered.txt`
```
L1: RUNYARIN L.
L2: (Belar)
L3: SKILLS
L4: EXCEL
L5: POWERPOINT
L6: WORD
L7: PHOTOSHOP
L8: HOBBIES
L9: TRAVEL
L10: MUSIC
L11: MOVIE
L12: SPORT
L13: CONTACT
L14: +66953648941
L15: Samut Prakan, Thailand
L16: Runyarin.lertchai@gmail.com
L17: ABOUT ME
L18: Open to freelance, full-time, and contract roles across APAC or remote
L19: Publisher Monetization, Programmatic Media, Account
L20: Management & Business Development Specialist
L21: With 10+ years of experience across Southeast Asia driving digital growth through ad tech, publisher strategy, and cross- platform execution.
L22: Key Skills:
L23: •
L24: Publisher Monetization & Yield Optimization
L25: •
L26: Programmatic Media Buying (RTB, Header Bidding)
L27: •
L28: SSPs, Ad Servers, Pixel & SDK Integration
L29: •    AdTech Tools: DV360, Appier, GAM, Google Ads, Facebook Ads
L30: • Analytics & Tracking: GA, Adjust, Appsflyer
L31: • Client Relations & Cross-Functional Team Leadership
L32: EDUCATION
L33: BACHELOR OF ARTS IN
L34: COMMUNICATION ARTS
L35: 2007-2011
L36: BANGKOK UNIVERSITY
L37: INTERNATIONAL COLLEGE
L38: NZQA NATIONAL CERTIFICATE
L39: CRAIGHEAD DIOCESAN SCHOOL,
L40: NEW  ZEALAND
L41: 2002-2007
L42: EXPERIENCES
L43: Appier Inc.(2021–Present): SEA Lead
L44: Account Manager
L45: •
L46: Led full-funnel programmatic campaigns for
L47: SEA advertisers
L48: •
L49: Supported yield improvement through strategic bidding and inventory insights
L50: •
L51: Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L52: Recognized for 30% YoY revenue growth and successful SSP optimization across accounts
L53:  Certificate of Achievement
L54: Havas Riverorchid(2021): Hybrid Media
L55: Manager
L56: •
L57: Crafted integrated media strategies for luxury and auto clients
L58: •
L59: Delivered performance-based media plans with measurable KPIs
L60: •
L61: Supervised cross-functional teams ensuring timely and accurate campaign execution
L62: Fivestones(2021): Account & Business
L63: Strategy Manager
L64: •
L65: Handled programmatic campaign setup via ad servers and SEM tools
L66: •
L67: Troubleshot pixel integrations and improved web analytics configurations
L68: •
L69: Acted as liaison between tech and business teams to enhance delivery
L70: Dentsu One(2018-2019): Account Manager
L71: • Managed Honda Connect app and website development, including CDP system integration and partner features (e.g., Major Cineplex)
L72: • Led successful SEO pitch for UmayPlus and managed full-year digital strategy including
L73: Facebook Ads, content, and search campaigns
L74: Martini Group(2017-2018):
L75: Brand Management & Digital Junior
L76: Manager
L77: • Managed end-to-end marketing campaigns from ideation to impact analysis
L78: • Executed SEO, social media content, and digital outreach (SMS, Email)
L79: • Developed brand assets and visuals to support creative marketing strategies
L80: • Contributed to brand building with hands-on design and content creation
L81: PHAR Partnerships, Air Asia[2014-2016):
L82: Digital Media Consultant
L83: • Supported go-to-market strategy development and secured internal alignment
L84: • Presented digital platforms to C-level stakeholders and partners
L85: • Planned and executed cross-channel marketing campaigns, including website and social media content
L86: - Reference Letter
L87: Innity Digital Media Co., Ltd.(2011-2013):
L88: Digital Campaign Specialist / Account Executive
L89: •
L90: Gained deep product knowledge to support client pitches and campaign execution
L91: •
L92: Provided technical guidance for pixel setup and campaign implementation
L93: •
L94: Collaborated with Sales, Business
L95: Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
L96: •
L97: Maintained media plans and managed reporting, budgeting, and updates across
L98: CRM, RTB platforms, and analytics tools (e.g., DoubleClick, ComScore, Google Dev)
```

#### PROBE-R3B-S2 R1 Runyarin `e1.pass1.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for
L49 — Supported yield improvement through strategic bidding and inventory insights
L55 — Crafted integrated media strategies for luxury and auto clients
L57 — Delivered performance-based media plans with measurable KPIs
L59 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L63 — Handled programmatic campaign setup via ad servers and SEM tools
L65 — Troubleshot pixel integrations and improved web analytics configurations
L67 — Acted as liaison between tech and business teams to enhance delivery
L75 — Managed end-to-end marketing campaigns from ideation to impact analysis
L76 — Executed SEO, social media content, and digital outreach (SMS, Email)
L77 — Developed brand assets and visuals to support creative marketing strategies
L78 — Contributed to brand building with hands-on design and content creation
L81 — Supported go-to-market strategy development and secured internal alignment
L82 — Presented digital platforms to C-level stakeholders and partners
L83 — Planned and executed cross-channel marketing campaigns, including website and social media content
L88 — Gained deep product knowledge to support client pitches and campaign execution
L90 — Provided technical guidance for pixel setup and campaign implementation
L92 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
Second pass?
```

#### PROBE-R3B-S2 R1 Runyarin `e1.pass2.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
```

#### PROBE-R3B-S2 R1 Runyarin `null_list.txt`
```
[NULL FILTRATION — R1]
RESUME: R1
NULL LINES:
L24 — Publisher Monetization & Yield Optimization
L26 — Programmatic Media Buying (RTB, Header Bidding)
L28 — SSPs, Ad Servers, Pixel & SDK Integration
L31 — Client Relations & Cross-Functional Team Leadership
L46 — Led full-funnel programmatic campaigns for SEA advertisers
L49 — Supported yield improvement through strategic bidding and inventory insights
L51 — Worked closely with internal tech teams for pixel setup, fraud reduction, and postback tracking
L57 — Crafted integrated media strategies for luxury and auto clients
L59 — Delivered performance-based media plans with measurable KPIs
L61 — Supervised cross-functional teams ensuring timely and accurate campaign execution
L65 — Handled programmatic campaign setup via ad servers and SEM tools
L67 — Troubleshot pixel integrations and improved web analytics configurations
L69 — Acted as liaison between tech and business teams to enhance delivery
L77 — Managed end-to-end marketing campaigns from ideation to impact analysis
L78 — Executed SEO, social media content, and digital outreach (SMS, Email)
L79 — Developed brand assets and visuals to support creative marketing strategies
L80 — Contributed to brand building with hands-on design and content creation
L83 — Supported go-to-market strategy development and secured internal alignment
L84 — Presented digital platforms to C-level stakeholders and partners
L85 — Planned and executed cross-channel marketing campaigns, including website and social media content
L90 — Gained deep product knowledge to support client pitches and campaign execution
L92 — Provided technical guidance for pixel setup and campaign implementation
L94 — Collaborated with Sales, Business Development, and Creative teams to plan, execute, and optimize campaigns based on client objectives
[FILTRATION-R1]
```

#### PROBE-R3B-S2 R1 Runyarin `e2.pass1.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Arts degree in Communication Arts.
⚖️ [10+ years in account management, digital campaign specialist, digital media consultant, and hybrid media manager roles] → Experience in a customer-facing role, with a focus on customer success, training, or support.: (equivalence explanation) Extensive client-facing account management and digital media roles demonstrate sustained responsibility for client outcomes and support, equivalent to customer success/support experience.
⚖️ [Led and managed multiple digital and account management roles over 10+ years] → Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (equivalence explanation) Long-term responsibility for managing accounts and campaigns, plus recognition for revenue growth, indicates ability to understand client needs and convert them into strategic actions and campaigns.
⚖️ [Recognized for 30% YoY revenue growth and ongoing campaign optimization responsibilities] → Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (equivalence explanation) Achieving 30% YoY revenue growth and optimizing campaigns implies strong analytical and problem-solving skills applied to performance data and client outcomes.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multiple account manager and consultant roles over many years require strong communication and relationship-building with clients and internal teams.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on explicit language skills; interview should confirm written and spoken proficiency in both languages)

[AUDIT-2026-001-0001]
```

#### PROBE-R3B-S2 R1 Runyarin `e2.pass2.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Arts degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) 10+ years in client-facing roles including account manager, account executive, digital media consultant, and related account management positions, responsible for ongoing client relationships and outcomes.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Long-term account management and strategy roles, including managing app and website development and leading full-year digital strategy campaigns, show ability to understand client goals and convert them into concrete plans and execution.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for 30% year-over-year revenue growth and responsibilities for reporting, budgeting, and optimization across media plans and analytics tools demonstrate strong analytical and problem-solving skills applied to performance data.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multiple years as account manager, consultant, and account executive require high-level communication and relationship-building with customers and internal teams.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on explicit language skills; interview should confirm written and spoken proficiency in both languages)

[AUDIT-2026-001-0002]
```

#### PROBE-R3B-S2 R1 Runyarin `evaluation.txt`
```
Customer Success Associate – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree in business, marketing, or a related field.
- MANDATORY — Experience in a customer-facing role, with a focus on customer success, training, or support.
- MANDATORY — Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.
- MANDATORY — Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.
- MANDATORY — Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.
- MANDATORY — Proficiency in both written and spoken English and Thai.

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 RUNYARIN L. - Advance – Verify

✅ Bachelor's degree in business, marketing, or a related field.: (MET-EVID) Bachelor of Arts degree.
✅ Experience in a customer-facing role, with a focus on customer success, training, or support.: (MET-INF) 10+ years in client-facing roles including account manager, account executive, digital media consultant, and related account management positions, responsible for ongoing client relationships and outcomes.
✅ Strong understanding of customer success principles and practices, with the ability to translate customer needs into actionable strategies.: (MET-INF) Long-term account management and strategy roles, including managing app and website development and leading full-year digital strategy campaigns, show ability to understand client goals and convert them into concrete plans and execution.
✅ Excellent problem-solving and analytical skills, with a data-driven approach to designing and delivering customer interventions.: (MET-EVID) Recognition for 30% year-over-year revenue growth and responsibilities for reporting, budgeting, and optimization across media plans and analytics tools demonstrate strong analytical and problem-solving skills applied to performance data.
✅ Exceptional communication and interpersonal skills, with the ability to engage and educate customers effectively.: (MET-INF) Multiple years as account manager, consultant, and account executive require high-level communication and relationship-building with customers and internal teams.
⚠️ REQ-LANG Proficiency in both written and spoken English and Thai.: (verification required - record silent on explicit language skills; interview should confirm written and spoken proficiency in both languages)

[AUDIT-2026-001-0002]
```

### Appendix — PROBE-R3B-S3-bkk

#### PROBE-R3B-S3-bkk `run.json`
```
{
  "run_id": "20260906-074045",
  "mode": "full",
  "boundary_sha256": "e03684d173785586b3de0a1b66600a8c28a7e504c443ff0377034774b5c2efb1",
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
  "jd": "battery/bangkok/jd.txt",
  "resumes": [
    "battery/bangkok/r02.txt"
  ]
}
```

#### PROBE-R3B-S3-bkk `requirement_set.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week
```

#### PROBE-R3B-S3-bkk `extraction.pass1.txt`
*not written this run*

#### PROBE-R3B-S3-bkk `extraction.pass2.txt`
*not written this run*

#### PROBE-R3B-S3-bkk R1 Krit `resume.numbered.txt`
```
L1: Krit Rattanapong
L2: Summary: Results-driven HR leader delivering 360 talent acquisition, ATS transformation, HRIS excellence, dashboard ownership, and strategic workforce planning - tailored to Bangkok Learning Group's hybrid growth model.
L3: Skills: Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever, Power BI, Tableau, Looker Studio, end-to-end hiring transformation
L4: Experience:
L5: Senior Talent Acquisition Executive - Hospitality group, 2021-present
L6: - Spearheaded end-to-end hiring transformation and owned the ATS strategy across the talent function.
L7: - Built leadership dashboards that improved hiring efficiency by 40% and elevated data-driven decision-making.
L8: - Drove HRIS excellence and optimized the full employee lifecycle.
L9: Recruitment Officer - Retail company, 2019-2021
L10: - Managed full-cycle recruitment, posted roles, screened candidates, scheduled interviews, and partnered with hiring managers on workforce planning.
L11: Education: BBA, Thammasat University
L12: Other: Thai national. Lives near Asok BTS. References describe him as polished and client-facing. No career gaps.
```

#### PROBE-R3B-S3-bkk R1 Krit `e1.pass1.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: Results-driven HR leader delivering 360 talent acquisition, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned the ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates, scheduled interviews  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3B-S3-bkk R1 Krit `e1.pass2.txt`
```
Second-pass integrity verified. Existing NULL list stands unchanged.
```

#### PROBE-R3B-S3-bkk R1 Krit `null_list.txt`
```
[NULL FILTRATION — R1]  
RESUME: R1  
NULL LINES:  
L2 — Summary: Results-driven HR leader delivering 360 talent acquisition, ATS transformation, HRIS excellence  
L6 — Spearheaded end-to-end hiring transformation and owned the ATS strategy  
L8 — Drove HRIS excellence and optimized the full employee lifecycle  
L10 — Managed full-cycle recruitment, posted roles, screened candidates, scheduled interviews  
[FILTRATION-R1]  
Second pass?
```

#### PROBE-R3B-S3-bkk R1 Krit `e2.pass1.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week  

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Krit Rattanapong - Advance

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
⚖️ 5 years of recruitment-focused roles (2019–present) with leadership dashboards improving hiring efficiency by 40% → 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (equivalence explanation — 4+ years directly in recruitment operations with significant measurable impact reasonably substitutes for the 5-year threshold)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills list includes Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills list includes Power BI, Tableau, Looker Studio; experience line notes leadership dashboards)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-INF — Senior Talent Acquisition Executive and Recruitment Officer roles imply process ownership and improvement in recruitment workflows and employee lifecycle)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles necessarily involve handling confidential candidate and employee data)  
⚠️ REQ-LANG Strong English communication skills for reports and leadership updates: (verification required — record does not explicitly state English ability; interview should confirm communication level)  
⚠️ REQ-ACC Able to work hybrid in Bangkok 3 days per week: (accommodation assessment required — current and prior roles are in the same metropolitan context; feasibility of 3-days-per-week hybrid pattern should be confirmed)

[AUDIT-2026-001-0001]
```

#### PROBE-R3B-S3-bkk R1 Krit `e2.pass2.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week  

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Krit Rattanapong - Advance – Verify

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide 5+ years in recruitment-focused roles)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills list includes Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills list includes Power BI, Tableau, Looker Studio; experience bullet notes leadership dashboards that improved hiring efficiency)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, directly enhancing recruitment workflows and decision-making)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles inherently involve handling confidential candidate and employee data)  
⚠️ REQ-LANG Strong English communication skills for reports and leadership updates: (verification required — record does not explicitly state English ability; interview should confirm communication level)  
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — no stated limitation affecting ability to follow a hybrid schedule; confirm details during hiring process)

[AUDIT-2026-001-0002]
```

#### PROBE-R3B-S3-bkk R1 Krit `evaluation.txt`
```
HR Operations & Recruitment Systems Manager – Requirements Extracted (parseable only)

- MANDATORY — Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems  
- MANDATORY — 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning  
- MANDATORY — Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar  
- MANDATORY — Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools  
- MANDATORY — Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes  
- MANDATORY — Experience handling confidential employee or candidate information  
- MANDATORY — Strong English communication skills for reports and leadership updates  
- ESSENTIAL-FUNCTION — Able to work hybrid in Bangkok 3 days per week  

All other listed "requirements" are non-parseable in this reality and exert no effect.

R1 Krit Rattanapong - Advance – Verify

✅ Bachelor's degree or equivalent professional experience in HR operations, recruitment operations, or workforce systems: (MET-EVID — BBA degree listed under Education)  
✅ 5+ years of experience in HR operations, recruitment operations, talent acquisition, people operations, or workforce planning: (MET-EVID — Recruitment Officer 2019–2021 and Senior Talent Acquisition Executive 2021–present provide 5+ years in recruitment-focused roles)  
✅ Experience using an ATS or HRIS such as Workday, Greenhouse, Lever, BambooHR, Manatal, Zoho Recruit, SmartRecruiters, SAP SuccessFactors, or similar: (MET-EVID — Skills list includes Workday, Greenhouse, SAP SuccessFactors, BambooHR, Manatal, Lever)  
✅ Ability to build reports, trackers, or dashboards using Excel, Google Sheets, Looker Studio, Power BI, Tableau, or similar tools: (MET-EVID — Skills list includes Power BI, Tableau, Looker Studio; experience bullet notes leadership dashboards that improved hiring efficiency)  
✅ Experience improving recruitment workflows, onboarding, retention, scheduling, or employee data processes: (MET-EVID — Built leadership dashboards that improved hiring efficiency by 40%, directly enhancing recruitment workflows and decision-making)  
✅ Experience handling confidential employee or candidate information: (MET-INF — Recruitment Officer and Senior Talent Acquisition Executive roles inherently involve handling confidential candidate and employee data)  
⚠️ REQ-LANG Strong English communication skills for reports and leadership updates: (verification required — record does not explicitly state English ability; interview should confirm communication level)  
✅ Able to work hybrid in Bangkok 3 days per week: (NO-CONTRA — no stated limitation affecting ability to follow a hybrid schedule; confirm details during hiring process)

[AUDIT-2026-001-0002]
```

