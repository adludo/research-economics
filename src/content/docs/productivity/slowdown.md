---
title: Interpreting the productivity slowdown
description: What slower productivity growth means, a dated country comparison, and how to check explanations and current claims.
---

## What the productivity problem means

The usual concern is **slower growth in real output per hour**, relative to an earlier period. A positive growth rate of 1% still raises productivity levels; it raises them more slowly than 2%. Over twenty years, purely hypothetical constant growth of 1% produces about a 22.0% increase, while 2% produces about 48.6%. The difference compounds.

This framing explains why productivity is discussed as a problem even when GDP or employment is rising. It also distinguishes a measured historical pattern from agreement about its causes. Countries, sectors, measures and comparison periods need to be specified. A broad concern about weak growth does not imply that every modern economy has the same trajectory.

[Goldin and coauthors](/papers/productivity/#goldin-and-coauthors-2024) and [Byrne–Fernald–Reinsdorf](/papers/productivity/#byrne-fernald-and-reinsdorf-2016) are further-reading routes into the slowdown and measurement debates. Their full texts were not accessible here, so this page does not attribute specific estimates or conclusions to them. The numerical comparison below is our own archive calculation.

## A reproducible historical comparison

For eight illustrative advanced economies, compute:

```text
P_t = real GDP using national-accounts growth rates / (persons engaged × annual hours per person)
Annualized growth (%) = 100 × [(P_end / P_start)^(1 / number of years) − 1]
```

The first window spans twelve years; the second spans nine. The table shows geometric annualized growth, not the arithmetic mean of annual rates. Change is the second rate minus the first, in percentage points.

<!-- BEGIN GROWTH TABLE -->
| Country | 1995–2007 | 2010–2019 | Change (percentage points) |
| --- | ---: | ---: | ---: |
| Australia | 1.97% | 0.93% | -1.03 |
| Canada | 1.39% | 1.05% | -0.34 |
| France | 1.56% | 0.90% | -0.66 |
| Germany | 1.56% | 0.89% | -0.67 |
| Japan | 1.69% | 0.88% | -0.82 |
| South Korea | 5.39% | 2.64% | -2.75 |
| United Kingdom | 2.19% | 0.34% | -1.85 |
| United States | 2.23% | 0.75% | -1.48 |
<!-- END GROWTH TABLE -->

All eight selected economies have slower growth in the second window in this archive. This illustrates the historical pattern; it is **not a representative survey, an OECD/world average, a test of expert consensus, or a causal estimate**. The comparison leaves out the 2008–2009 contraction and ends before the pandemic. Other windows and revised releases can change the results.

### Source and coverage

The numerator is PWT's `rgdpna` concept: real GDP at constant 2017 national prices, intended here for **within-country growth**, not a cross-country ranking of productivity levels. The denominator uses persons engaged and their average annual hours. OWID already expresses GDP and employment in absolute units, so no extra million-unit factor is applied.

Retrieved **3 November 2026** from a pinned [OWID PWT CSV](https://github.com/owid/owid-datasets/blob/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/Penn%20World%20Table%20version%2010.0.csv). The folder/metadata say PWT10.0; a separate check found that all **200 selected country-years** of GDP, employment and hours agree with the pinned CRAN-distributed PWT10.01 copy. That comparison does not authenticate the original provider release. See [variable definitions](/data/productivity/pwt-codebook.Rd), [original archive metadata](/data/productivity/pwt-metadata.json), [comparison record](/data/productivity/vintage-check.json), and [retrieval URLs/hashes](/data/productivity/sources.json).

**Downloads:** [200 country-years and inputs](/data/productivity/country-years.csv) · [Eight growth comparisons](/data/productivity/growth-comparison.csv) · [Transformations and limits](/data/productivity/provenance.json).

This is an archived comparison ending in **2019**, not evidence about the latest 2026 outcome. Direct provider agreement, current revisions and current reuse conditions remain unverified. No interpolation, country weighting or missing-value replacement is added.

## Explaining a slowdown is a separate task

The [growth-accounting framework](/productivity/calculation/#total-factor-productivity-and-growth-accounting) separates measured contributions before asking what caused them.

| Possible channel | What to measure | What the measure alone cannot establish |
| --- | --- | --- |
| Less capital deepening | Capital services per hour and asset composition | Why investment changed, or a causal policy effect |
| Slower improvement in labour composition | Composition-adjusted labour services relative to raw hours | The causal return to education or changes in unobserved skills |
| Slower residual MFP growth | Consistently measured output and combined inputs | Whether technology, utilisation, management, omitted inputs or measurement error is responsible |
| Shifts between firms or sectors | Matched output/hours shares and within-sector productivity | A universal change in individual worker efficiency |
| Output/input measurement changes | Deflators, quality adjustment, intangibles and production boundaries | That every unexplained change is a statistical mistake |

These are diagnostic possibilities, not findings that each caused the slowdown everywhere. Investment, diffusion, competition, skills and institutions may interact. Establishing their effects requires a research design beyond the accounting identity; see [causality versus correlation](/guides/causality/).

Digital services, free products and intangible investment raise questions about output boundaries and price/quality measurement. A consumer-welfare gain need not be an omitted unit of GDP. Claims that mismeasurement explains the slowdown need a quantitative reconciliation with the measured series; simply noting that some activity is hard to measure is insufficient.

## Checking a claim about recent years

Start with the latest [OECD productivity releases](https://www.oecd.org/en/topics/productivity.html), [BLS productivity statistics](https://www.bls.gov/productivity/), or the relevant national statistical office. Verify:

1. **Measure and coverage:** whole economy or a business sector; real output/hour, output/worker or MFP.
2. **Period and comparison:** one quarter, annual growth, a multi-year trend, or a gap from a previous forecast.
3. **Vintage and hours:** revisions, employment boundaries, actual hours and composition changes.
4. **Shock effects:** pandemic closures and reopening can change the mix of workers and sectors behind an average.
5. **Claim:** a change in measured productivity is not itself proof of a particular technology, policy or change in effort.

Post-2019 recoveries, setbacks and potential AI effects require newer data and their own evaluation. The historical table cannot settle those questions.

## Reproduce

```sh
python3 scripts/collate-productivity.py
npm run build
```

The script verifies all six pinned inputs, writes the full panel and comparison, and regenerates the table. The separate CRAN cross-distribution check is documented in the audit; it is not silently inferred from the archive's folder name. Vercel serves the committed tables and downloads without Python.
