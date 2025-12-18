# Research: Docusaurus RAG Chatbot UI

**Feature**: `010-docusaurus-chatbot-ui`
**Date**: 2025-12-17

## 1. Global Component Integration in Docusaurus

**Problem**: The chatbot needs to persist across page navigations and appear on every page without modifying every Markdown file or swizzling the entire Layout.

**Options**:
1.  **Swizzle `Layout`**: Wrap the default Layout. Powerful but brittle if Docusaurus updates the Layout props or structure.
2.  **`Root` Theme Component**: Create `src/theme/Root.js` (or `.tsx`). This component renders at the very top of the React tree, wrapping the entire Docusaurus app.
3.  **`BrowserOnly` in Layout**: Use a custom Layout wrapper.

**Decision**: Use **`src/theme/Root.tsx`**.
**Rationale**: It is the officially recommended "escape hatch" for rendering logic that shouldn't be unmounted on navigation. Ideally suited for global persistent UI elements like a floating chatbot or an announcement bar. It keeps the core Docusaurus `Layout` untouched.

## 2. Markdown Rendering

**Problem**: The backend returns answers in Markdown. The UI needs to render this safely.

**Options**:
1.  **`react-markdown`**: Standard, widely used, secure (does not execute HTML by default).
2.  **`marked` + `dangerouslySetInnerHTML`**: Faster but requires manual sanitization (DOMPurify).
3.  **Docusaurus Internal MDX**: Hard to reuse outside of the MDX content pipeline.

**Decision**: Use **`react-markdown`** with **`remark-gfm`**.
**Rationale**: `react-markdown` is a React component (not a string-to-html converter), making it safer and more idiomatic for React apps. `remark-gfm` adds support for tables and strikethrough, common in LLM outputs.

## 3. CORS Configuration

**Problem**: The Docusaurus frontend (localhost:3000 or production domain) needs to call the FastAPI backend (localhost:8000 or production API). Browsers block this by default.

**Decision**: Configure **FastAPI `CORSMiddleware`**.
**Details**:
-   **Allowed Origins**:
    -   `http://localhost:3000` (Local dev)
    -   `http://127.0.0.1:3000` (Local dev alternate)
    -   `https://*.github.io` (Production - specific user domain will be added)
-   **Allowed Methods**: `["POST", "OPTIONS"]` (Chat is POST).
-   **Allowed Headers**: `["*"]`.

## 4. State Management

**Problem**: Chat history should ideally persist if the user navigates to a new page.

**Decision**: React **Context** (implied by `Root` component hierarchy) or simple **Local State** in the `Chatbot` component lifted to `Root`.
**Rationale**: Since `Root` wraps the app, state held in `Root` (or a child rendered by `Root` that sits *outside* the Docusaurus router outlet) persists across navigation. We will render `<Chatbot />` inside `Root.tsx` alongside `{children}`.
