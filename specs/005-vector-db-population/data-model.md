# Data Model: Vector Database Population

## Qdrant Collection Configuration

- **Collection Name**: `rag_emabadding`
- **Vector Size**: 1024 (Matches Cohere `embed-english-v3.0`)
- **Distance Metric**: `Cosine`

## Point Structure

Each point in the vector database represents a chunk of text.

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID` (or str) | Deterministic UUID generated from the chunk text to ensure idempotency. |
| `vector` | `List[float]` | 1024-dimensional embedding vector. |
| `payload` | `JSON Object` | Metadata associated with the chunk. |

### Payload Schema

```json
{
  "source_url": "string (URL)",
  "title": "string (Page Title)",
  "text": "string (The actual chunk content)",
  "chunk_index": "integer (Order of chunk in page)"
}
```

## Entity Relationships

- **Page** (1) -> (Many) **Chunks**
- **Chunk** (1) -> (1) **Vector**
