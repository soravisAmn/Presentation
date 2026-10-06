# Writing search keys

The user wants to find literature themselves (ResearchGate, Google Scholar, ...) as well as have you search. When you give search keys, give ones that actually work, and log them in the Search Log.

## Anatomy of a good key

`"exact phrase"` + `OR` synonyms + a scope word + (optional) a source filter.

- **Quotes** keep a phrase together: `"network RTK"`.
- **OR** (capitals) covers synonyms: `"UAV" OR "drone" OR "unmanned aerial"`.
- **Minus** removes noise: `-questionnaire`.
- **site:** limits Google/Web search to one domain: `site:fig.net`, `site:iso.org`, `site:ngs.noaa.gov`.
- **filetype:pdf** finds papers, reports and slide decks: `filetype:pdf`.

## The "survey" trap

In this field "survey" collides with questionnaire/opinion surveys, and review papers are also called "survey papers". Always anchor with a domain word: `geomatics`, `land surveying`, `geodesy`, `photogrammetry`, `GNSS`, `LiDAR`, `hydrographic`, or the specific technique. Prefer `engineering surveying` over `survey engineering`.

## Where to search and what each is good for

| Place | Good for | Tips |
|---|---|---|
| Google Scholar | broad academic coverage, citation counts | use "Since 20XX" for recent work; "Cited by" to walk forward from a good paper; "Related articles" |
| ResearchGate | author-posted full texts, asking authors | search by phrase, then filter to Publications; many items are preprints, check the journal version |
| Scopus / Web of Science (if the university offers access) | systematic, filterable lists | search within Title-Abstract-Keywords; filter document type to Review |
| ScienceDirect, MDPI (Remote Sensing, Sensors), IEEE Xplore, Taylor & Francis | publisher full texts | MDPI is open access, useful for current trend papers |
| FIG (fig.net) | profession-level overview, working group publications | commission pages list working groups and publications |
| ISPRS (isprs.org) | photogrammetry, remote sensing, spatial information | congress proceedings, technical commission pages |
| IAG, IGS, UN-GGIM | geodesy, GNSS reference frames | for authoritative definitions of systems and datums |
| IHO | hydrography standards (S-44 etc.) | for survey-order accuracy standards, check the current edition |

## Finding the three kinds of material you need for slides

1. **Foundations and principles**: textbooks and course material. `"geomatics" textbook`, `"elementary surveying"`, `ASPRS Manual of Photogrammetry`. Look at table-of-contents pages.
2. **Current technology state**: review papers. `"review" OR "state of the art" GNSS "PPP-RTK"`, then filter to the last 3-5 years.
3. **Trends**: roadmaps and recent conference papers. `"roadmap" OR "future" geospatial`, FIG Working Week and ISPRS Congress proceedings, national mapping agency reports.

## Examples by topic (adapt, then log what they return)

```
GNSS / positioning      "PPP-RTK" OR "network RTK" review GNSS positioning
Reference frames        "ITRF" OR "height reference frame" geodesy site:fig.net
Photogrammetry / UAV    "UAV photogrammetry" accuracy review "ground control points"
LiDAR / scanning        "terrestrial laser scanning" OR "mobile mapping" review
InSAR / monitoring      InSAR "ground subsidence" monitoring review
Hydrographic            "multibeam echosounder" OR "unmanned surface vessel" hydrographic survey
Digital twin / BIM-GIS  "BIM GIS integration" OR "digital twin" geospatial review
AI in surveying         "deep learning" "point cloud" classification survey review
```

## Record keeping

For every key you try, add a Search Log row: exact text, where it was typed, what came back, and whether it was useful. If a source is found through it, copy the key into that source's `search_keywords`, so the user can repeat the search.
