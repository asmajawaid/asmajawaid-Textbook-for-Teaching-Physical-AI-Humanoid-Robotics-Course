# Implementation Plan: Docusaurus RAG Chatbot UI

**Branch**: `010-docusaurus-chatbot-ui` | **Date**: 2025-12-17 | **Spec**: [specs/010-docusaurus-chatbot-ui/spec.md](spec.md)
**Input**: Feature specification from `specs/010-docusaurus-chatbot-ui/spec.md`

## Summary

Integrate a RAG-powered chatbot into the existing Docusaurus website (`website/`) to allow users to query the book's content. This involves creating a React Chatbot component, injecting it globally via `src/theme/Root.js`, and connecting it to the existing FastAPI backend (`backend/`) using `axios`. Backend CORS settings will be updated to support the frontend.

## Technical Context

**Language/Version**: TypeScript (React/Docusaurus), Python 3.12 (FastAPI)
**Primary Dependencies**: 
- Frontend: `axios`, `react-markdown`, `remark-gfm`, `clsx`, `lucide-react` (for icons)
- Backend: `fastapi` (existing), `uvicorn` (existing)
**Storage**: N/A (Frontend is stateless; Backend uses existing Qdrant)
**Testing**: Manual End-to-End verification
**Target Platform**: Web (Static Site + SPA hydration)
**Project Type**: Web Integration
**Performance Goals**: UI should be responsive; Chat response latency depends on backend/LLM.
**Constraints**: No new root directories. All frontend code in `website/`. Backend code in `backend/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Source Quality**: N/A (Feature implementation, not content writing)
- [x] **Technical Accuracy**: Plan includes testing the integration (end-to-end).
- [x] **Citation Standard**: Chatbot UI designed to display citations (functional requirement).
- [x] **Readability & Voice**: N/A (Code).
- [x] **Plagiarism Check**: N/A (Code).
- [x] **Word Count**: N/A.
- [x] **Commit Evidence**: Will verify functionality and code quality before merge.

## Project Structure

### Documentation (this feature)

```text
specs/010-docusaurus-chatbot-ui/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── chat-api.yaml
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
backend/
├── main.py              # Update CORS

website/
├── .env                 # Add BACKEND_URL
├── src/
│   ├── components/
│   │   └── Chatbot/
│   │       ├── index.tsx
│   │       ├── styles.module.css
│   │       └── ChatBubble.tsx
│   └── theme/
│       └── Root.tsx     # Global wrapper for Chatbot
```

**Structure Decision**: Adhere strictly to the "No new root folders" constraint by placing all frontend logic within `website/src`. Use `theme/Root.tsx` for global persistence of the chatbot state across navigation.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | | |