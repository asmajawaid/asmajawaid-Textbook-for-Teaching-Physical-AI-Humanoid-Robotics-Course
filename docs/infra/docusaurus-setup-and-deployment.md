# Docusaurus Setup & Deployment Specification

This document serves as the authoritative specification for setting up, configuring, and deploying the "Teaching Physical AI and Humanoid Robotics" book project using Docusaurus v3.

## 1. Docusaurus Installation (Step-by-Step)

### Prerequisites
*   **Node.js**: Version 18.0 or higher (LTS recommended).
*   **OS**: Ubuntu 22.04 (Target), or Windows/macOS for development.

### Installation
To initialize a new Docusaurus site with the classic theme (already performed for this repository):

```bash
npx create-docusaurus@latest website classic --typescript
```

### Folder Structure
The following structure is enforced for this project:

```text
website/
├── blog/                   # Blog posts (markdown)
├── docs/                   # Documentation source files (Markdown/MDX)
│   ├── module-1-ros2/      # Content for Module 1
│   ├── module-2-digital-twin/
│   └── intro.md
├── src/                    # Custom React components and pages
│   ├── components/
│   ├── css/
│   └── pages/
├── static/                 # Static assets (images, fonts, robots.txt)
├── docusaurus.config.ts    # Main site configuration
├── sidebars.ts             # Sidebar navigation structure
├── package.json            # Dependencies and scripts
└── tsconfig.json           # TypeScript configuration
```

### Verification
Run the development server to verify installation:

```bash
cd website
npm start
```
*   Access the site at `http://localhost:3000`.

## 2. `docusaurus.config.ts` (FULL CONFIG)

The configuration file controls the site's metadata, plugins, and deployment settings.

```typescript
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Teaching Physical AI and Humanoid Robotics',
  tagline: 'A comprehensive guide to ROS 2, Digital Twins, and VLA',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://<your-github-username>.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/humuniod-spec-book/',

  // GitHub Pages deployment config
  organizationName: '<your-github-username>', // Usually your GitHub org/user name
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
            'https://github.com/<your-github-username>/humuniod-spec-book/tree/main/website/',
          routeBasePath: '/', // Serve docs at root (optional)
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/<your-github-username>/humuniod-spec-book/tree/main/website/',
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
          href: 'https://github.com/<your-github-username>/humuniod-spec-book',
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
            { label: 'ROS 2', to: '/module-1-ros2/intro' },
            { label: 'Digital Twin', to: '/module-2-digital-twin/intro' },
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
```

## 3. Sidebar & Routing Configuration

The `sidebars.ts` file structures the book into logical modules.

```typescript
import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro', // Introduction / Preface
    {
      type: 'category',
      label: 'Module 1: ROS 2 Foundation',
      collapsible: true,
      collapsed: false,
      items: [
        'module-1-ros2/ros2-architecture',
        'module-1-ros2/nodes-topics-services-actions',
        'module-1-ros2/packages-and-build-system',
        'module-1-ros2/launch-files',
        'module-1-ros2/urdf-robot-description',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twins',
      collapsible: true,
      collapsed: true,
      items: [
        'module-2-digital-twin/gazebo-physics-simulation',
        'module-2-digital-twin/sensor-simulation-lidar-realsense',
        'module-2-digital-twin/unity-visualization',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: NVIDIA Isaac Sim',
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: 'autogenerated', // Use autogen for this folder
          dirName: 'module-3-nvidia-isaac', 
        },
      ],
    },
    // Add additional modules here
  ],
};

export default sidebars;
```

## 4. GitHub Pages Deployment (Manual)

### Required `package.json` Scripts
Ensure these scripts exist in `website/package.json`:

```json
"scripts": {
  "docusaurus": "docusaurus",
  "start": "docusaurus start",
  "build": "docusaurus build",
  "swizzle": "docusaurus swizzle",
  "deploy": "docusaurus deploy",
  "clear": "docusaurus clear",
  "serve": "docusaurus serve",
  "write-translations": "docusaurus write-translations",
  "write-heading-ids": "docusaurus write-heading-ids",
  "typecheck": "tsc"
}
```

### Manual Deployment Command
To deploy manually from your local machine:

```bash
# Set user and deploy
cmd /C "set GIT_USER=<your-github-username> && npm run deploy"
# Or on Bash (Git Bash/WSL):
GIT_USER=<your-github-username> npm run deploy
```

## 5. CI/CD with GitHub Actions (REQUIRED)

Create the workflow file: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main
    # Target only the website directory if strictly separated, 
    # but usually we want to deploy on any push that might affect docs.
    paths:
      - 'website/**'
      - 'docs/**' 

permissions:
  contents: write

jobs:
  deploy:
    name: Deploy to GitHub Pages
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: website # Important if docusaurus is in a subdir
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: npm
          cache-dependency-path: website/package-lock.json

      - name: Install dependencies
        run: npm ci

      - name: Build website
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./website/build
          user_name: github-actions[bot]
          user_email: github-actions[bot]@users.noreply.github.com
```

**Note:** Ensure "Read and write permissions" are enabled for workflows in your GitHub Repository Settings > Actions > General.

## 6. Definition of Done (Deployment)

The deployment pipeline is considered "Done" when:

1.  **Build Success**: `npm run build` completes locally and in CI without errors.
2.  **Live URL**: The site is accessible at `https://<user>.github.io/humuniod-spec-book/`.
3.  **Navigation**: The sidebar correctly reflects the module structure defined in `sidebars.ts`.
4.  **Search**: (Optional) Algolia or local search bar appears (even if index is empty initially).
5.  **Responsiveness**: Site layout adapts correctly to mobile devices.
6.  **Assets**: Images and diagrams (Mermaid) render correctly.

## 7. Common Pitfalls & Debugging

*   **404 on GitHub Pages**:
    *   **Cause**: Incorrect `baseUrl` in `docusaurus.config.ts`.
    *   **Fix**: Ensure `baseUrl` matches your repository name with slashes (e.g., `/humuniod-spec-book/`).

*   **Sidebar Path Errors**:
    *   **Cause**: ID in `sidebars.ts` does not match the filename (minus extension) or `id` frontmatter.
    *   **Fix**: Check filenames in `docs/` and ensure they match the sidebar item strings exactly.

*   **Broken Links**:
    *   **Cause**: Moving files without updating Markdown links.
    *   **Fix**: Run `npm run build` locally; Docusaurus will throw errors for broken links (configured via `onBrokenLinks: 'throw'`).

*   **Deploy Fails on CI**:
    *   **Cause**: Missing permissions or incorrect working directory.
    *   **Fix**: Verify `permissions: contents: write` in YAML and `working-directory: website` settings.
