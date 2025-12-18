# Quickstart: Validate RAG Pipeline

**Feature**: 007-validate-rag-pipeline

## Purpose

This document provides quick instructions to set up and run the RAG pipeline validation script. This script is designed to verify the accuracy and performance of the semantic search against the populated Qdrant vector database.

## Prerequisites

-   Python 3.12 or higher installed.
-   `uv` (Ultrafast Python package installer and resolver) installed.
-   Environment variables `COHERE_API_KEY`, `QDRANT_URL`, and `QDRANT_API_KEY` configured with appropriate credentials.
-   The Qdrant collection `rag_emabadding` must be populated with data (e.g., by running `backend/main.py` if not already done).

## Setup

1.  **Navigate to the project root**:
    ```bash
    cd D:\Q4_SirHamzahSyed\Hackathon\humuniod-spec-book
    ```

2.  **Ensure Python dependencies are installed**:
    The script relies on `cohere` and `qdrant-client`, which should be installed in the `backend` virtual environment. If you encounter issues, navigate to the `backend` directory and install them:
    ```bash
    cd backend
    uv pip install -r requirements.txt # Assuming requirements.txt exists or generate from pyproject.toml
    cd ..
    ```
    *Note: `uv run` should handle this automatically for `pyproject.toml` dependencies.*

## Running the Validation Script

To execute the RAG pipeline validation script, use `uv run` from the project's `backend` directory:

```bash
uv run backend/test_retrieval.py
```

## Interpreting Results

The script will output the results of several predefined test queries. For each query, it will display:

-   The query text.
-   The time taken for retrieval (latency).
-   The number of relevant matches found above a set confidence threshold.
-   For each match: its similarity score, the document title, the source URL, and a text snippet.

**Expected Output Indicators**:

-   **High scores (e.g., > 0.6)** for relevant queries indicate good semantic similarity.
-   **Low latency (e.g., < 1.0s)** for most queries.
-   **Zero results** for irrelevant queries, demonstrating effective filtering.
-   **Valid URLs and Titles** for all retrieved documents.

If results are not satisfactory, refer to the `specs/007-validate-rag-pipeline/spec.md` and `specs/007-validate-rag-pipeline/plan.md` for details on refinement options.