#!/usr/bin/env python3
"""Intake layer — Python port of the salvaged PHP intake (src/Intake/*).

Ports the DOCTRINE, not the code: dual extraction, four deterministic
validators (V-X1..V-X4), the text normalizer, and the operator gate.
Thresholds carried over from the year-validated originals:
  V-X3 ORDER_DIVERGENCE_THRESHOLD = 0.08 (token-sequence, 5000-token cap)
V-X1 (INTAKE-FIX-03, 2026-09-06): no character floor. V-X1 now tests the
failure it was written for — a PDF page with image objects and no text
layer. Short pages are short, not failed. Non-PDF extractors (python-docx,
txt) have no page or text-layer failure mode; V-X1 checks only that some
text was extracted. A document from which no text at all was extracted
reports status "unreadable" and is never sent to the engines.
This layer judges EXTRACTIONS, never candidates. It blocks nothing by
itself: it produces a status (ok / degraded / blocked-for-operator) and
an evidence report; the operator gate is a human decision.

Extractors: pdfplumber (primary, layout-aware), `pdftotext -layout`
(secondary, for V-X3), PyMuPDF (fallback when primary yields nothing).
DOCX via python-docx if present; TXT read directly.

Output per document: normalized text, numbered lines (the pipeline's
numbering seam), and intake_report.json.
"""
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ORDER_DIVERGENCE_THRESHOLD = 0.08
RIGHT_BAND_MIN_CHARS = 400
MAX_TOKENS = 5000
MAX_REPORTED = 10

INVISIBLE = ["\u200b", "\u200c", "\u200d", "\u2060", "\ufeff", "\u00ad",
             "\u200e", "\u200f", "\u202a", "\u202b", "\u202c"]
MOJIBAKE = re.compile(r"[\u00c3\u00c2\u00e2][\u0080-\u00bf\u0152\u0153"
                      r"\u201a\u201e\u2020\u2021\u02c6\u2030\u2039\u20ac"
                      r"\u2018\u2019\u201c\u201d\u2013\u2014]")
TERMINATED = re.compile(r'[.!?:\u3002\uff01\uff1f\uff1a]["\)\]\u201d\u2019\u00bb]*$')
BULLET = re.compile(r"^[\u2022\u25cf\u25cb\u25e6\u25aa\u25ab\u2023\u2043"
                    r"\u2219\u00b7\-\*\u2013\u2014\u25a0\u25ba\u27a2]\s*")
LIST_MARKER = re.compile(r"^(?:\d+[.)\]:\u2013\u2014\-]|[a-zA-Z][.)]\s|[ivxlcdmIVXLCDM]+[.)]\s)")
CAPS_HEADING = re.compile(r"^[A-Z0-9&/.\-]{2,}$")


# ---------------------------------------------------------------- extraction
def extract_pdfplumber(path: Path):
    import pdfplumber
    pages = []
    with pdfplumber.open(str(path)) as pdf:
        for p in pdf.pages:
            pages.append(p.extract_text() or "")
    return pages


def extract_pymupdf(path: Path):
    import fitz
    doc = fitz.open(str(path))
    return [pg.get_text() for pg in doc]


def extract_pdftotext_layout(path: Path):
    if not shutil.which("pdftotext"):
        return None
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                         capture_output=True)
    if out.returncode != 0:
        return None
    return out.stdout.decode("utf-8", errors="replace").split("\f")


def detect_column_split(path: Path):
    """Per-page: x-coordinate splitting a left sidebar from a main column,
    or None. Deterministic geometry.

    A sidebar is a rail of content running down one side of the page beside
    a main column. The earlier signature — three or more blocks in a narrow
    left band vertically overlapping three or more blocks to their right —
    is also satisfied by the commonest CV layout there is: employer and role
    on the left, date range right-aligned on the same line. Splitting such a
    page severs every role from its dates, and duration evidence is read
    from dated roles downstream.

    One further condition separates a rail from a date column:

      SUBSTANCE — the right band must carry real content, not fragments.
      A date range, a page number, or a right-aligned label is short. The
      right band must hold at least RIGHT_BAND_MIN_CHARS characters of text
      across its blocks.

    A vertical-span condition was tried alongside this and removed. It
    measured the left band's height as a fraction of the page's, which is
    not scale-invariant for the property it was meant to capture: a
    continuous-scroll export is taller than A4, so an identical rail scores
    lower on it, and a genuine sidebar was excluded on a page 1.88 times A4
    while its substance passed eight times over. Across every document
    measured, substance alone gave the right answer and span never supplied
    a correct answer that substance had not already given.

    Substance plus the original signature must hold. A page failing either
    is read single-column, which is what it is.
    """
    import fitz
    splits = []
    with fitz.open(str(path)) as doc:
        for pg in doc:
            W = pg.rect.width
            blocks = [b for b in pg.get_text("blocks") if b[4].strip()]
            leftb = [b for b in blocks if b[2] < W * 0.45]
            rightb = [b for b in blocks if b[0] > W * 0.40]
            overlap = sum(1 for lb in leftb for rb in rightb
                          if lb[1] < rb[3] and rb[1] < lb[3])
            right_chars = sum(len(b[4].strip()) for b in rightb)
            is_sidebar = (len(leftb) >= 3 and overlap >= 3
                          and right_chars >= RIGHT_BAND_MIN_CHARS)
            splits.append(W * 0.45 if is_sidebar else None)
    return splits


def extract_columns_pymupdf(path: Path, splits):
    import fitz
    pages = []
    with fitz.open(str(path)) as doc:
        for pg, split in zip(doc, splits):
            if split is None:
                pages.append(pg.get_text())
                continue
            blocks = [b for b in pg.get_text("blocks") if b[4].strip()]
            left = sorted((b for b in blocks if b[2] <= split),
                          key=lambda b: (b[1], b[0]))
            right = sorted((b for b in blocks if b[2] > split),
                           key=lambda b: (b[1], b[0]))
            txt = "\n".join(b[4].rstrip() for b in left + right)
            pages.append(txt)
    return pages


def extract_columns_pdfplumber(path: Path, splits):
    import pdfplumber
    pages = []
    with pdfplumber.open(str(path)) as pdf:
        for pg, split in zip(pdf.pages, splits):
            if split is None:
                pages.append(pg.extract_text() or "")
                continue
            x0, y0, x1, y1 = pg.bbox
            left = pg.crop((x0, y0, split, y1)).extract_text() or ""
            right = pg.crop((split, y0, x1, y1)).extract_text() or ""
            pages.append(left + "\n" + right)
    return pages


def extract(path: Path):
    """Returns (pages, extractor_name, secondary_pages|None, notes).
    Single-column PDFs: pdfplumber primary vs `pdftotext -layout`.
    Column-signature PDFs: both independent extractors read column-wise,
    so V-X3 agreement is meaningful (comparing column order against an
    interleaved baseline would false-flag every designed CV)."""
    suf = path.suffix.lower()
    if suf == ".txt":
        return [path.read_text(errors="replace")], "txt", None, []
    if suf == ".docx":
        import docx
        d = docx.Document(str(path))
        return ["\n".join(p.text for p in d.paragraphs)], "python-docx", None, []
    notes = []
    splits = detect_column_split(path)
    if any(s is not None for s in splits):
        notes.append(f"column signature on page(s) "
                     f"{[i+1 for i, s in enumerate(splits) if s]} — "
                     f"column-aware extraction engaged (both extractors)")
        primary = extract_columns_pymupdf(path, splits)
        secondary = extract_columns_pdfplumber(path, splits)
        return primary, "pymupdf-columns", secondary, notes
    try:
        pages = extract_pdfplumber(path)
    except Exception as e:  # noqa: BLE001 — extraction fault, recorded
        pages, notes = [], [f"pdfplumber failed: {e}"]
    if not any(p.strip() for p in pages):
        notes.append("primary produced no text; PyMuPDF fallback used")
        pages = extract_pymupdf(path)
    return pages, "pdfplumber", extract_pdftotext_layout(path), notes


# ------------------------------------------------------------- normalization
def visible_skeleton(text: str) -> str:
    for ch in INVISIBLE:
        text = text.replace(ch, "")
    return re.sub(r"\s+", "", text)


def is_soft_wrap(before: str, after: str) -> bool:
    b, a = before.rstrip(), after.lstrip()
    if not b or not a:
        return False
    if TERMINATED.search(b):
        return False
    if BULLET.match(a) or LIST_MARKER.match(a):
        return False
    first = re.split(r"\s+", a, 1)[0]
    if CAPS_HEADING.match(first) and len(re.findall(r"[A-Z]", first)) >= 2:
        return False
    return a[0].islower() or b.endswith(("-", ","))


def normalize(raw: str):
    removed = {}
    text = raw
    for ch in INVISIBLE:
        n = text.count(ch)
        if n:
            removed[f"U+{ord(ch):04X}"] = n
            text = text.replace(ch, "")
    text = text.replace("\t", " ")
    text = unicodedata.normalize("NFC", text)
    lines = [ln.rstrip() for ln in text.splitlines()]
    out, rejoined = [], 0
    for ln in lines:
        if out and out[-1].strip() and ln.strip() and is_soft_wrap(out[-1], ln):
            out[-1] = out[-1].rstrip() + " " + ln.lstrip()
            rejoined += 1
        else:
            out.append(ln)
    return "\n".join(out), {"invisible_removed": removed,
                            "soft_wraps_rejoined": rejoined}


# ---------------------------------------------------------------- validators
def vx1_page_coverage(pages, path: Path, extractor: str):
    counts = [len(re.sub(r"\s", "", p)) for p in pages]
    if path.suffix.lower() != ".pdf":
        passed = any(counts)
        return {"name": "V-X1", "passed": passed,
                "detail": ("text extracted" if passed else
                           f"{extractor} extracted no text"),
                "evidence": {"per_page_chars": counts}}
    # PDF: image-only means a page carrying image objects with no text layer.
    images = []
    try:
        import fitz
        with fitz.open(str(path)) as doc:
            images = [len(pg.get_images()) for pg in doc]
    except Exception as e:  # noqa: BLE001 — recorded, not fatal
        images = []
    image_only = [i + 1 for i, c in enumerate(counts)
                  if c == 0 and i < len(images) and images[i] > 0]
    passed = not image_only
    return {"name": "V-X1", "passed": passed,
            "detail": ("no image-only pages" if passed else
                       f"page(s) {image_only} carry image objects and no "
                       f"text layer — image-only; OCR or operator review"),
            "evidence": {"per_page_chars": counts, "per_page_images": images}}


def vx2_encoding(text):
    repl = [i + 1 for i, ln in enumerate(text.splitlines()) if "\ufffd" in ln]
    moji = [(i + 1, MOJIBAKE.search(ln).group(0)) for i, ln in
            enumerate(text.splitlines()) if MOJIBAKE.search(ln)]
    passed = not repl and not moji
    parts = []
    if repl:
        parts.append(f"{len(repl)} U+FFFD on line(s) {repl[:MAX_REPORTED]}")
    if moji:
        parts.append(f"{len(moji)} mojibake signature(s) at "
                     f"{[m[0] for m in moji[:MAX_REPORTED]]}")
    return {"name": "V-X2", "passed": passed,
            "detail": "clean" if passed else "; ".join(parts),
            "evidence": {"replacement_lines": repl[:MAX_REPORTED],
                         "mojibake": moji[:MAX_REPORTED]}}


def vx3_reading_order(primary_pages, layout_pages):
    if layout_pages is None:
        return {"name": "V-X3", "passed": None,
                "detail": "NOT RUN — pdftotext unavailable (recorded, not a pass)",
                "evidence": {}}
    a = re.split(r"\s+", "\n".join(primary_pages).strip())[:MAX_TOKENS]
    b = re.split(r"\s+", "\n".join(layout_pages).strip())[:MAX_TOKENS]
    sm = SequenceMatcher(None, a, b, autojunk=False)
    divergence = 1.0 - sm.ratio()
    passed = divergence < ORDER_DIVERGENCE_THRESHOLD
    spans = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("replace", "delete", "insert") and len(spans) < 5:
            spans.append({"op": op, "primary": " ".join(a[i1:i2])[:120],
                          "layout": " ".join(b[j1:j2])[:120]})
    return {"name": "V-X3", "passed": passed,
            "detail": (f"divergence {divergence:.3f} vs threshold "
                       f"{ORDER_DIVERGENCE_THRESHOLD} "
                       f"({len(a)} primary / {len(b)} layout tokens)"
                       + ("" if passed else " — the two extractors disagree "
                          "about reading order; operator review before any "
                          "engine sees this document")),
            "evidence": {"divergence": round(divergence, 4),
                         "threshold": ORDER_DIVERGENCE_THRESHOLD,
                         "divergent_spans": spans}}


def vx4_normalization_safety(raw, normalized):
    """Every visible character must survive normalization.

    The comparison is made in NFC on both sides. The normalizer applies
    NFC, and NFC canonically reorders combining marks by combining class;
    Thai stacks a vowel mark and a tone mark on one base character, so an
    ordinary Thai CV is reordered by definition. Comparing a non-NFC raw
    against an NFC normalized reports that reordering as altered content
    and blocks the document, though the two strings render identically and
    hold the same characters. NFC is idempotent, so applying it to raw
    changes nothing about what this check catches: a normalizer that adds,
    drops, or substitutes a visible character still fails, because NFC
    cannot restore a character that is no longer there.
    """
    raw_skeleton = visible_skeleton(unicodedata.normalize("NFC", raw))
    norm_skeleton = visible_skeleton(normalized)
    ok = raw_skeleton == norm_skeleton
    evidence = {"skeleton_equal": ok, "compared_in": "NFC"}
    if not ok:
        for i, (a, b) in enumerate(zip(raw_skeleton, norm_skeleton)):
            if a != b:
                evidence["first_divergence"] = {
                    "offset": i,
                    "raw": f"U+{ord(a):04X}",
                    "normalized": f"U+{ord(b):04X}",
                    "raw_context": raw_skeleton[max(0, i - 40):i + 40],
                    "normalized_context": norm_skeleton[max(0, i - 40):i + 40]}
                break
        else:
            evidence["first_divergence"] = {
                "offset": min(len(raw_skeleton), len(norm_skeleton)),
                "detail": "one skeleton is a prefix of the other",
                "raw_len": len(raw_skeleton),
                "normalized_len": len(norm_skeleton)}
    return {"name": "V-X4", "passed": ok,
            "detail": ("normalized text preserves every visible character"
                       if ok else "normalization altered visible content — "
                       "BLOCKED; the normalizer may only touch whitespace "
                       "and invisibles"),
            "evidence": evidence}


# -------------------------------------------------------------------- intake
def intake(path: Path, outdir: Path) -> dict:
    outdir.mkdir(parents=True, exist_ok=True)
    pages, extractor, layout, notes = extract(path)
    raw = "\n".join(pages)
    normalized, norm_ev = normalize(raw)

    checks = [vx1_page_coverage(pages, path, extractor), vx2_encoding(normalized),
              vx3_reading_order(pages, layout),
              vx4_normalization_safety(raw, normalized)]

    (outdir / "normalized.txt").write_text(normalized)
    numbered, n = number_lines(normalized)

    if checks[3]["passed"] is False:
        status = "blocked"           # V-X4 outranks every other escalation
    elif n == 0:
        status = "unreadable"        # nothing extracted; nothing to evaluate
    elif any(c["passed"] is False for c in checks):
        status = "degraded-operator-review"
    else:
        status = "ok"

    (outdir / "numbered.txt").write_text(numbered)
    report = {"source": path.name, "extractor": extractor, "notes": notes,
              "pages": len(pages), "lines": n, "status": status,
              "normalization": norm_ev, "checks": checks}
    (outdir / "intake_report.json").write_text(json.dumps(report, indent=2))
    return report


def number_lines(text: str):
    out, n = [], 0
    for rawline in text.splitlines():
        line = rawline.rstrip()
        if not line.strip():
            continue
        n += 1
        out.append(f"L{n}: {line}")
    return "\n".join(out), n


if __name__ == "__main__":
    base = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("intake_out")
    r = intake(Path(sys.argv[1]), base / Path(sys.argv[1]).stem)
    print(json.dumps({k: r[k] for k in
                      ("source", "status", "pages", "lines")}, indent=1))
    for c in r["checks"]:
        mark = {True: "PASS", False: "FLAG", None: "SKIP"}[c["passed"]]
        print(f"  {c['name']} {mark}: {c['detail'][:150]}")
