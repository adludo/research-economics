# Research audit: Australian age, parity and state graphs

- Audited HEAD: `c179a64c99a9898045086c9037f39844786c048d`.
- Exact audited staged tree: `746ec7daef15e49bd2aedeea5c6348d76d5fd806`, containing 11 changed files. This report was not yet included.
- Scope: graph additions and accompanying documentation relative to that HEAD. The earlier family/jobs availability guide has a separate audit.
- Auditor: independent `/root/audit_australia_data`, following the repository’s research-auditor instructions.
- Date: 11 November 2026, UTC.
- Coverage: complete source-file identity; all 448 selected counts, 112 denominators and 56 calculated percentages; plotting script; two SVGs and two PNGs; affected prose and metadata.
- Verdict: **Calculations and figures verified against the pinned archive. Original ABS agreement remains unverified.** No remaining supported correction was found.

## Findings, highest severity first

| ID | Severity | Status | Repository location / claim | Evidence and locator | Required correction or next check |
| --- | --- | --- | --- | --- | --- |
| P1 | Major | Unverified | Agreement of the archived G28 counts with the original ABS release | The source is a checksum-pinned third-party transformation. Official ABS access remains blocked; archive identity does not authenticate original-provider agreement. | Compare with the official G28 release when accessible. Preserve the existing unverified qualification. |
| P2 | Minor, resolved | Verified | Statement about which table observations had been retrieved | Initial wording incorrectly included G29 among tables without retrieved counts, despite the existing family graphs using G29. | Corrected wording explicitly acknowledges the existing G29 counts. Rechecked in the final staged tree. |
| P3 | Scope limitation | Unverified | Occupation or parental-employment comparisons | No four-way extract or G47/G48/G54/G60 observations were obtained. | Obtain compatible joint data before producing those comparisons. The new figures correctly make narrower claims. |

## Evidence ledger

| Dataset, claim or graph | Check | Status | Source/version and locator | Method or limitation |
| --- | --- | --- | --- | --- |
| G28 source TSV | Retrieval identity | Verified | [Pinned source](https://raw.githubusercontent.com/HughParsonage/Census2021.DataPack/2cb84120792534c4d39adfa7a7d4d2abd092d981/tsv/STE/STE__Age5yr_ChildrenEverBorn.tsv) | Independently retrieved 29,685 bytes; SHA-256 `14e543b4fc15ab035242516ee0d18fe6092e627adc824117ae94ef77c8822569` matched the manifest and checked-in source copy. |
| Source mapping | G28 age and parity categories | Verified against archived code and metadata | Revision `2cb84120792534c4d39adfa7a7d4d2abd092d981`, `put-data.Rmd`, lines 1466–1474; previously inspected G28 descriptors | Zero means no children ever born; archive code `6` means six or more; blank parity represents not stated. Counts refer to women, not children or families. |
| Selected coverage | Eight jurisdictions, seven age bands | Verified | `parity-source.tsv`, `parity-summary.csv` | Every selected state/age group contains all eight categories. All 56 groups and 448 cells are present; no missing-cell filling occurs. Other Territories and other ages are excluded. |
| Summary CSV | Counts, denominators and percentages | Verified | All 56 rows of `parity-summary.csv` | Independently reconstructed every category count, all-category total, stated total and two-or-more percentage from freshly retrieved source rows. |
| Two-or-more formula | Numerator and denominator | Verified | `plot-australia-parity.py`; guide’s heatmap caption | Numerator includes categories 2–6+. Denominator excludes not stated while retaining zero births. No top-coded mean is calculated. |
| Heatmap | Values, order and colours | Verified | `two-plus-by-age-state.svg` | Checked all 56 percentage annotations and all 56 embedded raster-cell RGB values against the calculated percentages and the stated 0–100 colour scale, accounting for the SVG’s vertical transform. |
| Ages 45–49 distribution | Segment widths and denominator | Verified | `parity-45-49.svg` | Independently decoded all 64 stacked-bar segment boundaries from SVG coordinates and axis ticks. They match category counts divided by the sum of all eight categories, including not stated. |
| Rendered figures | Readability and attribution | Verified | Both final PNGs | Inspected both actual images. State/age labels, legends, units, source credits and retrieval references are readable. The figures distinguish stated-only percentages from distributions including not stated. |
| Interpretation | Population, timing and limits | Verified within archive scope | “Graphs of available joint data” and associated captions | The prose correctly identifies women’s Census age and children ever born, includes zero births, separates age groups from longitudinal cohorts, and avoids resident-family-size, current-job or causal claims. |
| Reproduction | Published outputs | Verified by independent comparison | `/tmp/parity-repro-d4wmb5fy` | All seven reproduced files—source, summary, graph manifest and four images—match the checkout byte-for-byte. The copied plotting script also matches. |

## Reproduction and visual checks

The auditor independently fetched the source and recalculated all selected observations in memory without executing the author’s plotting script or writing files.

The numerical checks covered:

- All **448 category counts**.
- All **112 denominators**: 56 all-category totals and 56 stated totals.
- All **56 two-or-more percentages**.
- All **56 heatmap annotations and cell colours**.
- All **64 stacked-bar segments**.

The author ran fresh-network reproduction in an isolated directory. The auditor independently compared its outputs and script with the checkout; every file matched. The auditor did not personally execute that filesystem-writing reproduction.

Both PNGs were visually inspected. The final staged tree exists and matches the working tree; staged `git diff --check` was clean.

The author reported a successful 33-page build, 107 local-reference checks and successful HTTP checks for the page, SVGs and CSV. Those application checks were not independently rerun by the auditor.

## Unverified and unrun checks

Original ABS transcription, original release metadata and newer-release availability remain unverified. The checksums establish the identity of the inspected archive.

No current occupation, industry or parental-employment observations were newly obtained. No approved HILDA records were accessed. The figures therefore do not establish the requested four-way relationship between job type, resident family size, state and parent age.

The source contains additional ages and Other Territories, but their observations are outside the figures’ stated selection. This audit does not extend the charts’ findings to excluded groups.

No paper findings, funding claims or paper-replication claims were introduced.

## Recheck requirements

No correction is required for the audited figures or calculations.

Recheck affected observations and renders after changes to source files, age/state selection, category mapping, denominators, captions or plotting code. Obtain and audit a compatible joint extract before adding job-type or parental-employment graphs.
