# Research audit: leisure, leisure/productivity, and trade/GDP graphs

- Target: `docs/leisure-trade-graphs`, new working-tree changes based on main `0435db26c24ef1228c830fc333999352adae5332`.
- Date: 1 November 2026, UTC.
- Independent auditor: `/root/audit_hours_graphs`, using the repository's research-auditor instructions.
- Scope: five SVG/PNG figures, four derived CSVs, frozen source metadata/provenance, two generation scripts and additions to the three existing data guides.
- Verdict: archive-to-extract correctness verified; original-provider definitions and scientific verification remain incomplete. The independent auditor completed final rendered-figure, source-link, correction and reproduction rechecks; no remaining material project defect was found within this scope.

## Source and numerical evidence

The auditor freshly retrieved and SHA-256 checked all eight pinned archive payloads. The raw inputs are the Ramey–Francis historical US leisure compilation, Statistics Norway time-use compilation, Fouquin–Hugot/CEPII-based export-share compilation, and PWT macro data, each with its metadata. Exact URLs/hashes are in [`provenance.json`](../../public/data/topic-graphs/provenance.json).

| Check | Coverage/result |
| --- | --- |
| US leisure | All 72 displayed observations match source rows for six declared total-sex age groups, 1900–2005 |
| Norwegian leisure | All 15 sex-year values match the archived series: all/female/male at five dates, 1970–2010 |
| Leisure/productivity join | All 12 exact-year pairs independently reconstructed: five Norwegian observations and seven US age14+ observations, 1950–2005 |
| Output/hour formula | Output-side real GDP divided by persons engaged times annual hours; absolute dollar/person input units; no extra million-unit multiplier |
| PWT distributed-copy comparison | All 12 output/hour values match CRAN PWT10.01, maximum absolute difference approximately `2.13e-14`; all 360 income values match, maximum approximately `7.28e-12` |
| Trade/income join | All 360 records match eight selected countries × 45 years, 1970–2014; exact same-year input matches |
| Trade definition | Export-share interpretation follows dataset title and explicit metadata formula, despite the raw column's broader “total merchandise trade” label |

PWT's archived folder/metadata still say10.0; prior and present cross-distribution checks support agreement with CRAN10.01 for the checked values. Neither that match nor an archive hash establishes retrieval from the original provider.

## Measures and limits preserved

- US leisure is a residual: total time less work, school, home production, commuting and personal care. The archive assumes personal care77 hours/week and commuting10% of work/school time. The age14+ aggregate overlaps the age-specific series and must not be summed with them.
- Norway leisure includes the source's recreation/travel categories. The archive normalises time budgets to1,440 minutes/day. Its age coverage is unspecified; “all” is the all-sex series, not verified all-age coverage.
- The leisure/productivity panels have different y-units and scales and are not pooled. National output and worker hours do not refer to exactly the same population as the leisure series.
- The supplied export/GDP ratio is not exports plus imports, services trade, or a policy-openness index. Original agreement with the CEPII release remains unresolved.
- Trade flows are described in the metadata as current British pounds. The GDP denominator's construction is not verified here. The percentage is copied unchanged, not recalculated using PWT PPP GDP.
- Illustrative country selection and aggregate time paths do not identify causal effects, individual welfare gains, or paper-model replications.

MTUS was considered but not plotted as a newly constructed total-leisure measure: its archived processing excludes zero-reported activity entries and normalises category means. No unsupported sum of those categories was substituted for total leisure.

## Presentation corrections during review

The initial trade figures used a40% upper bound that clipped China's44.2862% observation in2006. The main agent caught this during visual inspection; the auditor independently observed it. Both figures now use0–60%. The scatter-panel top margin was also lowered to keep the year colourbar away from the France heading.

The auditor identified an unsupported inference that the export-ratio GDP denominator was established as nominal/current-price GDP. The wording now states only what metadata establishes about trade-flow currency and leaves denominator construction explicitly unverified. No values were changed.

## Final figure checks

The auditor independently checked actual SVG coordinates: 72 US leisure vertices, 15 Norwegian vertices, 12 leisure/productivity vertices, 360 trade/income vertices plus scatter positions and year colours, and 360 trade/time-path vertices. Maximum geometry error was below `1e-6` SVG units. All five PNGs were viewed; final0–60% trade axes show China's44.2862% maximum without clipping, and the year colourbar no longer overlaps the France heading. Each figure retains visible retrieval references and correct SVG input links.

An extra diagnostic applying the documented residual formula to36 rounded upstream component rows differed from the source's leisure column by up to0.160001 hours. The cause was not verified. This project copies the published leisure column and does not claim to reconstruct it exactly from rounded components; original-data reconciliation remains pending.

## Reproduction

The main agent executed both scripts in an isolated writable copy, without changing checked-in source extracts:

```sh
python3 /tmp/leisure-trade-graphs/reproduction/scripts/collate-topic-graphs.py
python3 /tmp/leisure-trade-graphs/reproduction/scripts/plot-topic-graphs.py
```

The [comparison record](2026-11-01-topic-graphs-reproduction.json) records byte-for-byte agreement on the same retrieval date. The auditor independently compared all19 generated outputs; the21-file record also includes two copied scripts. Script execution is separate from the auditor's independent source retrieval, in-memory reconstruction, distributed-copy checks, plot-geometry checks and image inspection.

## Pending checks

Original Ramey–Francis paper inputs, Norwegian provider methodology/sample ages, original CEPII construction, current revisions and reuse conditions remain to be checked against originals. No claim of causal identification, original empirical replication or live Vercel/mobile behaviour follows from this audit. Keep the incompatible leisure populations/definitions separate and preserve the export-label and PWT-vintage disclosures.

## Technical validation

The production build passed with23 HTML pages and search assets. All1,319 internal links/images/anchors and exact copies of published graph/data assets passed checks. Existing optional i18n/404 and sitemap warnings remain. Technical integration does not validate causal or policy conclusions.
