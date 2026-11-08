---
title: Can we put a value on an hour of leisure?
description: Equations for the shadow value of leisure, an after-tax-wage approximation, and consumption-equivalent values with paper references.
---

**Yes. Economics has equations for valuing leisure in consumption or money terms. There is no single price that applies to every person or every free hour.** A useful starting point is the amount of consumption a person would give up for a small increase in leisure while remaining equally well off.

The directly checked source here is **Brouillette, Jones, and Klenow (2025)**, a published-layout author copy of an *AER: Insights* paper. It supplies both an explicit utility function and a wage-based calibration. [Paper details and precise locators](/papers/leisure-value/) · [Source file and checksum](/data/leisure-value/sources.json).

## The general equation: a shadow value

Let `U(c,L)` describe utility from consumption expenditure `c` and leisure hours `L`, measured over the same period. A local consumption value of another leisure hour is:

```text
Value of a marginal leisure hour = (∂U/∂L) / (∂U/∂c)
```

The numerator is the utility gained from more leisure; the denominator converts that utility into consumption money. The ratio is a **marginal rate of substitution**, also called a shadow value. It is not a market transaction price or an observation of happiness in dollars.

This equation needs preferences or an identifying choice model. A time diary alone does not tell us the derivatives. It also requires consistent units: annual consumption divided by a marginal utility for a whole leisure share is not yet dollars per hour.

## A rough rule: the marginal after-tax wage

If a person can freely trade another hour of leisure for an hour of paid work, has an interior choice, and faces no additional relevant wedges, the optimum satisfies:

```text
(∂U/∂L) / (∂U/∂c) = marginal after-tax hourly wage
```

A hypothetical $25 gross hourly wage and 20% marginal income tax would give a $20/hour opportunity-cost benchmark in this simplified setting. It is a starting assumption, not an independently estimated leisure value.

The equality can fail when hours are fixed, overtime is unavailable, jobs have fixed costs, or non-work is involuntary. A person who cannot work another hour need not value leisure at the posted wage; someone without a job does not thereby value time at zero. [Becker's time-allocation framework](/papers/leisure/#becker-1965-the-opportunity-cost-of-time) is the existing theoretical reading route. The directly inspected 2025 paper states its wage first-order condition on **printed p.439**.

## An explicit equation from the literature

On **printed p.433**, Brouillette–Jones–Klenow use:

```text
u(c,ℓ) = constant + ln(c) + v(ℓ)
v(ℓ)   = −[θ ε / (1+ε)] × (1−ℓ)^((1+ε)/ε)
```

Here `ℓ` is a leisure **share**, `θ > 0` is the leisure/labour-disutility weight, and `ε > 0` is the Frisch labour-supply elasticity. Frisch responses hold the marginal utility of wealth constant; elasticities using different income or wealth assumptions are not interchangeable.

Differentiating the paper's utility function gives our derived conversion:

```text
Value per unit of leisure share = c × θ × (1−ℓ)^(1/ε)

Value per extra annual leisure hour
  = [annual consumption × θ × (1−ℓ)^(1/ε)] / annual available hours
```

**The denominator matters.** This paper uses a reference budget of `16 × 365 = 5,840` annual waking hours. An extra hour in the year raises `ℓ` by `1/5,840`. Its annual consumption must therefore be divided by 5,840 in the hourly formula. The paper uses 366 days in leap years.

At fixed consumption and parameters, the formula gives a lower marginal value when leisure is already more abundant. At fixed leisure, higher consumption raises the consumption-money value. That income dependence is a property of the model; it does not settle how a social evaluation should weight different people's well-being.

## A rough numerical illustration

The paper's **pp.439–440** calibration uses **2006 moments expressed in 2012 dollars** and supplies these rounded values:

| Input | Value | Status |
| --- | ---: | --- |
| Annual consumption | $31,046 in 2012 US dollars | Paper calibration, net of insurance expenditure |
| Leisure share | 0.70 | Paper calibration moment |
| `θ` | 8.9 | Calibrated using a labour–leisure first-order condition |
| `ε` | 1 | Assumed baseline Frisch elasticity |
| Available hours | 5,840/year | Reference 365-day waking-time budget |

Our calculation is:

```text
31,046 × 8.9 × (1−0.70) / 5,840 ≈ $14.19 per hour, in 2012 dollars
```

**This is our model-implied illustration from rounded published parameters. It is not the paper's reported estimate of a universal leisure price.** The weight is calibrated from a wage condition, so the result largely restates that assumed trade-off. It is not independent evidence that everyone's leisure is worth $14.19. It is also not a current-dollar quote.

The calibration uses aggregate consumption and prime-age wage/leisure moments, not one person's complete observed budget. Applying it to a different population, a narrow recreation measure, or a different period requires reconsidering the parameters and units.

## Larger changes: willingness to pay is not simply hours times a wage

For this log-consumption utility, let `Δv = v(ℓ + Δℓ) − v(ℓ)`. Holding other welfare dimensions fixed, we derive two different comparisons:

```text
WTP for a leisure gain = C × [1 − exp(−Δv)]

Equivalent consumption increase at the original leisure level
  = C × [exp(Δv) − 1]
```

**WTP** is how much annual consumption can be removed after the leisure gain while preserving baseline utility. The **equivalent consumption increase** is the extra consumption at the original leisure allocation that would provide the same utility as the gain. Their comparison allocations differ, so the amounts need not be equal. The paper's consumption-equivalent welfare condition is on **p.433, eq.(1)**; these leisure-only formulas are our algebraic special cases, not its full lifetime welfare calculation.

Using the same rounded calibration, all monetary amounts below are **annual consumption amounts in 2012 dollars**:

<!-- BEGIN VALUE TABLE -->
| Extra leisure | Local linear approximation | Exact WTP | Equivalent consumption increase |
| --- | ---: | ---: | ---: |
| 1 hour in the year | $14.19 | $14.19 | $14.19 |
| 1 hour/day for 365 days | $5,180.80 | $4,310.89 | $5,005.99 |
<!-- END VALUE TABLE -->

The first row is one extra hour in the entire year. The second is 365 additional hours, not a one-hour gain. The local linear column holds the initial marginal value fixed; the exact columns allow for curvature. These are hypothetical static trades. They do not simulate lost wage income, a shorter-workweek policy, or a general-equilibrium response.

## What counts as leisure changes the answer

The paper's **pp.438–439** measure is broad non-market waking time, constructed from CPS work hours. It includes rough household adjustments and assigns full-time hours to people classified as involuntarily non-employed so their non-employment is not automatically counted as extra leisure. It is not a clean diary measure of recreation alone.

Unpaid care, sleep, unemployment, chosen holidays and an unexpected free evening can have different implications. A parameter calibrated for one definition should not be transferred to another unchanged. See [leisure measurement](/data/leisure/#choose-and-define-the-measure-first) and [the distinction between home production and leisure](/papers/leisure/#gronau-1977-separate-home-production-from-leisure).

## Practical use

For a rough opportunity-cost scenario, report a marginal net-wage benchmark and its assumptions. For a welfare-model calculation, report the utility function, consumption, leisure definition, time budget, calibration and sensitivity. If hours are constrained, investigate actual willingness-to-pay choices or an appropriate constrained model rather than assigning a wage mechanically.

Do not count the same saved hour both as extra earnings and as extra leisure. Leisure valuation is also different from measuring [output per hour](/productivity/) or adding unpaid time to GDP. Welfare accounting requires its own assumptions and can include additional dimensions.

## Reproduce and read further

```sh
python3 scripts/calculate-leisure-value.py --verify-source
npm run build
```

[Calibration inputs](/data/leisure-value/calibration.json) · [Worked examples CSV](/data/leisure-value/worked-examples.csv) · [Derived formulas and values](/data/leisure-value/derived-values.json) · [Literature and findings](/papers/leisure-value/).

The author-hosted published copy was read and pinned; publisher authentication, corrections/retractions and empirical replication remain separate checks. The older Becker and Jones–Klenow entries retain their existing primary-text verification limits. See [the audit record](https://github.com/adludo/research-economics/blob/docs/value-of-leisure/docs/audits/2026-11-08-leisure-value.md).
