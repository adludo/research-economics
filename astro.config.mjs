import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [starlight({
    title: 'Economics Research',
    description: 'A research wiki for economic literature, data sources, and evidence.',
    customCss: ['./src/styles/custom.css'],
    social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/adludo/research-economics' }],
    sidebar: [
      { label: 'Overview', link: '/' },
      { label: 'Glossary', link: '/glossary/' },
      { label: 'Papers', items: [
        { label: 'Paper register', link: '/papers/' },
        { label: 'Leisure and time allocation', link: '/papers/leisure/' },
        { label: 'Leisure, GDP, and productivity', link: '/papers/leisure-productivity/' },
        { label: 'Trade and income', link: '/papers/trade/' },
      ] },
      { label: 'Data sources', items: [
        { label: 'Data overview', link: '/data/' },
        { label: 'Hours worked around the world', link: '/data/working-hours/' },
        { label: 'Leisure data', link: '/data/leisure/' },
        { label: 'Leisure and productivity data', link: '/data/leisure-productivity/' },
        { label: 'Trade and GDP data', link: '/data/trade/' },
      ] },
      { label: 'Key findings', items: [
        { label: 'Evidence overview', link: '/findings/' },
        { label: 'Leisure findings', link: '/findings/leisure/' },
        { label: 'Leisure and productivity findings', link: '/findings/leisure-productivity/' },
        { label: 'Trade findings', link: '/findings/trade/' },
      ] },
      { label: 'Source and editorial notes', link: '/guides/sources/' },
      { label: 'Contributing research', link: '/guides/contributing/' },
    ],
  })],
});
