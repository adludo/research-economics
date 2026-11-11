# Research audit: Australian parents, jobs and family size

- Audited HEAD/base: `16a9e78ee6d6e20b6a5324684d1abc6950d618c7`.
- Exact audited staged tree: `0851d356f0ea62e8347096175bb29d3a59143d0e`, containing nine feature files. This report was not yet included.
- Auditor: independent `/root/audit_australia_data`, following `.codex/agents/research-auditor.toml`, `AGENTS.md` and `docs/RESEARCH_AUDIT.md`.
- Date: 11 November 2026, UTC.
- Coverage: new guide, four navigation/cross-link edits, four metadata JSON files, existing Australian extract schemas, five source inputs and all cited HILDA manual passages.
- Verdict: **Verified within the stated documentation scope.** The existing extracts lack the requested joint relationship. Archived HILDA documentation supports the proposed linkage route. A usable four-way extract and current access conditions remain **unverified**. No supported correction was required.

## Findings, highest severity first

| ID | Severity | Status | Repository location / claim | Evidence and locator | Required correction or next check |
| --- | --- | --- | --- | --- | --- |
| F1 | Major | Unverified | Availability of a Census parent occupation × child count × state × parent age table | No successful TableBuilder query or custom-table response was obtained. The official dictionary, TableBuilder and Census microdata endpoints returned proxy HTTP 403. | Confirm compatible variables, counting unit, family linkage, permitted combinations and access conditions. The guide correctly presents this as a specification to investigate. |
| F2 | Major | Unverified | Actual joint coverage in approved HILDA records | The inspected Release 21 manual documents linkage, but no individual records were obtained or analysed. | Validate the approved release, response coverage, links, child-count construction, weights and cell sizes before calculating results. |
| F3 | Minor | Unverified | Original-provider agreement and current product conditions | Census metadata and the HILDA manual were retrieved from third-party archives. Current official materials were inaccessible. | Preserve the disclosed limitations; compare with official documentation when accessible. |
| F4 | Minor | Contradicted within upstream metadata; disclosed | G58 population definition | The archived title says couple families **with children**, while its population field says couple families **with no children**. | The guide correctly preserves and flags the conflict. Resolve it against the original ABS table before using G58 observations. |

## Evidence ledger

| Dataset, claim or proposal | Check | Status | Source/version and locator | Method or limitation |
| --- | --- | --- | --- | --- |
| Existing Australian extracts | Joint relationship is absent | Verified | Eight existing Australian CSV/TSV files | Inspected every schema. Age cells identify generic age and state; family cells identify family type and child-status presence; employment identifies national industry and date. There are no person, household or family identifiers, linked parent ages or child counts. |
| Wider CSV/TSV inventory | Other relationship fields | Verified within header inventory | All 29 public CSV/TSV files | Independently scanned headers. Relationship-related fields occurred only in the existing Australian family files. This was a schema inventory, not a new audit of all existing observations. |
| Aggregate joining warning | State totals cannot recover family-level associations | Verified | Guide sections “What the wiki already contains” and “Define the question” | The missing joint dimensions and linkage keys cannot be reconstructed from these marginal counts. Occupation, industry and labour-force status are correctly distinguished. |
| Five manifest inputs | Identity and retrieval | Verified | `public/data/australia-family-jobs/sources.json` | Independently fetched all five inputs. Every SHA-256 hash and byte length matched. Checksums do not authenticate original-provider agreement. |
| Census table catalogue | Eight titles and populations | Verified against archive | `carlosyanez/auscensus`, `aux_files/tables.zip` | Independently decoded the Parquet payload and matched all eight selected records exactly, including the G58 conflict. |
| Illustrative Census descriptors | Seven complete records | Verified against archive | `aux_files/descriptors.zip` | All seven stored examples matched complete source records for 2021. G28 includes zero and six-or-more children; G47/G48 age descriptors refer to dependent children. |
| State-file locators | Complete selected inventory | Verified against archive | `aux_files/content.zip` | Independently reconstructed the selection. All 19 `STE` file locators, including multipart tables, matched exactly. No observation counts from those files were inspected. |
| Partial Census relationships | Units and missing dimensions | Verified against archived metadata | G28, G29, G30, G47, G48, G54 and G60 | G28 covers females aged 15+; G47/G48 count dependent children; G54/G60 cover employed persons aged 15+. The guide does not reinterpret these as complete parent/family joint tables. |
| Metadata lineage | Relationship to ABS workbook sheets | Verified as documented processing | [`process_data.R`](https://github.com/carlosyanez/auscensus/blob/fcd367e10fab602d561ea9a9cea3a7ea12df355d/data-raw/process_data.R), lines 93–146 and 319–336 | Code reads table and cell-description sheets and transforms their fields. This establishes documented processing, not authentication against the original workbook. |
| HILDA manual identity | Release and date | Verified in inspected document | [Archived Release 21 manual](https://github.com/Henrik-Alexander/transition_fatherhood_australia/blob/158860420d10a13610fedb38c798eaa3af08dc92/handbooks/HILDA-User-Manual-Release-21.0.pdf), title page | Melbourne Institute document, last modified 5 December 2022; 233 pages. Printed page numbers match PDF pages. |
| HILDA identifiers and file structure | Person, household, partner and parent linkage | Verified in manual | pp. 21–23, §§3.5–3.6, Table 3.2 | `xwaveid`, wave-specific household IDs, parent/partner links, state and family-number fields match the guide. Household ordering has no parental meaning. |
| Parent-age definitions | Reference dates | Verified in manual | p. 35, §4.1 | `_hgage` refers to 30 June before fieldwork; `_hhiage` refers to interview age. The guide correctly requires alignment. |
| Occupation and industry | Current job versus retrospective parental job | Verified in manual | pp. 50–52, §4.8, Table 4.7 | `_jbmo62` and `_jbmi62` identify current main-job occupation and industry. Retrospective parent occupations refer to around the respondent’s age 14. |
| Family and child construction | Family membership and coverage | Verified as documented route | pp. 21–22 and 55–60, §4.12, Table 4.10 | Enumerated people include children and non-interviewed adults. Co-resident parent definitions and biological-link limitations match the guide. Family membership, household totals and a particular parent’s children are correctly separated. |
| Weights and uncertainty | Unit and response sample | Verified in manual | pp. 98–104, Tables 4.30–4.31 | Cross-sectional, longitudinal and responding/enumerated weights differ; replicate weights support uncertainty estimation. The guide does not assume parent weights automatically produce family-level estimates. |
| HILDA access | Historical approved-access requirement | Verified for Release 21 | p. 20, §§3.1–3.3 | The manual requires application and confidentiality documentation. Current procedures remain unverified and are not presented as settled. |
| Proposed extraction | Units, denominators and interpretation | Verified as a defensible specification | “A concrete next extraction” | Specifies parent-level observations, same-wave linkage, distinct qualifying children, separate non-employed/missing categories, family-level alternatives and uncertainty checks. It makes no empirical or causal claim. |
| Papers, funding and new graphs | Applicability | Not applicable | This feature adds availability documentation and metadata | No new paper findings, funding statements, population estimates or empirical figures were introduced. |

## Reproduction and visual checks

The auditor independently decoded the source ZIPs in memory using the author-installed Parquet reader, without installing dependencies, modifying files or executing author generation code. All eight catalogue records, seven descriptor records and 19 file locators matched their archived sources.

The auditor read every cited HILDA passage directly, including access, identifiers, age definitions, current-job variables, retrospective parental jobs, family relationships and weighting.

The staged tree exists and matches the working tree. Staged `git diff --check` was clean. The author reported a successful 33-page build; the auditor did not independently rerun the filesystem-writing build. No graph reproduction or visual inspection was applicable because this change introduces no figures.

## Unverified and unrun checks

Independent requests to all four manifest-listed official endpoints—Census dictionary, TableBuilder, Census microdata and HILDA—returned proxy HTTP 403.

The following remain unchecked: official metadata agreement; current release availability; current access/reuse conditions; successful four-way TableBuilder compatibility; actual HILDA joint sample coverage; record linkage; final child counts; weighting implementation; uncertainty; and disclosure constraints.

The mutable `aux_files` release is correctly identified as mutable. Its checksums identify retrieved payloads, not a permanently pinned release or official authenticity.

## Recheck requirements

No correction is required for the inspected documentation.

Before creating the proposed graphs, obtain a compatible custom Census table or approved linked records. Audit the resulting unit, family definition, parent linkage, child-count denominator, employment/missing categories, age reference dates, weights, uncertainty and actual plotted observations. Retain the distinction between a parent-level association and a causal effect on fertility.

## Author application checks

The author ran `ASTRO_TELEMETRY_DISABLED=1 npm run build` successfully (33 pages). A standard-library HTML parser checked 337 internal link/image/anchor references across the four affected pages. All four metadata JSON files parsed successfully. Nine HTTP requests to the production preview returned 200: the new guide, the Australia overview, data index, Australia case study, all four new JSON downloads and the Pagefind JavaScript asset. These application checks were not independently rerun by the auditor and do not verify data or research claims.
