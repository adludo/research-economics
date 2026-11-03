---
title: Calculating productivity
description: How and why output per hour, per worker, multifactor, industry, firm and frontier measures differ.
---

Use the same production boundary, period and unit coverage for the numerator and denominator. Define the output before choosing inputs. **Labour productivity is a partial-input ratio; multifactor productivity accounts for several inputs.** Neither is automatically a measure of welfare.

## Output per hour

```text
Labour productivity = real output / total hours actually worked
```

**How:** Use a volume measure of output, not nominal sales. For the whole economy, output is usually real GDP, which avoids counting intermediate transactions repeatedly. For an industry, it is often real gross value added. Divide by total hours actually worked by the labour producing that output, including employees and self-employed people where the output boundary includes both.

**Why hours:** A person working ten hours and a person working forty hours supply different amounts of labour time. Hours make changes in part-time work and schedules visible. Paid hours, contracted hours and actual hours can differ because of leave, sickness or unpaid overtime.

**Why real output:** Inflation alone can raise revenue or nominal GDP without more production. Statistical agencies construct volume measures using prices and quantities, often with chain-linked indexes. Do not deflate every industry's sales by a consumer-price index and assume this reproduces official real output.

For growth within a country, use consistent real national-accounts output. For cross-country productivity **levels**, use an appropriate purchasing-power conversion and comparable hours; market exchange rates do not remove price-level differences. Do not splice incompatible releases or PPP bases.

**References:** [OECD methodology manual](/papers/productivity/#oecd-2001-methodology-manual), [Feenstra–Inklaar–Timmer](/papers/productivity/#feenstra-inklaar-and-timmer-2015), and [inspected variable definitions and implementation](/papers/productivity/#inspected-code-and-data-documentation).

## Output per worker

```text
Output per worker = real output / employed people
                 = output per hour × hours per employed person
```

**Why use it:** It is useful when comparable hours are unavailable or the question concerns production per employed person. **Why it differs:** A fall in hours per worker can reduce this ratio even if output per hour rises. Counting jobs instead of people also changes the denominator when people hold multiple jobs.

Compare employed people with the relevant output coverage. Working-age population and total resident population are different denominators. The [worked example](/productivity/#a-worked-example) shows why a per-worker result need not match the hourly result.

**References:** [OECD manual](/papers/productivity/#oecd-2001-methodology-manual) and [PWT documentation](/papers/productivity/#inspected-code-and-data-documentation).

## Labour composition and capital services

An hour is a unit of time, not a claim that all labour services are identical. A composition-adjusted labour-input index combines hours for worker groups using compensation weights. In a common index form:

```text
Δln(L*) = sum over worker groups j of [average compensation share_j × Δln(hours_j)]
```

`L*` is an index of labour services. Groups may distinguish education, experience or other observed characteristics. The weighting treats relative compensation as a proxy for relative input contribution, under modelling assumptions. Wages may also reflect bargaining, discrimination or other influences, so this is not a direct observation of innate worker ability. A composition index is also different from simply multiplying every worker's hours by years of education.

Capital input should similarly describe **services used in production**, not just the purchase price of assets. Machines, buildings and software provide different service flows. Capital-services indexes usually aggregate asset services using rental/user-cost weights that account for financing, depreciation and asset-price changes. A monetary wealth stock is a different object. Measuring own-account software, organisational investment and other intangibles also requires a specified asset boundary.

These adjustments help distinguish a rise in output per hour associated with more or different inputs from a residual productivity change. They do not establish a causal effect of education or investment.

**References:** [Jorgenson–Griliches](/papers/productivity/#jorgenson-and-griliches-1967) for input accounting; [Diewert](/papers/productivity/#diewert-1976) for index-number foundations; [OECD manual](/papers/productivity/#oecd-2001-methodology-manual) for implementation guidance.

## Total factor productivity and growth accounting

TFP, often called multifactor productivity (MFP), compares output with a combined input index. Under a two-input constant-returns model with competitively priced inputs, output elasticities can be represented by factor-income shares. A common growth-accounting form is:

```text
Δln(A) = Δln(Y) − sK × Δln(K services) − sL × Δln(L*)
where sK + sL = 1
```

Weights are typically averages of adjacent-period shares. This is an index/growth-accounting formula. The simpler `A = Y / (K^α × L*^(1−α))` is a constant-elasticity production-function example, not a universal agency calculation.

**Why subtract inputs:** Output can rise because a producer uses more equipment or more labour services. The residual asks how much output growth remains after the chosen input contributions have been accounted for.

**Why it is not pure technology:** Utilisation, omitted inputs, imperfect competition, scale effects, statistical revisions and measurement errors can enter the residual. A utilisation-adjusted TFP estimate adds further modelling; it is not the same series as unadjusted TFP. Growth accounting allocates measured growth and does not identify the causal effects of a policy.

### Hypothetical decomposition

Suppose annual **log growth**, expressed as percentages, is: output 3%, capital services 4%, hours 1%, and labour composition 0.5%. With capital share 0.4 and labour share 0.6, labour-services growth is 1.5%. Then:

```text
TFP growth = 3 − 0.4×4 − 0.6×1.5 = 0.5%

Output-per-hour growth = 3 − 1 = 2%
  = capital-deepening contribution: 0.4×(4−1) = 1.2 percentage points
  + labour-composition contribution: 0.6×0.5 = 0.3 percentage points
  + TFP growth: 0.5 percentage points
```

These are invented teaching inputs, not estimates. All rates in this decomposition use log changes. Ordinary percentage changes require the corresponding exact ratio calculation or an explicit approximation.

**References:** [Solow](/papers/productivity/#solow-1957), [Jorgenson–Griliches](/papers/productivity/#jorgenson-and-griliches-1967), [Diewert](/papers/productivity/#diewert-1976), and [OECD manual](/papers/productivity/#oecd-2001-methodology-manual).

## Industry value added and gross output

**Value added** removes intermediate purchases from gross output. Productivity based on real value added is useful for relating an industry's contribution to national output to its labour and capital. Constructing volume measures can require separate treatment of output and intermediate-input prices; this is often called double deflation.

**Gross-output MFP** instead accounts for purchased materials, energy and services alongside capital and labour:

```text
Gross-output MFP growth
  = gross-output volume growth − weighted growth of capital, labour and intermediate inputs
```

The input cost shares correspond to this wider production boundary. Omitting intermediates can make outsourcing look like a productivity improvement: production moves outside the firm while its measured employees fall. Value-added and gross-output MFP therefore answer different questions and should not be compared as identical residuals.

An economy's productivity is not an unweighted average of industry ratios. Output shares, hours shares and shifts between industries matter. Chain-linked real value-added levels are generally not additive, so summing published chain-volume industry levels can also be wrong.

**References:** [OECD manual](/papers/productivity/#oecd-2001-methodology-manual), [Jorgenson–Griliches](/papers/productivity/#jorgenson-and-griliches-1967), and [Syverson](/papers/productivity/#syverson-2011).

## Physical output and revenue productivity

At a plant, output could be tonnes of a comparable product, completed jobs meeting a quality standard, or an output index across products. Dividing by hours gives a physical labour-productivity measure; accounting for several inputs gives a physical production-function or index measure. Product quality, complexity and the mix of products still require adjustment.

Firm datasets often record revenue rather than comparable quantities and firm-specific prices. Deflated revenue per input can then reflect prices, demand, markups and product quality as well as physical efficiency. Dividing revenue by a broad industry deflator does not necessarily remove a firm's own price changes. Wages, profits, lines of code and tasks completed are not universal output measures across occupations.

**Why use firm measures:** They help study differences among producers that national averages conceal. **Why qualify them:** Identifying a causal production function also requires dealing with input choices and other econometric issues; computing a ratio alone does not solve those problems.

**Reference:** [Syverson's productivity review](/papers/productivity/#syverson-2011).

## Frontier-based measures

A frontier approach compares a producer with an estimated best-practice production boundary given its inputs. A Malmquist-type productivity-change index uses distance functions to compare periods and can distinguish movement toward the estimated frontier from a shift in that frontier, subject to its assumptions.

This is useful for benchmarking heterogeneous producers. The result depends on the technology assumptions, sample, input/output choices, treatment of noise and the estimated frontier. A firm scoring below that frontier has not thereby been shown to have a causal management failure. These indexes are different from the national headline GDP-per-hour series.

**Reference:** [Caves–Christensen–Diewert](/papers/productivity/#caves-christensen-and-diewert-1982).

## Make the result reproducible

Record the output boundary, deflator/volume index, actual-hours coverage, employee/self-employed treatment, capital and labour-service definitions, country/sector, period, release and missing-data treatment. Report the formula and whether a number is a level, an ordinary growth rate, a log change, or an annualized rate.

The [reference register](/papers/productivity/) distinguishes inspected documentation from suggested papers whose full texts could not be checked here. The [slowdown example](/productivity/slowdown/#a-reproducible-historical-comparison) demonstrates a fully specified hourly calculation.
