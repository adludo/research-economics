# Research audit: Australian population and economy

- Audited HEAD: `85f23e7374f37f3a0de864e668f06eb84309b914`, with 33 staged feature files.
- Exact audited staged tree: `b498a238731fae398a5c810c431e8e48f659a2eb`. The auditor confirmed the tree exists and found no working-tree differences against it. This report was not yet included.
- Base: `origin/main`, `606d580d8260f9d281c71ed0bb29291037739d41`. The branch also includes the earlier Australia case-study scaffold commit.
- Auditor: independent `/root/audit_australia_data`, following `.codex/agents/research-auditor.toml`, `AGENTS.md` and `docs/RESEARCH_AUDIT.md`.
- Date: 11 November 2026, UTC.
- Coverage: the new guide, navigation and scaffold changes; all 16 manifest inputs; all 3,504 derived CSV rows; eight WDI metadata records; 20 employment metadata records; both generation scripts; seven SVGs and seven PNGs.
- Verdict: **Archive extraction, calculations and figures verified within the stated scope. Original-provider verification remains incomplete.** No remaining numerical or rendering defects were found in the audited changes.

## Findings, highest severity first

| ID | Severity | Status | Repository location / claim | Evidence and locator | Required correction or next check |
| --- | --- | --- | --- | --- | --- |
| A1 | Major | Unverified | Agreement of archived data with original ABS, World Bank and ILO releases | Independent requests to ABS QuickStats, ABS Detailed Labour Force, the World Bank GDP indicator and ILO bulk data all failed with proxy `403 Forbidden`. Checksums establish archive identity, not original-provider authentication. | Compare the archived observations and metadata with official releases when accessible. Preserve the guide’s explicit unverified status. |
| A2 | Minor | Unverified | Current contents of the official-source catalogue, Census dictionary, latest releases and reuse policies | The guide links these destinations and explicitly states their current contents were not retrieved. No claim that these links establish the newest available release was verified. | Check each original catalogue destination, definitions and current release vintage. Verify ABS and dashboard reuse terms before treating them as settled. |
| A3 | Minor | Unverified | Exact observation status, calendar/financial-year alignment and employment classification rules | The WDI mirror lacks observation-level forecast/revision flags. The employment workbook does not establish all main-job allocation and survey-classification rules. | Retain the existing qualifications; consult original country notes and ABS explanatory material before cross-dataset analysis. |
| A4 | Minor, resolved | Verified | Figure readability | Initial population, age and family figures clipped “Other territories”; the initial sector legend overlapped data. All seven corrected PNGs were inspected. | No remaining correction required. Preserve the corrected margins and legend placement. |

## Evidence ledger

| Dataset, claim or graph | Check | Status | Source/version and locator | Method or limitation |
| --- | --- | --- | --- | --- |
| Manifest inputs | Archive identity | Verified | `public/data/australia/sources.json`; all 16 pinned retrieval URLs | Independently fetched every input. All SHA-256 hashes and byte lengths matched the manifest. |
| Census population | Nine geographic counts | Verified against archive | [Census archive](https://github.com/HughParsonage/Census2021.DataPack/tree/2cb84120792534c4d39adfa7a7d4d2abd092d981), `STE__Persons.tsv`; transformation lines 588–591 select G01 `Tot_P_P` | All nine extracted rows match. Other Territories is retained. No official national total is inferred from regional sums. |
| Census age | Three age groups, denominators and shares | Verified against archive | Same revision, `STE__Age.tsv`; G01 age extraction lines 606–614 | Independently grouped all 99 cells into under 15, 15–64 and 65+. Every output count and denominator matched. Shares use the same age cells as their denominator. |
| Census families | Families containing children under 15 | Verified against archive transformation | Same revision, `STE__CoupleFamily_HasChild_HasDependentStudent_HasNonDependentChild_families.tsv`; transformation lines 1500–1515 | Recomputed all 18 state/type groups from `HasChild=1`. The guide correctly distinguishes families from children and records the exclusion of couples without children. Official dictionary comparison remains unverified. |
| Annual WDI indicators | Country, years, precision and metadata | Verified against archive | [WDI archive](https://github.com/open-numbers/ddf--world_bank--world_development_indicators/tree/4252d91d988efc0f116d4fa48e92357b778729e5), eight indicator CSVs and `ddf--concepts--continuous.csv` | Independently reconstructed all 208 Australia observations, 2000–2025. Exact stored value strings and all eight selected metadata records matched. Commit timestamp independently confirmed as 14 October 2026. |
| WDI definitions | Units and denominators | Verified against archived metadata | `indicator-metadata.json` and source metadata | GDP is constant 2015 US dollars. Industry includes construction. Employment is relative to population aged 15+; unemployment is relative to the labour force. Both labour indicators are modeled ILO estimates. |
| Industry employment | Levels, dates, series selection and metadata | Verified against archived workbook | [Employment workbook](https://github.com/lehuukimlam/Aussie-Economy-Dashboard/blob/c70a360200771c9f9d7108fa89db84c7a2e5d250/data/Raw%20Employed%20By%20Industry.xlsx), `Data1`, metadata rows 1–10 and observations 11–173 | Independently matched all 3,260 observations and 20 metadata records. Each series has 163 quarterly observations, November 1984–May 2025. All date intervals are three months. Units are thousands of employed persons. |
| Employment ranking | Nineteen industries at May 2025 | Verified against archive | Last workbook observation; aggregate series `A84932381A` excluded from ranking | Health care and social assistance is largest, approximately 2.39 million people. The guide correctly avoids treating employed persons as job positions or FTEs. |
| Seasonal adjustment caveat | Industry totals need not add to aggregate | Verified in archive | May 2025 seasonally adjusted series | The 19 divisions sum to 14,694.4326122 thousand; the separately adjusted aggregate is 14,666.2525245 thousand. The guide does not calculate misleading shares from these nonadditive totals. |
| Guide numerical summaries | Endpoints and rounding | Verified against archive | `src/content/docs/data/australia.md`; annual and employment extracts | Checked every stated endpoint and rounded summary, including population, real GDP, sector growth and labour-market rates. |
| Seven SVG figures | Actual plotted coordinates | Verified | `public/charts/australia/*.svg` | Decoded axes from SVG ticks independently of the plotting script. All 73 bar boundaries and 208 annual vertices across eight lines matched the verified extracts within 0.00003 SVG points. |
| Seven PNG figures | Actual appearance | Verified | `population`, `age`, `families`, `macro`, `sector-growth`, `industry-employment`, `labour-market` | Inspected every final PNG. Labels, legends, units, sources and qualifications are readable; corrected clipping and overlap are resolved. |
| Paper identity, findings and funding | New paper claims | Not applicable | This feature adds descriptive data documentation | No new papers, paper findings, funding claims or paper-replication claims were introduced. |

## Reproduction and visual checks

The auditor independently reconstructed every derived CSV row in memory, without executing the author’s collation script or writing files:

- Nine population rows, nine age rows and 18 family rows.
- All 208 annual indicator observations.
- All 3,260 quarterly employment observations.
- All selected WDI and employment metadata records.

The author performed fresh network collation and plotting in `/tmp/australia-repro-g5gx457q`. The auditor independently compared both copied scripts and all **26 published data, metadata and image files** with the checkout; every file was byte-identical. The auditor did not personally execute that filesystem-writing reproduction.

All seven final PNGs were inspected, and all seven SVGs underwent independent coordinate checks. Figure credits identify the archive, revision, input file and retrieval date. The guide provides downloads, alt text, exact retrieval URLs and limitations.

Both working-tree and staged `git diff --check` checks were clean. The author additionally reported a successful 32-page build, 75 local URL/anchor checks and ten production-output HTTP checks. Those application checks were not independently rerun by the auditor.

The source-selection exclusions were independently checked:

- `Raw GDP Overall.xlsx`, column B, contains 161 nonempty observations dated March 1979–March 2019 despite metadata claiming 263 observations from September 1959–March 2025.
- `Raw GDP by Industry.xlsx`, column Z, places 91 construction GVA values on September 1959–March 1982 dates despite metadata identifying September 2002–March 2025.
- `Raw Unem by States.xlsx` explicitly identifies its measures as **employment-to-population ratios**, despite its filename.

These files were appropriately excluded from the published graphs.

## Unverified and unrun checks

Original-provider transcription, original Census dictionary definitions, current catalogue contents, newer-release availability, observation-level estimation/revision flags, exact year alignment, detailed employment allocation rules and current reuse terms remain unverified.

The official-source access failures are not evidence that the archives are fabricated or incorrect. Conversely, successful archive retrieval and reproduction do not authenticate their agreement with official releases.

This was a feature audit, not a repeat audit of the entire existing wiki. Existing literature, findings and unrelated charts were outside scope.

## Recheck requirements

No remaining correction is required for the inspected archive calculations or final renders.

Before describing the data as verified against original releases, compare the archived inputs with official ABS, World Bank and ILO records, check the original definitions and observation flags, and resolve the reuse-policy checks. Any later change to inputs, filters, calculations, captions or plotting code requires an affected-scope recheck.

## Author verification record

Output checksums and application-check counts are saved in [the reproduction record](2026-11-11-australia-reproduction.json), added after the audited research tree. The report and verification record do not alter the audited research files.
