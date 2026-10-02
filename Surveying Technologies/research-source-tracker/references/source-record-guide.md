# Source record guide

How to fill each field so the Excel record answers "where did this come from, and can I trust it?" in 30 seconds. The JSON format is defined at the top of `scripts/build_sources_xlsx.py`; a full example is `assets/example_input.json`.

## Sources sheet fields

| Field | What to put | Notes |
|---|---|---|
| `ref` | short nickname, e.g. `fig-c5` | only used so a summary can point at this source; the script assigns the real ID (S001, S002, ...) |
| `topic` | the presentation topic this supports | use the same wording across rows so the user can filter |
| `title` | exact title of the page/paper/book/chapter | copy it, do not paraphrase |
| `type` | Web page, Org website, Journal paper, Book/PDF, Standard, Dataset, Other | |
| `author` | person or organisation | |
| `year` | publication or last-updated year if shown | leave empty rather than guess |
| `url` | the link you actually saw | never build it from memory; for local PDFs leave empty and give the file name in `location` |
| `doi` | DOI if the source shows one | the script turns it into a link when `url` is empty |
| `location` | page, chapter, section, table | PDFs: `p. 123 (PDF p. 145), ch. 8` |
| `key_info` | one or two lines: what was taken from here | so the claim can be re-checked quickly |
| `reliability` | see below | be strict |
| `accessed` | date you opened it | defaults to today |
| `search_keywords` | the query that found it, or a query that would | essential for `From memory` rows |
| `notes` | caveats, conflicts with other sources, edition/version | |

## Reliability levels

- **Verified - opened**: you opened the page or PDF and read the supporting text there. Needs a link or a location.
- **Snippet only**: you saw it in a search-result snippet or abstract but did not open the full text. Fine for leads, say so.
- **From memory - verify**: recalled from background knowledge with nothing opened. No link. Always give `search_keywords` so the user can find the real source, and phrase the chat answer with the appropriate hedge.
- **Unverified**: anything else, such as a secondary site repeating a claim you could not trace.

Why this strictness matters: the user will put these facts on slides. A "From memory" fact that looks like a verified one is how a wrong number reaches an audience.

## Summary sheet fields

- `topic`: matches the Sources topics.
- `summary`: 2-5 sentences, plain language, what the user needs to know for the discussion.
- `key_points`: list of short statements (the script formats bullets).
- `open_questions`: what is unresolved, conflicting, or needs a better source; and decisions the user must make.
- `source_refs`: the `ref`s (or existing IDs like `S004`) that support the summary. Every summary should link to at least one source; the script warns when it does not.

## Search Log fields

`query` (exact text typed), `where` (Web search, Google Scholar, ResearchGate, Scopus, PDF search, ...), `result` (what came back, whether useful, what to try next), `url` (results page if it is stable). Log failures too; "no useful results, too many questionnaire papers" saves the next session time.

## Worked example (one topic)

```json
{
  "summaries": [{
    "topic": "FIG commissions",
    "summary": "FIG's technical work is organised into ten commissions. Commissions 3-6 and 10 are the technical ones relevant to survey technology.",
    "key_points": ["Commission 5: Positioning and Measurement", "Commission 6: Engineering Surveys"],
    "open_questions": ["Do we organise the slides by FIG commission or by technology?"],
    "source_refs": ["fig-comm"]
  }],
  "sources": [{
    "ref": "fig-comm",
    "topic": "FIG commissions",
    "title": "FIG Commissions",
    "type": "Org website",
    "author": "FIG",
    "url": "https://www.fig.net/organisation/comm/index.asp",
    "location": "main page",
    "key_info": "States that FIG's technical work is led by ten commissions.",
    "reliability": "Verified - opened",
    "search_keywords": "FIG commissions site:fig.net"
  }]
}
```

## Citing inside chat answers

Short form is enough, since the workbook has the details: `(Ghilani & Wolf, Elementary Surveying, p. 123 (PDF p. 145))` or `(FIG, Commission 5 page, S002)`. Using the S-ID lets the user jump to the row.
