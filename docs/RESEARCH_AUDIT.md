# Independent research audit

The `research_auditor` subagent checks whether this wiki's papers, findings, data, and graphs support what the main agent has written. It reviews evidence and reports defects; it does not repair its own review target.

## Invoke the auditor

In a Codex session that loads this trusted repository's `.codex/config.toml`, ask:

> Delegate an independent review to `research_auditor`. Audit the diff from `origin/main` to HEAD, including all affected citations, finding summaries, data transformations, and rendered graphs. Follow `docs/RESEARCH_AUDIT.md`. Return the evidence ledger, defects, and unverified checks.

For a baseline audit, replace the diff scope with “the entire wiki and all checked-in research data and graphs.” For a correction, provide the previous report and the new commit SHA; ask the auditor to recheck each affected finding.

The role is configured in `.codex/agents/research-auditor.toml`. It inherits the session's model and uses a read-only sandbox. The host must support custom agent roles and load repository configuration; adding files does not start an audit or prove the host loaded them. If named roles are unavailable, pass these role instructions and this guide to an independent subagent through the host's supported delegation tool. If independent delegation is unavailable, report that limitation; a self-review is not an independent audit.

## Evidence standard

Audit the exact commit SHA and diff range. Record a dirty working tree if relevant. Read `AGENTS.md`, inventory affected claims and figures, and trace dependencies beyond changed lines. For a full audit, list all papers, datasets, scripts, and charts before checking them. Do not sample silently or claim full coverage from a few spot checks.

Classify each check separately:

| Status | Meaning |
| --- | --- |
| Verified | The auditor inspected supporting primary evidence and it matches the specific claim or calculation. Include a locator and method. |
| Contradicted | Inspected evidence conflicts with the claim. Quote or identify the conflicting result. |
| Unverified | Evidence was unavailable, inaccessible, ambiguous, or insufficient. State the missing check and access failure. |
| Not applicable | The check does not apply. Give the reason; do not use this for unread sources. |

A real paper can have an unverified summary. A correct calculation can use data with unverified original provenance. Keep those checks separate. A source that cannot be accessed has not passed verification.

## Required checks

### Paper identity and version

- Resolve identifiers and inspect publisher, DOI, institutional, or official working-paper records. Match authors, title, outlet, year, and version.
- Read the actual referenced version. Record retractions or corrections when found; report whether those records were checked.
- Treat search results, abstracts, generated conversations, and secondary summaries as discovery aids, not full-text support for detailed results.
- Distinguish links that identify a paper from links that provide its text, data, or replication materials. Check that each opens the intended destination.

### Findings and interpretation

- Map each numerical and substantive finding to a primary-text page, table, figure, equation, or section. Record the identifier and version beside the locator.
- Compare sign, magnitude, units, denominator, population, sample restrictions, period, uncertainty, and robustness qualifications.
- Distinguish estimates from bounds, levels from growth rates, percentages from percentage points, and observed outcomes from model counterfactuals.
- Check causal wording against the research design and its assumptions. Preserve the paper's limitations and disagreements with other studies.
- Check any funding, sponsorship, and conflict-of-interest statements against acknowledgements or disclosures. Absence of a statement is not proof that funding was absent.

### Data and transformations

- Trace provider → release/vintage → archived copy → extracted CSV → script → displayed number. Inspect provenance, source definitions, retrieval dates, checksums, and reuse conditions.
- Treat checksums as evidence of file identity, not scientific validity or original-provider authentication. Compare archived data with original sources where accessible.
- Recalculate reported values independently from stored inputs. Check units, weights, aggregation, country labels, joins, denominators, missing values, exclusions, rounding, and endpoint choices.
- Check whether coverage and population definitions change over time or across sources. Identify interpolation, extrapolation, estimation, and splicing. Do not infer leisure directly from fewer market hours.

### Graphs and accompanying prose

- Inspect each rendered figure as well as its code. Match plotted series and highlighted values to source rows and the described transformation.
- Check axes, scale, ticks, units, dates, legends, endpoint labels, country selection, missing-year gaps, and captions. Look for clipping, misleading comparisons, and unsupported trend statements.
- Ensure straight connections between irregular observations are labelled as guides, not observed annual data. Do not hide missing years or merge incompatible series.
- Distinguish a descriptive chart of data from a replication of a paper's finding. Compare to a paper's figure only when the wiki makes that claim; still verify the data and descriptive statements otherwise.
- Check text alternatives and available data tables/downloads. A build or link check proves neither the scientific claim nor the plotted values.

## Report format

Return the following report in the response. The main agent saves it under `docs/audits/<date>-<scope>.md` when performing a research audit. Do not create a report that implies unperformed checks passed.

```markdown
# Research audit: <scope>

- Audited commit: <full SHA; dirty files if any>
- Base/diff: <range or full-wiki scope>
- Auditor: <role/session identifier when available>
- Date: <date and timezone>
- Coverage: <inventoried count, checked count, and unchecked items>
- Verdict: <verified within stated scope / corrections required / verification incomplete>

## Findings, highest severity first

| ID | Severity | Status | Repository location / claim | Evidence and locator | Required correction or next check |
| --- | --- | --- | --- | --- | --- |

## Evidence ledger

| Paper, claim, dataset, or graph | Check | Status | Source/version and locator | Method or limitation |
| --- | --- | --- | --- | --- |

## Reproduction and visual checks

<Commands or independent calculations, actual outcomes, and figures inspected.>

## Unverified and unrun checks

<Access failures, unread texts, missing originals, unavailable tools, and omitted scope.>

## Recheck requirements

<Which defects must be corrected and which checks must run again.>
```

Use **critical** for fabricated evidence or a materially reversed central conclusion; **major** for wrong estimates, versions, transformations, or misleading graphs; **minor** for defects that do not change the interpretation. An access failure is an unverified check, not evidence that a paper is fabricated.

## Main-agent responsibilities

Before pushing research changes, delegate the changed claims and their dependencies to the auditor. Give it the exact scope, not an instruction to approve. Save its report, correct supported defects, and request a recheck of affected items. Record unresolved or inaccessible evidence explicitly; do not call the research verified while required checks remain unverified.

A draft branch may be pushed for review with unresolved items if the report and handoff state them plainly. A report is a review record, not an automatic publication approval. For an agent-configuration-only change, review the role configuration and instructions; a complete literature audit is a separate scope.
