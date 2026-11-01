---
title: Leisure and productivity data
description: Sources and measurement choices for linking time use to output and welfare.
---

For collated country figures and downloadable extracts, see [Hours worked around the world](/data/working-hours/).

## Leisure and productivity graph

![Separate Norwegian and US panels compare leisure with output per hour in exactly matched years; their leisure units and populations differ.](/charts/topic-graphs/leisure-productivity.svg)

[Full-size SVG](/charts/topic-graphs/leisure-productivity.svg) · [PNG](/charts/topic-graphs/leisure-productivity.png) · [12 matched observations](/data/topic-graphs/leisure-productivity.csv) · [Source URLs and hashes](/data/topic-graphs/provenance.json).

The left panel uses five Norwegian survey dates, 1970–2010, in minutes/day. The right uses seven US age14+ residual-leisure estimates, 1950–2005, in hours/week. **The y-axes have different units and scales.** These definitions are not pooled or ranked against each other. See the [leisure graphs and definitions](/data/leisure/#leisure-graphs).

Output/hour is calculated from the PWT archive as **output-side real GDP ÷ (persons engaged × annual hours per worker)**, in 2017 PPP international dollars. GDP is already expressed in absolute dollars and persons engaged in people, so no million-unit factor is introduced. Exact calendar-year joins are used; absent years are not interpolated.

This pairs national economic aggregates with leisure aggregates, not the same individuals. US leisure covers age14+; Norwegian age coverage is unspecified in this archive; PWT measures output and work of persons engaged. Ageing, employment composition, capital and other factors can affect the paths. No regression, causal effect, TFP estimate or individual productivity claim is implied.

**PWT vintage:** the archived folder/metadata say10.0, but the earlier GDP comparison matched CRAN10.01 values. The present output/hour and income inputs are checked separately by the auditor. Original metadata and URLs remain intact; the figures flag the discrepancy rather than claiming an official-provider retrieval.

[Reproduction and limitations](#graph-reproduction). Every figure contains its retrieval source, and SVG source labels link to exact input CSVs.


## National output, hours, and employment

**Starting sources:** [OECD productivity data](https://www.oecd.org/en/topics/productivity.html) · [Penn World Table](https://www.rug.nl/ggdc/productivity/pwt/) · [ILOSTAT](https://ilostat.ilo.org/) · [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators).

- Use **real GDP per hour** for labour productivity, **real GDP per person** for market income/output per resident, and employment and hours measures for labour input.
- PWT releases include output, employment, and, where available, average annual hours. Read the selected release's variable definitions and coverage before constructing ratios.
- Labour-force surveys and ILOSTAT help distinguish employed workers' hours from employment/population effects. Cross-country harmonisation is central to [Bick et al.](/papers/leisure-productivity/).
- For level comparisons across countries, select appropriate PPP-based output measures; for changes over time, use consistent real series. Do not mix nominal output, incompatible base years, or different worker coverage.
- Hours per employed person differ from hours per working-age adult or resident. Check whether a source uses “workers” to mean employed persons, and match employment, job coverage, and denominator populations.

These are access routes for a new project, not claims that every paper used today's releases. Record release, download date, variables, units, geography, age range, employment concept, and treatment of missing hours. Provider terms and microdata access rules vary.

## Time use, recovery, and earnings

**Sources:** [ATUS files](https://www.bls.gov/tus/data.htm) · [US Current Population Survey](https://www.census.gov/programs-surveys/cps.html) · [MTUS](https://www.timeuse.org/mtus) · [OECD time-use database](https://www.oecd.org/en/data/datasets/time-use-database.html).

Time diaries can separate paid work, unpaid work, sleep, care, and discretionary leisure. Labour-force and earnings sources describe work and pay; linking them requires the exact design and identifiers allowed by the provider. A standard repeated cross-section does not become an individual panel simply because successive years are available.

For [Gibson–Shrader](/papers/leisure-productivity/#gibson-and-shrader-2018-sleep-and-labour-productivity), consult the article for exact time-use/earnings samples and sunset construction. Sunset timing is an additional identifying input, not a standard productivity field. Earnings are an outcome or proxy, not a direct observation of GDP or worker output.

See the existing [leisure data guide](/data/leisure/) for weighting, harmonisation, and activity definitions. Define whether sleep is included in leisure before comparing estimates.

## Workplace output and schedules

For [Pencavel's historical study](/papers/leisure-productivity/#pencavel-2015-diminishing-returns-to-long-working-hours), the relevant inputs are the paper's historical workplace hours and output records; national accounts cannot reproduce its worker-level relationship.

For modern research, look for shift-level or worker-level records of hours, breaks, output, quality, absence, and staffing. Account for occupation and production constraints. Public time diaries generally do not contain direct employer output, and firm records may require restricted access.

## Welfare accounting inputs

[Jones–Klenow](/papers/leisure-productivity/#jones-and-klenow-2016-valuing-leisure-beyond-gdp) combine consumption, leisure, longevity, and inequality in an explicit welfare framework. Start with the article and associated materials for original inputs, sample, and calibration. National accounts, time diaries, household distributions, and mortality sources measure different components; GDP alone is insufficient.

A new analysis should report sensitivity to leisure valuation, utility curvature, unequal time/consumption distributions, and treatment of unpaid work. Label the result **consumption-equivalent welfare**, not GDP.

## A minimal research design

| Choice | Record explicitly |
| --- | --- |
| Outcome | Total output, GDP/person, output/hour, wage, or welfare index |
| Time input | Paid hours, total work including home production, sleep, or discretionary leisure |
| Observation | Worker, workplace, region, or country-year |
| Design | Descriptive comparison, model counterfactual, policy study, or instrument |
| Confounders | Capital intensity, skills, sector, health, employment selection, and simultaneous reforms |
| Reproducibility | Data release, licence/access, weights, sample, code, and missing-value treatment |

**Next:** [Papers](/papers/leisure-productivity/) · [Findings](/findings/leisure-productivity/)

## Graph reproduction

```sh
python3 scripts/collate-topic-graphs.py
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-topic-graphs.py
npm run build
```

Sources are frozen at OWID revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`. The collation script verifies eight input checksums, retains the source metadata, and writes the downloadable extracts. Plotting uses only those extracts. SVG/PNG files are committed, so Vercel needs no Python runtime.

Original provider records, current revisions, source assumptions and reuse terms remain separate checks. These graphs do not replicate the papers' models or establish causality.
