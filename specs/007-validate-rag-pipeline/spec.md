# Feature Specification: Validate RAG Pipeline

**Feature Branch**: `007-validate-rag-pipeline`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: User description: "Validate the RAG pipeline by retrieving relevant data from Qdrant and testing the accuracy of the semantic search before connecting the LLM.📋 RequirementsSearch Implementation: Create a script to convert user queries into embeddings using the Cohere model.Qdrant Querying: Implement a search function to fetch the top $k$ (e.g., $k=3$) most relevant document chunks from the Qdrant collection.Similarity Threshold: Set a confidence score filter to ensure only highly relevant content is retrieved.Metadata Verification: Ensure the retrieved chunks include correct metadata (URLs and page titles) for future citations.Pipeline Validation: Run a series of test queries (Edge cases and specific book topics) to confirm the retrieval logic works as expected.✅ Success CriteriaInput queries successfully return the most semantically similar text from the vector DB.The latency of the retrieval process is within acceptable limits (sub-second).Retrieval accuracy is manually verified against the book's content."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - RAG Retrieval Validation (Priority: P1)

As a developer, I need to run a validation script that queries the vector database with specific book topics so that I can confirm the retrieval system returns semantically relevant content before integrating the LLM.

**Why this priority**: Essential to ensure the "G" (Generation) in RAG has valid "R" (Retrieval) context. Without this, the chatbot will hallucinate.

**Independent Test**: Can be tested by running the script with known queries (e.g., "ROS 2 architecture") and manually verifying that the printed text snippets match the query topic.

**Acceptance Scenarios**:

1. **Given** a populated Qdrant database and a query about "ROS 2 nodes", **When** the validation script is run, **Then** it should return 3 document chunks discussing ROS 2 nodes, topics, or services.
2. **Given** the script is executed, **When** it completes a query, **Then** it should display the latency for that retrieval operation.

---

### User Story 2 - Irrelevance Filtering (Priority: P2)

As a developer, I want the system to filter out search results that have low similarity scores so that the LLM is not provided with irrelevant context for unrelated queries.

**Why this priority**: Prevents the system from trying to answer "How to bake a cake" using robotics textbook content, which reduces hallucinations.

**Independent Test**: specific test case in the script using an off-topic query.

**Acceptance Scenarios**:

1. **Given** a query totally unrelated to the book (e.g., "baking recipes"), **When** the script runs, **Then** it should return zero results or results flagged as below the confidence threshold.

---

### User Story 3 - Citation Metadata Verification (Priority: P2)

As a developer, I want to ensure every retrieved text chunk includes the correct source URL and page title so that the final application can accurately cite sources.

**Why this priority**: Critical for academic/educational integrity of the RAG bot.

**Independent Test**: Inspect the output of the validation script to see if "Source URL" and "Title" fields are populated and valid.

**Acceptance Scenarios**:

1. **Given** a successful retrieval, **When** the results are displayed, **Then** each result must contain a non-empty "Title" and a valid "URL" pointing to the documentation site.

---

### Edge Cases

- **Empty Query**: Handling input of an empty string.
- **Nonsense Query**: Random characters (e.g., "asdfghjkl").
- **API Failure**: Handling connection timeouts to Cohere or Qdrant.
- **Missing Metadata**: Handling chunks that might (erroneously) lack a title or URL.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a script/function to convert natural language queries into vector embeddings using the configured embedding model (Cohere).
- **FR-002**: System MUST query the Qdrant vector collection to retrieve the top $k$ (default 3) nearest neighbors for the query vector.
- **FR-003**: System MUST apply a configurable similarity threshold (confidence score) to filter out irrelevant results.
- **FR-004**: System MUST return and display metadata for each retrieved chunk, specifically the Source URL and Page Title.
- **FR-005**: System MUST include a predefined test suite of queries covering:
    - Core technical topics (e.g., ROS 2, Isaac Sim).
    - Edge cases (e.g., irrelevant topics, specific keywords).
- **FR-006**: System MUST measure and report the latency (time taken) for the retrieval process (embedding + vector search).

### Non-Functional Requirements

- **NFR-001 (Performance)**: The end-to-end retrieval process (Embedding + Search) MUST complete in under 1 second for standard queries.
- **NFR-002 (Usability)**: The validation output MUST be human-readable, clearly separating passes, fails, and content snippets.

### Key Entities *(include if feature involves data)*

- **Query**: The user's input text string.
- **Document Chunk**: A piece of text from the book with associated vector and metadata.
- **Metadata**: Structured data linked to a chunk (URL, Title, Chunk Index).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of retrieval operations for standard queries complete in under 1.0 seconds.
- **SC-002**: 100% of "irrelevant" test queries (e.g., unrelated topics) return 0 results after threshold filtering.
- **SC-003**: 100% of "relevant" test queries return at least 1 result with a similarity score above the defined threshold.
- **SC-004**: 100% of retrieved search results contain valid, non-null URL and Title metadata.