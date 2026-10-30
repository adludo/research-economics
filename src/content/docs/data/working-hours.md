---
title: Hours worked around the world
description: Country working-hours data, historical comparisons, downloadable extracts, and source links.
---

## What this collection measures

**Annual hours per worker** measure market working time across a year. They reflect weekly schedules, part-time work, holidays, absences, and the composition of employment. They are not hours per resident, a statutory working week, or a direct measure of leisure.

This page collates two retrieved datasets: a **2019 comparison from Penn World Table 10.0** and a **1870–2000 historical comparison from Huberman and Minns**, both distributed by Our World in Data (OWID). They are separate series and should not be spliced together.

:::note[Release and retrieval status]
Retrieved on **30 October 2026** from OWID's public GitHub archive at a fixed revision. Direct official-provider and chart endpoints were blocked in this environment. The tables below were calculated from the retrieved CSV files and checked against their archived metadata; they are **not current-year estimates** or independently verified transcriptions of the original publications.
:::

## Data sources and downloads

| Collection | Measures and coverage | Source data and access |
| --- | --- | --- |
| Penn World Table (PWT) 10.0 | Annual hours per worker; 69 economies with at least one hours observation, 1950–2019, in this extract. The broader PWT database covers 183 countries; hours coverage is narrower. | [Official PWT releases](https://www.rug.nl/ggdc/productivity/pwt/) · [Archived OWID CSV](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/Penn%20World%20Table%20version%2010.0.csv) · [Archived metadata](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/datapackage.json) |
| Huberman and Minns (2007) | Selected observations, 1870–2000, for 14 economies; weekly and annual work hours, weeks worked, and holidays. Definitions and sources change over time. | [Published article](https://www.sciencedirect.com/science/article/pii/S0014498307000058) · [Archived OWID CSV](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Working%20Hours%20Data%20-%20Huberman%20%26%20Minns%20%282007%29/Working%20Hours%20Data%20-%20Huberman%20%26%20Minns%20%282007%29.csv) · [Archived metadata](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Working%20Hours%20Data%20-%20Huberman%20%26%20Minns%20%282007%29/datapackage.json) |

**Download the collated data:** [PWT annual-hours observations, all available years](/data/working-hours/pwt-hours.csv) · [2019 country comparison](/data/working-hours/pwt-hours-2019.csv) · [Historical hours observations](/data/working-hours/historical-hours.csv) · [Provenance and source checksums](/data/working-hours/provenance.json).

Missing observations are omitted from the PWT extract, not replaced with zeros. Country labels follow OWID. CSV values retain the source precision; displayed hours are rounded to whole hours.

## How working hours changed over time

The PWT charts use 12 selected economies to show contrasting paths across regions: Australia, the United States, the United Kingdom, France, Germany, Japan, South Korea, China, India, Brazil, Mexico, and South Africa. This is an illustrative selection, not a representative sample or a world average. The historical chart includes all 14 economies in that separate dataset.

### Recent country trends, 1970–2019

![Twelve country panels of annual hours per worker. South Korea, Japan, and several European countries trend down; China and India end above their 1990 levels. South Africa has shorter coverage and a gap.](/charts/working-hours/country-trends.svg)

Each panel uses the same axes. Labels show 2019 hours; missing observations remain gaps. South Africa starts in 2001 and has no observation in 2015. The other selected series cover the full displayed period. Straight or smooth-looking portions may reflect source estimation; they are not proof that workers' schedules never changed.

[Open full-size SVG](/charts/working-hours/country-trends.svg) · [Download PNG](/charts/working-hours/country-trends.png) · [Underlying PWT observations](/data/working-hours/pwt-hours.csv).

### Change over a common period, 1990–2019

![Bar chart of annual-hours changes for eleven selected economies from 1990 to 2019: South Korea has the largest decline in this selection, while China and India show increases.](/charts/working-hours/change-1990-2019.svg)

South Korea's hours fell **26.0%**, Japan's **16.6%**, and Germany's **12.4%** in this extract. China rose **9.8%** and India **2.1%**. These are endpoint changes in hours, not annual growth rates or changes in productivity. South Africa is omitted because 1990 is unavailable.

[Open full-size SVG](/charts/working-hours/change-1990-2019.svg) · [Download PNG](/charts/working-hours/change-1990-2019.png).

<!-- BEGIN CHART CHANGE TABLE -->
| Country | Annual hours, 1990 | Annual hours, 2019 | Change |
| --- | ---: | ---: | ---: |
| South Korea | 2,674 | 1,980 | -26.0% |
| Japan | 2,028 | 1,691 | -16.6% |
| Germany | 1,583 | 1,386 | -12.4% |
| Brazil | 1,879 | 1,708 | -9.1% |
| France | 1,645 | 1,505 | -8.5% |
| Australia | 1,864 | 1,727 | -7.4% |
| United Kingdom | 1,746 | 1,668 | -4.5% |
| Mexico | 2,176 | 2,137 | -1.8% |
| United States | 1,796 | 1,765 | -1.7% |
| India | 2,078 | 2,123 | +2.1% |
| China | 1,975 | 2,169 | +9.8% |
<!-- END CHART CHANGE TABLE -->

### Long-run historical trends, 1870–2000

![Fourteen historical country panels show annual hours lower in 2000 than in 1870, with different paths and some reversals between the selected observations.](/charts/working-hours/historical-trends.svg)

All 14 economies have lower endpoint hours in this compilation. The decline was not uninterrupted: some series show reversals. Dots are recorded observations; lines connect them as visual guides and do not supply missing annual estimates. Source and population definitions change over time, as detailed in the historical comparison below. Do not join these lines to the PWT series.

[Open full-size SVG](/charts/working-hours/historical-trends.svg) · [Download PNG](/charts/working-hours/historical-trends.png) · [Underlying historical observations](/data/working-hours/historical-hours.csv).

## Annual hours per worker in 2019

All available economies for the same year are shown alphabetically. Choosing 2019 avoids mixing countries' latest available years and predates pandemic disruptions. It does not remove national measurement differences.

<!-- BEGIN PWT TABLE -->
| Country/economy | Year | Annual hours per worker |
| --- | --- | ---: |
| Argentina | 2019 | 1,609 |
| Australia | 2019 | 1,727 |
| Austria | 2019 | 1,611 |
| Bangladesh | 2019 | 2,419 |
| Belgium | 2019 | 1,586 |
| Brazil | 2019 | 1,708 |
| Bulgaria | 2019 | 1,645 |
| Cambodia | 2019 | 2,475 |
| Canada | 2019 | 1,689 |
| Chile | 2019 | 1,914 |
| China | 2019 | 2,169 |
| Colombia | 2019 | 1,968 |
| Costa Rica | 2019 | 2,069 |
| Croatia | 2019 | 1,831 |
| Cyprus | 2019 | 1,805 |
| Czechia | 2019 | 1,788 |
| Denmark | 2019 | 1,381 |
| Dominican Republic | 2019 | 2,142 |
| Ecuador | 2019 | 1,552 |
| Estonia | 2019 | 1,797 |
| Finland | 2019 | 1,591 |
| France | 2019 | 1,505 |
| Germany | 2019 | 1,386 |
| Greece | 2019 | 2,036 |
| Hong Kong | 2019 | 2,148 |
| Hungary | 2019 | 1,725 |
| Iceland | 2019 | 1,454 |
| India | 2019 | 2,123 |
| Indonesia | 2019 | 2,020 |
| Ireland | 2019 | 1,772 |
| Israel | 2019 | 1,901 |
| Italy | 2019 | 1,718 |
| Japan | 2019 | 1,691 |
| Latvia | 2019 | 1,865 |
| Lithuania | 2019 | 1,886 |
| Luxembourg | 2019 | 1,506 |
| Malaysia | 2019 | 2,197 |
| Malta | 2019 | 1,915 |
| Mexico | 2019 | 2,137 |
| Myanmar | 2019 | 2,447 |
| Netherlands | 2019 | 1,440 |
| New Zealand | 2019 | 1,779 |
| Norway | 2019 | 1,384 |
| Pakistan | 2019 | 1,967 |
| Peru | 2019 | 2,140 |
| Philippines | 2019 | 2,168 |
| Poland | 2019 | 2,023 |
| Portugal | 2019 | 1,865 |
| Romania | 2019 | 1,792 |
| Russia | 2019 | 1,965 |
| Singapore | 2019 | 2,330 |
| Slovakia | 2019 | 1,695 |
| Slovenia | 2019 | 1,593 |
| South Africa | 2019 | 2,191 |
| South Korea | 2019 | 1,980 |
| Spain | 2019 | 1,686 |
| Sri Lanka | 2019 | 1,923 |
| Sweden | 2019 | 1,605 |
| Switzerland | 2019 | 1,557 |
| Taiwan | 2019 | 2,085 |
| Thailand | 2019 | 2,093 |
| Turkey | 2019 | 1,832 |
| United Kingdom | 2019 | 1,668 |
| United States | 2019 | 1,765 |
| Uruguay | 2019 | 1,533 |
| Vietnam | 2019 | 2,132 |
<!-- END PWT TABLE -->

**Interpretation:** Variation in hours is not a ranking of effort or productivity. Differences in part-time work, employment composition, informality, and measurement can affect country levels. Africa and other regions are sparsely represented in this hours series; this is not a complete world sample.

## Historical comparison: 1870 and 2000

**Citation:** Michael Huberman and Chris Minns (2007), “The times they are not changin’: Days and hours of work in Old and New Worlds, 1870–2000.” *Explorations in Economic History* 44(4), 538–567. The table uses the annual-hours column in OWID's archived dataset.

<!-- BEGIN HISTORICAL TABLE -->
| Country | Annual hours, 1870 | Annual hours, 2000 | Change |
| --- | ---: | ---: | ---: |
| Australia | 2,792 | 1,797 | -35.6% |
| Belgium | 3,483 | 1,547 | -55.6% |
| Canada | 2,845 | 1,825 | -35.9% |
| Denmark | 3,434 | 1,473 | -57.1% |
| France | 3,168 | 1,443 | -54.5% |
| Germany | 3,284 | 1,463 | -55.5% |
| Ireland | 3,108 | 1,686 | -45.8% |
| Italy | 3,000 | 1,612 | -46.3% |
| Netherlands | 3,274 | 1,352 | -58.7% |
| Spain | 2,968 | 1,815 | -38.8% |
| Sweden | 3,436 | 1,645 | -52.1% |
| Switzerland | 3,195 | 1,597 | -50.0% |
| United Kingdom | 2,755 | 1,653 | -40.0% |
| United States | 3,096 | 1,878 | -39.3% |
<!-- END HISTORICAL TABLE -->

The metadata labels work-hours measures as full-time production workers in non-agricultural activities. It also identifies changing original sources: the annual series uses historical reconstructions for early years and the Groningen/Conference Board Total Economy Database for 1950–2000. Treat this as a historical compilation with source transitions, not an unchanged population definition over 130 years. The weekly-hours series has its own sources; for 2000 OWID averages the male and female weekly estimates. That transformation is not a population-weighted average.

## Research findings supported by these extracts

<!-- BEGIN DATA SUMMARY -->
- The PWT extract contains **3,492 non-missing country-year observations** for **69 economies**, with **66** observed in 2019.
- In this 2019 sample, annual hours range from **1,381 in Denmark** to **2,475 in Cambodia**. These are sample extremes, not world-wide bounds.
- Annual hours fall between 1870 and 2000 in **14 of 14** historical endpoint comparisons. Changing source coverage limits a like-for-like interpretation.
<!-- END DATA SUMMARY -->

These are descriptive statements about the retrieved data. They do not show that reducing hours causes higher GDP, productivity, or welfare. Lost paid work can become household production or involuntary unemployment rather than discretionary leisure. See [leisure and productivity findings](/findings/leisure-productivity/).

## Other sources for broader or newer comparisons

These are official access routes, **not datasets downloaded for the tables above**. Check their current releases, definitions, and access conditions before use.

| Source | What to retrieve | Main caution |
| --- | --- | --- |
| [ILOSTAT working-time statistics](https://ilostat.ilo.org/topics/working-time/) and [bulk downloads](https://ilostat.ilo.org/data/bulk/) | Mean weekly hours actually worked, usual hours, and distributions, with sex and other breakdowns where available | Keep actual and usual hours separate; inspect age, job coverage, employment status, and whether observations are reported or modelled. |
| [OECD hours worked](https://www.oecd.org/en/data/indicators/hours-worked.html) | Average annual hours actually worked per worker and country metadata | Differences in sources and methods constrain country-level comparisons; consult the series' comparability notes. |
| [Eurostat working-time statistics](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Hours_of_work_-_annual_statistics) | Actual/usual weekly hours and full-time/part-time breakdowns from EU labour-force surveys | Reference-week hours are not annual hours divided by 52; check whether the measure covers the main job or all jobs. |
| [PWT official releases](https://www.rug.nl/ggdc/productivity/pwt/) | Annual hours, employment, output, and productivity measures | Do not combine vintages without recording revisions. A newer release may differ from this archived 10.0 extract. |
| [ATUS, MTUS, HETUS, and national diaries](/data/leisure/) | Paid work, unpaid work, sleep, care, and recreation | Needed to study leisure itself; market-hours series alone cannot describe the full time budget. |

## Reproduce or update

Run `python3 scripts/collate-working-hours.py` from the repository root. It downloads the pinned source CSVs and metadata, verifies SHA-256 checksums, writes the downloadable extracts, and regenerates the marked tables on this page. It uses Python's standard library and needs access to `raw.githubusercontent.com`.

To regenerate the charts without downloading new data:

```sh
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-working-hours.py
```

Matplotlib is needed only for regeneration. SVG and PNG files are committed, so Vercel builds need no Python or chart dependencies. The chart script reads the checked-in CSVs, leaves missing years as gaps, and regenerates the endpoint table above. On small screens, use the full-size SVG links to zoom into country panels.

To adopt another release, review its definitions and coverage before deliberately updating the source revision and checksums. Keep the release, observation year, and retrieval date separate. Do not describe this snapshot as the latest release.

For an empirical GDP comparison, pair hours with compatible real output and employment measures; see the [productivity data guide](/data/leisure-productivity/). For the relationship between income and working time across rich and poor countries, start with [Bick, Fuchs-Schündeln, and Lagakos](/papers/leisure-productivity/#bick-fuchs-schündeln-and-lagakos-2018-hours-across-income-levels).
