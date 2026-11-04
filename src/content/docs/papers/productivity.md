---
title: Productivity methodology and reading references
description: Foundational papers and reading questions for productivity calculations and the slowdown debate.
---

Use these references alongside the [calculation guide](/productivity/calculation/) and [slowdown example](/productivity/slowdown/). They connect each method to the literature on why output, inputs and weights are defined that way.

**Reading status:** The journal/manual endpoints below returned proxy HTTP 403. Their full texts, final versions, publisher metadata and correction/retraction records have **not** been independently verified here. These are suggested primary reading references, not verified summaries of their findings. The guide's numerical illustration is our own archive calculation. [Per-reference access record](/data/productivity/references.json).

## OECD (2001): methodology manual

**OECD.** *Measuring Productivity: OECD Manual. Measurement of Aggregate and Industry-level Productivity Growth*. [DOI/reference](https://doi.org/10.1787/9789264194519-en).

**Use with:** Output/hour, output/worker, capital and labour services, industry value added and gross-output MFP. **Reading question:** How should an official productivity index align production boundaries, volume measures, hours and input aggregation? This is a statistical methodology handbook, not a causal study or a current productivity release.

## Solow (1957)

**Robert M. Solow.** “Technical Change and the Aggregate Production Function.” *Review of Economics and Statistics*, 39(3), 312–320. [DOI/reference](https://doi.org/10.2307/1926047).

**Use with:** [TFP and growth accounting](/productivity/calculation/#total-factor-productivity-and-growth-accounting). **Reading question:** Under what production assumptions can output growth be separated into measured input contributions and a residual? Read the assumptions before interpreting a residual as technology.

## Jorgenson and Griliches (1967)

**Dale W. Jorgenson and Zvi Griliches.** “The Explanation of Productivity Change.” *Review of Economic Studies*, 34(3), 249–283. [DOI/reference](https://doi.org/10.2307/2296675).

**Use with:** [Labour composition and capital services](/productivity/calculation/#labour-composition-and-capital-services). **Reading question:** What changes when labour and capital are measured as heterogeneous input services rather than raw counts or a simple wealth stock? Keep input adjustments separate from causal claims about investment or education.

## Diewert (1976)

**W. Erwin Diewert.** “Exact and Superlative Index Numbers.” *Journal of Econometrics*, 4(2), 115–145. [DOI/reference](https://doi.org/10.1016/0304-4076(76)90009-9).

**Use with:** Weighted indexes of output and input growth. **Reading question:** What economic assumptions justify an index-number formula when there are many products or input types? This is the reading route behind the guide's use of adjacent-period share weights rather than arbitrary equal weights.

## Caves, Christensen, and Diewert (1982)

**Douglas W. Caves, Laurits R. Christensen, and W. Erwin Diewert.** “The Economic Theory of Index Numbers and the Measurement of Input, Output, and Productivity.” *Econometrica*, 50(6), 1393–1414. [DOI/reference](https://doi.org/10.2307/1913388).

**Use with:** [Frontier-based comparisons](/productivity/calculation/#frontier-based-measures) and productivity-change indexes. **Reading question:** How can comparisons be constructed using input/output distance functions, and what assumptions govern the benchmark? A frontier index is not the same object as GDP per hour.

## Syverson (2011)

**Chad Syverson.** “What Determines Productivity?” *Journal of Economic Literature*, 49(2), 326–365. [DOI/reference](https://doi.org/10.1257/jel.49.2.326).

**Use with:** [Firm-level measurement](/productivity/calculation/#physical-output-and-revenue-productivity), production functions and interpretation. **Reading question:** How can researchers distinguish physical production efficiency from revenue, prices, demand, quality and selection? This is a literature-review reference; no numerical findings from it are reproduced here.

## Feenstra, Inklaar, and Timmer (2015)

**Robert C. Feenstra, Robert Inklaar, and Marcel P. Timmer.** “The Next Generation of the Penn World Table.” *American Economic Review*, 105(10), 3150–3182. [DOI/reference](https://doi.org/10.1257/aer.20130954).

**Use with:** Real output and cross-country comparisons. **Reading question:** Which output concept suits a comparison of levels, and which suits growth over time? The inspected PWT codebook lists this paper as its methodological starting point. That codebook inspection does not verify the article's text or publisher record.

## Byrne, Fernald, and Reinsdorf (2016)

**David M. Byrne, John G. Fernald, and Marshall B. Reinsdorf.** “Does the United States Have a Productivity Slowdown or a Measurement Problem?” *Brookings Papers on Economic Activity*, Spring, 109–182. [DOI/reference](https://doi.org/10.1353/eca.2016.0002).

**Use with:** The [measurement debate](/productivity/slowdown/#explaining-a-slowdown-is-a-separate-task). **Reading question:** What evidence would distinguish slower output growth from errors in measured prices, quantities and production boundaries? The US focus should not be silently generalized to every economy. No estimate or conclusion from the unread text is attributed here.

## Goldin and coauthors (2024)

**Ian Goldin, Pantelis Koutroumpis, François Lafond, and Julian Winkler.** “Why Is Productivity Slowing Down?” *Journal of Economic Literature*, 62(1), 196–268. [DOI/reference](https://doi.org/10.1257/jel.20221543).

**Use with:** A broader reading route into the productivity-slowdown debate. **Reading question:** How do alternative explanations, country patterns and measurement choices fit together? This entry identifies a review to consult; its full-text arguments, quantitative conclusions and current publication record remain unchecked here. It is not evidence of the latest 2026 growth rate.

## Inspected code and data documentation

These supporting materials **were retrieved and read**, with exact versions in the [source manifest](/data/productivity/sources.json):

- **PWT10.01 variable codebook**, distributed in CRAN's `pwt10` package at revision `957b298fd706a567af96ccb1663ad68d5e5d07ba`: [pinned source](https://github.com/cran/pwt10/blob/957b298fd706a567af96ccb1663ad68d5e5d07ba/man/pwt10.01.Rd) · [stored copy](/data/productivity/pwt-codebook.Rd). Its `rgdpna`, `emp` and `avh` definitions support the selected real-output and hours calculation. Its `rkna` and `rtfpna` entries distinguish capital services and TFP indexes.
- **Boppart–Li author-hosted replication archive**, *Productivity slowdown: reducing the measure of our ignorance*, revision `e0e9a034342069e6608eff8cadee4d7b4ff979ec`: [README](https://github.com/huiyul/TFP_slowdown_BoppartLi/blob/e0e9a034342069e6608eff8cadee4d7b4ff979ec/README.md) and [implementation lines 156–162](https://github.com/huiyul/TFP_slowdown_BoppartLi/blob/e0e9a034342069e6608eff8cadee4d7b4ff979ec/Boppart_Li_2021_replication_final.py#L156-L162). The code constructs hours as `avh × emp` and output/hour as `rgdpna / hours`. Its raw PWT inputs require a million-unit conversion; our OWID archive already applies that conversion. The repository's legacy 2011-price labels are not reused. Reading this implementation is not reading its associated paper, validating all its results, or replicating it.

Original-provider identity, current releases and reuse conditions remain separate checks. See the [audit record](https://github.com/adludo/research-economics/blob/docs/productivity-measures/docs/audits/2026-11-03-productivity.md).
