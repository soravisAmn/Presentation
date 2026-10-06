# Reading PDFs: strategies and pitfalls

Read this when the straightforward `info → outline → search → extract` path is not enough.

## Pick the strategy by PDF type

| Type | Signs | Approach |
|---|---|---|
| Textbook / manual (hundreds of pages) | bookmarks exist, many chapters | `outline` for chapter pages, then `search` for the concept, then `extract` only 2-6 pages around the best hits. Prefer the page where the term is *defined* over the page where it is merely used. |
| Journal paper / report | 5-40 pages, abstract first | `extract` the first 2 pages (abstract, intro), then search for "conclusion", "results", "limitations". Note the DOI and year from page 1 for the record. |
| Standard / specification | numbered clauses | search the clause number or exact term; cite clause and page. |
| Slide-deck PDF | little text per page | `extract --layout` or `render`; text order may be scrambled. |
| Scanned PDF | `info` reports a missing text layer | `render` pages and read them visually (Read on the PNG), or OCR with `ocrmypdf` / `pytesseract` if installed. Say plainly that the content came from visual reading. |

## Page-number pitfalls

- A book's **printed** page number and the PDF's **index** usually differ because of front matter. The tool prints both: `PDF p.145 (printed 123)`. Cite the printed number first, as in `p. 123 (PDF p. 145)`, because that is what the user sees in the book and what a bibliography needs.
- If the PDF has no page labels, `info` says printed numbers may still be offset. Extract one page and read the number printed in the header or footer to find the offset, then say which convention you are using.
- `--label` makes `--pages` mean printed page numbers, handy when the user says "look at page 123".

## When search finds nothing

1. Try a stem or synonym ("traverse" vs "traversing", "levelling" vs "leveling", British vs American spelling matters in surveying texts).
2. Search for 2 terms with `--all` to find the page where the concept and its context meet.
3. Run `info`: a thin text layer explains empty results.
4. Run `extract --pages 1-20` to read the printed table of contents and index, then jump by printed page with `--label`.

## Tables, figures and equations

Text extraction flattens tables and drops equations. When a number comes from a table or an equation matters, `render` the page and look at it before quoting. Use `--layout` to keep columns aligned when the text itself is enough.

## Long extracts

`extract` caps output (default 30,000 characters) and tells you how to continue. Read in passes and note what you need as you go; do not try to hold a whole chapter. For something you will cite several times, write the page text to a file with `--out` and search that file.

## What counts as "read"

Only pages you extracted (or rendered and looked at) count as read. If a conclusion rests on a search snippet, log it as `Snippet only`. If a book is large and you read only the relevant section, say which section in `location` rather than implying you read the book.
