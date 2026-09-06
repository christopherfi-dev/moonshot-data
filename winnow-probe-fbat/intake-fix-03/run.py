#!/usr/bin/env python3
"""Two engines, nothing between them.

Per candidate, four calls, per-candidate (never batch):
  JD + numbered resume            -> E1 pass 1 -> provisional NULL list
    + provisional                 -> E1 pass 2 -> FINAL NULL list
  JD + numbered resume + NULLs    -> E2 pass 1 -> provisional evaluation
    + provisional                 -> E2 pass 2 -> FINAL evaluation

The boundary token is minted once PER RUN (not per call) so the fixed
prefix is byte-identical across candidates and provider caching works.

Usage:
  export DEEPSEEK_API_KEY=...   # Engine 1 (config.json e1)
  export OPENAI_API_KEY=...     # Engine 2 (config.json e2)
  python3 run.py --jd jd.txt --resumes r1.txt r2.txt r3.txt
"""
import argparse
import json
import secrets
import sys
import threading
import time
from concurrent import futures
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.injection import load_verified_assets          # noqa: E402
from lib.numbering import number_lines                  # noqa: E402
from lib.audit import AuditChain, h                     # noqa: E402
from lib.engines import (e1_payload, e2_payload, double_pass,  # noqa: E402
                         extraction_payload)
from lib.transport import call_model                    # noqa: E402
from intake import intake as intake_doc                 # noqa: E402

INTAKE_SUFFIXES = (".pdf", ".docx")

ROOT = Path(__file__).resolve().parent


def second_pass_final(result: dict) -> str:
    """The pass-2 output is authoritative. If pass 2 confirmed integrity,
    the pass-1 artifact stands; otherwise pass 2 IS the corrected artifact.
    Stored verbatim either way — this selects a file, it judges nothing."""
    p2 = result["pass2"].strip()
    if p2.startswith("Second-pass integrity verified"):
        return result["pass1"]
    return result["pass2"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jd", required=True)
    ap.add_argument("--resumes", nargs="*", default=[])
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--mode", choices=["full", "e1-only", "extract-only"],
                    default="full")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"))
    args = ap.parse_args()
    if args.mode != "extract-only" and not args.resumes:
        ap.error("--resumes is required unless --mode extract-only")
    if args.mode == "extract-only" and args.resumes:
        ap.error("--mode extract-only takes no --resumes")

    cfg = json.loads((ROOT / "config.json").read_text())
    assets = load_verified_assets()
    e1_asset = assets[cfg["e1_asset"]]
    e2_asset = assets[cfg["e2_asset"]]

    run_id = time.strftime("%Y%m%d-%H%M%S")
    run_dir = Path(args.outdir or (ROOT / "runs" / run_id))
    run_dir.mkdir(parents=True, exist_ok=True)
    audit = AuditChain(run_dir)
    attempts = []

    boundary = secrets.token_hex(16)  # per-RUN, constant across candidates
    jd_path = Path(args.jd)
    if jd_path.suffix.lower() in INTAKE_SUFFIXES:
        jd_rep = intake_doc(jd_path, run_dir / "jd-intake")
        if jd_rep["status"] != "ok":
            print(f"JD intake status '{jd_rep['status']}' — nothing sent to "
                  f"engines; operator review required: "
                  f"{run_dir / 'jd-intake' / 'intake_report.json'}")
            raise SystemExit(3)
        jd = (run_dir / "jd-intake" / "normalized.txt").read_text()
    else:
        jd = jd_path.read_text()
    audit.record("intake", "jd", jd, {"source": args.jd})

    # Run-constant requirement extraction (v28.10): double-passed like every
    # other call (R9); JD-level cached (R13) — first sight of a JD+asset pair
    # extracts and freezes the set; later runs reuse it verbatim, zero calls.
    # e1-only mode is a fluff report with no evaluation: no extraction, no
    # requirement set, no E2 — the mode selects which engines run; it checks
    # and rejects nothing. extract-only (ruling A, 2026-08-30) runs this
    # block exactly as full mode does, then stops: zero candidates, zero E1.
    req_set = None
    if args.mode in ("full", "extract-only"):
        cache_dir = ROOT / "cache" / "requirement-sets"
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = cache_dir / f"{h(jd)}-{h(e2_asset)}.txt"
        if cache_file.exists():
            req_set = cache_file.read_text()
            audit.record("extraction", "requirement_set.cache_hit", req_set,
                         {"cache": str(cache_file)})
        else:
            # Extraction and E2 pass 2 are different tasks that happened to
            # share one config key. Extraction reads a whole job description
            # once per run and its result governs every candidate; evaluation
            # pass 2 audits one candidate's lines. A model may need a
            # different reasoning effort for each, and with one key the two
            # could not be set independently — raising effort for extraction
            # silently raised it for evaluation, and lowering it for
            # evaluation silently lowered it for extraction.
            #
            # `extraction` is optional and defaults to `e2_pass2`, so a
            # config without it behaves exactly as before. Both passes of
            # extraction use it; the double-pass discipline is unchanged.
            ext_cfg = cfg.get("extraction", cfg["e2_pass2"])
            r0 = double_pass(e2_asset, extraction_payload(boundary, jd),
                             ext_cfg, attempts,
                             pass2_cfg=ext_cfg)
            (run_dir / "extraction.pass1.txt").write_text(r0["pass1"])
            (run_dir / "extraction.pass2.txt").write_text(r0["pass2"])
            req_set = second_pass_final(r0)
            cache_file.write_text(req_set)
            audit.record("extraction", "requirement_set.frozen", req_set,
                         {"cache": str(cache_file)})
        (run_dir / "requirement_set.txt").write_text(req_set)
        print(f"REQUIREMENT SET [{cache_file.name}]:\n{req_set}\n")

    # R14: candidates are independent — up to 4 in flight. Intake stays
    # serialized under a lock (the PDF libraries are not thread-safe);
    # engine calls run concurrently. Per-candidate dirs/audit unchanged.
    intake_lock = threading.Lock()

    def process_candidate(i, rpath):
        rid = f"R{i}"
        cdir = run_dir / rid
        cdir.mkdir(exist_ok=True)
        rp = Path(rpath)
        if rp.suffix.lower() in INTAKE_SUFFIXES:
            with intake_lock:
                rep = intake_doc(rp, cdir)
            if rep["status"] in ("blocked", "unreadable"):
                print(f"{rid}: intake status '{rep['status']}' ({rpath}) — "
                      f"withheld from engines; operator review required: "
                      f"{cdir / 'intake_report.json'}")
                audit.record("intake", f"{rid}.intake_status", rep["status"],
                             {"source": rpath})
                return
            if rep["status"] != "ok":
                # INTAKE-FIX-03: a degraded extraction is evaluated, flagged.
                # A non-evaluation is a decline the candidate never sees.
                failed = [c["name"] for c in rep["checks"] if c["passed"] is False]
                print(f"{rid}: intake status '{rep['status']}' ({rpath}) — "
                      f"evaluated with flag {failed}; see "
                      f"{cdir / 'intake_report.json'}")
                audit.record("intake", f"{rid}.intake_status", rep["status"],
                             {"source": rpath, "failed_checks": failed})
            raw = (cdir / "normalized.txt").read_text()
            numbered = (cdir / "numbered.txt").read_text()
            n = rep["lines"]
        else:
            raw = rp.read_text()
            numbered, n = number_lines(raw)
        (cdir / "resume.numbered.txt").write_text(numbered)
        audit.record("intake", f"{rid}.raw", raw, {"source": rpath})
        audit.record("intake", f"{rid}.numbered", numbered, {"lines": n})

        # ENGINE 1 — double pass
        p1 = e1_payload(boundary, jd, rid, numbered)
        r1 = double_pass(e1_asset, p1, cfg["e1"], attempts)
        (cdir / "e1.pass1.txt").write_text(r1["pass1"])
        (cdir / "e1.pass2.txt").write_text(r1["pass2"])
        null_list = second_pass_final(r1)
        (cdir / "null_list.txt").write_text(null_list)
        audit.record("e1", f"{rid}.pass1", r1["pass1"])
        audit.record("e1", f"{rid}.pass2", r1["pass2"])
        audit.record("e1", f"{rid}.null_list", null_list)

        # ENGINE 2 — double pass, original resume UNMODIFIED (full mode only)
        if args.mode == "full":
            p2 = f"EVALUATION DATE: {args.date}\n\n" + e2_payload(
                boundary, jd, rid, numbered, null_list, requirement_set=req_set)
            r2 = double_pass(e2_asset, p2, cfg["e2"], attempts,
                             pass2_cfg=cfg.get("e2_pass2"))
            (cdir / "e2.pass1.txt").write_text(r2["pass1"])
            (cdir / "e2.pass2.txt").write_text(r2["pass2"])
            final_eval = second_pass_final(r2)
            (cdir / "evaluation.txt").write_text(final_eval)
            audit.record("e2", f"{rid}.pass1", r2["pass1"])
            audit.record("e2", f"{rid}.pass2", r2["pass2"])
            audit.record("e2", f"{rid}.evaluation", final_eval)

        print(f"{rid}: done ({rpath})")

    with futures.ThreadPoolExecutor(max_workers=4) as pool:
        tasks = [pool.submit(process_candidate, i, rp)
                 for i, rp in enumerate(args.resumes, start=1)]
        for t in tasks:
            t.result()

    (run_dir / "transport.json").write_text(json.dumps(attempts, indent=2))
    (run_dir / "run.json").write_text(json.dumps({
        "run_id": run_id, "mode": args.mode, "boundary_sha256": h(boundary),
        "models": {"e1": cfg["e1"]["params"]["model"],
                   "e2": cfg["e2"]["params"]["model"],
                   "e2_pass2": cfg["e2_pass2"]["params"]["model"],
                   "extraction": cfg.get(
                       "extraction", cfg["e2_pass2"])["params"]["model"]},
        "reasoning_effort": {
            "e2": cfg["e2"]["params"].get("reasoning_effort"),
            "e2_pass2": cfg["e2_pass2"]["params"].get("reasoning_effort"),
            "extraction": cfg.get(
                "extraction", cfg["e2_pass2"])["params"].get(
                    "reasoning_effort")},
        "jd": args.jd, "resumes": args.resumes,
    }, indent=2))
    audit.write()
    print(f"\nRun complete: {run_dir}")


if __name__ == "__main__":
    main()
