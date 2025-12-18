# Research: Vector Database Population

**Feature**: Vector Database Population
**Status**: Resolved

## 1. Needs Clarification Resolution

| Unknown | Resolution | Source |
|---------|------------|--------|
| Docusaurus Structure | Site uses standard Docusaurus 2+ structure with `<main>` tags and `sitemap.xml`. | Tested via `Invoke-WebRequest`. |
| `uv` Availability | `uv` 0.5.5 is installed. | Verified via CLI. |
| Collection Name | User requested `rag_emabadding`. Will use exact spelling but document as `rag_emabadding`. | User Prompt. |

## 2. Technical Decisions

### Extraction Strategy
- **Decision**: Use `sitemap.xml` for URL discovery.
- **Rationale**: The site exposes a valid `sitemap.xml` at root. This is more reliable than recursive crawling for finding all pages.
- **Implementation**:
  - Fetch `https://.../sitemap.xml`.
  - Parse XML to get `<loc>` tags.
  - Filter for relevant paths if necessary (though sitemap usually contains all).

### Content Parsing
- **Decision**: `BeautifulSoup` to target `<main>` and `article` tags.
- **Rationale**: Docusaurus wraps content in `<main>`.
- **Detail**:
  - `soup.find('main')` to isolate content.
  - Remove navigation elements if present inside main (rare in Docusaurus, but headers/footers might need stripping).
  - Extract text with `get_text(separator=' ', strip=True)`.

### Chunking
- **Decision**: Recursive Character Text Splitter.
- **Params**: Chunk size 1000, Overlap 200.
- **Rationale**: Standard for RAG. Preserves context while fitting within context windows and vector coherence.

### Embedding Model
- **Decision**: Cohere `embed-english-v3.0`.
- **Rationale**: Specified by user. High performance for English retrieval.
- **Dimensions**: 1024 (standard for v3.0).

### Vector Database
- **Decision**: Qdrant Cloud.
- **Collection Name**: `rag_emabadding`.
- **Distance Metric**: Cosine.
- **Payload**: `{"source_url": "...", "text": "...", "title": "..."}`.

### Implementation Stack
- **Language**: Python 3.12+
- **Manager**: `uv`
- **Libraries**: `requests`, `beautifulsoup4`, `cohere`, `qdrant-client`, `langchain-text-splitters` (or manual implementation if keeping deps minimal, but langchain splitters are robust).

## 3. Alternatives Considered

- **Recursive Crawling**: Rejected because `sitemap.xml` is available and simpler.
- **Local Qdrant**: Rejected because User specified "Qdrant Cloud".
