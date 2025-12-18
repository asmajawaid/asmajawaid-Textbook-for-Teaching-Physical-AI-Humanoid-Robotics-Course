# Data Model: Validate RAG Pipeline

**Feature**: 007-validate-rag-pipeline

## Entities

### RetrievalResult
Represents a single document chunk returned from the vector database.

| Field | Type | Description |
|-------|------|-------------|
| `title` | `str` | Title of the document/page. |
| `source_url` | `str` | URL of the source page. |
| `score` | `float` | Cosine similarity score (0.0 to 1.0). |
| `text_snippet` | `str` | The actual text content of the chunk (truncated for display). |

### ValidationStats
Summary statistics for a validation run.

| Field | Type | Description |
|-------|------|-------------|
| `total_latency` | `float` | Time taken for embedding + search (seconds). |
| `results_found` | `int` | Number of results returned above threshold. |
| `status` | `str` | "PASS" or "FAIL" based on criteria. |
