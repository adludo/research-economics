# Research audit: statistics and causality guide

- Target: new guide on `docs/causality-statistics`, working tree based on `0435db26c24ef1228c830fc333999352adae5332`.
- Date: 1 November 2026, UTC.
- Independent auditor: `/root/audit_productivity`, following the repository's `research_auditor` instructions.
- Scope: `guides/causality.md`, source manifest, hypothetical arithmetic, and integration in navigation, overview, glossary, README and fertility-chart guidance.
- Verdict: **supported as an introductory methodological explanation within the inspected source-reading scope; two minor methodological refinements corrected and rechecked**.
- No material false causal claim or arithmetic error found. No new empirical causal effect is claimed.

## Source reading

The main agent read the relevant Markdown passages from nine original teaching notebooks in Matheus Facure's *Causal Inference for the Brave and True*. All are pinned at revision `4df1445987d3b6f9824d508863a1a2f0a503e888`. The auditor independently downloaded all nine URLs and verified byte sizes and SHA-256 hashes against the inspected files and [`sources.json`](../../public/data/causality/sources.json).

| Reference material | Inspected locators and supported explanation |
| --- | --- |
| Chapter1, Introduction to Causality | “When Association IS Causation,” “Bias,” and “Key Ideas”: potential outcomes, the missing counterfactual, and why association need not be causal |
| Chapter2, Randomised Experiments | “The Gold Standard” and assignment mechanism: comparability by assignment; expectation versus finite-sample balance |
| Chapter3, Statistics Review | Confidence intervals, tests and “P-values”: statistical uncertainty is not proof of causal identification |
| Chapter4, Graphical Causal Models | Confounding and selection sections: common causes and conditioning on common effects |
| Chapter7, Beyond Confounders | Good/bad controls: prediction does not justify controlling for mediators or colliders |
| Chapters8–9, Instruments and Non-Compliance/LATE | Instrument assumptions, weak instruments, monotonicity and local effects for compliers |
| Chapter13, Difference-in-Differences | “DID Estimator” and “Non Parallel Trends”: counterfactual trends and design limits |
| Chapter16, Regression Discontinuity | Cutoff comparisons, “RDD Estimation” and fuzzy designs: continuity, manipulation and local interpretation |

The source identities and named section locators match. These are educational references, not a new empirical study. The auditor did not execute the notebooks or validate every empirical example, chart, or code cell in them.

## Explanation and arithmetic checks

| Check | Result |
| --- | --- |
| Counterfactual comparison | Correctly states that both same-unit, same-period outcomes cannot be observed; comparison groups support population-average estimates under assumptions |
| Correlation alternatives | Causal effects, reverse causation, common causes, selection and time trends are presented as possibilities, not established empirical explanations |
| Treatment definition | A same-pay shorter-hours offer is not conflated with unemployment or a pure leisure intervention |
| Random assignment | Distinguished from sampling, actual take-up and finite-sample imbalance; missing outcomes and spillovers acknowledged |
| Adjustment | No claim that matching observed variables or adding all predictors eliminates unmeasured confounding |
| DiD | Parallel untreated trends, anticipation, spillovers and competing changes retained; pre-trends do not prove the unobserved future |
| Hypothetical example | Independently computed `(10 − 8) − (11 − 10) = +1` birth per1,000 residents. Under the stated comparison, A's untreated after-rate would be `8 + (11 − 10) = 9`. These are invented values, not country findings or statistical-significance evidence |
| Bad controls | Mediators and colliders distinguished; regression/fixed effects not presented as automatic causal designs |
| P-values | No probability of causation or posterior null probability inferred; uncertainty does not remove design bias |
| Existing graphs | Remain descriptive historical comparisons; this guide does not upgrade them into causal evidence |

## Corrections and recheck

The initial draft specified only untreated-outcome continuity in the RD row and described IV response assumptions too vaguely. The main agent corrected both:

1. The RD row now names smooth potential outcomes under either treatment status. A separate fuzzy-RD caution distinguishes the eligibility effect from the actual-treatment effect when eligibility only changes treatment probability.
2. The IV caution explicitly names the usual binary-instrument local interpretation, compliers and monotonicity/no opposite-direction responders. It does not generalise that local effect to everyone.

The independent auditor rechecked these changes and requested no further methodological correction within the introductory scope.

## Unverified and unrun checks

- Hernán and Robins, *Causal Inference: What If* (2020), and Cunningham, *Causal Inference: The Mixtape* (2021), are explicitly labelled further-reading suggestions. Their full texts and edition records were not independently checked for this guide. Both attempted book-page requests were blocked by proxy tunnel HTTP403; see the [access record](2026-11-01-causality-further-reading-access.json).
- No notebook code execution, empirical replication or full audit of the teaching book was performed.
- No causal effect in this wiki's existing datasets or graphs was newly estimated or verified.
- Complete live-browser/Vercel behaviour was not part of the methodological review.

## Technical validation

The production build passed with 24 HTML pages and search assets. All 1,345 internal links/images/anchors, nine source hashes and byte counts, the public manifest copy, hypothetical arithmetic, and local audit links passed validation. Existing optional i18n/404 and sitemap warnings remain. These integration checks do not certify causal effects or every claim in the references.
