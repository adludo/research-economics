# Research audit: fertility, GDP, and working-hours graphs

- Target: new graph collection on `docs/fertility-country-charts`, working tree based on `1ddbbda36208728e757d727bcbf10298ee3c3ec8`.
- Date: 1 November 2026, UTC.
- Independent auditor: `/root/audit_hours_graphs`, following `research_auditor` instructions.
- Scope: collation/plotting scripts, archived source inputs, complete/selected panels, endpoint table, three SVG/PNG figures, source footers and interpretation.
- Verdict: **archive extraction, computations and plotted values verified within the inspected scope; source-version label discrepancy corrected before publication. Original-provider agreement and causal claims remain unverified.**

## Material issue found and corrected

The OWID archive folder and metadata identify the PWT input as version10.0. An additional main-agent comparison against CRAN-distributed `pwt10.0.rda` found GDP differences. The independent auditor freshly retrieved the CRAN files, confirmed the discrepancy, and compared the matched panel with `pwt10.01.rda`.

All **2,517 GDP/person and hours observations** match the CRAN-distributed PWT10.01 data at relative tolerance `1e-10`; maximum absolute differences are approximately `1.46e-11` GDP/person and `9.09e-13` hours. GDP/person differs from PWT10.0 throughout this matched panel. Hours agree across these distributed versions.

The original OWID metadata, folder names, URLs and numeric values were preserved. Every new graph now says the archive is labelled10.0 and its matched values agree with CRAN10.01. The codebook cross-check uses10.01. The [comparison record](../../public/data/fertility-economy/pwt-vintage-check.json) includes both R-data URLs/hashes and six explicit aliases used only for that external check. The graph-input join still uses exact OWID names without aliases.

This is a cross-distribution consistency check, not a retrieval from the official PWT provider. It supersedes the initial inspection's unqualified PWT10.0 label; the numerical extraction and geometry checks themselves remain valid.

## Verified data checks

| Item | Independently checked result |
| --- | --- |
| Source identity | Five pinned payloads retrieved and SHA-256 checked: fertility CSV/metadata, PWT CSV/metadata, and the final CRAN PWT10.01 codebook |
| Fertility interpretation | Period TFR, births per woman; not birth counts, crude birth rate, or completed family size |
| Forecast cutoff | Gapminder v12 metadata identifies2015 onward as forecasts; every retained row is1970–2014 |
| Existing interpolation | Source metadata describes annual interpolation in the historical series; page discloses this; no interpolation added by this project |
| Same-year join | Exact entity and year; all measures required, unique keys, positive finite values, no missing-value filling |
| Complete panel | All 2,517 records across 67 economies independently reconstructed |
| Plotted panel | All 509 records across 12 economies independently selected and compared |
| Exclusions | 1,061 eligible-window PWT rows lack fertility; a further 5,780 lack GDP/population/hours after fertility was available |
| GDP/person | Archived GDP divided by archived population; both are absolute units, so no million multiplier is applied |
| PWT cross-distribution check | All matched GDP/person and hours values agree with CRAN10.01; GDP/population quantities are consistent with the documented2017 PPP units |
| Endpoints | All 12 country rows, dates, counts and six endpoint values match full-precision records and displayed rounding |
| Selected coverage | Eleven countries have 45 consecutive years,1970–2014; South Africa has 14 consecutive years,2001–2014 |

The complete-case restriction applies even to the GDP-only relationship figure, so it uses the same sample as the hours figure. This omits early South African fertility/GDP observations where hours are missing; it does not imply those two measures are unavailable. The selection is illustrative, not representative or a world average.

## Verified graph checks

The auditor inspected actual SVG geometry rather than treating plotting code or a build as proof. It also viewed all three PNGs.

| Graph | Independent coordinate/visual checks |
| --- | --- |
| Fertility vs GDP/person |509 scatter coordinates and509 line vertices; calendar-year colours; first/last-year labels; common logarithmic GDP axis1000–100000; TFR0–7 |
| Fertility vs hours |509 scatter coordinates and509 line vertices; year colours/labels; common linear hours axis0–3200; TFR0–7 |
| Four-country time paths |540 vertices across 12 panels; consistent year axis and scales within each measure; logarithmic GDP and linear fertility/hours; separate units, no dual-axis inference |
| Missing years | Connections restricted to consecutive retained years; no invented rows or lines spanning absent interior years |
| Clipping | None of the selected input values is outside the declared limits |
| Source references | Each SVG and PNG visibly names the sources, pinned archive URL, retrieval date, historical window, forecast exclusion and non-causal interpretation; SVG labels link to the exact two CSV inputs |

Initial geometry errors were below `2e-6` SVG coordinate units. Numeric data were not changed by the source-label correction. The auditor completed the final recheck: numeric CSVs and plot-axes XML groups were unchanged, final source labels and links were correct, all final PNGs were freshly inspected, the10.01 codebook matched its new hash, and the17 reproduction files matched independently. The corrected source-version attribution issue is resolved within this distributed-copy scope.

Selected input ranges: TFR 1.16–6.83; GDP/person approximately 1,166.17–57,116.95 international dollars; annual worker hours approximately 1,396.46–2,918.93. These are sample ranges, not worldwide bounds.

## Reproduction

The main agent ran both final scripts in an isolated writable copy, leaving repository inputs untouched:

```sh
python3 /tmp/fertility-charts/reproduction-final/scripts/collate-fertility-economy.py
python3 /tmp/fertility-charts/reproduction-final/scripts/plot-fertility-economy.py
```

All 17 compared files were byte-identical on this retrieval date, including CSVs, metadata, codebook, page, provenance, version-comparison record, scripts and all SVG/PNG exports. See the [comparison record](2026-11-01-fertility-charts-reproduction.json). On a later date, retrieval-date fields and figure footers can change without changes to the underlying observations.

Script execution was main-agent work. The auditor's independent source downloads, in-memory reconstruction, arithmetic, CRAN comparison, SVG geometry and image inspection are separate checks.

## Original sources and interpretation still pending

Fresh original Gapminder and PWT provider requests returned proxy tunnelHTTP 403. Not established:

- Agreement with original Gapminder/UN/PWT release files, current revisions or corrections.
- Full original-provider/OWID reuse conditions; an accessible archive is not proof of unrestricted rights.
- An official-provider explanation for the archive version label; the observed cross-distribution match is documented instead.
- Causal effects of income, working hours, childcare or leisure on fertility.
- Replication of the linked structural or empirical fertility papers.
- Live Vercel/mobile behaviour.

TFR, national average market-worker hours, mothers' own hours, childcare, leisure, GDP/person and hourly productivity are kept distinct. The new figures show descriptive country paths, not fitted effects or policy prescriptions.

## Technical checks

The production build passed with 23 generated HTML pages and search assets. All 1,256 internal links, images and anchors passed; published chart/data downloads matched repository files exactly. Source footers were independently rechecked. Existing optional i18n/404 and sitemap warnings remain. These checks do not establish scientific causation or official-provider identity.
