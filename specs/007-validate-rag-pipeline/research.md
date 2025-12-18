# Research: Validate RAG Pipeline

**Feature**: Validate RAG Pipeline (007)
**Date**: 2025-12-17

## Decisions

### 1. Script Location and Naming
- **Decision**: Create the script at `backend/test_retrieval.py`.
- **Rationale**: The user explicitly requested `test_retrieval.py` in the planning prompt, overriding the generic "validation script" name from the spec. It resides in `backend/` to leverage the existing python environment and `.venv`.
- **Alternatives**: `backend/validate_rag.py` (used in my internal thought process previously, but user input takes precedence).

### 2. Dependency Management
- **Decision**: Use `uv` to run the script.
- **Rationale**: Project uses `uv` for python management. No new dependencies are needed as `cohere` and `qdrant-client` are already in `backend/pyproject.toml`.

### 3. Qdrant Filtering Logic
- **Decision**: Use client-side filtering or Qdrant's `score_threshold` parameter if available in `search` method.
- **Rationale**: Qdrant `search` (and `query_points`) supports a `score_threshold` parameter directly. This is more efficient than fetching and filtering in Python.
- **Reference**: Qdrant Client documentation.

### 4. Output Formatting
- **Decision**: Use standard stdout printing with separators for readability (e.g., "---").
- **Rationale**: Meets the NFR for human-readability without needing complex TUI libraries.

## Open Questions Resolved

- **Q**: What specific metadata fields are available?
- **A**: `source_url` and `title` are confirmed present in the `rag_emabadding` collection payload from previous `main.py` analysis.

- **Q**: How to handle API keys?
- **A**: Use `os.environ.get()` for `COHERE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`, consistent with `main.py`.
