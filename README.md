# Economics Research Wiki

A Markdown/MDX documentation site built with [Astro](https://astro.build/) and [Starlight](https://starlight.astro.build/), with sidebar navigation, full-text search, responsive layout, and light/dark themes.

## Local development

Requires Node.js 24.x and npm.

```sh
npm ci
npm run dev
```

`npm run build` generates the static site in `dist/`. `npm run preview` serves that production build locally.

## Publish on Vercel

1. Push this repository to GitHub and import it as a Vercel project.
2. Set the root directory to this repository's root and select Node.js 24.x.
3. Deploy. `vercel.json` selects Astro, `npm ci`, `npm run build`, and `dist/`.

No secrets or backend services are needed. Vercel creates preview deployments for subsequent pull requests when its Git integration is enabled.

## Edit the wiki

Documentation lives in `src/content/docs/`. Edit the section indexes or add individual Markdown/MDX pages and link them from the indexes. Update `astro.config.mjs` to change the sidebar. Research contribution guidance is included in the site.

## Research coverage

The wiki includes a glossary of key economic and research terms at `/glossary/`.

The wiki documents 22 core papers and one review, combining the supplied research discussion with a further reading guide:

- **Leisure and time allocation:** theory, historical trends, home production, recessions, unemployment, and leisure technology.
- **Leisure, GDP, and productivity:** seven additional papers on hours and development, taxation, institutions, welfare beyond GDP, fatigue, and sleep.
- **Closed economies and trade:** historical autarky/opening, growth evidence, identification critiques, natural experiments, and welfare counterfactuals.

Each topic has paper links, data-source guidance, and key finding summaries. See `src/content/docs/guides/sources.md` for provenance and verification limits. The original summaries follow the supplied discussion; the leisure–productivity extension is an additional literature guide. External links and numerical claims have not been independently verified against full texts in this environment.

## Collated working-hours data

`/data/working-hours/` contains a 2019 comparison of 66 economies from PWT 10.0 and a separate Huberman–Minns historical comparison. Downloads and source metadata live in `public/data/working-hours/`. Run `python3 scripts/collate-working-hours.py` to regenerate them from checksum-verified OWID archive files. These historical releases are not current-year estimates.

The working-hours page also includes three graphs: selected-country trends, changes over 1990–2019, and historical trends. Run `python3 -m pip install -r scripts/requirements-charts.txt`, then `python3 scripts/plot-working-hours.py` to regenerate their SVG/PNG files and the endpoint table from the checked-in CSVs. Chart dependencies are not needed for Vercel builds.

## Independent research auditor

The repository defines a read-only Codex subagent, `research_auditor`, in `.codex/config.toml`. Its job is to check paper identities, primary-text support for findings, data provenance, calculations, and rendered graphs independently of the author. See [the audit guide](docs/RESEARCH_AUDIT.md) for invocation, evidence standards, host support, and the report format. Configuration alone does not run an audit or certify existing research.

## Current audit status

The merged wiki includes an audit-status page at `/guides/audit-status/`. The [main-branch audit report](docs/audits/2026-10-31-main-audit.md) records verified archive extraction, calculations and graph geometry separately from outstanding primary-paper, original-data and reuse checks. The full wiki is not yet primary-source verified.
