import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Teaching Physical AI and Humanoid Robotics',
  tagline: 'A comprehensive guide to ROS 2, Digital Twins, and VLA',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://asmajawaid.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/humuniod-spec-book/',

  // GitHub Pages deployment config
  organizationName: 'asmajawaid', // Usually your GitHub org/user name
  projectName: 'humuniod-spec-book', // Usually your repo name
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  markdown: {
    mermaid: true, // Enable Mermaid support
  },
  themes: ['@docusaurus/theme-mermaid'], // Add Mermaid theme

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/asmajawaid/humuniod-spec-book/tree/main/website/',
          // routeBasePath: '/', // Serve docs at root (optional)
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/asmajawaid/humuniod-spec-book/tree/main/website/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Humanoid Robotics Book',
      logo: {
        alt: 'Humanoid Robot Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Book Content',
        },
        {to: '/blog', label: 'Updates', position: 'left'},
        {
          href: 'https://github.com/asmajawaid/humuniod-spec-book',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Modules',
          items: [
            { label: 'ROS 2', to: '/docs/module-1-ros2/ros2-architecture' },
            { label: 'Digital Twin', to: '/docs/module-2-digital-twin/gazebo-physics-simulation' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
            { label: 'Twitter', href: 'https://twitter.com/docusaurus' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Humanoid Robotics Project. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'python', 'cpp', 'cmake'], // Syntax highlighting
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
