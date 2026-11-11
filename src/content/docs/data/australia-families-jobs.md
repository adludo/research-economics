---
title: Australian parents, jobs and family size
description: What the existing Australian data can link, and where to obtain joint occupation, family-size, state and parent-age data.
---

**The existing wiki extracts cannot link job type, family size, state and parent age for the same parents.** They contain separate aggregates. HILDA's documented person and family links provide a route to joint analysis with approved data access. A custom Census table is another route to investigate, but the required combination has not been confirmed in TableBuilder.

**Checked 11 November 2026.** This is a data-availability finding, not an estimate of how occupation affects fertility. No joint observations or new empirical graphs were obtained. Original ABS and HILDA websites returned proxy HTTP 403. The evidence below comes from the checked-in extracts, archived Census metadata and an inspected HILDA user manual; current products and access conditions still need checking.

## What the wiki already contains

The [Australian population and economy guide](/data/australia/) provides the following downloads. None contains person, family or household identifiers.

| Existing extract | Dimensions actually stored | What is missing for this question |
| --- | --- | --- |
| [Census population](/data/australia/census-population.csv) | State/territory and people counted in 2021 | Parent status, ages, jobs and family size. |
| [Census age counts](/data/australia/census-age.csv), with [original age bands](/data/australia/census-age.tsv) | State/territory × age group, all people | Ages are not identified as parents' ages; no job or family-size link. |
| [Census families](/data/australia/census-families.csv), with [original child-status cells](/data/australia/census-families.tsv) | State/territory × couple/one-parent family; presence of children under 15, dependent students and non-dependent children in the source | Presence is not a count of children. No parent age or job type; the archive also omits couples without children. |
| [Industry employment](/data/australia/industry-employment.csv) | National industry × quarterly date, November 1984–May 2025 | No state, occupation, parent status, age or family size. Industry is the employer's activity, not the worker's occupation. |
| [Annual indicators](/data/australia/annual-indicators.csv) | National indicator × year, 2000–2025 | No parent or family characteristics. |

Joining state age totals to state family totals would not reveal which ages belong to those parents. Combining them with national industry totals would not recover occupations or families either. Such aggregate comparisons cannot establish individual associations: see [ecological inference and causality](/guides/causality/).

## Define the question before requesting data

| Term | Definition to choose |
| --- | --- |
| Job type | **Occupation** describes the work performed, such as professional or trades work. **Industry** describes the employer's activity, such as health care or construction. **Labour-force status** describes employment, unemployment or being outside the labour force; full-time/part-time status is another distinction. Keep these separate. |
| Family size | Choose total people in the family, all resident children, resident dependent children, or resident children under 15. A household can contain more than one family. |
| Fertility / children ever born | A lifetime childbearing measure differs from children currently living with a parent. Resident counts change when children leave home, even without a new birth. |
| Parent age | Use the age of the identified parent. The age of a dependent child, a household reference person's age and the age of an arbitrary adult are different measures. |
| Parent and unit of analysis | Decide whether each row represents one parent, one family, or one child. Two parents can contribute two parent observations but only one family. Specify whether the question concerns co-resident, biological, adoptive, step or non-resident parents. |

For a first descriptive comparison, use **parents' current occupation × number of resident children × state × the same parent's age group**, retaining employment status separately. For birth timing or completed fertility, request childbearing histories instead of substituting resident-child counts.

## Census tables that provide partial links

The archived 2021 General Community Profile metadata identifies the tables below. The [state-file inventory](/data/australia-family-jobs/census-state-file-locators.json) lists their `STE` files, including multipart tables. We inspected metadata, not the observation counts in those files. Obtain the actual tables from [ABS DataPacks](https://www.abs.gov.au/census/find-census-data/datapacks) or [Community Profiles](https://www.abs.gov.au/census/find-census-data/community-profiles).

| Table | Archived title and population | Useful link / missing link |
| --- | --- | --- |
| **G28** | *Number of Children Ever Born*; females aged 15 years and over | Cell descriptors link the woman's age group to children ever born. This includes zero children and a **six-or-more** category. It lacks occupation and is not a count of resident children or a table of both parents. |
| **G29** | *Family Composition*; families and persons in families in occupied private dwellings | Source of the existing family-type extract. Does not supply the requested job × child-count × parent-age relationship. |
| **G30** | *Family Composition and Country of Birth of Parents by Age of Dependent Children*; dependent children | Parents' birthplace and family composition are linked to the **child's age**. This is not parents' ages or occupations. |
| **G47** | *Labour Force Status by Sex of Parents by Age of Dependent Children for Couple Families*; dependent children in couple families | Connects parents' labour-force status with their dependent children's ages. Counts children, not families; does not identify the parents' occupation, age or family child count. |
| **G48** | *Labour Force Status by Sex of Parent by Age of Dependent Children for One Parent Families*; dependent children in one-parent families | Similar partial link for one-parent families. Again, the age is the child's and the counting unit is children. |
| **G54** | *Industry of Employment by Age by Sex*; employed persons aged 15 years and over | Connects industry with workers' ages, but does not identify which workers are parents or attach child counts. |
| **G60** | *Occupation by age by Sex*; employed persons aged 15 years and over | Connects occupation with workers' ages, but does not identify parents or their family size. |

These tables are useful starting points, but merging their state totals cannot create the missing joint distribution. G47 and G48 do not answer “how many families have two employed parents?” without a separate family-counting table.

One catalogue inconsistency needs resolution: **G58** is titled “Total Family Income (Weekly) by Labour Force Status of Parents/Partners for Couple Families with Children”, while its archived population says “Couple families with no children”. Both strings are preserved in the [catalogue extract](/data/australia-family-jobs/census-table-catalogue.json). Do not choose a universe from this contradictory metadata without checking the original ABS table.

## Where to obtain a joint dataset

### Census TableBuilder or an ABS custom table

Start with the [2021 Census dictionary](https://www.abs.gov.au/census/guide-census-data/census-dictionary/2021), [Census microdata product page](https://www.abs.gov.au/statistics/microdata-tablebuilder/available-microdata-tablebuilder/census-population-and-housing) and [TableBuilder](https://www.abs.gov.au/statistics/microdata-tablebuilder/tablebuilder).

Ask whether a **person-counting table restricted to identified parents** can combine state of usual residence, the parent's age, current occupation or industry, and the count of children in that person's family. Check that the child count belongs to the same family, rather than all children in the dwelling. Confirm variable availability, universes and counting units in the selected product before export. No successful four-way TableBuilder query has been run here; this is a request specification, not a verified ready-made table.

If the product cannot attach these family characteristics to the same parent, ask ABS about a custom aggregate table or Census microdata with person–family–dwelling linkage through its [microdata access services](https://www.abs.gov.au/statistics/microdata-tablebuilder). Current registration, fees, permitted combinations, detailed-geography access and approval conditions were not verified. For characteristics of **both** parents, request two sets of parent fields on a single family record rather than assuming a standard person table supplies them.

### HILDA: a documented route to person and family linkage

The Household, Income and Labour Dynamics in Australia Survey is a stronger documented candidate for this joint question and for following changes over time. The inspected **HILDA User Manual, Release 21**, last modified **5 December 2022**, describes these fields and links. This is evidence about a documented historical release; no HILDA individual records were obtained or analysed.

[Official HILDA site and access information](https://melbourneinstitute.unimelb.edu.au/hilda) · [Inspected archived manual](https://github.com/Henrik-Alexander/transition_fatherhood_australia/blob/158860420d10a13610fedb38c798eaa3af08dc92/handbooks/HILDA-User-Manual-Release-21.0.pdf).

| Required information | Documented HILDA variables / procedure | Manual locator |
| --- | --- | --- |
| Same person across years | `xwaveid`; household identifier `_hhrhid` is wave-specific and changes between waves | pp. 21–23, §§3.5–3.6 |
| State and parent age | `_hhstate`; `_hgage` is age at 30 June before fieldwork, while `_hhiage` is age at interview | p. 23, Table 3.2; p. 35, §4.1 |
| Parent's current job | `_jbmo62`, two-digit ANZSCO occupation; `_jbmi62`, two-digit ANZSIC industry, for the current main job | pp. 50–51, §4.8 and Table 4.7 |
| Employment status | `_esbrd` / `_esdtl`, broad / detailed employment status | p. 23, Table 3.2 |
| Parent–child and partner links | On the child's record, `_hhfxid` and `_hhmxid` identify co-resident parents by cross-wave ID; `_hhpxid` identifies a partner | p. 22, §3.6 |
| Distinguish families within a household | `_hhfam`, family number; `_hhrih`, relationship in household; `_hhfty`, family type. Use wave + household + family number, not family number alone | pp. 55–60, §4.12 and Table 4.10 |
| Family size / resident children | Derive the chosen count from enumerated people, family membership and parent–child links. The enumerated file includes children and non-interviewed adults; the responding-person file alone is incomplete for household composition | p. 21, §3.5; pp. 55–60, §4.12 |
| Weights and uncertainty | Choose weights for the actual unit and response sample; cross-sectional and longitudinal weights differ. Use the documented survey-design procedures and replicate weights for uncertainty | pp. 98–104, weighting discussion and Tables 4.30–4.31 |

The underscore in a variable name is replaced by the wave letter. A viable construction links a child's parent ID to the parent's `xwaveid` **in the same wave**, attaches that parent's job and age, then counts distinct qualifying children under the chosen family definition. Check for missing links, multiple families, non-response and duplication. Household listing order has no parental meaning (p. 21).

Important limits from the manual:

- Co-resident parent identifiers include adoptive, step and foster parents and a parent's de facto partner. Separate biological identifiers have their own “ever co-resident” coverage (p. 22). These links do not enumerate every non-resident parent or every lifetime birth.
- The “father's occupation” and “mother's occupation” history variables describe jobs around the time the respondent was **14**, not necessarily a current parent's job (p. 52). Use the identified parent's own current-job fields for the proposed comparison.
- Household child-age counts in Table 4.10 are not automatically counts of that particular parent's children. The manual's dependent-child age counts use a 30 June reference date; align ages and composition dates before combining them (pp. 35, 59–60).
- Detailed codes can depend on the release and access tier. Some codes are restricted; check the precise fields, missing-value codes, wave coverage and sample sizes in the approved release (pp. 50–52). Fine state × age × occupation × child-count cells may be sparse.
- The manual requires an online application through HILDA Dataverse, managed by the Australian Data Archive, and confidentiality documentation (p. 20). Check today's procedure through the official HILDA site. Public documentation does not mean unrestricted access to records or permission to publish them.

This establishes a documented linkage route, not a verified final four-way extract. A current data dictionary, access approval, actual record coverage, family-count construction and suitable weights still need validation. A parent-weighted comparison describes parents; producing one row per family requires a separate, justified family-level weighting strategy.

## A concrete next extraction

Request one cross-tabulation or approved-record extract with the following specification:

1. **Population and unit:** co-resident parents, including those not employed; one parent observation per year/wave. State whether step/adoptive/foster parents are included. A family-level analysis would instead need one record per family and explicit fields for each parent.
2. **Dimensions:** state of usual residence, that parent's age group, main-job occupation, main-job industry, labour-force status, family type, and the number of resident children under the chosen definition. Preserve non-employed and job-information-missing categories separately.
3. **Child measure:** start with children under 15 in the same family; request all resident children as a separate measure. Do not use household totals or children ever born as substitutes. For fertility analysis, separately establish childbearing-history coverage and definitions.
4. **Timing and quality:** keep one Census vintage or same-wave HILDA records; record age/composition reference dates, classifications, missing responses, confidentiality perturbation, top-coding and, for survey data, weights and standard errors. Pool years only with an explicit design.
5. **Output:** counts and the distribution of child counts within each parent-age × state × occupation group, with denominators and source metadata. Broaden age/job groups where cells are unreliable. Do not interpret an open-ended category as an exact count when calculating means.

Once this joint extract exists, suitable graphs would compare child-count distributions by occupation within state and parent-age bands. The current separate aggregates cannot support those graphs. Even a valid joint table would show association; selection into work, income, age and reverse effects of children on employment require a separate [causal research design](/guides/causality/).

## Evidence and remaining checks

The [source manifest](/data/australia-family-jobs/sources.json) records retrieval URLs, hashes, versions and access failures. The [catalogue](/data/australia-family-jobs/census-table-catalogue.json), [illustrative cell descriptors](/data/australia-family-jobs/census-cell-examples.json) and [state-file locators](/data/australia-family-jobs/census-state-file-locators.json) preserve the inspected metadata. They contain no new population counts or confidential records.

The Census metadata comes from the third-party `auscensus` **`aux_files` release**, fetched on 11 November 2026. That release tag is mutable; the manifest's checksums identify the retrieved payloads. The [processing code at revision `fcd367e`](https://github.com/carlosyanez/auscensus/blob/fcd367e10fab602d561ea9a9cea3a7ea12df355d/data-raw/process_data.R) traces the catalogue and descriptors to ABS DataPack metadata workbook sheets. It does not authenticate the archived metadata against the official 2021 workbook.

The HILDA manual is a primary provider document hosted in a third-party archive, pinned at revision `158860420d10a13610fedb38c798eaa3af08dc92`. Its title page and page-specific content were inspected. Agreement with the currently hosted official manual, newer-release availability and current access/reuse conditions remain unverified. References are to the manual's printed page numbers, which match the PDF pages in this copy.

See the [independent audit record](https://github.com/adludo/research-economics/blob/docs/australia-family-jobs-data/docs/audits/2026-11-11-australia-family-jobs.md) for completed checks and unresolved evidence. The immediate next step is to confirm the custom Census table's variable compatibility; HILDA offers a documented alternative where approved linked records are needed.
