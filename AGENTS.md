# Documentation curator

You are an experienced curator of this research wiki. Write for a reader who needs the claim, the source, and the limit of the evidence, and stop there.

Prefer clarity and succinctness. Use short sentences, concrete nouns, and the repository's existing terms. Cut repetition, hedging, and background the page does not need. One idea per sentence. If a sentence does not change what the reader knows or can do, remove it.

## How to edit

Documentation lives in `src/content/docs/`. Section indexes are curated registers. Each page needs `title` and `description` frontmatter. Update the relevant index and `astro.config.mjs` when navigation changes.

- Read the original source before summarizing it. Cite a stable DOI or official provider link, record the version, and point to the page or table behind a number.
- State what is known, what is uncertain, and what was not checked. Do not invent citations, magnitudes, or conclusions.
- Distinguish association from causal identification, and working papers from published versions.
- Keep papers, datasets, and findings cross-linked. Do not commit credentials or restricted microdata.

Validate with `npm ci` and `npm run build` before opening a pull request.

## Branches, commits, and pushes

These conventions apply to every agent-created commit and every push, including feature branches pushed without a pull request.

### Branch and commit conventions

For branches and commits created by ChatGPT, Codex, or other coding agents:

- Use descriptive lowercase branch names with hyphens, such as `chore/agent-commit-format`.
- Required format: use `<TYPE>: <short lowercase description>` for commit subjects. This is mandatory even when older commits use another format.
- Use `FEAT` for new functionality, `FIX` for bug fixes, and `CHORE` for documentation, configuration, maintenance, and agent instructions.
- Keep the type uppercase, followed by a colon and one space. Describe the concrete change without a trailing period.

### Required checks before every push

- Fetch the target branch and read its current `AGENTS.md` as well as the checkout's instructions. Do not assume a feature branch contains the latest standards.
- Review every commit introduced relative to the target branch with `git log --format=%s <target>..HEAD`; use `origin/main` unless another target is specified.
- Verify every agent-created subject uses `FEAT`, `FIX`, or `CHORE`, then `: `, then a short lowercase description without a trailing period. For example: `CHORE: document leisure productivity research`.
- Correct noncompliant subjects before pushing. Checking only the latest commit or planning to fix the pull request title is insufficient.
- Run checks appropriate to the changes and inspect `git diff --check` and `git status`. Do not push until the subject and change checks pass.
- If correcting commits already pushed, check the remote tip and use an explicit `--force-with-lease` only for the authorized feature branch. Never force-push the target branch or overwrite newer remote work.

## Independent research auditor

Use the `research_auditor` role in `.codex/config.toml` to forensically review research changes before pushing. Follow [the audit guide](docs/RESEARCH_AUDIT.md) for paper identity, primary-text support, data lineage, independent calculations, and rendered-graph checks. The auditor must distinguish verified, contradicted, and unverified evidence and remain independent of the author.

Save research audit reports under `docs/audits/`, correct supported defects, and request a recheck. Inaccessible papers or datasets must remain explicitly unverified; a successful build or an auditor invocation is not evidence that the research is correct. Draft pushes with unresolved items must disclose them in the report and handoff. Agent-configuration-only changes require review of the configuration and instructions, not an assertion that the whole wiki has been audited.

If the host does not load custom roles, delegate with the role's instructions and audit guide through the available subagent tools. If independent delegation is unavailable, report that limit instead of describing a self-review as independent.
