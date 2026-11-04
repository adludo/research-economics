---
title: Leisure data sources
description: Time-use diaries, historical series, and international comparison sources.
---

This guide describes commonly used sources from the discussion. It is not a claim that every listed paper used every dataset. Follow each paper's methods and replication documentation for its exact vintage and sample.

## Reading the survey figures

Every source section below now includes a visual. **ATUS, HETUS, Finland, and historical US diaries show archived numerical examples. MTUS shows extract coverage. AHTUS and OECD show conceptual measurement diagrams**, because no suitable numerical extract was retrieved for them. Diagrams do not substitute invented data for missing observations.

The public extracts were retrieved on **2 November 2026**, from a fixed OWID GitHub revision. They illustrate the measures, not the latest provider releases. The figures keep daily minutes, weekly hours, age profiles, and survey coverage separate. Original-provider agreement and current reuse terms remain unverified where network access was blocked. See [the audit record](https://github.com/adludo/research-economics/blob/docs/leisure-survey-graphs/docs/audits/2026-11-02-leisure-surveys.md).

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

### Example: social time by respondent age

![Six panels show daily minutes alone or with children, coworkers, family, friends, and a partner, by respondent age label, from pooled ATUS 2009–2019 data.](/charts/leisure-surveys/atus-social-time.svg)

This public OWID extract illustrates ATUS's **social context**, not total leisure. Six selected company categories are copied from the population-weighted 2009–2019 pooled estimates. Categories overlap: time with a partner and friends can count in both. Some activities have no “who” records; sleeping is excluded. Do not sum the lines into a daily time budget.

The archive column named `Year` encodes **respondent age**, not calendar year. The download relabels it. These are different age groups, not a longitudinal path or a trend over 2009–2019. Source labels 80 and 85 are retained; their exact top-coding/age-band interpretation has not been verified. Absent labels 81–84 remain gaps.

[Full-size SVG](/charts/leisure-surveys/atus-social-time.svg) · [PNG](/charts/leisure-surveys/atus-social-time.png) · [402 age/category values](/data/leisure-surveys/atus-social-time.csv) · [Archived source definitions](/data/leisure-surveys/atus.json).


## Historical US diaries: AHTUS

**Source:** [American Heritage Time Use Study, Centre for Time Use Research](https://www.timeuse.org/ahtus).

- **Coverage and measures:** Harmonised historical US diaries, incorporating earlier surveys and ATUS.
- **Best use:** Long-run comparisons such as the questions studied by [Aguiar and Hurst](/papers/leisure/#aguiar-and-hurst-2007-five-decades-of-leisure-trends).
- **Access:** Consult the provider's current registration, release, and use conditions.
- **Limitations:** Harmonisation cannot erase differences in survey design, respondent coverage, and coding. AHTUS is a modern access route, not an assertion that the 2007 paper used today's release.
- **Record:** Original survey year, harmonised release, population restrictions, and definitions mapped across surveys.

### What an AHTUS measure requires

![Conceptual workflow: original US diary surveys, harmonised activity codes, chosen sample and weights, then activity averages. This diagram contains no empirical quantities.](/charts/leisure-surveys/ahtus-measurement.svg)

This is a **conceptual reading guide**, not an AHTUS provider flowchart or a graph of estimated leisure. No current AHTUS numerical extract was retrieved. The boxes explain what to document before making a historical comparison; release-specific processing and current provider definitions remain unchecked. The [historical reconstruction example below](#historical-reconstruction) uses a separately attributed working-paper archive, not AHTUS data.

[Full-size SVG](/charts/leisure-surveys/ahtus-measurement.svg) · [PNG](/charts/leisure-surveys/ahtus-measurement.png) · [Authored diagram specification](/data/leisure-surveys/measurement-diagrams.json).


## Multinational Time Use Study (MTUS)

**Source:** [MTUS, Centre for Time Use Research](https://www.timeuse.org/mtus).

- **Coverage:** Harmonised national diary surveys across countries and historical periods.
- **Best use:** International individual-level analysis of time allocation.
- **Access:** Follow current provider registration and licence requirements for the desired extract.
- **Limitations:** Country-year availability and survey designs differ. Harmonised categories may conceal national detail; comparability still needs checking.
- **Record:** Release, country-year, survey design, activity mapping, and weights.

### Public archive coverage

![A country-year dot plot shows the 89 entries for 16 countries in the public MTUS-derived archive, with no leisure quantities on the axes.](/charts/leisure-surveys/mtus-coverage.svg)

Each dot identifies a country-year entry in this **specific archived extract**, not the full current MTUS catalogue or an estimate of leisure minutes. Its processed sample is aged 21–65. The [download](/data/leisure-surveys/mtus-coverage.csv) also records how many of the 24 activity fields are nonempty; that count is not diary sample size.

The archive's activity processing excludes zero reports before calculating weighted means, then adjusts activities to total 1,440 minutes/day. Summing those values would not yield a defensible population leisure total. The coverage graph therefore shows available inputs without presenting the processed activity means as ordinary daily time budgets.

[Full-size SVG](/charts/leisure-surveys/mtus-coverage.svg) · [PNG](/charts/leisure-surveys/mtus-coverage.png) · [89 country-year entries](/data/leisure-surveys/mtus-coverage.csv) · [Processing description](/data/leisure-surveys/mtus.json).


## Harmonised European Time Use Surveys (HETUS)

**Source:** [Eurostat time-use overview](https://ec.europa.eu/eurostat/web/time-use-surveys).

- **Coverage:** European surveys using household and individual questionnaires plus weekday and weekend diaries; Eurostat also provides aggregate tables.
- **Best use:** European comparisons by gender and household structure, including simultaneous activities where recorded.
- **Access:** Aggregates and research microdata are different products; eligibility and availability depend on wave and country.
- **Limitations:** Survey timing and implementation vary across countries. Do not infer a common observation year from a harmonised label.
- **Record:** Country, wave, survey fieldwork dates, diary structure, and access product.

### Leisure, social, and associative life

![Alphabetical country rows show archived daily leisure, social, and associative-life minutes, with separate dots for HETUS wave labels 2000 and 2010.](/charts/leisure-surveys/hetus-leisure.svg)

The graph copies **population time spent**, not time among activity participants or a participation percentage. It contains 32 country-wave values across 22 countries. “Leisure, social, and associative life” includes hobbies, sport, media, social life, organisational work, and informal help. It is broader than some narrow leisure definitions.

The archive labels the waves **2000 and 2010**; these are not verified fieldwork dates for every country. Its activities were normalised to 1,440 minutes/day. We preserve the leisure values unchanged and apply no second normalization. Institutional residents are excluded; common age coverage has not been established. Missing wave values are absent dots, not zero leisure. Different survey dates and populations limit country comparisons.

[Full-size SVG](/charts/leisure-surveys/hetus-leisure.svg) · [PNG](/charts/leisure-surveys/hetus-leisure.png) · [32 country-wave values](/data/leisure-surveys/hetus-leisure.csv) · [Definitions and archived processing](/data/leisure-surveys/hetus.json).


## OECD Time Use Database

**Source:** [OECD time-use database and comparability notes](https://www.oecd.org/en/data/datasets/time-use-database.html).

- **Measures:** Aggregate time in paid work/study, unpaid work, personal care, leisure, and other activities.
- **Best use:** A quick country-level overview rather than detailed individual-level inference.
- **Access:** Use the current OECD tables/downloads and accompanying metadata.
- **Limitations:** Broad categories and different national survey years and methods constrain rankings. Do not treat the database as a same-year international panel without checking.

### What the broad categories distinguish

![A conceptual diagram labels paid work and study, unpaid work, personal care, leisure, and other activities. Box sizes do not represent time shares.](/charts/leisure-surveys/oecd-measurement.svg)

This **category map contains no numerical estimates**. It illustrates the five broad groups described in this guide, so leisure is not confused with unpaid work or personal care. Box sizes do not represent minutes or shares. No OECD numerical extract was retrieved; the provider's current category definitions, national survey dates, and comparability notes remain to be checked before plotting a country ranking.

[Full-size SVG](/charts/leisure-surveys/oecd-measurement.svg) · [PNG](/charts/leisure-surveys/oecd-measurement.png) · [Authored diagram specification](/data/leisure-surveys/measurement-diagrams.json).


## National statistical-office surveys

**Example:** [Statistics Bureau of Japan: Survey on Time Use and Leisure Activities](https://www.stat.go.jp/english/data/shakai/).

National sources can retain more activity detail than harmonised extracts. They suit within-country research, but cross-country use requires explicit recoding and design checks. Access to published tables does not imply unrestricted microdata access.

### Additional national example: Statistics Finland

![Three lines show Statistics Finland's archived free-time minutes for all sexes, men, and women at the four labelled survey dates 1979, 1987, 1999, and 2009.](/charts/leisure-surveys/finland-free-time.svg)

This graph uses **Statistics Finland**, an additional national example; it is not Japanese data. [Official Finnish time-use statistics](https://stat.fi/en/statistics/akay) · [Archived source metadata](/data/leisure-surveys/finland.json).

Free time includes participatory activities, sport/outdoors, culture, reading, media, socialising, hobbies, other free time, and related travel. All 12 supplied sex/year values are copied without averaging or another normalization. The archive does not establish the sample's age coverage; “all” means the all-sex series. Lines between the four labelled dates are visual guides, not added annual estimates. These archived values are not the latest Finnish release.

[Full-size SVG](/charts/leisure-surveys/finland-free-time.svg) · [PNG](/charts/leisure-surveys/finland-free-time.png) · [12 sex/year values](/data/leisure-surveys/finland-free-time.csv).


## Historical reconstruction

For [Ramey (2009)](/papers/leisure/#ramey-2009-home-production-over-the-twentieth-century) and [Ramey–Francis (2009)](/papers/leisure/#ramey-and-francis-2009-a-century-of-work-and-leisure), start with the articles and their linked source/replication materials. Older diaries, schooling, demographics, and work estimates may need reconstruction; no single modern database reproduces the full century automatically.

### Example: four definitions in historical US diaries

![Four panels show historical US weekly leisure estimates under four definitions, using five source-labelled survey years from 1965 to 2003 and common axes.](/charts/leisure-surveys/historical-definitions.svg)

This separate public archive is attributed to **Aguiar and Hurst's 2006 working paper**. It is not a current AHTUS extract, a Ramey reconstruction, or a replication of the final 2007 paper. We retain the source label “All individuals”; the archive does not verify that this means all US residents or establish the original sample's age exclusions.

The archived metadata distinguishes activity-based leisure (measure 1, including recreational childcare), adding sleep/eating/personal care (measure 2), adding primary/educational childcare (measure 3), and residual time after total work (measure 4). These are alternative definitions, not components to sum. The metadata flags a 2003 childcare coding discontinuity. Original working-paper tables and sample restrictions remain unverified. Lines connect five survey-labelled observations as guides; no intermediate annual values are supplied.

[Full-size SVG](/charts/leisure-surveys/historical-definitions.svg) · [PNG](/charts/leisure-surveys/historical-definitions.png) · [20 definition/year values](/data/leisure-surveys/historical-definitions.csv) · [Archived definitions](/data/leisure-surveys/historical.json).


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

## Survey-figure reproduction

```sh
python3 scripts/collate-leisure-surveys.py
python3 -m pip install -r scripts/requirements-charts.txt
python3 scripts/plot-leisure-surveys.py
npm run build
```

The collator verifies all ten input hashes, preserves five source metadata files, and writes five extracts. The plotter also reads the authored diagram specification. No survey microdata, new weighting, imputation, or interpolation is added. [Retrieval manifest](/data/leisure-surveys/sources.json) · [Transformations, coverage, and limits](/data/leisure-surveys/provenance.json). Each exported figure contains its source or guide reference. SVG/PNG assets are served directly on Vercel.
