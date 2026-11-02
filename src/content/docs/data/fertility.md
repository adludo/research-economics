---
title: "Fertility data sources"
description: "Birth-rate and fertility measures, GDP and time-use sources, and reproducible research design."
---

:::tip[Newer data through 2024]
See the [recent fertility, GDP, and working-hours graphs](/data/recent-fertility-hours/) for newer World Bank and ILOSTAT estimates. GDP uses a different PPP base, and hours are weekly rather than annual. The page explains coverage and comparability.
:::


For matched country-year data and graphs, see [Fertility, GDP, and working hours](/data/fertility-charts/). This source guide does not itself contain demographic observations.

## Choose the outcome before comparing countries

| Measure | Meaning | Main interpretation limit |
| --- | --- | --- |
| Crude birth rate | Live births during a period per 1,000 population, generally using a mid-year population denominator | Depends heavily on age structure; not a woman's expected family size |
| Period total fertility rate (TFR) | Births per woman implied by the period's age-specific fertility rates | A synthetic-period measure, not a forecast or completed fertility; postponement can change it |
| Completed cohort fertility | Average lifetime births to women in a birth cohort, assessed near the end of reproductive life | Available with a long lag; different from current-year TFR |
| Desired/intended fertility | Survey reports of preferred family size or future childbearing | Intentions can change and need not become births; respondents and question wording matter |
| Surviving children / net fertility in a model | Children surviving to the model's specified age | Check survival age and sex coverage; not automatically the demographic net reproduction rate |

These are measurement guidance, not newly downloaded estimates. Provider-specific definitions still need checking. The selected papers use different outcomes; do not pool them as a single “birth rate.”

## Demographic and macroeconomic access routes

Official endpoints below are suggested routes for a new project. Their current versions, access rules, and documentation could not be retrieved in this environment. This page provides access guidance; the separate [country-graph collection](/data/fertility-charts/) contains retrieved archived observations and documents its exact sources.

| Source | Useful measures | Appropriate use and limits |
| --- | --- | --- |
| [UN World Population Prospects](https://population.un.org/wpp/) | Births, TFR, age structure, mortality, and projections | Broad international context. Keep estimates separate from projections, specify the revision, and record population definitions. |
| [World Bank WDI](https://data.worldbank.org/indicator) | `SP.DYN.TFRT.IN` (TFR), `SP.DYN.CBRT.IN` (crude birth rate), real/PPP GDP per person | A practical country panel. Record source/revisions and do not interpret trade-offs from simple country correlations. Indicator codes are suggested selections pending live provider confirmation. |
| [Human Fertility Database](https://www.humanfertility.org/) | Detailed period/cohort fertility series and age-specific rates | Useful for distinguishing timing from completed family size; coverage is not worldwide. Check country documentation and registration/reuse conditions. |
| [OECD Family Database](https://www.oecd.org/en/data/datasets/oecd-family-database.html) | Family indicators, fertility, childcare, leave and employment context | Useful for rich-country comparisons; policy definitions, reference years and eligibility differ. |
| [PWT](/data/leisure-productivity/) and [working-hours extracts](/data/working-hours/) | Output, employment, hours, and productivity inputs | Match real-output and population concepts. The stored working-hours extracts end in 2019 and do not supply birth outcomes. |

For GDP growth use a consistent real series; for international living-standard levels use an appropriate PPP measure. Employment and hours are not interchangeable, and neither alone measures leisure.

## Household intentions and bargaining

| Paper/source | What was checked in the paper | Access route and remaining work |
| --- | --- | --- |
| Doepke–Kindermann (2019), pp. 3269–3270 | GGP data connect intentions, later births, and care allocation. One respondent reports own and partner intentions. The intentions and linked-outcomes samples differ. | [Generations and Gender Programme](https://www.ggp-i.org/). Obtain the precise release, countries, waves, permissions and linkage rules; the publication does not imply unrestricted data access. |
| Doepke–Tertilt (2018), pp. 358–361 | Uses cross-country empowerment/fertility evidence and DHS couples, including Burkina Faso and Ethiopia; Table 1 relates realised fertility to partners' desired fertility. | [DHS Program data](https://dhsprogram.com/data/) and [OECD SIGI](https://www.oecd.org/en/topics/social-institutions-and-gender-index.html). Check survey years, couple matching, age restrictions and the historical index vintage used in the paper. |

A couple-level study should record who answered each question, partner matching, intention horizon, subsequent-birth observation windows, attrition, existing children, and whether the outcome measures timing or final family size.

## Time-use and childcare

The 2023 review's §8.1, pp. 224–229, identifies parental time as a key research area. Its Figure 29 uses ATUS/CPS; Figure 30 uses MTUS, with explicit country-year and parental-sample restrictions. These are checked source attributions in the review, not a replication of its figures.

Use the existing [ATUS/MTUS/HETUS guide](/data/leisure/) to separate paid work, primary and secondary childcare, other unpaid work, sleep, and recreation. Record partners' contributions and paid childcare availability. A diary repeated cross-section does not automatically follow the same person's fertility decisions over time; linkage or a suitable panel is needed.

## Historical growth and mortality studies

The [2004 transition paper](/papers/fertility/#doepke-2004-fertility-decline-during-the-transition-to-growth) compares stylised England/Brazil/Korea paths; its Figure 1 (p. 348) cites historical fertility sources and PWT/Maddison income inputs. The [mortality paper](/papers/fertility/#doepke-2005-child-mortality-and-fertility) calibrates historical English conditions. Use the actual historical inputs and model definitions, not a current WDI extract as a substitute.

The [2003 differential-fertility study](/papers/fertility/#de-la-croix-and-doepke-2003-differential-fertility-and-growth) combines historical country growth and education/fertility distributions; pp. 1106–1108 discuss data timing and endogeneity. The [baby-boom paper](/papers/fertility/#doepke-hazan-and-maoz-2015-the-baby-boom-and-wartime-work) needs cohort fertility and historical labour-market inputs, not just annual aggregate birth rates.

## A defensible research design

1. Define births versus TFR versus completed fertility, plus the geography, age range, parity and observation period.
2. Select the direction of the question: income/productivity affecting births, or fertility affecting later output and skills.
3. Match wages/income, output per person, hourly productivity and time diaries without mixing denominators or releases.
4. Address timing, survival, childcare policy, education, family structure, and both partners' constraints.
5. Use an identification strategy appropriate to the claim. Before/after differences or cross-country regressions alone do not isolate leisure or policy effects.
6. Record source releases, retrieval dates, sample restrictions, weights, transformations and access conditions before estimating anything.

[Paper register](/papers/fertility/) · [Key findings](/findings/fertility/) · [Inspected source-copy provenance](/data/fertility/sources.json).
