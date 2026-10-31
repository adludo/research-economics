# Research audit: supplemental working-hours data and graphs

- Audited commit: `73c59947e3ad7f9946f8ac772ee1cbd2bea53860`.
- Scope: working-hours page, CSV extracts, metadata/provenance, two generation scripts, and three graphs in SVG and PNG formats; all 16 files in the inspected snapshot matched the Git commit.
- Branch: `docs/world-working-hours`. These files are not in audited main `06433e338a3baf2fad2625013075baf42c70ca18`.
- Auditor: independent subagent `/root/audit_hours_graphs`, following the research-auditor instructions.
- Date: 31 October 2026, UTC.
- Verdict: **verified against the pinned OWID archive within the inspected scope; original-provider and original-paper verification incomplete**.
- Material defects found in extraction, calculations, or graph coordinates: none.

## Findings and limits

| ID | Status | Evidence | Required next check |
| --- | --- | --- | --- |
| H-01 | Unverified original provenance and scientific support | Original PWT and Huberman–Minns article requests were blocked with proxy tunnel 403 | Retrieve original files/documentation and the paper; compare definitions and tables |
| H-02 | Unverified third-party reuse terms | Retrieved archive metadata does not establish a specific licence for the underlying data | Inspect original-provider and OWID reuse terms; do not assert unrestricted rights |
| H-03 | Verified scope boundary | Files exist at `73c5994`, not at audited main `06433e3` | Keep this verdict separate from the merged wiki |

No wrong numbers, reversed changes, clipped data, incompatible source splicing, or hidden connections across the missing South African year were found.

## Source and extraction ledger

Archive revision: `6155d4ca1ea14ef30e753010a25521eeb416e8a2`. Exact payload URLs are recorded in the audited `public/data/working-hours/provenance.json`.

| Payload | Independently retrieved SHA-256; matched the recorded hash |
| --- | --- |
| PWT CSV | `0ecd5c71e0f1dfdbeecd624f7c61875b5fa64094e639cccf6304b2fd181be505` |
| PWT metadata | `79bcd8893b84bbdc00cea3465c7d1710301de364b526a4d139e2d8469e4d1a57` |
| Historical CSV | `534c2e6df4c4d8ca165598052021b70fe4143ddba68fe0f4ae61b3f9a1482291` |
| Historical metadata | `99c047264eb01a2460b0c6c9f45a176c25a45cb7470dbcd4ebd25865edeb09cc` |

| Check | Status | Independent evidence/method |
| --- | --- | --- |
| Every PWT extract value | Verified | Selected nonempty annual-hours values from the upstream CSV, renamed fields and sorted country/year; every one of 3,492 records matched |
| PWT hours coverage | Verified against archive | 69 economies, 1950–2019, independently counted; narrower than the broader database |
| Every 2019 extract value | Verified | All 66 observations matched the independent filter; no imputed zeros |
| Every historical field | Verified | All 182 rows matched an independent column rename, preserving empty cells |
| Broader PWT coverage | Verified against archive metadata only | Metadata states 183 countries, 1950–2019; original release not inspected |
| Historical source transitions | Verified against archive metadata only | Early reconstructed sources; later Groningen/Conference Board annual hours; Spain 1938/1936 qualification; male/female averaging for 2000 weekly hours |
| Original paper identity and detailed tables | Unverified | Archive citation is not independent publisher/full-text confirmation |
| Funding/disclosure claims | Not applicable | Supplemental page and graphs make no funding claims; original acknowledgements were not checked |

Checksums establish archived file identity, not scientific validity or authentication against the original provider.

## Table and highlight ledger

All **91 table rows** were independently checked: 66 rows for 2019, 14 historical endpoint rows, and 11 common-period change rows. Display rounding and country labels agree with the source extracts.

| Check | Status | Result |
| --- | --- | --- |
| 2019 table | Verified | All 66 values, year labels and whole-hour rounding match |
| Historical endpoint table | Verified | All 14 changes equal `100 × (2000 hours / 1870 hours − 1)` |
| Recent endpoint table | Verified | All 11 changes equal `100 × (2019 hours / 1990 hours − 1)` |
| 2019 sample minimum | Verified | Denmark: stored approximately 1380.607643405578, displayed 1,381 hours |
| 2019 sample maximum | Verified | Cambodia: stored approximately 2474.9118933530062, displayed 2,475 hours |
| Historical direction | Verified | All 14 endpoints lower in 2000 than 1870; not necessarily monotonic between dates |
| South Africa | Verified | Starts in 2001, lacks 2015 and 1990; correctly excluded from common-period bars |
| Selection disclaimer | Verified | Twelve illustrative economies, not a representative sample or world average |

Independently calculated 1990–2019 changes:

| Country | Change |
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

The page correctly describes these as changes in hours, not GDP/productivity growth or causal welfare effects.

## Rendered graph and SVG geometry ledger

| Graph | Status | Independent checks |
| --- | --- | --- |
| `country-trends.svg` | Verified | All 12 series and 568 vertices matched CSV-to-SVG transforms within `2 × 10⁻⁶` coordinate units; path breaks preserve missing 2015; every final-hour label matched |
| Recent axis limits | Verified | Shared x bounds 1968–2021 and y bounds 0–3,000 hours; no selected observation clipped |
| `historical-trends.svg` | Verified | All 14 series and 182 vertices matched; actual observation years determine positions; every endpoint label matched |
| Historical axis limits | Verified | Shared bounds 1865–2005 and 0–4,000; no clipping; caption identifies dots as observations and lines as guides |
| `change-1990-2019.svg` | Verified | All 11 bar widths/signs matched independent percentage transforms within `2 × 10⁻⁶` units on the −33% to +15% scale; labels, sorting, and South Africa exclusion correct |
| All three PNGs | Verified at inspected resolution | Auditor viewed the actual images; titles, axes, captions, signs and labels visible; no material visual defect found |
| Embedding/accessibility | Verified by source inspection | Descriptive image alternatives, full-size SVG/PNG links, CSV downloads and endpoint table present |
| Live-browser/mobile rendering | Unverified | Complete page interaction was not inspected |

The historical and PWT series are not spliced. The existing warning about smooth/flat source estimates is appropriate; the figures cannot prove unchanged individual schedules.

## Reproduction

Independent read-only work by the auditor included snapshot identity checks, four upstream downloads and hashes, independent reconstruction of the CSVs, recalculation of all displayed tables, parsing actual SVG geometry, and viewing all PNG figures.

The parent then ran both original scripts in a **separate writable copy**, leaving the audited snapshot untouched:

```sh
python3 /tmp/wiki-audit-reproduction-73c5994/scripts/collate-working-hours.py
python3 /tmp/wiki-audit-reproduction-73c5994/scripts/plot-working-hours.py
```

The auditor independently compared the reproduced files: source Markdown, three CSVs, two metadata files, three SVGs, and three PNGs were byte-identical. Provenance was identical except the retrieval date advanced from 2026-10-30 to 2026-10-31. The [comparison record](2026-10-31-reproduction-results.json) is retained. Script execution was parent-run, distinct from the auditor's independent extraction, arithmetic, and coordinate checks.

## Unverified and unrun scope

Both original-source requests failed with proxy tunnel HTTP 403:

- `https://www.rug.nl/ggdc/productivity/pwt/`
- `https://www.sciencedirect.com/science/article/pii/S0014498307000058`

Not verified: agreement with original PWT release files or original paper tables; full-text methods; corrections/retractions; reuse terms; current OECD/ILO/Eurostat metadata; later PWT revisions; live-browser page rendering; literature outside this supplemental scope.

## Recheck requirements

Obtain original-source access, compare the original release/paper and record primary locators, check definitions/revisions/reuse terms, and preserve the main-versus-supplemental distinction. Re-run extraction, arithmetic and SVG checks after data, selection, date-window, or plotting changes. This verdict does not certify the original research papers.
