# Research audit: merged wiki on main

- Audited commit: `68eb30f465deecfa99d098b682f396013d91deb3`.
- Branch: `main`; this commit includes the working-hours collection, all three graphs, and the glossary.
- Date: 31 October 2026, UTC.
- Independent reviewers: `/root/audit_hours_graphs` and `/root/audit_productivity`, following the repository's `research_auditor` role and audit guide through the supported delegation tools.
- Verdict: **archive-to-graph correctness verified within the checks below; full primary-source verification incomplete**.
- New material data/graph defects found: none.

## Scope and relationship to the earlier audit

The merged working-hours files are byte-identical to previously audited `73c59947e3ad7f9946f8ac772ee1cbd2bea53860`. The current data/graph auditor independently confirmed that identity and performed fresh source-download, extraction, table, coordinate, and image checks against this main commit. Its verdict no longer concerns an unmerged branch.

The paper and findings pages are unchanged from earlier audited `06433e338a3baf2fad2625013075baf42c70ca18`. Their earlier primary-source verification gaps still apply. The main agent freshly probed all 23 paper-reference URLs plus the two original working-hours provider/article URLs; all 25 failed with proxy tunnel HTTP 403. Those probes are not primary-text readings. The current integration auditor independently retried two representative paper URLs, also blocked.

The updated integration review covers all 25 glossary terms, reading notes, overview/navigation, source notes, and productivity-data guidance. It does not silently replace the previous literature audit with a new full-text audit.

## Verified checks

| Item | Status | Evidence and method |
| --- | --- | --- |
| Merged artifact identity | Verified | All 16 working-hours files match audited main and the earlier graph commit exactly |
| Pinned archive identity | Verified against archived distribution | Fresh independent downloads of both CSVs and both metadata files matched all four recorded SHA-256 hashes at OWID revision `6155d4ca1ea14ef30e753010a25521eeb416e8a2` |
| PWT extract | Verified against archive | All 3,492 non-missing country-year values, 69 economies, 1950–2019, independently extracted and compared |
| PWT 2019 subset | Verified against archive | All 66 values, labels and year filters independently checked; missing values not replaced with zero |
| Historical extract | Verified against archive | All 182 records across 14 economies, including empty fields and archived source-transition notes |
| Displayed tables | Verified | All 91 rows: 66 for 2019, 14 historical endpoints, 11 percentage changes; recomputed from full-precision observations |
| Recent-trend curves | Verified | All 568 vertices across 12 countries checked against actual SVG path geometry within `2 × 10⁻⁶` coordinate units |
| Historical curves | Verified | All 182 vertices across 14 countries checked against actual SVG geometry within `2 × 10⁻⁶` units |
| Change bars | Verified | All 11 signs, bar widths, ordering and labels checked against independent endpoint calculations |
| Chart presentation | Verified at inspected resolution | All three PNGs freshly viewed; axis bounds, panel scales, endpoint labels and captions checked; no material clipping or visual defect found |
| Missing data | Verified | South Africa begins in 2001, lacks 2015, and is excluded from 1990 comparisons; actual SVG path breaks preserve the gap |
| Selection and comparability cautions | Verified in text/code | Recent selection is 12 illustrative economies, not a world average; historical and PWT series are not spliced; observation guides distinguished from annual estimates |
| Reproduction | Verified, execution by main agent | Both scripts executed in an isolated copy of this main snapshot. All 13 compared outputs match, except the expected provenance retrieval-date update. Auditor separately compares outputs; this is distinct from its independent recalculations |
| Glossary inventory and arithmetic | Verified internally | 25 terms plus reading notes; percentage-point example gives `3 − 2 = 1` point and `(3/2 − 1) × 100 = 50%` |
| Glossary interpretation | Internal review, limited | No material conceptual error established; concepts are not thereby verified against original statistical manuals or each linked paper |

Hashes, source URLs and transformations remain in `public/data/working-hours/provenance.json`. A checksum establishes identity with an archive payload, not the scientific validity of the original data.

### Independently recomputed chart highlights

| Country | Change in annual hours, 1990–2019 |
| --- | ---: |
| South Korea | −26.0% |
| Japan | −16.6% |
| Germany | −12.4% |
| Brazil | −9.1% |
| France | −8.5% |
| Australia | −7.4% |
| United Kingdom | −4.5% |
| Mexico | −1.8% |
| United States | −1.7% |
| India | +2.1% |
| China | +9.8% |

The 2019 sample minimum is Denmark, approximately 1,380.6076 hours, displayed as 1,381. Its maximum is Cambodia, approximately 2,474.9119, displayed as 2,475. All 14 historical 2000 endpoints are below their 1870 endpoints; the intervening paths need not be monotonic. None of these descriptive results proves a causal effect on GDP, productivity, leisure, or welfare.

## What remains unchecked

| Check | Status | Next action |
| --- | --- | --- |
| All 22 core-paper identities and the review reference | Unverified against primary records | Resolve each DOI/NBER/publisher record and match authors, title, date and version |
| Paper-derived numerical and qualitative findings | Unverified against primary texts | Read the exact versions; attach page, table, figure, equation or section locators |
| Final-versus-working-paper estimates | Unverified | Compare versions, especially Irwin's welfare loss and the leisure-technology estimate |
| Recession allocation shares | Unverified | Reconcile approximately 30% versus the earlier 30–40% range with specific definitions/specifications |
| Original PWT release and Huberman–Minns source tables | Unverified | Compare archived values and population/source definitions directly with original files and publication |
| Corrections, retractions, funding and disclosures in original studies | Unverified | Inspect original records and acknowledgements; no claim of absent funding is justified |
| Provider definitions, current releases and access conditions | Unverified where originals inaccessible | Read original PWT, OECD, ILO and other provider documentation; archived data are not current-year estimates |
| Third-party reuse terms | Unverified | Check original-provider and OWID terms before asserting a particular licence or unrestricted rights |
| Paper estimation/causal replication | Not performed | Reproduce the original empirical/model analyses from their actual inputs; descriptive chart reproduction is a different task |
| Live Vercel deployment and mobile interaction | Not inspected | Test the deployed page independently; build, asset checks and PNG inspection do not establish deployed behaviour |

The complete fresh reference-probe record is [main-source-access.json](2026-10-31-main-source-access.json). It records public URLs, timestamps and failures, not retrieved article text. All 25 probes returned `Tunnel connection failed: 403 Forbidden` through inherited proxy settings. No network or TLS controls were bypassed.

## Minor corrections and recheck

1. `data/leisure-productivity.md`: clarify that “worker” and “employed person” can refer to the same denominator; require matching population and job coverage.
2. `guides/sources.md`: scope the “no data downloaded” statement to the original literature guides, distinguishing the separate downloaded working-hours collection.

These are editorial corrections, not demonstrated errors in the research estimates. The independent integration auditor rechecked both corrections and the public status summary and confirmed PV-02 and GI-01 are resolved. The data/graph auditor separately confirmed that the report and status page accurately represent its fresh checks and limits. No existing data or figure is changed by the audit record.

## Reproduction commands and records

The main agent ran these in a separate copy of the exact main snapshot, leaving checked-in inputs and graphs untouched:

```sh
python3 /tmp/wiki-audit-main-68eb30f-reproduction/scripts/collate-working-hours.py
python3 /tmp/wiki-audit-main-68eb30f-reproduction/scripts/plot-working-hours.py
```

The [comparison record](2026-10-31-main-reproduction.json) covers the Markdown page, three CSVs, two metadata files, all six SVG/PNG files, and provenance. Only provenance's retrieval date changes from 2026-10-30 to 2026-10-31.

## Required follow-up

Enable supported access to the cited sources or provide lawful local copies; confirm actual access before continuing. The proposed source allowlist is already saved in environment settings but has not changed this runtime's enforced policy. Complete the unchecked primary-source items above before describing the full wiki as scientifically verified. Rerun data/table/geometry checks after changes to inputs, selections, dates or plotting code.

## Site validation after adding the status page

The production build passed with 19 generated HTML pages and search assets. A local parser checked 915 internal links, images and heading anchors; audit-report links and all 25 source-probe records also passed consistency checks. Existing optional i18n/404 and sitemap warnings remain. These technical results do not establish deployed Vercel behaviour or primary-source correctness.
