# Research audit: productivity methods and slowdown

- **Audited base:** `c51e7034496c133e27020d486c71883a4cf06f0f`.
- **Branch:** `docs/productivity-measures`.
- **State:** Dirty working tree before the feature commit.
- **Auditor:** `/root/audit_productivity_methods`, independently delegated with the repository research-auditor instructions and audit guide. The author saved this record of the returned checks.
- **Date:** 3 November 2026, UTC.
- **Coverage:** Three productivity pages, reading register, collator, eight data/reference/provenance files, navigation/cross-links, glossary/index changes, and final audit-status addition.
- **Verdict:** Conceptual explanations and arithmetic are internally consistent; archive extraction and calculations verified within scope. No material implementation defect found. Primary-paper and original-provider verification remain incomplete.

## Findings, highest severity first

| ID | Severity | Status | Location / claim | Evidence and locator | Required next check |
| --- | --- | --- | --- | --- | --- |
| P-01 | Verification limit | Unverified; disclosed | Nine paper/manual references: publisher identity, final versions, primary-text support | Fresh independent requests to all nine DOI endpoints returned proxy HTTP 403 | Inspect publisher records/full texts before presenting verified paper-result summaries |
| P-02 | Verification limit | Unverified; disclosed | Original PWT release identity and current provider estimates | Agreement with pinned CRAN copy does not authenticate original-provider release | Compare original releases and current documentation |
| P-03 | Verification limit | Unverified; disclosed | Current outcomes and representative expert consensus | Eight-country table ends in 2019 | Use newer releases and representative evidence for those claims |
| P-04 | Verification limit | Unverified; disclosed | Corrections/retractions and current reuse conditions | Original publication/provider records inaccessible | Check separately |

These are evidence limits, not demonstrated errors. The pages distinguish explanatory derivations, inspected documentation, archive calculations and unread further-reading references. No unread paper's numerical result is attributed to that paper.

## Conceptual and methodological review

| Topic | Completed independent internal-consistency check |
| --- | --- |
| Headline labour productivity | Real output divided by matched total actual hours; whole economy and business sectors distinguished |
| Output per worker/resident | Hours per worker separated; output/population identity and domestic/resident coverage warning correct |
| Output measurement | Real/nominal, within-country growth/PPP levels, and vintages distinguished |
| Labour composition | Compensation-weighted hours index and assumptions; not innate ability or causal education effect |
| Capital input | Service flows distinguished from purchases and wealth stock |
| TFP/MFP | Residual, competitive/constant-returns assumptions, adjacent-period weighting, and constant-elasticity illustration distinguished |
| TFP interpretation | Utilisation, omitted inputs, market imperfections, revisions and measurement can enter residual; not directly observed technology |
| Industry measures | Value-added/gross-output boundaries, intermediates, outsourcing and chain-volume nonadditivity |
| Firm measures | Physical production separated from revenue, prices, demand, markups, quality and mix |
| Frontier measures | Benchmark dependence, distance functions, and conditional efficiency interpretation |
| Slowdown | Slower positive growth separated from falling levels; period/country/sector heterogeneity retained |

The historical comparison is not described as an OECD/world average, representative sample, consensus test or 2026 nowcast. The final audit-status paragraph accurately reports the checks and limits.

## Inspected source evidence

All six manifest inputs were independently retrieved and hash-verified. Cached source files also matched. [Exact URLs/hashes](../../public/data/productivity/sources.json).

| Source | Status | Locator / method |
| --- | --- | --- |
| OWID PWT CSV/metadata | Verified archive identity/extraction | Revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`; input hashes verified |
| CRAN PWT10.01 codebook | Verified distribution documentation | Definitions of `rgdpna`, `emp`, `avh`, `rkna`, `rtfpna` inspected |
| CRAN PWT10.01 R data | Verified cross-distribution agreement | Every selected GDP/employment/hours field independently compared with appropriate million-unit conversion |
| Boppart–Li README/implementation | Verified inspected computational material | Revision `e0e9a034342069e6608eff8cadee4d7b4ff979ec`, implementation lines 156–162 construct `avh×emp` hours and `rgdpna/hours` |
| Nine scholarly/manual references | Unverified primary records/full texts | All independent DOI requests returned HTTP 403; statuses recorded accurately |

Boppart–Li's legacy 2011-price labels are not reused. Reading its code is not reading the paper or validating all results. Stored PWT metadata is byte-identical to its input. Stored codebook differs only by stripped trailing line whitespace; the original hash is verified first and normalization disclosed.

## Independent data reconstruction

The auditor independently reconstructed expected records from source data without executing the collator:

- All 200 country-years, eight countries over 1995–2019, with unique keys.
- All 1,000 numeric fields: GDP, persons engaged, annual hours, total hours, output/hour. Every field matches exactly.
- All selected `rgdpna`, `emp`, `avh` fields match CRAN-distributed PWT10.01 at relative tolerance `1e-10`.
- Every CAGR and percentage-point difference matches within `1e-12`.
- All eight rounded table rows match, in both Markdown and actual built HTML.

CAGR uses twelve elapsed years for 1995–2007 and nine for 2010–2019. OWID GDP and employment are already in absolute units; no extra million-unit factor is applied.

| Country | 1995–2007 annualized growth | 2010–2019 annualized growth |
| --- | ---: | ---: |
| Australia | 1.966508% | 0.934888% |
| Canada | 1.387112% | 1.046935% |
| France | 1.557430% | 0.899069% |
| Germany | 1.564772% | 0.894780% |
| Japan | 1.692772% | 0.876398% |
| South Korea | 5.385414% | 2.638829% |
| United Kingdom | 2.190248% | 0.337486% |
| United States | 2.226700% | 0.746845% |

All selected comparisons are slower in the second window. That verifies the archive illustration, not a representative claim about every economy.

## Hypothetical arithmetic

The auditor recalculated every teaching example:

- `1040/102 = 10.196078…`, displayed `10.1961`.
- Exact hourly growth `1.960784…%`, displayed `1.9608%`.
- Twenty years at 1% yields `22.0190…%`; at 2%, `48.5947…%`, rounded to 22.0% and 48.6%.
- TFP log growth `3 − 0.4×4 − 0.6×1.5 = 0.5%`.
- Labour-productivity log growth `1.2 + 0.3 + 0.5 = 2%`.

Exact ordinary percentage changes and additive log changes are correctly distinguished. These invented teaching inputs are not empirical findings.

## Reproduction and presentation

The author ran the final collator in `/tmp/productivity-guide/reproduction`, freshly retrieving/hash-checking all six inputs. The auditor independently compared all ten files and recorded hashes:

- Six generated artifacts: five generated data/documentation/provenance files and regenerated slowdown page.
- Four copied inputs/script: manifest, reference-access record, vintage-check record, collator.
- All ten files byte-identical. [Comparison record](2026-11-03-productivity-reproduction.json).

Static reference/vintage records are review inputs, not validations generated by the collator. Script execution was parent-run; independent checks comprised retrieval, reconstruction, arithmetic, cross-distribution comparison, file/hash comparison and built-table inspection.

No new charts/images were introduced; SVG/PNG checks are not applicable. The auditor inspected the actual built slowdown table. The parent ran `ASTRO_TELEMETRY_DISABLED=1 npm run build`: 29 pages built. Its HTML parser checked all 2,124 internal references, image text alternatives, and all eight new public assets against their built copies. Staged whitespace checks passed. The auditor did not independently run the build or site-wide HTML checker.

## Unverified and unrun checks

Journal/manual publisher identity, final versions, primary-text findings, corrections/retractions, original-provider authentication, current revisions/terms, post-2019 or 2026 outcomes, representative expert consensus, causal slowdown explanations, and live Vercel/mobile behavior remain unverified. See [per-reference access records](../../public/data/productivity/references.json).

## Recheck requirements

No supported implementation defect remains. Recheck changes to formulas, assumptions, sources, selection, periods, values or attributed paper claims. The handoff must distinguish verified archive calculations/internal mathematical review from unverified primary-paper/provider checks.
