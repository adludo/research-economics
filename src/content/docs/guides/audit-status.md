---
title: Research audit status
description: What has been verified in the merged wiki, and what still needs primary-source checks.
---

**Audit date: 31 October 2026 (UTC).** The independent research auditors checked `main` at commit `68eb30f465deecfa99d098b682f396013d91deb3`, including the merged working-hours graphs and glossary.

**Result:** The working-hours extracts, calculations and graphs match the pinned archived data. The original 23 paper references and summaries still require primary-source verification; the later [fertility collection](#fertility-collection) has a separate source-reading status. This is not a scientific certification of the full wiki.

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

- **Paper identities and versions:** the 22 core papers and one review in that original audit still need independent checks against DOI, publisher or official working-paper records.
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

## Fertility collection

The later fertility extension adds six research papers and one review. Their identities and selected findings were checked against inspected author-hosted publication copies, with page locators and [pinned source hashes](/data/fertility/sources.json). This is a stronger source-reading status than the original discussion-based collection, whose historical audit above remains unchanged.

Independent research auditors checked the new summaries and page locators against those copies; no material contradiction was found in the reviewed claims. Publisher/DOI records, corrections/retractions, original data, model/empirical replication, and current demographic-provider documentation remain unchecked or inaccessible. The collection does not establish a causal effect of leisure on births. The [paper register](/papers/fertility/) states each design and its limits.

## Fertility, GDP, and working-hours graphs

The [new graph collection](/data/fertility-charts/) has a separate data audit: 2,517 same-year complete records across 67 economies, with 509 records plotted for 12 illustrative economies. Archive extraction, endpoints, log/linear scales, year colours, and graph coordinates were independently checked. Forecast rows from 2015 onward are excluded. Each graph contains a visible source reference and SVG links to the exact CSV inputs.

A material source-version label discrepancy was found before publication: the OWID archive is titled PWT10.0, while the matched GDP/person and hours values agree with CRAN-distributed PWT10.01. The figures and [provenance](/data/fertility-economy/provenance.json) now state both facts. This cross-distribution comparison does not establish original-provider identity or a causal fertility effect; original releases, revisions, reuse terms and live deployment remain separate checks.

## Recent fertility, GDP, and weekly hours — 1 November 2026

The [newer-data page](/data/recent-fertility-hours/) uses WDI and ILOSTAT copies with estimates through 2024. The independent auditor retrieved and hash-checked all 22 source inputs, reconstructed all 420 country-year rows and both pairwise extracts (420 fertility/GDP and 190 fertility/hours records), and checked all 12 coverage rows. All four rendered PNGs and every plotted SVG coordinate were inspected. Isolated reproduction produced identical files.

These checks establish consistency with the retrieved copies. Direct World Bank/ILO file agreement, original observation flags, common age coverage, series breaks, and current ILO reuse terms remain unverified. The weekly-hours series is kept separate from the older annual-hours data. See the [detailed audit](https://github.com/adludo/research-economics/blob/docs/recent-fertility-hours-graphs/docs/audits/2026-11-01-recent-economy.md) and [reproduction record](https://github.com/adludo/research-economics/blob/docs/recent-fertility-hours-graphs/docs/audits/2026-11-01-recent-economy-reproduction.json).

## Leisure-survey figures — 2 November 2026

The [leisure-source guide](/data/leisure/#reading-the-survey-figures) adds seven section-specific visuals. Independent checks retrieved and hash-verified ten source payloads and reconstructed all 555 extracted rows: 402 ATUS age/category values, 89 MTUS coverage entries, 32 HETUS country/wave values, 12 Finnish sex/year values, and 20 historical definition/year values. All five source metadata files, numerical SVG coordinates, and seven actual PNGs were inspected.

ATUS is a pooled social-time age profile, MTUS shows archive coverage, and AHTUS/OECD are conceptual diagrams with no empirical values. The latter are reading aids based on this guide, not verified current provider definitions or numerical extracts. Direct provider agreement, current revisions/terms, ATUS upper-age coding, HETUS fieldwork dates, and some sample-age definitions remain unverified. See the [detailed audit](https://github.com/adludo/research-economics/blob/docs/leisure-survey-graphs/docs/audits/2026-11-02-leisure-surveys.md) and [reproduction record](https://github.com/adludo/research-economics/blob/docs/leisure-survey-graphs/docs/audits/2026-11-02-leisure-surveys-reproduction.json).
