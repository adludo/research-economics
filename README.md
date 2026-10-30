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

The wiki documents 15 core papers and one review from the supplied research discussion:

- **Leisure and time allocation:** theory, historical trends, home production, recessions, unemployment, and leisure technology.
- **Closed economies and trade:** historical autarky/opening, growth evidence, identification critiques, natural experiments, and welfare counterfactuals.

Each topic has paper links, data-source guidance, and key finding summaries. See `src/content/docs/guides/sources.md` for provenance and verification limits. Summaries follow the supplied discussion; external links and numerical claims have not been independently verified against full texts in this environment.
