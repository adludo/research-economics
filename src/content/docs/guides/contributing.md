---
title: Contributing research
description: How to add sources and maintain the research wiki.
---

## Add documentation

Edit Markdown or MDX files in `src/content/docs/`. Every page needs YAML frontmatter with a `title` and `description`. Place individual papers under `papers/`, datasets under `data/`, and findings under `findings/`.

Link new entries from their section's `index.md`; these indexes serve as curated registers. Navigation is configured in `astro.config.mjs`. Starlight generates the table of contents and search index at build time.

## Check sources

Read the original source before writing a summary. Use stable DOI or official provider links, record the version, and include page or table references for numerical claims. Identify uncertainty, disagreements, and access restrictions. A conversation or abstract alone does not verify a result.

## Validate changes

Run `npm ci`, then `npm run build`. Use `npm run dev` for local editing or `npm run preview` to inspect the production build. Check new links, citations, and search results before publishing.

## Deploy

Import the GitHub repository into Vercel. Use the Astro framework preset and Node.js 24.x. The checked-in configuration runs `npm ci`, builds with `npm run build`, and serves `dist/`. No environment variables, database, or running backend service are required.
