# Research audit: recent fertility, GDP, and working-hours graphs

- **Initial audited base:** `0435db26c24ef1228c830fc333999352adae5332`.
- **Final integration base:** `9be353f86c616679ea7efe647b188479e08cf6d3` (`origin/main`, statistics-guide merge).
- **Branch:** `docs/recent-fertility-hours-graphs`.
- **Audited state:** Dirty working tree before the feature commit. New page, two scripts, seven data/provenance files, eight chart files, sidebar/index/cross-links, README, audit-status addition, and reproduction record. Integration with the newer main did not change the audited numerical artifacts.
- **Auditor:** `/root/audit_recent_graphs`, independently delegated with the repository's research-auditor role instructions and audit guide. This report records its returned checks; the author saved it.
- **Date:** 1 November 2026, UTC.
- **Coverage:** All 22 pinned input payloads; all derived records and coverage rows; all four SVGs and four actual PNGs; affected documentation and source-processing dependencies.
- **Verdict:** Archive extraction, joins, metadata transcription, and graph coordinates verified within scope. Original-provider verification remains incomplete. No material project data or graph defect was found in the inspected artifacts.

## Findings, highest severity first

| ID | Severity | Status | Location / claim | Evidence and locator | Required correction or next check |
| --- | --- | --- | --- | --- | --- |
| R-01 | Verification gap | Unverified; disclosed | Public mirror agreement with current official WDI/ILO files | Fresh World Bank API and ILO requests returned proxy tunnel HTTP 403 | Compare pinned copies with original-provider files before claiming original-provider validation |
| R-02 | Verification gap | Unverified; disclosed | ILO point-level survey basis, age coverage, flags, and breaks | Mirror processing discards source identifiers and notes; indicator has no age dimension | Retrieve original observations and metadata before asserting harmonized populations or uninterrupted comparability |
| R-03 | Verification gap | Unverified; disclosed | Exact WPP vintage and each fertility value's estimate/forecast classification | WDI definitions describe estimation/interpolation/extrapolation; flat data lack row classifications | Do not call all values direct measurements or guarantee they are forecast-free |
| R-04 | Verification gap | Unverified; disclosed | Current ILO reuse conditions and subsequent provider corrections | Original-provider pages inaccessible | Check current terms and revisions separately |

These are evidence limits, not demonstrated transcription defects. The page and provenance disclose them. No supported defect required a numerical or graph correction.

## Evidence ledger

All source URLs and SHA-256 hashes are in [the manifest](../../public/data/recent-economy/sources.json).

| Dataset, claim, or graph | Check | Status | Source/version and locator | Method or limitation |
| --- | --- | --- | --- | --- |
| All pinned inputs | URL/file identity and SHA-256 | Verified | Manifest, 22 inputs | Fresh independent retrieval of every payload; all hashes matched |
| WDI snapshot date | Copy dated 14 October 2026 | Verified against repository record | `open-numbers/ddf--world_bank--world_development_indicators`, revision `4252d91d988efc0f116d4fa48e92357b778729e5` | Commit date identifies mirror, not observation date |
| ILO snapshot date | Copy dated 27 February 2026 | Verified against repository record | `open-numbers/ddf--ilo--ilostat`, revision `c4dd68c687df8162835e1684cffec8723b19eee8` | Commit and archived indicator metadata inspected |
| Fertility definition | Period TFR, births per woman | Verified against archived metadata | WDI `SP.DYN.TFRT.IN`, continuous-concepts file | Stored definition matches; not birth count or completed family size |
| GDP definition | GDP/person, constant 2021 PPP international dollars | Verified against archived metadata | WDI `NY.GDP.PCAP.PP.KD` | No new GDP/population division or price conversion performed |
| Hours definition | Mean weekly hours actually worked per employed person | Verified against archived metadata | ILO `HOW_TEMP_SEX_ECO_NB` | Employed persons, not employees only |
| Sex filter | `sex_t` means Total | Verified | Pinned sex dictionary | Exact dictionary inspection |
| Economic-activity filter | `eco_aggregate_total` means Economic activity (Aggregate): Total | Verified | Pinned classif1 dictionary | Exact dictionary inspection |
| ILO source selection | Select country source using metadata ordering, then notes for duplicates | Verified against mirror processing | Pinned `etl/scripts/etl_manual.py`, `create_datapoints()`, and README | Mirror heuristic is not proof of ILO endorsement of source ranking |
| WDI transformation | Normalize country codes, remove missing values, decimal CSV export | Verified against processing code | Pinned WDI `etl/scripts/etl.py` | Original WDICSV bulk file is not retained in inspected mirror |
| Country labels | Twelve declared countries | Verified | Pinned WDI entity definitions | Source country labels retained with project display names |
| Stored metadata | All five sections match source rows | Verified | `indicator-metadata.json` | WDI indicators, ILO indicator, country labels, total-sex and total-sector rows compared |
| Measurement separation | Weekly/annual hours and different PPP bases kept separate | Verified | New page, links, provenance, scripts | No multiplication by 52 or splicing |
| Causal wording | Descriptive associations only | Verified for changed documentation | Page and figure footers | No claim that hours or income cause fertility changes |
| Paper findings | New paper estimates or model replications | Not applicable | No paper or finding summaries changed | Existing literature register not revalidated |

## Independent reconstruction

The auditor reconstructed every expected value and key directly from freshly retrieved source CSVs, without executing the author's writing script.

| Output | Coverage checked | Result |
| --- | --- | --- |
| `country-years.csv` | All 420 rows, labels, fertility/GDP/hours values, and missing cells | Verified |
| `fertility-gdp.csv` | All 420 pairs: twelve countries × 35 years, 1990–2024 | Verified |
| `fertility-hours.csv` | All 190 pairs in the nine-country recent-hours subset | Verified |
| `coverage.csv` | All twelve rows: dates, counts, endpoint hours, inclusion flags | Verified |
| `indicator-metadata.json` | All five stored metadata sections | Verified |
| `provenance.json` | Manifest, countries, recent-country subset, and counts | Verified |

The all-country extract has 233 non-missing weekly-hours values inside 2000–2024, of which 190 belong to the recent-hours sample:

- United States: 22 years, 2003–2024.
- United Kingdom, France, Germany, South Korea, South Africa: 25 years each, 2000–2024.
- India: seven years, 2018–2024.
- Brazil: thirteen years, 2012–2024.
- Mexico: 23 years, 2002–2024.

These selected windows are consecutive. Excluded countries remain accurately listed: Australia has 21 years, 2000–2020; Japan has eleven years, 2009–2020, missing 2011; China has eleven years, 2005–2016, missing 2015.

The GDP comparison uses a separate fertility/GDP join. Missing hours do not remove GDP estimates. The project adds no interpolation, weighting, imputation, zero filling, or extrapolation.

The checked 2024 weekly-hours endpoints, in the country's plotted order, are 37.56, 35.08, 35.49, 33.27, 37.88, 45.72, 38.86, 42.19, and 42.39. The coverage table keeps two decimals; the trend figure correctly rounds to one.

## Graph-coordinate and visual checks

The auditor parsed actual SVG line vertices and marker positions and compared them with independently transformed CSV values using each displayed scale and plotting rectangle.

| Figure | Actual graphical elements checked | Result |
| --- | --- | --- |
| `fertility-gdp.svg` | All 420 line vertices, 420 scatter positions/year colours, twelve titles | Verified |
| `fertility-hours.svg` | All 190 line vertices, 190 scatter positions/year colours, nine titles | Verified |
| `working-hours.svg` | All 190 line vertices and 190 markers | Verified |
| `country-time-paths.svg` | All 279 line vertices and 279 markers across twelve panels | Verified |

Maximum coordinate differences are approximately 1.05 × 10⁻⁶ SVG units, consistent with six-decimal coordinate serialization. All selected values lie within the axes.

The auditor viewed all four actual PNGs. Titles, endpoints, scales, colour bars, separate time-series units, and source footers are legible. No clipping or material overlap was found. All SVGs/PNGs visibly identify retrieval location, date, and descriptive scope; SVG source labels link to pinned inputs, and hours-panel titles link to country CSVs.

## Reproduction

The author ran collation with fresh downloads and plotting in `/tmp/recent-economics/reproduction`. The auditor independently compared all 18 comparison files with the working tree: all were byte-identical.

- Fourteen generated outputs: six data/metadata/provenance files and eight charts.
- Four additional comparison files: source manifest, two scripts, and regenerated-coverage page.
- [Reproduction hashes and results](2026-11-01-recent-economy-reproduction.json).

Script execution was parent-run. The auditor independently retrieved sources, checked hashes, reconstructed extraction/joins, inspected metadata and processing code, checked SVG coordinates/colours, viewed images, and compared the isolated outputs. Those tasks are distinct from running the author's scripts.

After integrating the newer main, the parent ran `ASTRO_TELEMETRY_DISABLED=1 npm run build`: 25 pages built successfully. Its HTML checker passed all 1,636 local link/image/anchor references and checked all 15 new public assets against their built copies. All images have text alternatives. `git diff --check` passed. The auditor did not independently rerun the site build or HTML checker. Live Vercel/mobile checks were not run.

## Unverified and unrun checks

Fresh original-provider requests failed with proxy tunnel HTTP 403:

- World Bank API, USA `SP.DYN.TFRT.IN`.
- World Bank API, USA `NY.GDP.PCAP.PP.KD`.
- ILO Rplumber API, USA `HOW_TEMP_SEX_ECO_NB`, total sex/activity.
- ILOSTAT working-time topic page.

Agreement with current original-provider downloads, ILO row flags/sources/age coverage/breaks, exact WPP vintage/classification, subsequent corrections, current ILO reuse terms, causal identification, paper replication, live Vercel behavior, and mobile presentation remain unverified.

## Final integration and recheck requirements

The final branch includes main's statistics-guide merge. Its README conflict was resolved by retaining both guides; sidebar and fertility-page changes merged together. No source, selected value, generated dataset, or chart changed during integration. The auditor independently rechecked the final documentation diff and audit-status summary against the new base, confirmed both guides and correct links, and found no integration defect. It re-compared all eighteen audited files with the isolated outputs and confirmed they remained byte-identical.

The final staged check found generated CSV CRLF line endings and SVG trailing spaces. The generators now write LF CSVs and trim SVG line whitespace. The auditor compared all eight files against their previous committed contents after independent whitespace normalization, confirmed both script changes affect formatting only, and verified all four PNGs remain byte-identical. A fresh isolated run of the final scripts again matched all eighteen comparison files; the auditor independently checked every updated hash. The numerical and visual checks remain applicable. The final build, 1,636 internal-reference checks, 15 asset comparisons, and complete diff whitespace check passed after this correction.

Recheck any subsequent numerical, source, selection, axis, caption, or plotting change. This report establishes consistency with pinned public mirrors within the stated scope, not complete verification of original-provider data or scientific findings.
