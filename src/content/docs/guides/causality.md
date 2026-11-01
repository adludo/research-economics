---
title: "Statistics: correlation and causation"
description: A practical explanation of counterfactuals, experiments, causal research designs, and their assumptions.
---

**Correlation asks whether two variables move together. Causation asks whether changing one would change the other.**

A graph relating fertility to working hours can show a pattern. It cannot, by itself, tell us what would happen if a government shortened the working week. To answer that question, we need a credible comparison with what would have happened without the change.

## The missing comparison: a counterfactual

Suppose we want to know whether offering shorter working hours changes the probability of a birth over the next three years.

For each person, imagine two outcomes: one under the offer and one without it. Their difference is that person's causal effect. We cannot observe both outcomes for the same person over the same period. Researchers therefore use an experiment or a defensible comparison group to estimate an **average effect** for a defined population. Comparing the same person before and after is not enough: other things also change over time. [1]

The key question is: **Is this comparison a good stand-in for what would have happened without the intervention?**

## Why two variables can move together

| Explanation | Possible example in this wiki |
| --- | --- |
| X affects Y | Working schedules could affect the feasibility of having a child. |
| Y affects X: reverse causality | Having a child could change a parent's working hours. |
| A third factor affects both: confounding | Education or childcare policy could affect both employment and birth decisions. |
| Selection changes who is compared | Comparing only employed parents excludes people whose employment changed after a birth. |
| Both follow time trends | Two national series can move together while responding to different changes. |

These are possible explanations, not findings established by the examples. Country averages can also conceal different relationships among individuals or groups. Temporal order helps, but “X happened first” is not sufficient evidence of causation. [1, 3]

## Define the question before choosing a method

Specify **the intervention, population, outcome, and time horizon**.

“Do fewer hours cause more births?” is too vague. An offer of a 32-hour week with unchanged pay is different from losing paid hours during unemployment. The former changes the hours/pay arrangement, so its effect should not be described as a pure effect of leisure.

A clearer question is: “Among eligible employees, what is the effect of being offered this schedule, compared with the existing schedule, on having a birth within three years?” Check that the outcome measures births rather than intentions, and distinguish birth timing from completed family size. [1, 2]

## When an experiment is possible

Randomly assign eligible participants to the offer or to a comparison group. Randomisation makes assignment independent of their potential outcomes **in expectation**, allowing a valid comparison if the experiment is implemented and analysed appropriately. It does not guarantee identical groups in a finite sample. [2]

Follow both groups using the same outcome rules. Check missing outcomes, spillovers between groups, and whether people follow their assignments. Comparing groups as assigned estimates the **effect of the offer**; estimating the effect of actually taking it up needs additional assumptions. Random assignment is different from randomly sampling people, which concerns representation. [2, 5]

## When random assignment is unavailable

The method must explain why the comparison is credible. A label such as “natural experiment” does not establish that on its own.

| Design | Basic idea | What must be defended |
| --- | --- | --- |
| Adjustment, regression, or matching | Compare people similar in relevant characteristics measured before treatment. | No remaining confounding after adjustment, enough comparable treated/untreated people, appropriate measurement and analysis. Matching observed variables does not remove unmeasured differences. [1, 3, 4] |
| Difference-in-differences | Compare the treated group's change with an untreated group's change. | Without treatment, their outcomes would have followed parallel trends; no anticipation, contaminating spillovers, or competing changes that undermine that comparison. [6] |
| Regression discontinuity | Compare units just above and below a treatment-eligibility cutoff. | Potential outcomes under either treatment status vary smoothly at the cutoff; no sorting or other discontinuous change invalidates the comparison. The estimate is local to the cutoff. [7] |
| Instrumental variables | Use an outside source of variation that changes treatment. | The instrument predicts treatment, is independent of the relevant unobserved outcome determinants, and affects the outcome only through treatment. The usual local-effect interpretation also needs assumptions about how people respond; see the cautions below. [5] |

Two cautions matter when interpreting the result:

- If a cutoff only changes the **probability** of receiving treatment, the outcome jump estimates an eligibility effect. Estimating the effect of actual treatment needs additional instrumental-variable assumptions (a **fuzzy** discontinuity design). [7]
- For the usual binary-instrument local-effect interpretation, the effect concerns **compliers**: people whose treatment changes because of the instrument. It requires **monotonicity**—the instrument does not move some people into treatment while moving others out. This is not automatically an average effect for everyone. [5]

With different policy start dates or effects that vary across groups and years, a basic difference-in-differences regression may be inappropriate. The estimator must match the design; the simple example below is not a recipe for every policy panel. Diagnostics can expose some assumption failures, but cannot prove every identifying assumption.

## A worked example: difference-in-differences

**Invented numbers for explanation—not evidence from a country or paper.** For this separate, district-level example, suppose A introduces a working-hours policy and B does not. The outcome is annual live births per 1,000 residents.

| District | Before | After | Change |
| --- | ---: | ---: | ---: |
| A: policy introduced | 8 | 10 | +2 |
| B: no policy | 10 | 11 | +1 |

A before/after comparison would attribute the whole **+2** to the policy. Difference-in-differences subtracts B's change:

**Estimated effect = (10 − 8) − (11 − 10) = +1 birth per 1,000 residents.**

That is a causal interpretation **only if the identifying assumptions hold**. For example, a simultaneous childcare expansion or changing age composition in A could invalidate it. Similar pre-policy trends help assess the design but do not prove what the untreated future would have been. These four invented values also do not establish statistical significance. [6]

## Why “control for everything” can fail

A useful control can block a confounding explanation. But adding more variables is not automatically safer. [3, 4]

- A **mediator** lies on the causal pathway. If a schedule change affects childcare and childcare affects births, controlling for childcare can remove part of the total effect we wanted to estimate.
- A **collider** is affected by two other variables. Restricting or adjusting for it can create a misleading association. If both family demands and job opportunities influence whether someone stays employed, comparing only employed people can artificially link those two causes.

Choose controls using the causal question and plausible relationships, not merely whichever variables improve prediction. Country fixed effects remove stable country differences; they do not remove changing confounders automatically.

## A small p-value is not a causal design

A p-value describes how unusual the test result would be under a specified null model and its assumptions. It is **not the probability that X causes Y**. A small p-value cannot rule out confounding, reverse causality, measurement problems, or a poor comparison group. [8]

Report effect size and uncertainty alongside the design. A narrow confidence interval can still surround a biased estimate. A large p-value does not prove there is no effect. Likewise, strong prediction is not the same as knowing what an intervention would do. [1, 8]

## A practical checklist for a causal claim

1. What exactly changes, for whom, and over what period?
2. What comparison represents the outcome without that change?
3. Why would the groups be comparable? What assumptions could fail?
4. Could reverse causality, selection, other policies, or time trends explain the result?
5. Are the controls appropriate, and are outcomes missing or measured differently?
6. How large and uncertain is the estimate? Do alternative reasonable choices change it?
7. Does the result apply to this population and intervention, or is it local to a cutoff or to people whose treatment changes because of an instrument?

For this wiki's [fertility/GDP/hours graphs](/data/fertility-charts/), the appropriate claim is **“these variables followed these paths in the selected data.”** A claim that changing hours or GDP would change births needs a causal design and supporting evidence beyond those graphs.

## References and further reading

The explanations were checked against these chapters of Matheus Facure's open *Causal Inference for the Brave and True*, at pinned revision `4df1445987d3b6f9824d508863a1a2f0a503e888`. These are teaching references, not new empirical results. Section names identify the inspected passages.

1. [Introduction to Causality](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/01-Introduction-To-Causality.ipynb): “When Association IS Causation,” “Bias,” and “Key Ideas.”
2. [Randomised Experiments](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/02-Randomised-Experiments.ipynb): “The Gold Standard” and “The Assignment Mechanism.”
3. [Graphical Causal Models](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/04-Graphical-Causal-Models.ipynb): “Confounding Bias” and “Selection Bias.”
4. [Beyond Confounders](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/07-Beyond-Confounders.ipynb): “Good Controls” and “Bad Controls — Selection Bias.”
5. [Instrumental Variables](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/08-Instrumental-Variables.ipynb) and [Non-Compliance and LATE](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/09-Non-Compliance-and-LATE.ipynb): instrument assumptions, weakness, and local effects among compliers.
6. [Difference-in-Differences](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/13-Difference-in-Differences.ipynb): “DID Estimator” and “Non Parallel Trends.”
7. [Regression Discontinuity Design](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/16-Regression-Discontinuity-Design.ipynb): cutoff comparison, “RDD Estimation,” and fuzzy designs.
8. [Statistics Review](https://github.com/matheusfacure/python-causality-handbook/blob/4df1445987d3b6f9824d508863a1a2f0a503e888/causal-inference-for-the-brave-and-true/03-Stats-Review-The-Most-Dangerous-Equation.ipynb): confidence intervals and “P-values.”

For fuller textbook treatments: Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (2020), [author's book page](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/); Scott Cunningham, *Causal Inference: The Mixtape* (2021), [open book](https://mixtape.scunning.com/). These are further-reading suggestions; their full texts were not inspected for this guide.

[Inspected-chapter URLs and hashes](/data/causality/sources.json) record the reference versions. This guide explains how to assess causal claims; it does not turn the wiki's descriptive graphs into causal evidence.
