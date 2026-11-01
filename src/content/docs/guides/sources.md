---
title: Source and editorial notes
description: Provenance, verification status, and interpretation rules for this research wiki.
---

## Source material

The initial research content was prepared from the user-supplied **“Pasted text.txt”** discussion, supplied on 30 October 2026. It covers economics of leisure, closed economies and GDP, and a follow-up on the findings of each leisure paper. The [shared conversation](https://chatgpt.com/share/6ae3d9dc-5678-83ec-9fde-8474c85c588a) is a contextual reference; the pasted text is the material used here.

## Verification status

See the [audit status](/guides/audit-status/) for checks completed on the merged data and graphs and the primary-source checks still outstanding.

- The original leisure and trade collections reorganise the supplied discussion into citations, dataset guides, and finding summaries. The leisure–productivity extension is a separate literature selection, not content from that discussion.
- For the original 23-reference reading lists, publisher/provider access was blocked and independent full-text checks have **not** been completed. The later fertility collection is different: relevant passages were read from author-hosted publication copies, while independent publisher-record and current provider checks remain outstanding.
- Approximate numbers remain approximate. They should be checked against the final paper's table/page before quotation in further research.
- A working-paper link is explicitly labelled and may not match the final publication's estimates. A dataset catalogue is an access route, not evidence that a paper used the current release.
- The original literature reading guides did not download data or replicate estimates. The separate [working-hours collection](/data/working-hours/) includes retrieved data and generated graphs. Data-access conditions in the reading guides remain guidance, not a claim of access approval.

## Reconciliation of the discussion

The recession paper's published title is **“Time Use During the Great Recession.”** The initial discussion used the working-paper title “Time Use During Recessions.” Its initial home-production estimate was a 30–40% range; the follow-up used about 30%. The wiki retains that discrepancy rather than implying exact agreement.

Ramey–Francis and Aguiar–Hurst are kept separate because period, population, and activity definitions differ. The trade section preserves the distinction between welfare-equivalent gains, income-level effects, and GDP-growth rates.

## Next verification steps

1. Read the final publications and add page/table references for numerical claims.
2. Confirm linked working papers against the final versions, including the embargo and leisure-technology estimates.
3. Select dataset releases, licences, weights, and samples for a concrete empirical question.
4. Add reproducible analysis only after recording those choices.

Use the [contribution guide](/guides/contributing/) for new entries. This is a curated starting bibliography, not an exhaustive or systematic review.

## Leisure–GDP–productivity extension

Added on 30 October 2026 in response to the question about leisure and GDP/general productivity. Seven additional studies cover hours and development (Bick et al.), taxes (Prescott), institutions and coordinated leisure (Alesina et al.), European output and hours (Blanchard), welfare accounting (Jones–Klenow), long-hours productivity (Pencavel), and sleep/wages (Gibson–Shrader).

This extension is a reading guide based on established literature rather than new live-source research. External publisher access was blocked; bibliographic details, link destinations, and qualitative summaries await independent verification against final articles. No estimates were replicated. No numerical effect sizes are quoted for the new studies; the arithmetic example in the findings page is explicitly illustrative. The original collection's numerical summaries retain their separate discussion-based provenance.

## Working-hours data collection

The international hours page uses CSV files and metadata retrieved on 30 October 2026 from OWID's public `owid-datasets` archive, pinned to revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2`. Unlike the earlier reading guides, its country figures were calculated from retrieved data. They were not checked against original paper tables or current provider releases. Direct OECD, ILO, and OWID chart endpoints remained inaccessible. The page links to both the archive and official providers and records source checksums, transformations, and attribution in its downloadable provenance file.

The metadata and CSV downloads on that page are the exception to the original collection's statement that no data were downloaded. The paper summaries remain unreplicated.

## Fertility, development, and parents’ time

The fertility extension adds six research papers and one review published in 2003–2023. Unlike the earlier discussion-based reading lists, the relevant primary-text passages were read from author-hosted publication copies in Matthias Doepke’s public research repository, pinned at `d25df3c1d402d07977615f81f7cbe39c8ba8bc37`. [Source URLs and SHA-256 hashes](/data/fertility/sources.json) identify the inspected files; the wiki links rather than redistributes the PDFs.

The paper register includes printed-page and PDF-page locators. Publication-copy support does not establish independent publisher-record verification, data validity, causal identification beyond the paper’s design, current provider access, or replication. This author-centred collection is a focused entry point, not a systematic review. The initial literature reading guide did not generate demographic observations or graphs. The later [fertility/GDP/hours graph collection](/data/fertility-charts/) is a separate archived-data analysis. See [fertility audit status](/guides/audit-status/#fertility-collection).

## Fertility, GDP, and hours graphs

The later graph collection uses same-country, same-year historical estimates from 1970–2014. Fertility comes from Gapminder v12 via the pinned OWID archive; forecasts from 2015 onward are excluded. GDP, population, and hours come from the OWID PWT archive. Its folder/metadata say “10.0”, but the matched values agree with CRAN-distributed PWT10.01 rather than 10.0; this discrepancy is disclosed on every figure and in the [comparison record](/data/fertility-economy/pwt-vintage-check.json). Original metadata and retrieval URLs are preserved.

This is descriptive data analysis, not replication of the fertility papers. It uses TFR rather than counts of births, and does not treat market hours as leisure or GDP per person as hourly productivity.

## Leisure and trade graph additions

The leisure, leisure/productivity and trade data pages now include frozen-archive graphs and CSV extracts. US residual leisure and Norwegian daily leisure are kept separate. Productivity uses output GDP divided by total market worker hours; exports/GDP is interpreted from the archive's documented export formula despite its conflicting column label. Every figure contains retrieval references. These additions check aggregate archive values and do not verify the original papers' estimates or establish causal effects.
