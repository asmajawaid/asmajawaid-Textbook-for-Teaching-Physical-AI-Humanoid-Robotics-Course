# Tasks: Validate RAG Pipeline

**Feature**: Validate RAG Pipeline
**Branch**: `007-validate-rag-pipeline`
**Date**: 2025-12-17
**Spec**: `specs/007-validate-rag-pipeline/spec.md`

## Summary

This document outlines the tasks required to implement and validate the RAG pipeline retrieval mechanism. The process is broken down into phases corresponding to user stories, ensuring incremental and independently testable delivery. The primary output will be a Python script for testing semantic search accuracy and latency.

## Implementation Strategy

The implementation will follow an MVP-first approach, starting with the core retrieval validation (US1), then enhancing it with irrelevance filtering (US2) and robust metadata verification (US3). Each phase will build upon the previous one, ensuring that a functional and testable component is available at each step.

## Project Structure

This feature focuses on a single Python script within the existing `backend/` directory.

```text
backend/
├── main.py
├── pyproject.toml
├── validate_rag.py     # Existing validation script
└── test_retrieval.py   # New script for this feature
```

## Phase 1: Setup

**Goal**: Prepare the environment and create the necessary file for the validation script.

- [x] T001 Create `backend/test_retrieval.py` as the dedicated validation script.
- [x] T002 Verify `cohere` and `qdrant-client` dependencies are available in `backend/pyproject.toml` and installed (uv handles this automatically).

## Phase 2: Foundational Components

**Goal**: Implement the basic infrastructure for connecting to Cohere and Qdrant.

- [x] T003 Implement environment variable loading (`COHERE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`) in `backend/test_retrieval.py`.
- [x] T004 Implement Cohere and Qdrant client initialization and error handling for connection in `backend/test_retrieval.py`.

## Phase 3: User Story 1 (P1) - RAG Retrieval Validation

**Goal**: Confirm the retrieval system returns semantically relevant content for specific book topics.

**Independent Test**: Run `backend/test_retrieval.py` with known queries (e.g., "ROS 2 architecture") and manually verify that the printed text snippets are relevant to the query and that latency is displayed.

- [x] T005 [US1] Implement Cohere query embedding (`embed-english-v3.0`, `search_query` type) within a `perform_search` function in `backend/test_retrieval.py`.
- [x] T006 [US1] Implement Qdrant querying for top `k` (default 3) nearest neighbors using `client.query_points` in `perform_search` function in `backend/test_retrieval.py`.
- [x] T007 [US1] Measure and report the latency of the embedding and Qdrant search process within `perform_search` function in `backend/test_retrieval.py`.
- [x] T008 [US1] Add a predefined set of relevant test queries to the script (e.g., "ROS 2 architecture nodes and topics", "How to simulate sensors in Gazebo?", "Reinforcement learning for humanoid walking", "NVIDIA Isaac Sim features").
- [x] T009 [US1] Implement basic output display for each query, showing `Query`, `Latency`, `Title`, `URL`, and a truncated `Snippet` of the retrieved text.

## Phase 4: User Story 2 (P2) - Irrelevance Filtering

**Goal**: Filter out search results with low similarity scores to prevent irrelevant context from reaching the LLM.

**Independent Test**: Run `backend/test_retrieval.py` with an off-topic query (e.g., "baking recipes") and confirm that zero results are returned or explicitly flagged as below the confidence threshold.

- [x] T010 [US2] Implement a configurable similarity threshold parameter within the `perform_search` function and apply it to filter Qdrant results in `backend/test_retrieval.py`.
- [x] T011 [US2] Add a predefined irrelevant test query (e.g., "How to bake a chocolate cake") to the script's test suite in `backend/test_retrieval.py`.

## Phase 5: User Story 3 (P2) - Citation Metadata Verification

**Goal**: Ensure every retrieved text chunk includes the correct source URL and page title for accurate citations.

**Independent Test**: Inspect the output of `backend/test_retrieval.py` to confirm that all displayed results have non-empty and valid `URL` and `Title` fields.

- [x] T012 [US3] Ensure `source_url` and `title` are explicitly extracted from the Qdrant payload within the `perform_search` function in `backend/test_retrieval.py`.
- [x] T013 [US3] Verify that the output display includes the `source_url` and `title` for every retrieved result, and ensure they are populated correctly (manual output inspection).

## Final Phase: Polish & Cross-Cutting Concerns

**Goal**: Enhance robustness, usability, and handle edge cases.

- [x] T014 Add edge case test queries (e.g., empty string, nonsense characters) to the test suite in `backend/test_retrieval.py`.
- [x] T015 Implement robust error handling for network issues or unexpected API responses from Cohere or Qdrant within `backend/test_retrieval.py`.
- [x] T016 Refine the overall output formatting to improve clarity and human-readability as per the `script-output.md` contract in `backend/test_retrieval.py`.
- [x] T017 Review `backend/validate_rag.py` and remove it if `backend/test_retrieval.py` now covers all its functionality and becomes the primary validation script.

## Dependencies

- User Story 1 is foundational.
- User Story 2 depends on US1.
- User Story 3 depends on US1.

## Parallel Execution Opportunities

- Tasks T005, T006, T007, T009 are core to US1 and could be implemented sequentially.
- Tasks T010 and T011 for US2 can be implemented once T005, T006, T009 are in place.
- Tasks T012 and T013 for US3 can also be implemented once T005, T006, T009 are in place.
- T014, T015, T016 for polishing can be worked on once the core functionality is there.

## Independent Test Criteria

- **US1 (RAG Retrieval Validation)**: Running the script with relevant queries should show meaningful results and latency.
- **US2 (Irrelevance Filtering)**: Running the script with irrelevant queries should show no results or clearly filtered ones.
- **US3 (Citation Metadata Verification)**: Running the script should show correctly populated URL and Title for all relevant results.