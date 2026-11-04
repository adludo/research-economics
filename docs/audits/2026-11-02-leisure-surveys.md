# Research audit: leisure-source section figures

- **Audited base:** `c51e7034496c133e27020d486c71883a4cf06f0f`.
- **Branch:** `docs/leisure-survey-graphs`.
- **State:** Dirty working tree before the feature commit.
- **Auditor:** `/root/audit_leisure_surveys`, independently delegated with the repository research-auditor instructions and audit guide. The author saved this record of the auditor's returned checks.
- **Date:** 2 November 2026, UTC.
- **Coverage:** Two scripts, thirteen data/specification/provenance files, seven SVGs and seven actual PNGs, leisure-page and README additions. The audit-status summary received a final documentation recheck. The two previously published leisure graphs were outside the changed numerical scope.
- **Verdict:** Extraction, metadata transcription, plotted coordinates, and presentation verified against the pinned archive within scope. No material implementation defect found. Original-provider agreement remains unverified. AHTUS/OECD visuals are conceptual diagrams, not empirical graphs.

## Findings, highest severity first

| ID | Severity | Status | Location / claim | Evidence and locator | Required next check |
| --- | --- | --- | --- | --- | --- |
| L-01 | Verification limit | Unverified; disclosed | Agreement with original releases and paper tables | Seven original-source requests returned HTTP 403 | Compare archived extracts with original releases before claiming original-source validation |
| L-02 | Verification limit | Unverified; disclosed | AHTUS release-specific workflow and OECD definitions | No numerical extracts retrieved; provider pages inaccessible | Inspect current provider documentation; diagrams are authored reading aids, not official specifications |
| L-03 | Verification limit | Unverified; disclosed | ATUS 80/85 age coding | Archive supplies labels but not exact top-code/age-band interpretation | Verify original coding; retain uncertainty |
| L-04 | Verification limit | Unverified; disclosed | Common ages, exact HETUS fieldwork dates, historical sample exclusions | Inspected metadata does not establish these details | Retrieve original survey/working-paper documentation |
| L-05 | Verification limit | Unverified; disclosed | Current releases, corrections and reuse conditions | Original sources inaccessible | Check separately before broader reuse |

These are evidence limits, not demonstrated extraction defects. No supported implementation defect required correction during the independent review. Before that review, the author corrected initial diagram title overlap and box clipping and inspected the resulting figures.

## Evidence ledger

All exact retrieval URLs and SHA-256 hashes are in [the manifest](../../public/data/leisure-surveys/sources.json), pinned to OWID revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`.

| Material | Check | Status | Evidence / method |
| --- | --- | --- | --- |
| Ten inputs | File identity and SHA-256 | Verified | Independent fresh retrieval of every manifest URL; all hashes matched |
| Five stored metadata files | Exact preservation | Verified | Retrieved JSON bytes compared with stored files |
| ATUS interpretation | Pooled 2009–2019 social context; population weighting, overlap, sleep excluded | Verified against archived metadata | `atus.json`; not total leisure or longitudinal aging paths |
| ATUS age field | `Year` encodes respondent age | Verified against archive fields/data | Labels 15–80 and 85; absent 81–84 remain unconnected |
| AHTUS diagram | Authored conceptual workflow without quantities | Verified as presentation/specification | Diagram JSON, code, SVG/PNG and page agree; provider-specific workflow remains unverified |
| MTUS processing | Positive-report averaging and normalization prevent summing an ordinary population leisure budget | Verified against archived metadata | `mtus.json`; plot correctly uses coverage instead |
| MTUS population | Ages 21–65 in this processed extract | Verified against archived metadata | Not asserted for the full current catalogue |
| HETUS measure | Population Time spent leisure/social/associative life | Verified | Correct column; participation-time/rate columns excluded |
| HETUS interpretation | Wave labels, normalization, institutional-population exclusion | Verified against archived metadata | No claim of common fieldwork year; no second normalization |
| OECD diagram | Five broad groups without quantities/shares | Verified as presentation/specification | Box sizes explicitly nonquantitative; current official definitions remain unverified |
| Finland attribution | Statistics Finland, separate from the retained Japanese example | Verified against metadata and prose | Finnish data are not labelled Japanese |
| Finland free time | Supplied all/men/women series and definition | Verified against archived metadata | Leisure travel included; age coverage remains unspecified |
| Historical measures | Four supplied All individuals definitions | Verified against field metadata | Recreational childcare in measure 1; broader definitions and 2003 coding discontinuity disclosed |
| Historical version | Archive attributed to Aguiar–Hurst 2006 working paper | Verified as archive attribution | Not a current AHTUS extract, Ramey reconstruction, or final 2007 paper replication |
| Causal interpretation | Descriptive only | Verified for changed material | No causal effect or model replication asserted |
| Original paper results/tables | Primary-text support | Unverified | Working paper inaccessible; no new primary-paper verification claimed |

## Independent reconstruction

The auditor rebuilt expected records from freshly retrieved upstream CSVs without executing the author's collation script.

| Extract | Records checked | Result |
| --- | ---: | --- |
| `atus-social-time.csv` | 402: 67 age codes × six categories | Every value, label, key, zero and age code matches |
| `mtus-coverage.csv` | 89 country-years, sixteen countries | Every country/year and nonempty-field count matches |
| `hetus-leisure.csv` | 32 country-waves, 22 countries | Every value and wave matches |
| `finland-free-time.csv` | Twelve sex/year values | Every value and four date labels match |
| `historical-definitions.csv` | Twenty definition/year values | Every estimate and five date labels match |

All 555 rows were checked, together with key uniqueness, coverage counts, manifest agreement, and provenance transformations/exclusions. No project weighting, interpolation, imputation, country averaging, or normalization was added. MTUS field counts measure field availability, not diary sample size.

## Graph-coordinate and visual checks

The auditor parsed actual SVG elements and compared coordinates with independently transformed CSV values using the displayed axes and SVG plotting rectangles.

| Figure | Actual elements checked |
| --- | --- |
| ATUS social time | All 402 line vertices and 402 markers, including separation of age labels 80/85 |
| MTUS coverage | All 89 markers, including country-row placement |
| HETUS leisure | All 32 markers and correct wave colours |
| Finland free time | All twelve line vertices and markers |
| Historical definitions | All twenty line vertices and markers |

Maximum coordinate error was 7.5 × 10⁻⁷ SVG units, consistent with coordinate serialization.

The auditor viewed all seven actual PNGs, including both diagrams. Titles, labels, units, legends, sources and limits are visible. No material clipping or overlap remains. Diagram titles and boxes fit the figures.

The five data/coverage SVGs show the archive retrieval URL/date, an exact pinned CSV link, and descriptive/non-causal scope. The two diagrams visibly state that no quantities or time shares are plotted, give their guide references, and disclose unverified original-provider definitions/access.

## Reproduction and site validation

The author ran both scripts in `/tmp/leisure-surveys/reproduction`, with fresh retrieval and checksum verification of all ten inputs, then offline plotting. The auditor independently compared all 29 files and verified their recorded SHA-256 hashes:

- 25 generated files: eleven data/metadata/provenance files and fourteen charts.
- Four inputs/scripts: manifest, authored diagram specification, two scripts.
- All 29 files were byte-identical. [Detailed comparison](2026-11-02-leisure-surveys-reproduction.json).

Script execution was parent-run. Independent checks comprised source retrieval/hashes, complete extraction reconstruction, metadata inspection, SVG-coordinate checks, actual image inspection, and reproduction/hash comparison.

After adding the audit-status summary, the author ran `ASTRO_TELEMETRY_DISABLED=1 npm run build`: 25 pages built successfully. An HTML parser checked all 1,773 internal links/images/anchors and image text alternatives. All 27 new public assets match their built copies. Staged whitespace checks passed. The auditor did not independently rerun the build or HTML checker.

## Unverified and unrun checks

Fresh requests failed for BLS's multi-year ATUS data page, AHTUS, MTUS, Eurostat time-use metadata, OECD's time-use database, the archived Statistics Finland PXWeb source, and the linked EconStor working-paper PDF. Six returned proxy tunnel HTTP 403; the Finnish HTTP endpoint returned HTTP 403.

Original-provider transcription, current releases/terms, original working-paper tables and sample restrictions, precise ATUS top-coding, common population ages, HETUS fieldwork dates, and current AHTUS/OECD definitions remain unverified. No live Vercel or mobile inspection was performed.

## Recheck requirements

No supported implementation defect remains in the inspected artifacts. Recheck any subsequent source, numerical, selection, caption, axis, or plotting change. Final handoff must distinguish five data/coverage figures from two conceptual diagrams and retain the original-provider verification limits.
