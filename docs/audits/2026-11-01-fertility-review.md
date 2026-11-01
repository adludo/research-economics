# Research audit: fertility, development, and parents' time

- Target: fertility extension on `docs/fertility-economics`, working tree based on `e878230adf393914de8b01b7499fe28ed08df426`.
- Date: 1 November 2026, UTC.
- Independent auditors: `/root/audit_leisure` and `/root/audit_productivity`, following the repository's `research_auditor` role.
- Scope: six research papers, one handbook review, their findings and data guides, source-copy provenance, and integration/evidence-status wording.
- Verdict: **selected identities and summary claims supported by inspected author-hosted publication copies; independent publisher-record checks and empirical replication incomplete**.
- Material contradictions in the scoped paper summaries: none found.

## What changed from earlier collections

The main agent obtained seven original author-hosted publication copies from the public repository `mdoepke/mdoepke.github.io` at revision `d25df3c1d402d07977615f81f7cbe39c8ba8bc37`. It read the relevant primary passages before drafting summaries. The author bibliography was also retrieved at that revision and matched the page used for citation checks.

The independent reviewers inspected the PDF texts, citation mastheads and author bibliography. Both matched recorded hashes/byte counts to the copies they read; the four-source reviewer independently downloaded those four PDFs as well. The three-source reviewer checked the supplied original files without making a fresh independent download. Exact links and hashes are in [`public/data/fertility/sources.json`](../../public/data/fertility/sources.json).

This is stronger than a reading list based on an inaccessible conversation or remembered abstracts. It is still **author-hosted publication-copy verification**, not a live DOI/publisher-record or retraction check. No copyrighted PDF is redistributed in this repository.

## Evidence ledger

Printed-page locators refer to pagination in the inspected publication; PDF-page locators count from the file's first page.

| Source | Identity and primary passages inspected | Supported summary and boundary |
| --- | --- | --- |
| Doepke (2004), *Accounting for Fertility Decline During the Transition to Growth*, JEG 9(3), 347–383 | PDF masthead and author bibliography; §6 p.365/PDF19; policy comparison and welfare discussion p.373/PDF27; conclusion p.374/PDF28 | Calibrated growth/fertility/education mechanisms and larger role of child-labour restrictions than subsidies alone in the comparisons. Not an experimental policy estimate or a leisure effect. Higher GDP need not be a Pareto gain. |
| de la Croix and Doepke (2003), *Inequality and Growth: Why Differential Fertility Matters*, AER 93(4), 1091–1113 | Identity from PDF/bibliography; mechanism pp.1091–1093/PDF1–3; Tables 3–4 pp.1107–1108/PDF17–18; conclusion p.1109/PDF19 | Model links fertility differences, education and growth; regressions provide associations. Data timing and endogeneity qualifications pp.1106–1108 are retained; no universal fertility-reduction policy claim. |
| Doepke (2005), *Child mortality and fertility decline: Does the Barro-Becker model fit the facts?*, JPopEcon 18(2), 337–366 | Masthead/printed DOI `10.1007/s00148-004-0208-z`; calibration pp.344–345/PDF8–9; extension/conclusion pp.357–360/PDF21–24 | Calibrated historical mortality decline does not reproduce declining surviving-family size. The draft explicitly avoids claiming that better survival always lowers births; p.359 describes non-monotonicity. |
| Doepke, Hazan and Maoz (2015), *The Baby Boom and World War II: A Macroeconomic Analysis*, ReStud 82(3), 1031–1073 | Masthead/printed DOI `10.1093/restud/rdv010`; abstract p.1031/PDF1; mechanism pp.1033–1034/PDF3–4 | Historical labour-supply/cohort-competition mechanism and model attribution. Not a direct leisure experiment or a universal effect of shorter work schedules. |
| Doepke and Kindermann (2019), *Bargaining over Babies*, AER 109(9), 3264–3306 | Masthead/printed DOI `10.1257/aer.20160328`; mechanism/policy pp.3264–3267/PDF1–4; respondent/sample definitions pp.3269–3270/PDF6–7; birth association pp.3273–3274/PDF10–11 | Partner agreement/birth association, childcare-cost allocation and model policy predictions. One respondent reports both partners' intentions; analytic samples differ. Freed childcare time is not assumed to become leisure. |
| Doepke and Tertilt (2018), *Women's Empowerment, the Gender Gap in Desired Fertility, and Fertility Outcomes in Developing Countries*, AEA P&P108, 358–362 | Masthead/printed DOI `10.1257/pandp.20181085`; §§I–II pp.358–359/PDF1–2; Table1 and §§V–VI pp.360–361/PDF3–4 | Descriptive empowerment/desired-fertility evidence and bargaining interpretation. Not a causal empowerment-to-GDP experiment; desired family size differs from wanting another child or realised births. |
| Doepke, Hannusch, Kindermann and Tertilt (2023), *The Economics of Fertility: A New Era*, Handbook of the Economics of the Family vol.1, ch.4, 151–254 | Masthead/printed DOI `10.1016/bs.hefam.2023.01.003`; changing relationships pp.153–154,169–174; time use pp.225–229; conclusion p.233 | Survey synthesis of high-income patterns and career–family compatibility, not a universal new causal estimate. The direct leisure bridge on p.227/PDF77 is correctly described as a synthesis of US time-use research. |

All five DOI strings included in the new register are actually printed in the inspected copies. The two other entries do not invent a DOI. The handbook is counted as a review rather than an additional independent empirical finding.

## Key interpretation checks

- The six research papers and one review are explicitly described as an author-centred, non-systematic entry point, not an exhaustive survey or a ranking of the latest 2026 evidence.
- The findings table preserves model versus association versus review distinctions.
- The 2005 mortality finding is scoped to calibrated historical comparisons; the hump-shaped births–survival relation is retained.
- The 2019 bargaining paper's one-respondent measurement structure is stated; intentions and outcome samples are not conflated.
- The review's p.227 discussion links increased childcare time with declines in other housework and leisure in the US evidence it synthesises. The wiki does not claim to replicate the underlying time-use studies or identify a leisure-to-birth causal effect.
- Fertility/education channels are not presented as isolated TFP estimates, and GDP, GDP per person, hourly productivity and welfare are kept distinct.
- Crude birth rate, period TFR, completed fertility, intentions, and surviving children are separated. Model “net fertility” is not automatically called the demographic net reproduction rate.

## Data guidance and remaining checks

The household and time-use source attributions were checked against the papers: GGP respondent structure, DHS couple evidence, ATUS/CPS in handbook Figure29, MTUS in Figure30, and historical sources described in the growth papers.

However, the collection adds **no new demographic observations, simulations, or graphs**. Official-provider links are discovery routes for future work. Fresh access probes to all seven external provider links in `data/fertility.md` were blocked by proxy tunnel HTTP403. The [access record](2026-11-01-fertility-provider-access.json) preserves exact URLs and outcomes.

Pending work:

1. Independently check live publisher/DOI records, publication corrections and retractions.
2. Confirm demographic-provider definitions, indicator codes, current releases and access conditions, including WDI birth-rate/TFR codes, WPP, HFD, GGP, DHS and OECD products.
3. Verify original empirical inputs and replicate estimates/simulations before claiming replication or robust causal identification.
4. Expand author/source coverage before presenting a systematic or representative literature review.
5. Inspect source funding/disclosure records systematically if future summaries make such claims. The new entries make no funding claims; absence of claims is not evidence of absent funding.

## Corrections during review

The reviewers requested that the old global statement about uncompleted full-text checks be scoped to the original 23-reference collection. The source and audit-status pages now distinguish that historical status from the fertility extension's inspected-copy status; the four-source reviewer rechecked both corrections. The three-source reviewer also confirmed removal of “subsequent” from the 2003 regression sentence, avoiding an overstatement of temporal ordering. The research summaries required no material correction in the reviewed source-reading scope.

## Technical validation

The production build passed, generating 22 HTML pages and search assets. Local validation passed 1141 internal link/image/anchor checks, all seven source-copy hashes, the public provenance copy, and local audit-record links. Existing optional i18n/404 and sitemap warnings remain. These checks validate documentation integration, not the original research's scientific correctness.
