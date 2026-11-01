---
title: Leisure data sources
description: Time-use diaries, historical series, and international comparison sources.
---

This guide describes commonly used sources from the discussion. It is not a claim that every listed paper used every dataset. Follow each paper's methods and replication documentation for its exact vintage and sample.

## Leisure graphs

These two sources actually report leisure; neither is calculated as “168 hours minus paid work.” Their populations and definitions differ, so they are shown separately.

### United States: historical residual leisure by age

![Six separate age-group panels show historical US residual leisure estimates in weekly hours, 1900–2005.](/charts/topic-graphs/us-leisure.svg)

[Full-size SVG](/charts/topic-graphs/us-leisure.svg) · [PNG](/charts/topic-graphs/us-leisure.png) · [72 plotted observations](/data/topic-graphs/us-leisure.csv) · [Source metadata](/data/topic-graphs/us.json).

Source: Ramey and Francis (2009), distributed in the pinned OWID archive. Leisure is residual time after work, school, home production, commuting and personal care. Archived assumptions include commuting equal to 10% of work/school hours and personal care fixed at 77 hours/week. These are reconstructed estimates, not annual diary observations. The age14+ aggregate overlaps the other groups; do not sum them.

### Norway: leisure on an average day

![Norway leisure minutes per average day for the archived all-sex, female and male series in five survey years, 1970–2010.](/charts/topic-graphs/norway-leisure.svg)

[Full-size SVG](/charts/topic-graphs/norway-leisure.svg) · [PNG](/charts/topic-graphs/norway-leisure.png) · [15 sex-year observations](/data/topic-graphs/norway-leisure.csv) · [Source metadata](/data/topic-graphs/norway.json).

Source: Statistics Norway via OWID. Leisure includes sport/outdoors, entertainment/culture, socialising, reading, television, other leisure and associated travel. The archive says activities are normalised to 1,440 minutes/day by distributing missing minutes across activities. We copy those values rather than applying another correction. Age coverage is not specified in the archived metadata; “all” identifies the all-sex series, not a verified all-age sample.

These are two historical national collections, not a harmonised global leisure ranking. Lines connect published observations; intermediate years are not added. Both graphs carry retrieval references. [Exact CSV URLs, hashes and transformations](/data/topic-graphs/provenance.json) · [Reproduction and limits](#graph-reproduction).


## American Time Use Survey (ATUS)

**Official sources:** [Bureau of Labor Statistics ATUS](https://www.bls.gov/tus/) · [Data files](https://www.bls.gov/tus/data.htm) · [Well-being module](https://www.bls.gov/tus/wbdatafiles.htm).

- **Coverage and measures:** Annual US diaries since 2003, with detailed activities and respondent characteristics; selected supplements add well-being and other measures.
- **Best use:** Recent US leisure, work, care, and recession comparisons, including the setting of [Aguiar et al. (2013)](/papers/leisure/#aguiar-hurst-and-karabarbounis-2013-recession-time-use).
- **Access:** Public-use files and documentation are available through BLS; read the relevant survey and module documentation.
- **Limitations:** Primarily repeated cross-sections, not a long-running panel of the same people's leisure. The 2020 collection interruption affects annual estimates. Supplements do not cover every year.
- **Record for reproducibility:** Year, activity-code version, module availability, sample exclusions, survey weights, and diary-day treatment.

## Historical US diaries: AHTUS

**Source:** [American Heritage Time Use Study, Centre for Time Use Research](https://www.timeuse.org/ahtus).

- **Coverage and measures:** Harmonised historical US diaries, incorporating earlier surveys and ATUS.
- **Best use:** Long-run comparisons such as the questions studied by [Aguiar and Hurst](/papers/leisure/#aguiar-and-hurst-2007-five-decades-of-leisure-trends).
- **Access:** Consult the provider's current registration, release, and use conditions.
- **Limitations:** Harmonisation cannot erase differences in survey design, respondent coverage, and coding. AHTUS is a modern access route, not an assertion that the 2007 paper used today's release.
- **Record:** Original survey year, harmonised release, population restrictions, and definitions mapped across surveys.

## Multinational Time Use Study (MTUS)

**Source:** [MTUS, Centre for Time Use Research](https://www.timeuse.org/mtus).

- **Coverage:** Harmonised national diary surveys across countries and historical periods.
- **Best use:** International individual-level analysis of time allocation.
- **Access:** Follow current provider registration and licence requirements for the desired extract.
- **Limitations:** Country-year availability and survey designs differ. Harmonised categories may conceal national detail; comparability still needs checking.
- **Record:** Release, country-year, survey design, activity mapping, and weights.

## Harmonised European Time Use Surveys (HETUS)

**Source:** [Eurostat time-use overview](https://ec.europa.eu/eurostat/web/time-use-surveys).

- **Coverage:** European surveys using household and individual questionnaires plus weekday and weekend diaries; Eurostat also provides aggregate tables.
- **Best use:** European comparisons by gender and household structure, including simultaneous activities where recorded.
- **Access:** Aggregates and research microdata are different products; eligibility and availability depend on wave and country.
- **Limitations:** Survey timing and implementation vary across countries. Do not infer a common observation year from a harmonised label.
- **Record:** Country, wave, survey fieldwork dates, diary structure, and access product.

## OECD Time Use Database

**Source:** [OECD time-use database and comparability notes](https://www.oecd.org/en/data/datasets/time-use-database.html).

- **Measures:** Aggregate time in paid work/study, unpaid work, personal care, leisure, and other activities.
- **Best use:** A quick country-level overview rather than detailed individual-level inference.
- **Access:** Use the current OECD tables/downloads and accompanying metadata.
- **Limitations:** Broad categories and different national survey years and methods constrain rankings. Do not treat the database as a same-year international panel without checking.

## National statistical-office surveys

**Example:** [Statistics Bureau of Japan: Survey on Time Use and Leisure Activities](https://www.stat.go.jp/english/data/shakai/).

National sources can retain more activity detail than harmonised extracts. They suit within-country research, but cross-country use requires explicit recoding and design checks. Access to published tables does not imply unrestricted microdata access.

## Historical reconstruction

For [Ramey (2009)](/papers/leisure/#ramey-2009-home-production-over-the-twentieth-century) and [Ramey–Francis (2009)](/papers/leisure/#ramey-and-francis-2009-a-century-of-work-and-leisure), start with the articles and their linked source/replication materials. Older diaries, schooling, demographics, and work estimates may need reconstruction; no single modern database reproduces the full century automatically.

## Choose and define the measure first

| Research question | Starting point | Essential check |
| --- | --- | --- |
| Recent US leisure | ATUS | Activity definitions, diary weights, and module years |
| Historical US trends | AHTUS and original surveys | Common sample and comparable activity mapping |
| International microdata | MTUS or HETUS | Country-year coverage and survey design |
| Quick country overview | OECD | National survey dates and category comparability |
| Emotional value of unemployment time | Relevant longitudinal study | Well-being measure, transitions, and actual panel access |

Specify whether leisure includes **sleep, eating, travel, or childcare**, whether secondary activities count, and whether children, retirees, and unemployed people enter the population. Record both the time budget and the welfare interpretation.

## Graph reproduction

```sh
python3 scripts/collate-topic-graphs.py
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-topic-graphs.py
npm run build
```

Sources are frozen at OWID revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`. The collation script verifies eight input checksums, retains the source metadata, and writes the downloadable extracts. Plotting uses only those extracts. SVG/PNG files are committed, so Vercel needs no Python runtime.

Original provider records, current revisions, source assumptions and reuse terms remain separate checks. These graphs do not replicate the papers' models or establish causality.
