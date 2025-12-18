# Tasks: Vector Database Population

**Feature Branch**: `005-vector-db-population`
**Spec**: [specs/005-vector-db-population/spec.md](specs/005-vector-db-population/spec.md)

## Dependencies

1. **Setup Phase** -> **Foundational Phase**
2. **Foundational Phase** -> **US1: Content Extraction**
3. **US1: Content Extraction** -> **US2: Embed & Store**
4. **US2: Embed & Store** -> **US3: Verification**

## Implementation Strategy

- **MVP**: Single script `backend/main.py` that crawls, embeds, and uploads.
- **Incremental**:
  1. Setup environment.
  2. Implement extraction logic and verify text output.
  3. Implement embedding and storage.
  4. Add verification.

## Phase 1: Setup (Project Initialization)

**Goal**: Initialize the Python environment and install dependencies.

- [x] T001 Initialize `uv` project in `backend/` directory with `uv init`
- [x] T002 Add dependencies: `cohere`, `qdrant-client`, `requests`, `beautifulsoup4`, `langchain-text-splitters` using `uv add`
- [x] T003 Create `.env` file template (e.g., `.env.example`) in `backend/` for API keys

## Phase 2: Foundational (Blocking Prerequisites)

**Goal**: Create the script skeleton with required imports and function stubs.

- [x] T004 Create `backend/main.py` with required imports and empty function signatures: `get_all_urls`, `extract_text_from_url`, `chunk_text`, `embed`, `create_collection`, `save_chunk_to_qdrant`, `main`
- [x] T005 Implement `main` function entry point in `backend/main.py` to handle environment variable loading (using `os.environ`) and basic orchestration structure

## Phase 3: Content Extraction & Preparation (US1)

**Goal**: Extract clean text from the Docusaurus site and chunk it.
**Independent Test criteria**: Run script and inspect printed chunks/metadata.

- [x] T006 [US1] Implement `get_all_urls` in `backend/main.py` to fetch and parse `sitemap.xml`
- [x] T007 [US1] Implement `extract_text_from_url` in `backend/main.py` using BeautifulSoup to target `<main>` content
- [x] T008 [US1] Implement `chunk_text` in `backend/main.py` using `RecursiveCharacterTextSplitter` (size=1000, overlap=200)

## Phase 4: Embedding Generation & Storage (US2)

**Goal**: Generate vectors via Cohere and upsert to Qdrant.
**Independent Test criteria**: Vectors visible in Qdrant Cloud dashboard.

- [x] T009 [US2] Implement `create_collection` in `backend/main.py` to initialize Qdrant collection `rag_emabadding` with Cosine distance (1024 dims)
- [x] T010 [US2] Implement `embed` in `backend/main.py` to call Cohere `embed-english-v3.0` API
- [x] T011 [US2] Implement `save_chunk_to_qdrant` in `backend/main.py` to batch upsert points with payload (url, title, text)
- [x] T012 [US2] Wire up the `main` orchestration in `backend/main.py` to loop through URLs, extract, chunk, embed, and save

## Phase 5: Retrieval Verification (US3)

**Goal**: Verify data quality via search.

- [x] T013 [US3] Add a verification step in `backend/main.py` (or separate flag) to perform a test query (e.g., "ROS 2 architecture") and print results

## Phase 6: Polish & Cross-cutting

**Goal**: Robustness and cleanup.

- [x] T014 Add error handling and logging to `backend/main.py` (e.g., try-except blocks for API calls)
- [x] T015 Verify `pyproject.toml` and `uv.lock` are consistent
