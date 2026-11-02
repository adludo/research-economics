---
title: Recent fertility, GDP, and working-hours graphs
description: Newer World Bank and ILOSTAT estimates through 2024, with country paths, source links, and coverage notes.
---

## What is newer

These graphs add **World Bank fertility and GDP estimates through 2024** and **ILOSTAT weekly working hours through 2024 for nine selected countries**. They complement the [1970–2014 fertility graphs](/data/fertility-charts/) and [annual-hours graphs ending in 2019](/data/working-hours/).

The newer inputs measure similar variables, with two important changes: GDP uses **constant 2021 PPP international dollars**, and working time is **mean weekly hours actually worked per employed person**. The older GDP series uses 2017 PPP dollars and its hours are annual. Do not splice the releases, multiply these weekly hours by 52, or interpret a difference between releases as economic growth.

TFR is period total fertility rate, in births per woman. It is not a birth count or completed family size. GDP per person is not productivity, and market working time is not leisure. These are descriptive comparisons, not estimates of causal effects. See the [fertility literature](/papers/fertility/) and [measurement definitions](/data/fertility/).

## Sources and retrieval

| Variable | Reputable provider and definition | Exact retrieved copy |
| --- | --- | --- |
| Total fertility rate | [World Bank WDI, SP.DYN.TFRT.IN](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN), drawing on UN Population Division and national/Eurostat statistics; births per woman implied by that year's age-specific rates | [Versioned CSV](https://github.com/open-numbers/ddf--world_bank--world_development_indicators/blob/4252d91d988efc0f116d4fa48e92357b778729e5/datapoints/ddf--datapoints--sp_dyn_tfrt_in--by--economy--year.csv) |
| Real GDP per person | [World Bank WDI, NY.GDP.PCAP.PP.KD](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD); constant 2021 international dollars, adjusted for purchasing power | [Versioned CSV](https://github.com/open-numbers/ddf--world_bank--world_development_indicators/blob/4252d91d988efc0f116d4fa48e92357b778729e5/datapoints/ddf--datapoints--ny_gdp_pcap_pp_kd--by--economy--year.csv) |
| Weekly working hours | [ILOSTAT working time](https://ilostat.ilo.org/topics/working-time/), `HOW_TEMP_SEX_ECO_NB`: mean weekly hours actually worked per employed person; total sexes (`SEX_T`), total economic activity (`ECO_AGGREGATE_TOTAL`) | [Versioned country CSV collection](https://github.com/open-numbers/ddf--ilo--ilostat/tree/c4dd68c687df8162835e1684cffec8723b19eee8/datapoints/ddf--datapoints--how_temp_sex_eco_nb--by--ref_area--sex--classif1--time) · individual file URLs in the download manifest and SVG country titles |

Retrieved **1 November 2026** from Open Numbers' versioned GitHub mirrors. The WDI copy is dated **14 October 2026**; the ILO copy **27 February 2026**. These dates identify the copies, not the year each country was surveyed. [Stored indicator definitions and country labels](/data/recent-economy/indicator-metadata.json) · [All 22 input URLs and SHA-256 hashes](/data/recent-economy/sources.json).

**Verification limit:** direct provider requests were blocked by the environment's network policy. The original WDI/ILO files have not been compared with these copies. The sources' provenance, extraction, and chart checks are recorded in [the independent audit](https://github.com/adludo/research-economics/blob/docs/recent-fertility-hours-graphs/docs/audits/2026-11-01-recent-economy.md). Provider reputation does not verify a mirror's transcription.

## Fertility and GDP through 2024

![Twelve country panels show fertility against real GDP per person from 1990 to 2024, with calendar-year colours and first/last year labels.](/charts/recent-economy/fertility-gdp.svg)

All 12 countries have **35 matched years, 1990–2024**: **420 country-years**. The horizontal axis is logarithmic, so equal distances represent equal proportional changes. Lines follow consecutive calendar years. No fitted relationship is shown. Unlike the older complete-case panel, this comparison does not require working-hours data.

[Full-size SVG](/charts/recent-economy/fertility-gdp.svg) · [PNG](/charts/recent-economy/fertility-gdp.png) · [Plotted data](/data/recent-economy/fertility-gdp.csv).

## Fertility and weekly hours through 2024

![Nine country panels show fertility against weekly hours actually worked per employed person, using same-year values through 2024.](/charts/recent-economy/fertility-hours.svg)

The **190 matched country-years** use the nine countries with a 2024 hours value. Some series begin after 2000; India begins in 2018 and Brazil in 2012. Every point joins fertility and hours in the same country and year. The plot does not measure parents' hours, unpaid childcare, or the work–family balance of the same individuals.

[Full-size SVG](/charts/recent-economy/fertility-hours.svg) · [PNG](/charts/recent-economy/fertility-hours.png) · [Plotted data](/data/recent-economy/fertility-hours.csv).

## Weekly working-hours trends

![Nine country panels show weekly hours through 2024 with common zero-to-sixty-hour scales and dots for the available annual estimates.](/charts/recent-economy/working-hours.svg)

Each panel uses the same linear scale. Endpoint labels show weekly hours in 2024. Dots mark published estimates; they do not imply a survey in every year. Changing surveys, source selection, employment composition, and treatment of absences can affect comparisons. A lower national market-hours average does not establish that leisure increased.

[Full-size SVG](/charts/recent-economy/working-hours.svg) · [PNG](/charts/recent-economy/working-hours.png) · [Underlying hours in the matched extract](/data/recent-economy/fertility-hours.csv).

## Country time paths

![Separate time-series rows show fertility, GDP per person, and weekly hours for South Korea, Germany, the United States, and India over 2000–2024. India's hours row starts in 2018.](/charts/recent-economy/country-time-paths.svg)

The four examples retain separate units and common scales within each row. Each variable uses its own available years, so an absent hours estimate does not remove a fertility or GDP estimate. The GDP row uses a logarithmic scale. Lines stop at missing years rather than filling them.

[Full-size SVG](/charts/recent-economy/country-time-paths.svg) · [PNG](/charts/recent-economy/country-time-paths.png) · [Country-year data, with missing cells retained](/data/recent-economy/country-years.csv).

## Actual coverage

The sample retains the original 12 illustrative countries for fertility/GDP. The nine-country hours sample is the subset with a 2024 value, not a representative world sample. Australia, Japan, and China remain in the coverage register but are excluded from the recent hours graphs. Their newer-source endpoints do not extend the old annual-hours graphs equally far. Counts refer to available years inside the chosen windows, not continuous survey coverage.

<!-- BEGIN COVERAGE -->
| Country | GDP + fertility years | Weekly-hours years (count) | Latest weekly hours | In recent hours graphs? |
| --- | --- | --- | ---: | --- |
| Australia | 1990–2024 (35) | 2000–2020 (21) | 32.29 (2020) | No |
| United States | 1990–2024 (35) | 2003–2024 (22) | 37.56 (2024) | Yes |
| United Kingdom | 1990–2024 (35) | 2000–2024 (25) | 35.08 (2024) | Yes |
| France | 1990–2024 (35) | 2000–2024 (25) | 35.49 (2024) | Yes |
| Germany | 1990–2024 (35) | 2000–2024 (25) | 33.27 (2024) | Yes |
| Japan | 1990–2024 (35) | 2009–2020 (11) | 36.60 (2020) | No |
| South Korea | 1990–2024 (35) | 2000–2024 (25) | 37.88 (2024) | Yes |
| China | 1990–2024 (35) | 2005–2016 (11) | 46.10 (2016) | No |
| India | 1990–2024 (35) | 2018–2024 (7) | 45.72 (2024) | Yes |
| Brazil | 1990–2024 (35) | 2012–2024 (13) | 38.86 (2024) | Yes |
| Mexico | 1990–2024 (35) | 2002–2024 (23) | 42.19 (2024) | Yes |
| South Africa | 1990–2024 (35) | 2000–2024 (25) | 42.39 (2024) | Yes |
<!-- END COVERAGE -->

[Download coverage table](/data/recent-economy/coverage.csv). No world average, country weighting, imputation, or interpolation is added by this project. The 2024 cutoff excludes later source rows, including GDP and hours entries for 2025; it does not establish that every retained value is measured rather than estimated.

## Source limitations

WDI's fertility metadata describes vital registration, census/survey estimates, interpolation, and extrapolation. The flat copy does not identify an exact WPP release or row-level estimate/forecast flags. GDP metadata describes PPP extrapolation and linked national-accounts series. These are published statistical estimates, not uniformly direct measurements.

The ILO mirror's [processing code](https://github.com/open-numbers/ddf--ilo--ilostat/blob/c4dd68c687df8162835e1684cffec8723b19eee8/etl/scripts/etl_manual.py) and [notes](https://github.com/open-numbers/ddf--ilo--ilostat/blob/c4dd68c687df8162835e1684cffec8723b19eee8/README.md) select a source per country using the ordering of ILO source metadata, then source notes. They discard source identifiers, observation flags, and notes. We cannot inspect each point's survey basis or series breaks from these CSVs. The indicator has no age dimension; common age coverage across countries has not been established. The total-sex, total-sector filter does not resolve those limits.

WDI's stored indicator metadata lists **CC BY 4.0**. Consult [World Bank terms](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets) and [ILO terms](https://www.ilo.org/global/copyright/lang--en/index.htm) before redistribution beyond this attributed extract; current ILO reuse conditions have not been verified here.

## Reproduce

```sh
python3 scripts/collate-recent-economy.py
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-recent-economy.py
npm run build
```

The collator verifies all pinned hashes before writing. It copies the selected published values and performs exact country-code/year joins separately for each pair. Full-precision CSVs and [provenance](/data/recent-economy/provenance.json) accompany the figures. All SVGs and PNGs print retrieval references; the SVG source labels are clickable. Vercel serves these committed assets without running Python.
