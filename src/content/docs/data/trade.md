---
title: Trade and GDP data sources
description: Sources for output, income, trade flows, policy restrictions, and historical autarky.
---

Use separate measures for **economic performance**, **trade exposure**, and **policy restrictions**. Low trade/GDP alone does not establish that a government closed its economy.

## World Development Indicators (WDI)

**Sources:** [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) · [Indicator catalogue](https://data.worldbank.org/indicator).

- **Measures:** GDP, GDP per capita, growth, investment, population, and trade indicators for modern country panels.
- **Useful series:** `NY.GDP.MKTP.KD.ZG` (GDP growth), `NY.GDP.PCAP.KD` (real GDP per capita), `NY.GDP.PCAP.PP.KD` (PPP real GDP per capita), and `NE.TRD.GNFS.ZS` (trade in goods and services as a share of GDP).
- **Use:** Constant-price measures for growth; PPP-adjusted measures for cross-country living-standard comparisons.
- **Limitations:** Missing observations, revisions, changing PPP benchmarks, and uneven national-account quality. A trade/GDP ratio is an outcome, not a policy index.
- **Record:** Indicator code, units, base/PPP vintage, country sample, retrieval date, and treatment of missing years.

## Penn World Table (PWT)

**Source:** [Groningen Growth and Development Centre: Penn World Table](https://www.rug.nl/ggdc/productivity/pwt/).

- **Measures:** Comparable output, expenditure, inputs, and productivity.
- **Use:** Cross-country growth and productivity analysis. Choose the output-side or expenditure-side measure appropriate to the research question.
- **Limitations:** Dataset revisions and PPP construction affect comparisons. Modern releases are not necessarily the releases used in older studies.
- **Record:** Release, variable definitions, price concept, and sample. Follow the release's citation and usage terms.

## Maddison Project Database

**Source:** [Groningen: Maddison Project Database](https://www.rug.nl/ggdc/historicaldevelopment/maddison/).

- **Measures:** Long-run historical GDP per capita and population.
- **Use:** Context for historical periods of isolation and opening.
- **Limitations:** Early values are reconstructions with substantial uncertainty. They do not replace episode-specific prices or customs evidence.
- **Record:** Version, geographical boundaries, historical units, and interpolation choices.

## Merchandise trade: UN Comtrade and WITS

**Sources:** [UN Comtrade](https://comtradeplus.un.org/) · [World Integrated Trade Solution (WITS)](https://wits.worldbank.org/).

- **Measures:** Imports and exports by reporting country, partner, product, and period.
- **Use:** Trade exposure, partner dependence, and composition. WITS provides access to selected trade and tariff sources; it is not a substitute name for all Comtrade access.
- **Access:** Check current account, API, download, and rate-limit requirements at the provider. No credentials are needed to read this wiki.
- **Limitations:** Merchandise excludes services; reporter/partner discrepancies, valuation conventions, classification changes, and missing reports require attention. Missing trade should not automatically become zero.
- **Record:** Reporter, partner, flow, classification/revision, valuation, year, and download date.

## Trade policy: WITS and UNCTAD TRAINS

**Sources:** [WITS](https://wits.worldbank.org/) · [UNCTAD TRAINS](https://trainsonline.unctad.org/).

- **Measures:** Applied and preferential tariffs, and non-tariff measures.
- **Use:** Policy restrictions rather than trade volumes; important when interpreting the [Rodríguez–Rodrik critique](/papers/trade/#rodríguez-and-rodrik-2001-a-methodological-critique).
- **Limitations:** Applied versus bound rates, preferences, exemptions, and tariff weighting matter. Recorded non-tariff measures are not automatically comparable estimates of restrictiveness. Tariffs alone do not capture closure.
- **Record:** Rate type, product code/version, partner treatment, aggregation weights, and policy year.

## Wacziarg–Welch classifications and dates

**Starting points:** [Article and associated materials](https://doi.org/10.1093/wber/lhn007) · [Romain Wacziarg's research page](https://www.anderson.ucla.edu/faculty-and-research/global-economics-and-management/faculty/wacziarg).

- **Measures:** Openness classifications and liberalisation dates for before/after or event-study designs.
- **Limitations:** Binary classifications simplify complex regimes. Check country histories, coding rules, reform reversals, and simultaneous reforms. The author page is a discovery route, not a guaranteed direct dataset download.
- **Record:** Exact file/version, country coding, reform date, and matching to the article's sample.

## Historical prices, customs, and national accounts

For [the US embargo](/papers/trade/#irwin-2005-the-jeffersonian-embargo) and [Japan's opening](/papers/trade/#bernhofen-and-brown-2005-japans-opening), consult each paper's cited historical records and any associated materials. Autarky prices, commodity quantities, and reconstructed national accounts are central. Modern WDI or Comtrade series cannot supply these nineteenth-century observations.

For [the Suez closure study](/papers/trade/#feyrer-2021-the-suez-canal-natural-experiment), shipping-distance changes are an additional input, not a standard GDP or tariff field.

## A defensible empirical comparison

1. Define closure: policy restrictions, an embargo, or measured trade exposure.
2. Separate total GDP, real GDP per capita, productivity, consumption, and welfare.
3. Match policy timing to comparable outcome data and record the data vintage.
4. Identify the counterfactual; before/after growth differences alone do not isolate trade reform.
5. Report robustness to institutions, contemporaneous reforms, sample composition, and measurement choices.
