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

## Pull requests

When you open a pull request, follow these branch and commit conventions.

### Branch and commit conventions

For branches and commits created by ChatGPT, Codex, or other coding agents:

- Use descriptive lowercase branch names with hyphens, such as `chore/agent-commit-format`.
- Follow the existing repository history: use `<TYPE>: <short lowercase description>` for commit subjects.
- Use `FEAT` for new functionality, `FIX` for bug fixes, and `CHORE` for documentation, configuration, maintenance, and agent instructions.
- Keep the type uppercase, followed by a colon and one space. Describe the concrete change without a trailing period.
