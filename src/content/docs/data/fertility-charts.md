---
title: Fertility, GDP, and working-hours graphs
description: Matched country-year graphs linking fertility with GDP per person and annual market working hours.
---

## Measures and scope

These graphs compare **period total fertility rate (TFR, births per woman)** with **real GDP per person** and **annual hours worked per worker**. TFR is not a count of babies, a crude birth rate, or completed family size. GDP per person is not hourly productivity, and market hours are not leisure.

We join the archived Gapminder v12 fertility series and OWID PWT series by the same country name and calendar year. **1970–2014 only:** the fertility metadata identifies 2015 onward as forecasts, so those rows are excluded. Historical fertility values include source interpolation; this project adds none.

The complete-case panel contains **2,517 country-years across 67 economies**. The graphs select 12 illustrative economies, using **509 complete country-years**. Every plotted point has all three measures; early South African fertility/GDP values are therefore excluded where hours are unavailable. The selection is not representative of the world.

## Data sources and downloads

| Input | Version and measure | Where retrieved |
| --- | --- | --- |
| Fertility | Gapminder v12 (2017), complete series, mostly based on UN WPP2017 annual estimates during 1950–2014; includes other historical inputs | [Pinned CSV](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Fertility%20rate%20%28Complete%20Gapminder%2C%20v12%29%20%282017%29/Fertility%20rate%20%28Complete%20Gapminder%2C%20v12%29%20%282017%29.csv) · [Metadata](/data/fertility-economy/gapminder-metadata.json) · [Gapminder data](https://www.gapminder.org/data/) |
| GDP and population | OWID PWT archive (labelled 10.0; matched values agree with CRAN-distributed 10.01), expenditure-side real GDP using multiple price benchmarks and population; GDP/population gives 2017 PPP international dollars per person | [Pinned CSV](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/Penn%20World%20Table%20version%2010.0.csv) · [Metadata](/data/fertility-economy/pwt-metadata.json) · [PWT release page](https://www.rug.nl/ggdc/productivity/pwt/) |
| Working hours | Same PWT archive, annual hours per worker/person engaged | Same PWT CSV; compare the existing [working-hours collection](/data/working-hours/) |
| Definition cross-check | PWT10.01 variable documentation distributed with CRAN's `pwt10` package | [Pinned codebook](https://github.com/cran/pwt10/blob/957b298fd706a567af96ccb1663ad68d5e5d07ba/man/pwt10.01.Rd) · [Stored copy](/data/fertility-economy/pwt10.01-codebook.Rd) |

**Version discrepancy:** the archive folder and original metadata say “PWT10.0”, but an additional comparison found that all 2,517 matched GDP/person and hours records agree with the CRAN-distributed PWT10.01 file. The selected GDP values differ from PWT10.0. We preserve the original archive metadata and URLs and label this discrepancy on every figure; no numeric values are silently replaced. [Comparison sources, hashes, and results](/data/fertility-economy/pwt-vintage-check.json).

The actual retrieval route is the public OWID GitHub archive at revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`. Every graph prints the archive reference and dataset names; its SVG source labels also link directly to the source CSVs. These are archived estimates, not the latest provider releases.

**Downloads:** [All matched country-years](/data/fertility-economy/matched-country-years.csv) · [Plotted country-years](/data/fertility-economy/selected-country-years.csv) · [Endpoints](/data/fertility-economy/country-endpoints.csv) · [Exact retrieval URLs and SHA-256 hashes](/data/fertility-economy/provenance.json).

## Fertility and GDP per person over time

![Twelve country panels trace fertility against real GDP per person, with point colour indicating year and labels marking the first and last available years.](/charts/fertility-economy/fertility-gdp.svg)

Each panel follows one country through time. The GDP axis is logarithmic: equal spacing means equal proportional changes. All panels use the same scales. Colour indicates calendar year, and connecting lines follow consecutive observations rather than a fitted relationship.

[Full-size SVG](/charts/fertility-economy/fertility-gdp.svg) · [PNG](/charts/fertility-economy/fertility-gdp.png).

## Fertility and annual working hours over time

![Twelve country panels trace fertility against annual market hours per worker using the same matched years as the GDP comparison.](/charts/fertility-economy/fertility-hours.svg)

The hours axis is linear and common across panels. This compares fertility with workers' average market hours, not mothers' hours, total household work, or leisure. All else need not be equal along a country's path.

[Full-size SVG](/charts/fertility-economy/fertility-hours.svg) · [PNG](/charts/fertility-economy/fertility-hours.png).

## Country time paths in their original units

![Aligned time-series panels for South Korea, China, Germany, and the United States show fertility, real GDP per person, and annual hours separately, with common scales within each row.](/charts/fertility-economy/country-time-paths.svg)

These four examples make the time direction explicit without putting unlike quantities on a dual axis. Fertility, GDP and hours retain separate units. The GDP row uses a logarithmic scale; the other rows are linear.

[Full-size SVG](/charts/fertility-economy/country-time-paths.svg) · [PNG](/charts/fertility-economy/country-time-paths.png).

## First and last matched observations

GDP values are 2017 PPP international dollars per person; hours are annual hours per worker. Display rounding does not alter the full-precision downloadable data.

<!-- BEGIN ENDPOINT TABLE -->
| Country | Years | Matched years | TFR, first → last | GDP/person, first → last | Hours/worker, first → last |
| --- | --- | ---: | ---: | ---: | ---: |
| Australia | 1970–2014 | 45 | 2.81 → 1.87 | $21,044 → $49,516 | 1,942 → 1,746 |
| United States | 1970–2014 | 45 | 2.46 → 1.95 | $25,354 → $57,117 | 1,893 → 1,758 |
| United Kingdom | 1970–2014 | 45 | 2.29 → 1.88 | $16,302 → $42,263 | 1,871 → 1,672 |
| France | 1970–2014 | 45 | 2.49 → 1.98 | $17,765 → $40,729 | 1,993 → 1,518 |
| Germany | 1970–2014 | 45 | 2.04 → 1.44 | $16,183 → $46,808 | 1,973 → 1,400 |
| Japan | 1970–2014 | 45 | 2.11 → 1.43 | $14,034 → $38,725 | 2,137 → 1,762 |
| South Korea | 1970–2014 | 45 | 4.34 → 1.26 | $2,170 → $35,525 | 2,919 → 2,070 |
| China | 1970–2014 | 45 | 5.75 → 1.61 | $1,300 → $12,232 | 1,976 → 2,179 |
| India | 1970–2014 | 45 | 5.59 → 2.38 | $1,430 → $5,165 | 2,077 → 2,119 |
| Brazil | 1970–2014 | 45 | 5.02 → 1.75 | $3,817 → $16,186 | 2,145 → 1,739 |
| Mexico | 1970–2014 | 45 | 6.83 → 2.24 | $8,905 → $18,629 | 2,182 → 2,134 |
| South Africa | 2001–2014 | 14 | 2.79 → 2.51 | $9,992 → $12,932 | 2,376 → 2,209 |
<!-- END ENDPOINT TABLE -->

South Africa starts in 2001 because the common panel requires working-hours coverage. All other selected countries have every year from 1970 to 2014. Lines do not fill absent years with zeros or interpolate over gaps.

## Interpretation in light of the literature

In the selected historical data, South Korea and China both end with lower fertility, but annual worker hours fall in South Korea and rise in China. National hours alone therefore do not provide a common explanation of these two paths.

These graphs illustrate paths, not causal effects. The [statistics guide](/guides/causality/) explains the comparison groups and assumptions needed to go further. They do not replicate the [fertility papers](/papers/fertility/) or establish that reducing working hours changes births. Age structure, birth timing, education, childcare policy, women's employment, income, and social norms may all affect the relationship.

In particular, [the modern fertility review](/papers/fertility/#doepke-et-al-2023-a-new-era-of-fertility-research) cautions against treating the historical income–fertility pattern as universal. The [household-bargaining paper](/papers/fertility/#doepke-and-kindermann-2019-bargaining-over-babies) concerns the distribution of childcare burdens, which is not measured by average national worker hours.

## Reproduce and audit

```sh
python3 scripts/collate-fertility-economy.py
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-fertility-economy.py
npm run build
```

The first script downloads and verifies pinned inputs, performs an exact complete-case country-year join, and regenerates the endpoint table. The plotting script uses only the checked-in extract. Vercel serves committed charts and downloads; Python is not needed for deployment.

Original-provider agreement, current revisions, reuse terms, and any causal interpretation require separate checks. Archive consistency, arithmetic, visual checks, and primary-paper support are distinct verification tasks.
