---
title: Leisure and productivity data
description: Sources and measurement choices for linking time use to output and welfare.
---

For collated country figures and downloadable extracts, see [Hours worked around the world](/data/working-hours/).

## National output, hours, and employment

**Starting sources:** [OECD productivity data](https://www.oecd.org/en/topics/productivity.html) · [Penn World Table](https://www.rug.nl/ggdc/productivity/pwt/) · [ILOSTAT](https://ilostat.ilo.org/) · [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators).

- Use **real GDP per hour** for labour productivity, **real GDP per person** for market income/output per resident, and employment and hours measures for labour input.
- PWT releases include output, employment, and, where available, average annual hours. Read the selected release's variable definitions and coverage before constructing ratios.
- Labour-force surveys and ILOSTAT help distinguish employed workers' hours from employment/population effects. Cross-country harmonisation is central to [Bick et al.](/papers/leisure-productivity/).
- For level comparisons across countries, select appropriate PPP-based output measures; for changes over time, use consistent real series. Do not mix nominal output, incompatible base years, or different worker coverage.
- Hours per worker, hours per employed person, hours per working-age adult, and hours per resident are different statistics. Match numerator and denominator populations.

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
