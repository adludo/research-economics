---
title: Research audit status
description: What has been verified in the merged wiki, and what still needs primary-source checks.
---

**Audit date: 31 October 2026 (UTC).** The independent research auditors checked `main` at commit `68eb30f465deecfa99d098b682f396013d91deb3`, including the merged working-hours graphs and glossary.

**Result:** The working-hours extracts, calculations and graphs match the pinned archived data. The paper summaries still require primary-source verification. This is not a scientific certification of the full wiki.

## Verified

| Material | Completed checks |
| --- | --- |
| [Working-hours data](/data/working-hours/) | Four archive files freshly retrieved and hash-checked; all 3,492 PWT observations, 66 observations for 2019, and 182 historical records compared independently |
| Displayed tables | All 91 rows recalculated, including rounding, endpoint changes and sample extrema |
| Recent-trend graphs | All 568 plotted vertices, country labels, endpoint labels, scales and missing-year gaps checked against the CSVs |
| Historical graphs | All 182 plotted vertices and endpoint labels checked; irregular observation dates preserved and the two datasets kept separate |
| Percentage-change graph | All 11 bar widths, signs, labels and ordering recalculated |
| Rendered figures | All three PNGs viewed; no material visual defect or clipping found |
| Reproducibility | Both generation scripts rerun in an isolated copy; generated data, page and figures match, apart from the expected new retrieval date |
| [Glossary](/glossary/) | All 25 terms reviewed for internal conceptual consistency; percentage-point arithmetic checked |

For example, the archived data support the chart's 1990–2019 changes of **−26.0% for South Korea**, **−16.6% for Japan**, and **+9.8% for China**. These are changes in annual hours, not estimates of productivity gains or welfare effects.

“Verified” here means the stated check passed. Archive consistency does not prove that the original source measurements, assumptions, or research conclusions are correct.

## Still needs checking

- **Paper identities and versions:** all 22 core papers and one review still need independent checks against DOI, publisher or official working-paper records.
- **Findings:** numerical and qualitative summaries need full-text checks and precise page/table/figure references. Read working-paper and final versions separately where estimates may differ.
- **Original data:** compare the archived PWT and historical series with original release files, paper tables and population definitions.
- **Methods and causal claims:** reproduce the papers' actual analyses before claiming their estimates have been replicated. Reproducing descriptive graphs is not the same task.
- **Source conditions:** check corrections, retractions, funding/disclosures, current provider definitions, and reuse terms.
- **Deployment:** live Vercel and mobile interaction have not been inspected by this audit.

Primary-reference requests remain blocked by the environment's proxy. Fresh probes of all 23 paper links and the two original working-hours source links returned tunnel HTTP 403. A blocked source is **unverified**, not evidence that it is fabricated.

## Corrections made

The audit clarified that “workers” and “employed persons” can use the same denominator. It also limited the original “no data downloaded” note to the literature reading guides; the working-hours collection does contain retrieved data.

## Audit records and next steps

The [detailed report](https://github.com/adludo/research-economics/blob/main/docs/audits/2026-10-31-main-audit.md) records the exact scope, methods, limitations, [source-access results](https://github.com/adludo/research-economics/blob/main/docs/audits/2026-10-31-main-source-access.json), and [reproduction comparison](https://github.com/adludo/research-economics/blob/main/docs/audits/2026-10-31-main-reproduction.json).

Complete the primary-source checks once source access is available. Re-audit any changes to data, country selection, date ranges, calculations or plotting code. See [source notes](/guides/sources/) for the collection's provenance.
