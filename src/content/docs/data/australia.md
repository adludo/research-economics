---
title: Australian population and economy
description: Census demographics, industry employment, GDP and sector growth, with source links and reproducible charts.
---

This guide collects public sources for the [Australia case study](/case-studies/australia/). The graphs describe population, families and economic activity. They do not identify causes of growth or demographic change.

**Evidence status, 11 November 2026:** The graphs use pinned public archives of ABS Census extracts, an ABS-format employment workbook, and World Bank World Development Indicators (WDI). Official ABS, World Bank and ILO endpoints could not be retrieved through this environment's network policy. Agreement with original releases and the availability of newer releases remain **unverified**. The [source manifest](/data/australia/sources.json) records exact retrieval URLs and checksums. These are dated snapshots, not a live dashboard.

## Census population and demographics

The 2021 Census provides a common snapshot for small-area demographics. Census counts differ from **estimated resident population (ERP)**, which adjusts for undercount and residents temporarily overseas. Use ERP for population growth between censuses. Do not subtract a Census count from an ERP estimate to measure migration.

| Official source | Measures and use | Access / limits |
| --- | --- | --- |
| [2021 Australia QuickStats](https://www.abs.gov.au/census/find-census-data/quickstats/2021/AUS) | Age, sex, families, children, birthplace, language, ancestry, Indigenous status, education, income, occupation and industry summaries. | Public summaries; official page not retrieved here. Select the same year and geography before comparing. |
| [Census DataPacks](https://www.abs.gov.au/census/find-census-data/datapacks) and [Community Profiles](https://www.abs.gov.au/census/find-census-data/community-profiles) | Downloadable geographic tables. Relevant General Community Profile tables include G01 population, G04 age/sex and G29 family composition. | Public aggregates. The graphs use third-party transformations of G01 and G29; their complete source links are below. |
| [2021 Census dictionary](https://www.abs.gov.au/census/guide-census-data/census-dictionary/2021) | Variable definitions, universes, classifications and “not stated” categories. | Use with each table. A person, a family, a household and a dwelling are different units. Original dictionary not retrieved. |
| [ABS TableBuilder](https://www.abs.gov.au/statistics/microdata-tablebuilder/tablebuilder) | Custom cross-tabulations, such as age × occupation or family composition × income. | Registration and product access conditions may apply. No restricted records are stored here. |
| [National, state and territory population](https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release) | ERP, births, deaths and migration components. | Revised quarterly estimates; official release not retrieved. |
| [Regional population by age and sex](https://www.abs.gov.au/statistics/people/population/regional-population-age-and-sex/latest-release) | Age/sex estimates for subnational areas. | Geography changes and revisions matter. No series extracted here. |
| [Births, Australia](https://www.abs.gov.au/statistics/people/population/births-australia/latest-release) | Registered births, fertility rates and parental characteristics. | Registration year can differ from occurrence year; neither measure is a count of children living in families. See also [fertility definitions](/data/fertility/). |

All official links in this catalogue are source destinations to consult; their current contents and release dates were not checked because access was blocked.

### Population by state and territory

![Horizontal bars show 2021 Census population for all nine state and territory categories, with exact counts beside each bar.](/charts/australia/population.svg)

[Population CSV](/data/australia/census-population.csv) · [PNG](/charts/australia/population.png). This is the archived G01 all-person count, not a series of annual population estimates. “Other territories” is retained rather than silently dropped. No national total is inferred by adding perturbed cells.

### Age structure

![Stacked bars show the percentage under 15, aged 15–64 and aged 65 or older in each state and territory in the 2021 Census.](/charts/australia/age.svg)

[Age counts and denominators CSV](/data/australia/census-age.csv) · [PNG](/charts/australia/age.png). Eleven source age bands are grouped into under 15, 15–64 and 65+. Each denominator is the sum of the same state's age cells. ABS confidentiality perturbation means those totals can differ slightly from the separate G01 population count. Age composition alone does not measure economic dependency or unpaid care.

### Families with children

![Grouped bars compare couple and one-parent families containing at least one child under 15 in each state and territory in 2021.](/charts/australia/families.svg)

[Family counts CSV](/data/australia/census-families.csv) · [PNG](/charts/australia/families.png). The G29-derived archive identifies families with **at least one child under 15** (`HasChild=1`). We sum disjoint combinations of dependent students and non-dependent children within couple/one-parent groups. These families may also contain older children. The graph counts families, not children, births, all parents or all families. The archive drops couples without children, so it cannot support a complete family-composition percentage chart.

Birthplace, ancestry, Indigenous status, language, educational attainment, occupation and household income remain linked source topics rather than plotted extracts. Their missing/not-stated categories and distinct population universes need checking before charting. Ancestry responses can be multiple; they should not be treated as mutually exclusive population shares.

## GDP, population growth and industry output

| Official source | Measures and use | Limits |
| --- | --- | --- |
| [Australian National Accounts: National Income, Expenditure and Product](https://www.abs.gov.au/statistics/economy/national-accounts/australian-national-accounts-national-income-expenditure-and-product/latest-release) | Quarterly GDP, GDP per capita and gross value added (GVA) by industry; chain-volume measures for real growth. | Distinguish current prices from volume measures, trend from seasonally adjusted series, and quarter-on-quarter from year-on-year growth. Current release not retrieved. |
| [Australian System of National Accounts](https://www.abs.gov.au/statistics/economy/national-accounts/australian-system-national-accounts/latest-release) | Annual production, income and expenditure accounts; detailed industry output and productivity inputs. | Australian financial-year labels need care when joining calendar-year demographic data. Original tables not retrieved. |
| [State Accounts](https://www.abs.gov.au/statistics/economy/national-accounts/australian-national-accounts-state-accounts/latest-release) | Gross state product and state industry GVA. | Useful for state comparisons; state output is not household income. No extract plotted here. |
| [RBA statistical tables](https://www.rba.gov.au/statistics/tables/) | Public macroeconomic tables, including activity, prices, interest rates and exchange rates. | Supplementary catalogue; no RBA series plotted or current table contents verified here. |
| [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | Internationally documented annual population, GDP, sector and labour indicators. | The charts below use an archived WDI snapshot, with statistical estimates and revisions. Exact agreement with ABS and current WDI is unverified. |

### Population and real GDP over time

![Three panels trace Australian population, real GDP in constant 2015 US dollars, and annual GDP growth from 2000 through 2025.](/charts/australia/macro.svg)

[Annual indicator CSV](/data/australia/annual-indicators.csv) · [PNG](/charts/australia/macro.png). Population rises from about 19.03 million in 2000 to 27.61 million in 2025 in this archive. Real GDP rises from about US$874.93 billion to US$1,694.66 billion in constant 2015 prices. Archived GDP growth for 2025 is 1.35%. These are total output and population measures; GDP is neither welfare nor output per hour. Population is WDI's estimate series, not the Census count above.

### Growth by broad sector

![Three lines show annual real value-added growth in agriculture, industry including construction, and services from 2000 to 2025.](/charts/australia/sector-growth.svg)

[Annual indicator CSV](/data/australia/annual-indicators.csv) · [PNG](/charts/australia/sector-growth.png). The archived 2025 growth rates are 8.90% for agriculture, forestry and fishing, −0.58% for industry including construction, and 1.72% for services. These are **real value-added growth rates**, not employment growth or sector shares. They cannot be added to obtain GDP growth. WDI's three broad sectors are not the 19 ABS industry divisions in the employment graph.

We did not graph two discovered third-party GDP workbooks: one had ambiguous price-basis metadata and truncated observations; the other had date/metadata misalignment in some column blocks. The WDI series provide a documented alternative. Detailed ABS industry GVA remains a source for a future verified extract.

## Employment, unemployment and jobs

| Official source | Measures and use | Limits |
| --- | --- | --- |
| [Labour Force, Australia](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release) | Monthly employment, unemployment, participation, hours and employment/population ratios. | Survey estimates; seasonally adjusted, trend and original series differ. Unemployment is a share of the labour force, not of all residents. |
| [Labour Force, Australia, Detailed](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/latest-release) | Industry, occupation, age and other labour-force breakdowns. | Industry employment counts people; it is not a count of all job positions. Industry and occupation answer different questions. |
| [Jobs in Australia](https://www.abs.gov.au/statistics/labour/jobs/jobs-australia/latest-release) | Administrative employment and job characteristics, including multiple-job holders. | A person may have more than one job. Administrative coverage differs from a household survey; no extract plotted here. |
| [Census QuickStats and profiles](https://www.abs.gov.au/census/find-census-data/quickstats/2021/AUS) | Employment status, hours, occupation, industry and commuting at Census time. | A five-year snapshot cannot substitute for a monthly labour-market series. |

Official labour releases were not retrieved; the workbook below is a pinned third-party archive. The annual WDI/ILO figures are separate modeled estimates.

### Employment by industry

![Nineteen horizontal bars rank seasonally adjusted Australian employed persons by industry in May 2025, in thousands.](/charts/australia/industry-employment.svg)

[Full quarterly employment CSV, November 1984–May 2025](/data/australia/industry-employment.csv) · [Series metadata and identifiers](/data/australia/employment-metadata.json) · [PNG](/charts/australia/industry-employment.png). Workbook `Data1`, rows 1–10, identifies the units as thousands, frequency as quarter and series type as seasonally adjusted. The graph uses the last row, May 2025, and excludes the separately adjusted aggregate from the industry ranking. Health care and social assistance is the largest division in this snapshot, about 2.39 million employed people.

These are people, not job vacancies, full-time-equivalent workers or counts of all jobs. Separately seasonally adjusted divisions need not add to the adjusted national total. The archive headers do not establish every survey classification and main-job allocation rule; consult the original ABS explanatory notes before cross-dataset comparisons.

### Annual labour-market trends

![Two panels trace the employment-to-population ratio for people aged 15 or older and unemployment as a share of the labour force from 2000 to 2025.](/charts/australia/labour-market.svg)

[Annual indicator CSV](/data/australia/annual-indicators.csv) · [PNG](/charts/australia/labour-market.png). Archived 2025 values are 63.82% employed relative to the population aged 15+, and 4.09% unemployed relative to the labour force. Both are **modeled ILO estimates** distributed through WDI. The archived metadata says the ILO source was accessed on 17 January 2026. They are not the latest monthly ABS unemployment figures, and the two rates do not add to 100%.

## Indicator definitions and links

All eight annual indicators have 26 Australia observations, 2000–2025, in the pinned archive. Values retain the source precision in the download. The year is the WDI year label; exact calendar/financial-year alignment with ABS was not independently established. The mirror omits observation-level forecast/revision flags, so a 2025 row is not proof of a directly measured, forecast-free observation.

| WDI code and provider link | Measure / denominator |
| --- | --- |
| [SP.POP.TOTL](https://data.worldbank.org/indicator/SP.POP.TOTL?locations=AU) | Total population, people; estimates. |
| [NY.GDP.MKTP.KD](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD?locations=AU) | Real GDP, constant 2015 US dollars; not PPP GDP. |
| [NY.GDP.MKTP.KD.ZG](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=AU) | Annual real GDP growth, percent. |
| [NV.AGR.TOTL.KD.ZG](https://data.worldbank.org/indicator/NV.AGR.TOTL.KD.ZG?locations=AU) | Agriculture, forestry and fishing real value-added growth, percent. |
| [NV.IND.TOTL.KD.ZG](https://data.worldbank.org/indicator/NV.IND.TOTL.KD.ZG?locations=AU) | Industry including construction real value-added growth, percent. |
| [NV.SRV.TOTL.KD.ZG](https://data.worldbank.org/indicator/NV.SRV.TOTL.KD.ZG?locations=AU) | Services real value-added growth, percent. |
| [SL.EMP.TOTL.SP.ZS](https://data.worldbank.org/indicator/SL.EMP.TOTL.SP.ZS?locations=AU) | Employment / population aged 15+, percent; modeled ILO estimate. |
| [SL.UEM.TOTL.ZS](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=AU) | Unemployment / total labour force, percent; modeled ILO estimate. |

The [archived indicator metadata](/data/australia/indicator-metadata.json) includes definitions, limitations, source organisations and licenses. The [productivity guide](/productivity/calculation/) explains why GDP growth and employment levels alone do not measure labour productivity.

## Sources and reproduction

Retrieved **11 November 2026 (UTC)**. Each graph names the archive, revision, input file and retrieval date. SVG source credits link to the retrieved file. The [manifest](/data/australia/sources.json) gives every exact URL, byte count and SHA-256 hash.

| Inputs | Version and precise locator | Transformation |
| --- | --- | --- |
| [Census2021.DataPack archive](https://github.com/HughParsonage/Census2021.DataPack/tree/2cb84120792534c4d39adfa7a7d4d2abd092d981) | Revision `2cb84120792534c4d39adfa7a7d4d2abd092d981`; `tsv/STE/STE__Persons.tsv`, `STE__Age.tsv`, `STE__CoupleFamily_HasChild_HasDependentStudent_HasNonDependentChild_families.tsv`. [README](https://github.com/HughParsonage/Census2021.DataPack/blob/2cb84120792534c4d39adfa7a7d4d2abd092d981/README.md) and [transformation code](https://github.com/HughParsonage/Census2021.DataPack/blob/2cb84120792534c4d39adfa7a7d4d2abd092d981/data-raw/put-data.Rmd). | Nine geographies including Other Territories. Persons: G01 `Tot_P_P` in source code lines 588–591. Age: 11 all-person bands; no sex-table summation. Families: G29 transformation, lines 1500–1515; drops `CF_no_children_F`. Only `HasChild=1` is summed for the graph. |
| [Australian dashboard raw workbook](https://github.com/lehuukimlam/Aussie-Economy-Dashboard/blob/c70a360200771c9f9d7108fa89db84c7a2e5d250/data/Raw%20Employed%20By%20Industry.xlsx) | Revision `c70a360200771c9f9d7108fa89db84c7a2e5d250`; `Data1`, metadata rows 1–10, observations rows 11–173. [Project source description](https://github.com/lehuukimlam/Aussie-Economy-Dashboard/blob/c70a360200771c9f9d7108fa89db84c7a2e5d250/README.md). | Retain all 20 seasonally adjusted series in the CSV, 163 observations each; graph 19 industries at the last date. Copy published levels without recalculating seasonal adjustment. |
| [WDI Open Numbers archive](https://github.com/open-numbers/ddf--world_bank--world_development_indicators/tree/4252d91d988efc0f116d4fa48e92357b778729e5) | Revision `4252d91d988efc0f116d4fa48e92357b778729e5` (14 October 2026); `datapoints/ddf--datapoints--<indicator>--by--economy--year.csv`; `ddf--concepts--continuous.csv`. | Filter `economy=aus`, years 2000–2025. No interpolation, extrapolation, averaging or cross-source joins. Plot population / 1 million and GDP / 1 billion; retain unscaled values in CSV. |

The Census input TSVs are also available locally: [persons](/data/australia/census-persons.tsv), [age](/data/australia/census-age.tsv), [families](/data/australia/census-families.tsv). [Coverage counts](/data/australia/coverage.json) record the extract sizes. Census perturbation is retained; no attempt is made to “correct” small-cell differences.

The WDI metadata identifies CC BY 4.0 licensing for the selected indicators. The Census package's software license does not establish the underlying ABS data terms. Consult the [ABS copyright and licensing policy](https://www.abs.gov.au/website-privacy-copyright-and-disclaimer) and retain ABS attribution; the current policy and dashboard data reuse terms were not independently verified here.

To reproduce from checksum-pinned public inputs:

```sh
python -m pip install -r scripts/requirements-australia.txt
python scripts/collate-australia.py
python scripts/plot-australia.py
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Alternatively pass `--input-cache /path/to/files` to the collation script, using the manifest's local filenames. The static site build uses the checked-in CSVs and images and requires no Python or external data requests. These graphs describe datasets, not replications of a paper. Original-provider comparisons, additional demographic extracts and newer releases remain next checks; see the [independent audit record](https://github.com/adludo/research-economics/blob/docs/australia-data-sources/docs/audits/2026-11-11-australia-data.md).
