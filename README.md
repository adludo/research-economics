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

## Research status

The [source conversation](https://chatgpt.com/share/6ae3d9dc-5678-83ec-9fde-8474c85c588a) could not be accessed from the development environment. The site includes structured sections for papers, data sources, and findings, but substantive research content is pending access to the discussion. No citations or conclusions have been invented.
