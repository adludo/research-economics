# Research audit: equations for the value of leisure

- **Audited base:** `606d580d8260f9d281c71ed0bb29291037739d41`.
- **Branch:** `docs/value-of-leisure`.
- **State:** Dirty working tree before the feature commit.
- **Auditor:** `/root/audit_leisure_value`, independently delegated with the repository research-auditor instructions and audit guide. The author saved this record of the returned checks.
- **Date:** 8 November 2026, UTC.
- **Coverage:** Two new pages, calculator, five source/input/result files, navigation/cross-links, glossary, editorial notes, README, and final audit-status summary. One directly read primary publication copy; two earlier foundations retain their original reading limits. No new chart or empirical dataset was introduced.
- **Verdict:** Primary-copy equation/definition/calibration checks and independent derived arithmetic passed within scope. No material implementation defect found. Publisher authentication, corrections/retractions, older full texts and empirical replication remain unverified.

## Findings, highest severity first

| ID | Severity | Status | Location / claim | Evidence and locator | Required next check |
| --- | --- | --- | --- | --- | --- |
| V-01 | Verification limit | Unverified; disclosed | Publisher authentication and correction/retraction status | DOI requests failed with proxy HTTP 403 | Inspect original publication and correction records separately |
| V-02 | Verification limit | Unverified; disclosed | Original Jones–Klenow (2016) and Becker (1965) full texts | DOI/Stanford routes blocked | Read originals before extending primary-text verification to their earlier wiki summaries |
| V-03 | Interpretation limit | Correctly qualified | Approximately $14.19/hour monetary result | Own derivation from rounded 2006 calibration in 2012 dollars, not a reported universal price | Do not present as a current or individually estimated leisure price |
| V-04 | Model boundary | Correctly qualified | Interior wage equality and broad non-market time | Read primary copy pp.438–440 | Reconsider constraints, definitions and calibration before applying elsewhere |

Blocked originals are unverified, not evidence of fabrication. No supported defect remained in the final inspected implementation.

## Primary source and identity

**Jean-Félix Brouillette, Charles I. Jones, and Peter J. Klenow (2025).** “Race and Economic Well-Being in the United States.” *AER: Insights* 7(4), 429–446. DOI `10.1257/aeri.20240467`.

The auditor independently retrieved the 676,739-byte [author-hosted copy](https://github.com/jfbrou/jfbrou.github.io/blob/1eeeb63a3a020e97778eb926cc09ca3ea472d32b/papers/dignity.pdf). SHA-256:

`563fd50e571f782cc29255e39a4892429b1520534b91972e99d73ab2ebba8836`

The copy's masthead, title, authors, journal/pages, year and DOI were inspected. The GitHub profile identifies `jfbrou` as Jean-Félix Brouillette, matching the first author. These checks establish the inspected copy and its displayed metadata, not independent publisher authentication. The copyrighted PDF is linked rather than committed.

## Evidence ledger

| Claim / object | Status | Locator and method |
| --- | --- | --- |
| `u(c,ℓ)=constant+ln(c)+v(ℓ)` and constant-Frisch `v(ℓ)` | Verified against primary copy | Printed p.433, PDF p.5, unnumbered utility equations |
| Marginal-rate-of-substitution wage condition | Verified against primary copy | Printed p.439, PDF p.11; Section III |
| Consumption-equivalent welfare condition | Verified against primary copy | Printed p.433 eq.(1), p.434 eq.(3); PDF pp.5–6 |
| Leisure share from waking time and annual market work | Verified against primary copy | Printed pp.438–439, PDF pp.10–11; Section II.E |
| 5,840-hour reference budget; leap-year treatment | Verified against primary copy | Printed p.439: 16 hours/day ×365; footnote uses366 in leap years |
| Household and unemployment adjustments | Verified against primary copy | Printed p.439; rough allocation within households and full-time-hour adjustment for involuntary non-employment |
| Calibration inputs | Verified against primary copy | Printed pp.439–440, PDF pp.11–12: `ε=1`, `θ=8.9`, leisure0.70, consumption$31,046, earnings$38,491, marginal tax0.353; 2006 calibration in2012dollars |
| Jones–Klenow bibliographic foundation | Verified as citation in inspected source | Printed p.446, PDF p.18; original full text remains unread |
| Becker foundation | Reading pointer; original unverified | Existing wiki entry retained; no newly verified Becker result asserted |
| Generic MRS and consistent hour/share units | Verified as own algebra / conceptual check | Both new pages and glossary distinguish expenditure/hour from consumption/share |
| Frisch definition | Correctly qualified | Marginal utility of wealth held fixed; not equated to other wage elasticities |
| Interpretation | Correctly qualified | Calibrated/static/conditional welfare calculation; not causal policy simulation, clean recreation measure, or universal market price |

The 2025 study uses period cross sections rather than a cohort panel. The new leisure-only derivations hold other welfare dimensions fixed and do not purport to replicate its full lifetime/racial welfare analysis. No new funding or disclosure claim is inferred.

## Independent derivations and arithmetic

From the read utility function, the auditor independently derived:

```text
Hourly marginal value = C × θ × (1−ℓ)^(1/ε) / H
Δv = v(ℓ + extra_hours/H) − v(ℓ)
WTP = C × [1 − exp(−Δv)]
Equivalent consumption increase = C × [exp(Δv) − 1]
```

The last two comparisons use different reference allocations. The auditor independently solved the utility-indifference conditions rather than accepting the calculator formulas as evidence.

| Quantity | Independently checked result (2012 US dollars) |
| --- | ---: |
| Marginal value per additional annual hour | 14.193976 |
| Net hourly wage derived from rounded calibration moments | 14.214428 |
| One extra annual hour: linear / WTP / equivalent increase | 14.193976 /14.186683 /14.193169 |
| 365 extra annual hours: linear / WTP / equivalent increase | 5,180.801250 /4,310.887186 /5,005.993598 |

The slight difference from the wage condition reflects rounded calibration moments and `θ`; no exact equality is demanded. All twelve numeric CSV fields and derived marginal/net-wage values match within tolerance `1e-10`. Indifference identities hold within `1e-12`. The separate hypothetical $25 gross wage/20% marginal tax example correctly yields $20/hour under its stated assumptions.

The findings page correctly distinguishes one extra hour in a year from one extra hour per day for365days, local approximations from finite changes, and dollar-year units from current dollars.

## Reproduction and rendered presentation

The author ran the calculator in `/tmp/leisure-value/reproduction` with fresh retrieval and checksum verification of the pinned PDF. The auditor independently compared all seven files and recorded hashes:

- Three generated artifacts: two result files and the regenerated findings page/table.
- Four copied inputs/script: source, calibration and access records, and the calculator.
- All seven files byte-identical. [Detailed comparison](2026-11-08-leisure-value-reproduction.json).

Script execution was parent-run. Independent checks comprised source/profile/locator inspection, utility-indifference calculations, metadata/record checks, and reproduction/hash comparisons. The auditor also inspected the actual built HTML, confirming all calibration entries and both rounded table rows, including `$5,180.80 / $4,310.89 / $5,005.99`. No new figures were introduced; SVG/PNG checks do not apply.

The auditor read the final audit-status addition and found it consistent with the completed checks and limits.

## Site validation performed by the author

- `ASTRO_TELEMETRY_DISABLED=1 npm run build`:31HTMLpages built successfully.
- HTML parser: all2,417internal href/src/anchor references passed; image text alternatives present.
- All five new public data assets match built copies; Pagefind search assets present.
- Preview HTTP/content checks: `/`, `/papers/`, `/data/`, `/findings/`, `/guides/contributing/`, and both new routes returned200with expected content.
- Staged whitespace checks passed.

These site/build/HTTP checks were parent-run, not an independent browser/mobile or live-Vercel audit.

## Unverified and unrun checks

The auditor independently requested the 2025 DOI, the 2016 DOI, the Becker DOI and the Stanford2016PDF route; all four returned proxy HTTP403. Original publisher authentication, correction/retraction records, older full texts, underlying empirical data, full-model replication, external/live deployment, and mobile presentation remain unverified or unrun. See [access records](../../public/data/leisure-value/access-status.json).

An unpublished fallback manuscript was considered during discovery but excluded from the wiki's source-supported claims. No findings from it support these pages. The search is focused rather than systematic.

## Recheck requirements

No supported implementation defect remains. Recheck changes to utility forms, derivatives, time units, calibration, source versions, counterfactuals or attributed findings. Preserve the distinction between a read primary publication copy, our own model-derived values, and unverified publisher/older-source checks.
