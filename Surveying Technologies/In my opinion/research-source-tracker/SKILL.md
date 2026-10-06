---
name: research-source-tracker
description: Read PDFs page-accurately and log every source behind a research answer into an Excel workbook (links, page numbers, search keywords, how reliable each source is) together with a summary per topic. Use this whenever the user asks you to search, look up, research, compare or summarize something, to read or pull facts from a PDF, paper, book or standard, or to prepare findings to discuss with them, even if they never mention Excel or sources. Typical Thai cues - หาข้อมูล, ค้นข้อมูล, สรุป, อ่าน pdf, ขอที่มา, ขอลิงก์, แหล่งอ้างอิง, เตรียมสไลด์, ปรึกษา.
---

# Research source tracker

The user (Soravis) is building a presentation on surveying technologies and wants to discuss your findings with you. A finding is only useful to them if they can trace it: where it came from, which page, how it was found, and whether you actually opened it or only remembered it. Earlier in this project they asked "where did that number come from?" and the honest answer was "my own grouping, partly from memory". This skill exists so that question can always be answered by opening one spreadsheet.

So every time you research, read a PDF, or summarize something to discuss with them, do two things: **read sources properly**, and **leave a traceable record in `Research_Sources.xlsx`**. Chat stays short; the workbook carries the detail.

## 1. Reading PDFs

Use `scripts/read_pdf.py` instead of dumping a PDF into context. Textbooks run to hundreds of pages, and a citation without a correct page number is nearly worthless. Run `python scripts/read_pdf.py --help` if you need the options.

Work from cheap to expensive:

1. `info FILE` - page count, whether printed page numbers differ from the file's page index, whether there is a text layer (a scanned PDF needs `render` and visual reading or OCR, and you should say so).
2. `outline FILE` - the bookmarks, to find the right chapter. No bookmarks? Go straight to `search`.
3. `search FILE "term" "another term"` - which pages mention the terms, with snippets. Add `--all` to require every term on the page.
4. `extract FILE --pages 45-52` - read only those pages. Output is capped; follow the continue hint instead of reading everything.
5. `render FILE --pages 45` - when the answer lives in a figure, table or equation, make a PNG and look at it with Read.

Rules that keep the record honest:
- Cite the **printed page** the user will see, and give the PDF index when it differs: `p. 123 (PDF p. 145)`. The tool prints both for every page.
- Only record what you actually read on the page. If search snippets pointed you to a page but you did not extract it, the reliability is "Snippet only".
- If extraction returns little or no text, do not guess the content. Say the page needs OCR or visual reading.
- Read `references/pdf-reading.md` when the PDF is a scanned book, a paper with two columns/tables, or when `search` finds nothing.

## 2. Keeping every source

Log **each** source you used, including PDFs (with page numbers), web pages, papers and standards. Read `references/source-record-guide.md` for the field meanings and a worked example; the essentials:

- **Links come only from what you actually saw** in a search result or fetched page. Never construct a URL, DOI or citation from memory. A link you cannot show is worse than none.
- If a fact comes from your own knowledge with no source opened, log it as `From memory - verify`, leave the link empty, and put a **search key** in `search_keywords` so the user can find the real source. Do not present it as established.
- **Reliability** is one of `Verified - opened`, `Snippet only`, `From memory - verify`, `Unverified`. Be strict: `Verified` means you opened the page/PDF and read the supporting text there.
- Record the **location** inside the source (page, section, table) and a one-line **key info taken**, so the claim can be checked in 30 seconds.
- Record the search queries that worked (and the useful failures) in `searches`. The user wants to learn where and how to search (ResearchGate, Google Scholar, etc.); `references/search-keys.md` has domain tips for writing search keys, including a trap: "survey" alone returns questionnaire papers, so add "geomatics", "land surveying", "geodesy" or the specific technique.
- Where sources disagree (different counts, dates, definitions), say so in the summary rather than silently choosing one.

## 3. The workbook

File name: `Research_Sources.xlsx`, kept in the user's project folder (the "Surveying Technologies" folder they connected). One workbook accumulates across sessions with three sheets:

| Sheet | One row per | Purpose |
|---|---|---|
| Summary | topic discussed | short summary, key points, open questions, linked source IDs |
| Sources | source / page used | link, location, key info, reliability, keywords |
| Search Log | search made | what was searched where, what came back |

Build rows by writing a JSON file (format documented at the top of `scripts/build_sources_xlsx.py`; a filled example is in `assets/example_input.json`) and running:

```
python scripts/build_sources_xlsx.py input.json Research_Sources.xlsx
```

The script creates the workbook or appends to it (IDs continue, duplicates are skipped, links become clickable, reliability is colour-coded) and prints warnings, for example when a "Verified" source has no link or page. Fix the warnings before you hand over.

Getting the file to and from the user's folder:
1. Check whether `Research_Sources.xlsx` already exists there (`device_list_dir`). If it does, stage it (`device_stage_files`), copy it to your working directory, and append to the copy. Appending, not rebuilding, protects what earlier sessions and the user's own edits put in.
2. Write the result back with `device_commit_files`, passing the `mtimeMs` from staging as `expectedMtimeMs` so you do not overwrite an edit the user made in the meantime. If it refuses because the file changed, re-stage and redo the append.
3. If `device_bash` is available, run the script on the folder directly instead.
4. If the computer cannot be reached, send the workbook with `SendUserFile` and say it could not be saved to their folder.

Do not let a long session pass without writing the workbook. Write it at the end of each research or summary turn, so what the user reads in chat is always already in the file.

## 4. What to say in chat

Reply in Thai unless the user writes otherwise. Give the short answer or summary they asked for, flag anything that is `From memory - verify` or in conflict, and mention the workbook in one line (which topics and how many sources were added). End with a "Sources:" list of the links actually used. Do not paste the whole table into chat; that is what the file is for.

## Files in this skill

- `scripts/read_pdf.py` - info / outline / search / extract / render for PDFs
- `scripts/build_sources_xlsx.py` - create or append to the workbook
- `references/pdf-reading.md` - strategies for different kinds of PDF, page-number pitfalls
- `references/source-record-guide.md` - field-by-field guide, reliability levels, example
- `references/search-keys.md` - writing search keys for Google Scholar, ResearchGate and others
- `assets/example_input.json` - a complete input example for the workbook script
