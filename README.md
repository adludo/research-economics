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

The wiki documents 28 core papers and two reviews, combining the supplied research discussion with a further reading guide:

- **Fertility, growth, and time allocation:** six papers and a review, with author-hosted source copies, page locators, data guidance, and independent research-auditor review.
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

## Fertility research sources

The fertility collection uses seven inspected author-hosted publication copies, with pinned source URLs and hashes in `public/data/fertility/sources.json`. The pages distinguish source-supported summaries from empirical replication and from independent publisher/DOI verification. It adds data-access guidance, not a new fertility dataset or causal graph.

The [fertility source-reading audit](docs/audits/2026-11-01-fertility-review.md) records which claims were checked and which publisher/data/replication checks remain outstanding.

## Fertility, GDP, and hours graphs

`/data/fertility-charts/` links period fertility with real GDP per person and market working hours across matching country-years, 1970–2014. Three source-referenced SVG/PNG charts and downloadable extracts are included. Forecast fertility rows from 2015 onward are excluded. Run `python3 scripts/collate-fertility-economy.py` and `python3 scripts/plot-fertility-economy.py` to regenerate them. The figures are descriptive comparisons, not causal estimates or paper replications.

The [fertility/GDP/hours graph audit](docs/audits/2026-11-01-fertility-charts.md) records the independent data and geometry checks, the corrected PWT archive-version attribution, and remaining source limits.

## Leisure and trade graph collections

The leisure, leisure/productivity and trade data guides include five source-referenced graphs with downloadable extracts. Sources and caveats distinguish US residual leisure, Norwegian daily leisure, output/hour, and merchandise exports/GDP. Rebuild with `python3 scripts/collate-topic-graphs.py` and `python3 scripts/plot-topic-graphs.py`. No Python is needed for Vercel deployment.

The [leisure and trade graph audit](docs/audits/2026-11-01-topic-graphs.md) records source checks, corrected presentation issues, and remaining original-provider limits.
## Statistics guide

`/guides/causality/` explains correlation versus causation, counterfactuals, randomised experiments, adjustment, difference-in-differences, discontinuity designs, instruments, and statistical uncertainty. It includes a labelled hypothetical example and pinned teaching references.

The [causality-guide audit](docs/audits/2026-11-01-causality-guide.md) records independent methodological review, corrections, and source-reading limits.

## Recent fertility, GDP, and weekly hours

The [recent-data guide](src/content/docs/data/recent-fertility-hours.md) adds four source-referenced figures with World Bank/ILOSTAT estimates through 2024. Regenerate them with `python3 scripts/collate-recent-economy.py` and `python3 scripts/plot-recent-economy.py` after installing `scripts/requirements-charts.txt`. The older annual-hours and fertility archives remain separate. See [the audit](docs/audits/2026-11-01-recent-economy.md) for verified and outstanding checks.

## Productivity measures and slowdown

The [productivity section](src/content/docs/productivity/index.md) explains headline output/hour, alternative calculations and input accounting, with a [reading register](src/content/docs/papers/productivity.md). The historical slowdown example includes eight country comparisons and 200 downloadable country-years. Regenerate it with `python3 scripts/collate-productivity.py`. [Audit scope and source-reading limits](docs/audits/2026-11-03-productivity.md).
## Leisure-survey figures

The [leisure-source guide](src/content/docs/data/leisure.md) includes section-specific numerical examples, MTUS coverage, and clearly labelled AHTUS/OECD measurement diagrams. Rebuild with `python3 scripts/collate-leisure-surveys.py` and `python3 scripts/plot-leisure-surveys.py`, using `scripts/requirements-charts.txt`. The [audit record](docs/audits/2026-11-02-leisure-surveys.md) separates archive checks from original-provider and diagram-definition limits.

## Valuing leisure time

The [equation guide](src/content/docs/findings/leisure-value.md) and [literature register](src/content/docs/papers/leisure-value.md) cover marginal shadow values, the conditional net-wage benchmark and finite consumption-equivalent examples from an inspected 2025 paper. Run `python3 scripts/calculate-leisure-value.py --verify-source` to regenerate the worked examples and table. See [the audit](docs/audits/2026-11-08-leisure-value.md) for source locators and verification limits.
