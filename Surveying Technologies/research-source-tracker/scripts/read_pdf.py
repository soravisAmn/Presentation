#!/usr/bin/env python3
"""Page-accurate PDF reader for research work.

Why this exists: large PDFs (textbooks, standards, theses) cannot be pasted into
context, and a citation is only useful if it points to the right page. This tool
lets you look around a PDF cheaply (info / outline / search) and then read only
the pages you need (extract), always reporting both the PDF page index and the
printed page label, so the page number you cite is the page the user will see.

Commands
  info    FILE                         pages, metadata, page labels, text-layer check
  outline FILE [--depth N]             bookmarks / table of contents with page numbers
  search  FILE TERM [TERM ...]         which pages mention the terms, with snippets
  extract FILE --pages 45-52,60        text of selected pages (with page headers)
  render  FILE --pages 45 [--dpi 110]  PNG of pages, for figures/tables/equations

Page numbers: by default --pages means PDF page index (1 = first page of the file).
Add --label to mean the printed page label instead (what the book itself prints).

Dependencies: pypdf (required), pdftotext/pdftoppm from poppler (recommended, faster).
Text is extracted once and cached in the system temp dir, so repeated searches on a
big file are fast.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


# ----------------------------------------------------------------- PDF access
def open_reader(pdf):
    try:
        from pypdf import PdfReader
    except ImportError:
        die("pypdf is not installed. Run: pip install pypdf --break-system-packages")
    if not os.path.isfile(pdf):
        die(f"file not found: {pdf}")
    try:
        reader = PdfReader(pdf, strict=False)
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                die("PDF is password-protected; ask the user for the password or an unlocked copy")
        return reader
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        die(f"cannot open PDF: {e}")


def page_labels(reader):
    n = len(reader.pages)
    try:
        labels = [str(x) for x in reader.page_labels]
        if len(labels) == n:
            return labels
    except Exception:  # noqa: BLE001
        pass
    return [str(i + 1) for i in range(n)]


def _cache_file(pdf, layout):
    st = os.stat(pdf)
    key = f"{os.path.abspath(pdf)}|{st.st_size}|{int(st.st_mtime)}|{layout}"
    h = hashlib.sha1(key.encode()).hexdigest()[:16]
    d = os.path.join(tempfile.gettempdir(), "pdf_text_cache")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, h + ".txt")


def load_pages(pdf, n_pages, layout=False):
    """Return a list of page texts; index 0 is PDF page 1."""
    cache = _cache_file(pdf, layout)
    if not os.path.exists(cache):
        tmp = cache + ".part"
        if shutil.which("pdftotext"):
            cmd = ["pdftotext", "-enc", "UTF-8"] + (["-layout"] if layout else []) + [pdf, tmp]
            p = subprocess.run(cmd, capture_output=True, text=True)
            if p.returncode != 0:
                die(f"pdftotext failed: {p.stderr.strip()[:300]}")
        else:
            reader = open_reader(pdf)
            parts = []
            for pg in reader.pages:
                try:
                    parts.append(pg.extract_text() or "")
                except Exception:  # noqa: BLE001
                    parts.append("")
            with open(tmp, "w", encoding="utf-8") as f:
                f.write("\f".join(parts) + "\f")
        os.replace(tmp, cache)
    with open(cache, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    pages = raw.split("\f")
    if pages and pages[-1] == "":
        pages.pop()
    return (pages + [""] * n_pages)[:n_pages]


def parse_pages(spec, n, labels=None):
    """'3-5,9' -> [3,4,5,9] (PDF indexes). With labels, tokens are printed labels."""
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            a = int(a) if a.strip() else 1
            b = int(b) if b.strip() else (n if labels is None else int(labels[-1]) if labels[-1].isdigit() else n)
        else:
            a = b = int(part)
        if a > b:
            die(f"bad page range: {part}")
        if labels is None:
            if a < 1 or b > n:
                die(f"page range {part} outside 1-{n}")
            out.extend(range(a, b + 1))
        else:
            for v in range(a, b + 1):
                if str(v) in labels:
                    out.append(labels.index(str(v)) + 1)
                else:
                    print(f"warning: printed page '{v}' not found, skipped", file=sys.stderr)
    return out


def clean(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def page_tag(i, labels):
    lab = labels[i - 1]
    return f"PDF p.{i}" + (f" (printed {lab})" if lab != str(i) else "")


# ------------------------------------------------------------------- commands
def cmd_info(a):
    reader = open_reader(a.file)
    n = len(reader.pages)
    labels = page_labels(reader)
    meta = reader.metadata or {}
    print(f"File: {os.path.basename(a.file)}  ({os.path.getsize(a.file) / 1e6:.1f} MB)")
    print(f"Pages: {n}")
    for k in ("title", "author", "subject", "creation_date"):
        v = getattr(meta, k, None)
        if v:
            print(f"{k.replace('_', ' ').title()}: {v}")

    differs = [i for i, l in enumerate(labels, 1) if l != str(i)]
    if differs:
        print(f"Printed page labels differ from PDF index (e.g. PDF p.{differs[0]} = '{labels[differs[0] - 1]}'). "
              "Cite the printed label and mention the PDF index too.")
    else:
        print("Page labels: none defined, printed numbers may still be offset from the PDF index "
              "(check a page with `extract` to see the printed number).")

    try:
        has_outline = bool(reader.outline)
    except Exception:  # noqa: BLE001
        has_outline = False
    print(f"Bookmarks/outline: {'yes -> run `outline`' if has_outline else 'none -> use `search`'}")

    # text-layer check on a spread of pages (cheap, does not extract the whole file)
    step = max(1, n // 12)
    sample = list(range(0, n, step))[:12]
    chars = []
    for i in sample:
        try:
            chars.append(len((reader.pages[i].extract_text() or "").strip()))
        except Exception:  # noqa: BLE001
            chars.append(0)
    avg = sum(chars) / max(1, len(chars))
    if avg < 80:
        print(f"Text layer: MISSING or very thin (avg {avg:.0f} chars/page over {len(sample)} sampled pages). "
              "Likely a scanned PDF: render pages and read them visually, or OCR (ocrmypdf / pytesseract).")
    else:
        print(f"Text layer: OK (avg {avg:.0f} chars/page over {len(sample)} sampled pages)")


def cmd_outline(a):
    reader = open_reader(a.file)
    labels = page_labels(reader)
    out = []

    def walk(items, depth):
        for it in items:
            if isinstance(it, list):
                walk(it, depth + 1)
                continue
            try:
                pn = reader.get_destination_page_number(it) + 1
            except Exception:  # noqa: BLE001
                pn = None
            out.append((depth, str(getattr(it, "title", it)).strip(), pn))

    try:
        walk(reader.outline, 0)
    except Exception as e:  # noqa: BLE001
        die(f"could not read outline: {e}")
    if not out:
        print("No bookmarks in this PDF. Use `search` with topic keywords, or `extract` the first pages "
              "(the printed table of contents is usually within the first 15-20 pages).")
        return
    for depth, title, pn in out:
        if depth > a.depth:
            continue
        loc = page_tag(pn, labels) if pn else "p.?"
        print(f"{'  ' * depth}- {title}  [{loc}]")


def cmd_search(a):
    reader = open_reader(a.file)
    n = len(reader.pages)
    labels = page_labels(reader)
    pages = load_pages(a.file, n, a.layout)
    pats = {t: re.compile(r"\s+".join(re.escape(w) for w in t.split()), re.I) for t in a.terms}

    rows = []
    totals = {t: [0, 0] for t in a.terms}  # hits, pages
    for i, text in enumerate(pages, 1):
        counts = {t: len(p.findall(text)) for t, p in pats.items()}
        if a.all and not all(counts.values()):
            continue
        if not any(counts.values()):
            continue
        for t, c in counts.items():
            if c:
                totals[t][0] += c
                totals[t][1] += 1
        rows.append((i, counts, text))

    rows.sort(key=lambda r: (-sum(r[1].values()), r[0]))
    top = rows[: a.top]

    def snippet(text, pat):
        m = pat.search(text)
        if not m:
            return ""
        s = max(0, m.start() - a.context)
        e = min(len(text), m.end() + a.context)
        return re.sub(r"\s+", " ", text[s:e]).strip()

    if a.json:
        print(json.dumps({
            "file": os.path.basename(a.file),
            "terms": a.terms,
            "totals": {t: {"hits": h, "pages": p} for t, (h, p) in totals.items()},
            "top_pages": [{
                "pdf_page": i, "printed_page": labels[i - 1],
                "counts": counts,
                "snippet": snippet(text, next(p for t, p in pats.items() if counts[t])),
            } for i, counts, text in top],
        }, ensure_ascii=False, indent=2))
        return

    print(f"Search in {os.path.basename(a.file)} ({n} pages) for: " + ", ".join(f"'{t}'" for t in a.terms))
    for t, (h, p) in totals.items():
        print(f"  '{t}': {h} hits on {p} pages")
    if not rows:
        print("No hits. Try a synonym, a shorter stem, or check the text layer with `info`.")
        return
    print(f"\nTop {len(top)} pages (most hits first). Read them with: extract FILE --pages N\n")
    for i, counts, text in top:
        summary = ", ".join(f"{t} x{c}" for t, c in counts.items() if c)
        first = next(p for t, p in pats.items() if counts[t])
        print(f"- {page_tag(i, labels)}: {summary}")
        print(f"    ...{snippet(text, first)}...")


def cmd_extract(a):
    reader = open_reader(a.file)
    n = len(reader.pages)
    labels = page_labels(reader)
    idxs = parse_pages(a.pages, n, labels if a.label else None)
    if not idxs:
        die("no pages selected")
    pages = load_pages(a.file, n, a.layout)
    blocks = [f"===== {page_tag(i, labels)} =====\n{clean(pages[i - 1]) or '[no extractable text on this page - try `render`]'}"
              for i in idxs]
    full = "\n\n".join(blocks)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(full)
        print(f"wrote {len(idxs)} pages ({len(full)} chars) to {a.out}")
        return
    if len(full) > a.max_chars:
        cut = full[: a.max_chars]
        last = cut.rfind("\n=====")
        if last > 0:
            shown = cut[:last]
            done = shown.count("===== PDF p.")
            print(shown)
            print(f"\n[truncated after {done} of {len(idxs)} pages (cap {a.max_chars} chars); "
                  f"continue with --pages {idxs[done]}-{idxs[-1]}, or raise --max-chars / use --out]")
        else:  # the very first page alone is longer than the cap
            print(cut)
            print(f"\n[page text cut at {a.max_chars} chars; raise --max-chars or use --out to see all of it]")
    else:
        print(full)


def cmd_render(a):
    if not shutil.which("pdftoppm"):
        die("pdftoppm (poppler-utils) not found; cannot render pages")
    reader = open_reader(a.file)
    n = len(reader.pages)
    labels = page_labels(reader)
    idxs = parse_pages(a.pages, n, labels if a.label else None)
    os.makedirs(a.outdir, exist_ok=True)
    stem = re.sub(r"[^A-Za-z0-9_-]+", "_", os.path.splitext(os.path.basename(a.file))[0])[:40]
    for i in idxs:
        prefix = os.path.join(a.outdir, f"{stem}_p{i}")
        p = subprocess.run(["pdftoppm", "-f", str(i), "-l", str(i), "-r", str(a.dpi), "-png", "-singlefile",
                            a.file, prefix], capture_output=True, text=True)
        if p.returncode != 0:
            die(f"pdftoppm failed on page {i}: {p.stderr.strip()[:200]}")
        print(f"{prefix}.png   ({page_tag(i, labels)})")
    print("Open the PNG with the Read tool to look at figures, tables or equations.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("info"); p.add_argument("file"); p.set_defaults(fn=cmd_info)

    p = sub.add_parser("outline"); p.add_argument("file")
    p.add_argument("--depth", type=int, default=1, help="deepest bookmark level to show (0 = top only)")
    p.set_defaults(fn=cmd_outline)

    p = sub.add_parser("search"); p.add_argument("file"); p.add_argument("terms", nargs="+")
    p.add_argument("--all", action="store_true", help="only pages containing ALL terms")
    p.add_argument("--top", type=int, default=15, help="how many pages to list")
    p.add_argument("--context", type=int, default=110, help="snippet characters on each side")
    p.add_argument("--layout", action="store_true", help="keep physical layout (columns/tables)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_search)

    p = sub.add_parser("extract"); p.add_argument("file")
    p.add_argument("--pages", required=True, help="e.g. 45-52,60")
    p.add_argument("--label", action="store_true", help="treat --pages as printed page labels")
    p.add_argument("--layout", action="store_true")
    p.add_argument("--max-chars", type=int, default=30000)
    p.add_argument("--out", help="write full text to this file instead of printing")
    p.set_defaults(fn=cmd_extract)

    p = sub.add_parser("render"); p.add_argument("file")
    p.add_argument("--pages", required=True)
    p.add_argument("--label", action="store_true")
    p.add_argument("--dpi", type=int, default=110)
    p.add_argument("--outdir", default=os.path.join(tempfile.gettempdir(), "pdf_renders"))
    p.set_defaults(fn=cmd_render)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
