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
      { label: 'Papers', link: '/papers/' },
      { label: 'Data sources', link: '/data/' },
      { label: 'Key findings', link: '/findings/' },
      { label: 'Contributing research', link: '/guides/contributing/' },
    ],
  })],
});
