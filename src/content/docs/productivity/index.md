---
title: Understanding productivity
description: The usual headline measure, the alternatives, and how to interpret a productivity slowdown.
---

**Productivity measures output relative to the inputs used to produce it.** For an economy, the usual headline labour-productivity measure is **real GDP per hour worked**. For a particular business sector, it is that sector's real output per hour. US headlines often concern nonfarm-business output per hour rather than whole-economy GDP.

The commonly discussed productivity problem is **slow growth in output per hour over time**. An economy can still become more productive while improving more slowly than before. [The slowdown guide](/productivity/slowdown/) gives a dated, reproducible example for eight economies and explains why neither the measurement nor the causes should be treated as uniform across countries.

## Start with the question

| Question | Useful measure | What it leaves unresolved |
| --- | --- | --- |
| How much market output does an hour of work produce? | [Real output per hour](/productivity/calculation/#output-per-hour) | Capital, skills, organisation and worker composition all affect it |
| How much output is produced per employed person? | [Real output per worker](/productivity/calculation/#output-per-worker) | Differences in working hours |
| What remains after accounting for capital and labour inputs? | [Total/multifactor productivity](/productivity/calculation/#total-factor-productivity-and-growth-accounting) | Residual measurement and modelling assumptions |
| How does an industry's production use purchased materials and services? | [Gross-output productivity](/productivity/calculation/#industry-value-added-and-gross-output) | Intermediate-input measurement and outsourcing |
| How efficiently does a plant make a particular product? | [Physical and revenue measures](/productivity/calculation/#physical-output-and-revenue-productivity) | Product quality, prices, demand and product mix |
| How far is a producer from an estimated best-practice benchmark? | [Frontier measures](/productivity/calculation/#frontier-based-measures) | The benchmark and assumptions about noise and inefficiency |

GDP per resident, wages, profits and welfare answer other questions. They are related to productivity but cannot be used interchangeably with it. See the [glossary](/glossary/).

## A worked example

These are **hypothetical values**, not a country's statistics. Output is already adjusted for price changes; workers and hours cover the same production.

| Quantity | First year | Second year | Change |
| --- | ---: | ---: | ---: |
| Real output | 1,000 units | 1,040 units | +4% |
| Total hours worked | 100 hours | 102 hours | +2% |
| Employed people | 10 | 10 | 0% |
| Resident population | 20 | 20 | 0% |
| Output per hour | 10 | 10.1961 | **+1.9608%** |
| Output per worker | 100 | 104 | +4% |
| Output per resident | 50 | 52 | +4% |

Hourly productivity grows by `(1.04 / 1.02 − 1) × 100 = 1.9608%`. Subtracting 2% from 4% gives an approximation, not the exact rate. Log changes do subtract exactly: `Δln(output/hour) = Δln(output) − Δln(hours)`.

For the same matched quantities:

```text
output / population
  = (output / hours) × (hours / employed person) × (employed people / population)
```

This separates output per hour from working schedules and employment. In actual international accounts, domestic jobs/persons and resident populations can differ; inspect coverage before interpreting the last term as a resident employment rate.

## Why the headline is not a measure of effort

More equipment per hour, better skills, improved processes, different products, and changes in which firms or workers operate can raise measured output per hour. The ratio does not isolate how hard people work. A contraction in low-productivity activities can raise an aggregate average even while employment and total output fall.

Productivity can support higher material living standards, but its gains need not translate one-for-one into wages or leisure. Distribution, prices, taxes, employment and choices about working time matter. [Leisure and welfare research](/papers/leisure-productivity/) covers those additional questions.

## Read next

- [How the different calculations work](/productivity/calculation/): outputs, hours, capital services, labour composition, index numbers and firm-level measures.
- [Interpreting the productivity slowdown](/productivity/slowdown/): a historical comparison, alternative explanations and a guide to checking current claims.
- [Methodology and paper references](/papers/productivity/): a reference for each approach, with reading questions and access status.

The equations are explanatory derivations. The data example uses inspected archive files, a variable codebook and an author-hosted implementation. Journal full texts and publisher records were inaccessible here; the references are reading pointers rather than independently verified paper-result summaries. The [research audit](https://github.com/adludo/research-economics/blob/docs/productivity-measures/docs/audits/2026-11-03-productivity.md) records the completed checks and limits.
