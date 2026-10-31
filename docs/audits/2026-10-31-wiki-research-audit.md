# Research audit: current wiki and supplemental working-hours branch

- Audited main commit: `06433e338a3baf2fad2625013075baf42c70ca18`.
- Supplemental data/graph commit: `73c59947e3ad7f9946f8ac772ee1cbd2bea53860`, on `docs/world-working-hours`; **not merged into the audited main commit**.
- Date: 31 October 2026, UTC.
- Auditors: independent subagents `/root/audit_leisure`, `/root/audit_trade`, `/root/audit_productivity`, and `/root/audit_hours_graphs`, following the repository's `research_auditor` instructions through the supported delegation fallback.
- Verdict: **verification incomplete**. The working-hours archive-to-extract-to-graph pipeline passed the inspected checks. No primary paper identity or paper-derived substantive finding could be verified because all attempted publisher/reference requests were denied by the proxy. This is not evidence that a paper is fictitious or that a finding is false.

## Scope and coverage

| Scope | Inventory and work completed | Boundary |
| --- | --- | --- |
| Main leisure collection | Eight core papers, one review, their findings, seven data-source categories, all numerical finding groups; 17 reference/provider requests | No primary text or provider record retrieved |
| Main trade collection | Seven papers, their findings, seven data-source groups; 15 reference/provider requests | No primary text or provider record retrieved |
| Main leisure/productivity collection | Seven papers, their findings, four data-guide sections, two mathematical checks; 15 reference/provider requests | No primary text or provider record retrieved |
| Main site structure | Production build, 16 generated HTML pages, 614 internal targets/anchors, generated search files | Technical checks, not scientific verification |
| Supplemental working hours | Two datasets; four upstream payloads; 3,492 PWT observations, 66 common-year rows, 182 historical rows; 91 displayed table rows; three figures with SVG and PNG exports | Archived distribution verified; original-provider science/definitions and reuse terms remain unverified |

The three literature sub-auditors checked their scoped files against the exact main SHA, not just a mutable checkout. The graph auditor inspected a separate snapshot extracted from its exact SHA. The glossary branch is not in audited main and is outside this report. Main has data-source guides, not downloaded empirical data or graphs; the latter checks refer only to the explicitly identified supplemental branch.

## Findings, highest priority first

| ID | Severity / type | Status | Location and evidence | Next action |
| --- | --- | --- | --- | --- |
| AUD-01 | Major verification gap | Unverified | All 23 paper references: DOI, AEA, and NBER attempts failed with `Tunnel connection failed: 403 Forbidden`. No full text or primary identity record was inspected. | Resolve each reference, read the exact cited version, and check substantive claims. Do not label the research verified. |
| AUD-02 | Traceability defect; minor in trade sub-review, major verification importance in leisure sub-review | Missing locators verified; scientific support unverified | Numerical summaries in `papers/leisure.md:43,55,67,79,103` and `papers/trade.md:19,30,63,74`, repeated in finding tables, do not cite specific primary pages/tables/figures. Existing notices correctly disclose pending verification. | Add version-specific locators after obtaining texts. Do not invent them or remove the notices. |
| AUD-03 | Version-specific verification gap | Unverified | Irwin's published-version 5% result links to a working paper; the leisure-technology 2% result also needs final-versus-working-paper verification. Both pages disclose the version distinction. | Read both versions and identify the source supporting each estimate. |
| AUD-04 | Specification-specific verification gap | Unverified | Recession home-production shares of about 30% and the earlier 30–40% range are both disclosed, but cannot be reconciled against inaccessible primary tables. | Record the specification, activity definition, and version behind each number. |
| AUD-05 | Minor editorial ambiguity | Corrected and independently rechecked | `data/leisure-productivity.md:14` had implied that “hours per worker” and “hours per employed person” must be different statistics. They can use the same denominator. | Wording now requires checking source terminology, employment/job coverage, and populations. No provider definition has thereby been verified. |
| AUD-06 | Original-data verification gap | Unverified | Working-hours archive files and graph calculations passed, but original PWT and Huberman–Minns publication access remained blocked. Metadata contains changing historical source definitions. | Verify the original-provider definitions, historical reconstruction, revisions, and reuse terms before treating archive consistency as scientific validation. |

No primary-source-backed contradiction or fabrication was established. Internal agreement cannot exclude a consistently repeated mistake.

## Evidence ledgers

- [Every paper and its claim set](2026-10-31-paper-evidence-ledger.md): 22 core papers plus one review, identities and substantive/numerical results all primary-source unverified.
- [Working-hours data and graph checks](2026-10-31-working-hours-audit.md): independent data lineage, recalculation, rendered-image and SVG geometry checks, and reproduction limits.

### Numerical claims in the literature

| Claim group | Internal check | Primary support |
| --- | --- | --- |
| Aguiar–Hurst: men +6–9, women +4–8 weekly leisure hours, 1965–2003 | Values, period, and definition caveats agree between paper and finding pages | Unverified |
| Ramey–Francis: +4–5 weekly leisure hours over the century | Values and population caveats agree | Unverified; exact denominator needs checking |
| Ramey: prime-age women −18, men +13 weekly household-work hours, 1900–2005; slight aggregate increase | Signs, values, period, and population distinction agree | Unverified |
| Recession: approximately 30% home production, 50% leisure; earlier home-production range 30–40% | Discrepancy is consistently disclosed | Unverified; reconcile specifications |
| Leisure technology: ages 21–30; approximately 2% lower work hours | Approximation and model-based attribution retained | Unverified; version-specific check needed |
| Irwin: welfare loss approximately 5% of 1807 GNP | Denominator and distinction from observed GDP decline agree | Unverified |
| Bernhofen–Brown: upper bound approximately 8–9% of GDP | Bound and welfare interpretation retained | Unverified |
| Wacziarg–Welch: approximately +1.5 percentage points annual growth, 1950–1998 | Percentage-point and confounding qualifications retained | Unverified |
| Feyrer: income–trade elasticity approximately 0.25 | 10% more trade → approximately 2.5% income is a valid first-order illustration; exact constant-elasticity calculation is 2.4114% | Coefficient and identification unverified; arithmetic only verified |
| GDP/person = GDP/hour × hours/worker × workers/person | Verified algebraic cancellation when concepts/populations match | Accounting identity, not an empirical finding |
| 10% fewer hours and 5% higher output/hour → 5.5% less output | Independently calculated with Decimal: 0.90 × 1.05 = 0.945 | Verified illustrative arithmetic; correctly not attributed to a paper |

The productivity extension adds no numerical empirical effect estimates. Its seven qualitative summaries still need primary-text support.

### Data-source guide checks

The auditors inventoried ATUS and its well-being files, AHTUS, MTUS, HETUS, OECD time use, Japan's national survey, historical reconstruction sources, WDI and its four indicator codes, PWT, Maddison, Comtrade, WITS/TRAINS, Wacziarg–Welch reform dates, OECD productivity, ILOSTAT, CPS, and workplace/welfare-accounting guidance. All attempted official-provider links were denied. No current provider metadata, access conditions, data vintage, or paper-to-dataset correspondence was independently verified from those pages.

The guides generally distinguish recommended access routes from a paper's exact input version. They are not replications. Definitions, country coverage, licences, sample restrictions, and access requirements must still be checked at the source.

### Interpretation and disclosure checks

Within the inspected wording, the following distinctions are consistently retained: welfare versus GDP; income levels versus growth; estimates versus upper bounds; percentages versus percentage points; market work versus unpaid work; sleep versus discretionary leisure; wages versus physical productivity; and association or calibrated attribution versus experimental causation. These are internal wording checks, not confirmation that each paper supports every interpretation.

No funding, sponsorship, or conflict-of-interest claim was found in the scoped research summaries. Checking an asserted funding claim was therefore not applicable. Original acknowledgements, corrections, and retraction records were not retrieved; their absence from this report does not establish absence in the originals.

## Reproduction and technical checks

The main agent ran the main site's production build with `ASTRO_TELEMETRY_DISABLED=1 npm run build`. It completed successfully, generating 16 HTML pages and search files. A local HTML parser checked 614 internal targets/anchors. Existing warnings concern optional i18n/404 entries and an unset sitemap `site`; they do not prove or disprove research claims.

The main agent also ran both working-hours scripts in a separate writable copy of the exact supplemental snapshot. All CSVs, archived metadata, six SVG/PNG exports, and the generated Markdown page matched byte-for-byte. Only `retrieved_date_utc` in provenance advanced from 2026-10-30 to 2026-10-31. The graph auditor inspected that comparison separately from its own independent recalculation and coordinate checks.

The denominator wording correction was rechecked by `/root/audit_productivity`: PV-02 is resolved as an editorial ambiguity. All original primary-source gaps remain.

## Access blocker and configuration

Across the three literature sub-audits, 47 reference/provider requests were made, with overlap between scopes. Every request failed at the proxy tunnel with a 403, before source content could be read. No TLS verification or network controls were bypassed.

A proposed allowlist was saved to the environment configuration draft for DOI/Crossref, NBER, AEA, referenced publishers, and official data providers. Existing package-manager presets were preserved. The draft save is confirmed; it has **not applied runtime access or published the environment**. Redirects or full-text hosts may require additional exact destinations once source access is enabled.

## Recheck requirements

1. Review/save the proposed network changes in environment settings and publish the environment as required by the product, or provide lawful local copies of the originals.
2. Retest actual source access; an allowlist declaration alone is not proof of access or entitlement to paywalled text.
3. Verify all 23 paper identities and final/working-paper correspondences, then attach primary locators to every numerical and substantive finding.
4. Resolve the recession-share and version-specific estimate checks; inspect corrections/retractions.
5. Verify current provider definitions, source releases, access/reuse conditions, and original working-hours provenance.
6. Keep current verification notices. Do not describe the full wiki as scientifically verified based on this audit.
