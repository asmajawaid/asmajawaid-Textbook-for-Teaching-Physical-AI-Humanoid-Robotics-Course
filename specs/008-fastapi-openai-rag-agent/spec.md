# Feature Specification: FastAPI OpenAI RAG Agent

**Feature Branch**: `008-fastapi-openai-rag-agent`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: User description: "Build a production-ready backend using FastAPI and the OpenAI Agents/ChatKit SDK to create a conversational agent capable of answering questions based on the book's content. 🛠 Tech Stack Framework: FastAPI. Agent Framework: OpenAI Agents / ChatKit SDK. Vector Store: Qdrant Cloud (via Spec 2 retrieval logic). Language Model: OpenAI GPT-4o (or compatible model). 📋 Requirements FastAPI Setup: Initialize a robust FastAPI application with structured routing. Implement a POST endpoint /chat to receive user queries and session IDs. Agent Logic: Configure the OpenAI Agent with a System Prompt defining its persona as the "Book Assistant." Integrate the retrieval pipeline as a Tool/Function Call that the agent can invoke to fetch context from Qdrant. Context Injection: Ensure the agent synthesizes answers strictly using retrieved chunks. Handle cases where no relevant information is found (graceful "I don't know" responses). Session Management: Implement basic chat history or state management using the SDK to allow follow-up questions. Error Handling: Add logging and middleware to handle API timeouts or retrieval failures. ✅ Success Criteria The API endpoint /chat returns accurate, context-aware responses. The Agent successfully triggers the retrieval tool when a question about the book is asked. The system handles both general queries and specific text-based questions."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a Book-Related Question (Priority: P1)

As a user, I want to ask questions about the book's content via a chat interface so that I can quickly get accurate information.

**Why this priority**: This is the core functionality and primary value proposition of the conversational agent.

**Independent Test**: Can be fully tested by sending a specific book-related question to the `/chat` endpoint and verifying the response contains accurate information derived from the book.

**Acceptance Scenarios**:

1. **Given** the chat agent is initialized and the Qdrant database is populated, **When** a user sends a query like "What is ROS 2 architecture?", **Then** the agent should trigger the retrieval tool, find relevant chunks, and return an accurate summary of ROS 2 architecture.
2. **Given** the agent receives a book-related question, **When** it processes the query, **Then** the response should include citations (URLs and titles) to the source material.

---

### User Story 2 - Ask a Follow-up Question (Priority: P2)

As a user, I want to ask follow-up questions in the same conversation session so that I can have a natural, continuous dialogue with the agent.

**Why this priority**: Enhances user experience and allows for more in-depth exploration of topics.

**Independent Test**: Send an initial book-related question, then a follow-up question (e.g., "Tell me more about it" or "What about topics?") within the same session ID, and verify the response contextually relates to the previous turns.

**Acceptance Scenarios**:

1. **Given** a user has asked an initial question and received a response, **When** the user asks a follow-up question in the same session, **Then** the agent should incorporate the conversation history to provide a contextually relevant answer.

---

### User Story 3 - Ask an Irrelevant Question (Priority: P2)

As a user, I want to ask questions outside the book's scope so that the agent can clearly communicate its limitations and avoid providing incorrect information.

**Why this priority**: Prevents hallucinations and builds user trust by clearly defining boundaries.

**Independent Test**: Send a question completely unrelated to the book's content to the `/chat` endpoint and verify the agent responds gracefully indicating it cannot answer or lacks information.

**Acceptance Scenarios**:

1. **Given** the chat agent is initialized, **When** a user sends a query like "What is the weather today?", **Then** the agent should respond with a message indicating that it can only answer questions related to the book's content.

---

### Edge Cases

-   **Empty Query**: What happens when an empty string is sent to `/chat`?
-   **API Timeouts**: How does the system respond if the OpenAI or Qdrant API times out?
-   **Retrieval Failures**: What if the retrieval tool fails to return any relevant chunks due to an internal error?
-   **Malicious/Prompt Injection**: How are attempts to bypass the agent's persona or extract sensitive information handled? (Graceful failure or persona adherence).

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: System MUST implement a FastAPI application with structured routing.
-   **FR-002**: System MUST expose a POST endpoint `/chat` that accepts a `user_query` (string) and a `session_id` (string).
-   **FR-003**: System MUST configure an OpenAI Agent with a System Prompt establishing its persona as a "Book Assistant" specializing in the provided content.
-   **FR-004**: System MUST integrate the previously developed retrieval pipeline (from Spec 007) as a Tool/Function Call that the OpenAI Agent can invoke.
-   **FR-005**: The agent MUST synthesize answers strictly based on the context retrieved by the retrieval tool.
-   **FR-006**: The agent MUST provide a graceful "I don't know" response if no relevant information is found by the retrieval tool or if the query is outside the scope of its knowledge base.
-   **FR-007**: System MUST implement persistent chat history using Neon Serverless Postgres to allow follow-up questions across server restarts. Sessions MUST expire after 30 days of inactivity.
-   **FR-008**: System MUST include logging for incoming requests, agent tool calls, responses, and errors.
-   **FR-009**: System MUST implement middleware or decorators for robust error handling, including API timeouts (OpenAI, Qdrant) and retrieval tool failures, returning errors in the format: `{ "detail": "Error description here", "code": "ERROR_CODE" }`.
-   **FR-010**: The `/chat` endpoint response MUST include the agent's answer and any relevant citations (source URLs and titles) if context was retrieved.

-   **FR-011**: System MUST support a "Selected-Text-Only" mode. If `selected_text` is provided in the request, the agent MUST ignore the retrieval tool and answer strictly using the provided text.
-   **FR-012**: The agent MUST return a specific message (e.g., "Information not found in the selected text") if it cannot answer a `selected_text` query using only that context.

-   **FR-013**: The system MUST support queries and responses in English only for the current phase.

### Non-Functional Requirements

-   **NFR-001 (Performance)**: The average response time for the `/chat` endpoint MUST be under 5 seconds for book-related questions.
-   **NFR-002 (Scalability)**: The FastAPI application MUST be horizontally scalable to handle increased user load.
-   **NFR-003 (Reliability)**: The `/chat` endpoint MUST maintain an uptime of 99.9%.
-   **NFR-004 (Security)**: The FastAPI application MUST be resilient to common web vulnerabilities (e.g., XSS, SQLi, CSRF, as applicable to a chat API). (This will be an implicit check, not a direct implementation task within this spec).
-   **NFR-005 (Security)**: The `/chat` API endpoint MUST be publicly accessible without authentication in the current phase.
-   **NFR-006 (Integration)**: The FastAPI application MUST enable Cross-Origin Resource Sharing (CORS) for all origins (`*`) to facilitate frontend integration during development.
-   **NFR-007 (Security)**: The `/chat` API endpoint MUST implement rate limiting of 10 requests per minute per IP address to prevent abuse.

### Key Entities *(include if feature involves data)*

-   **ChatRequest**:
    -   `user_query`: User's natural language question (string).
    -   `session_id`: Unique identifier for the chat session (string).
    -   `selected_text`: Optional string containing text selected by the user from the book. If present, triggers context-restricted mode.
-   **ChatResponse**:
    -   `answer`: The agent's generated response (string).
    -   `citations`: List of dictionaries, each containing `url` and `title` (list of objects).
-   **ChatMessage**:
    -   `role`: "user" or "assistant" (string).
    -   `content`: Message text (string).
-   **ToolCall**:
    -   `tool_name`: Name of the tool invoked (string, e.g., "retrieval_tool").
    -   `tool_input`: Parameters passed to the tool (JSON object/dictionary).
    -   `tool_output`: Result returned by the tool (JSON object/dictionary).

## Clarifications
### Session 2025-12-18
- Q: How should the "Selected-Text-Only Q&A" mode be implemented in the `/chat` endpoint? → A: Add `selected_text` (optional string) to `ChatRequest`; if present, agent MUST skip RAG and answer only from that text.
- Q: What specific rate limiting parameters should be applied to the `/chat` endpoint? → A: 10 requests per minute per IP address.
- Q: Should chat session history be persistent across server restarts? → A: Yes, implement Neon Postgres immediately for session persistence.
- Q: What is the desired expiration policy for persistent sessions? → A: Sessions expire after 30 days of inactivity.
- Q: What languages should the conversational agent support? → A: Support English only.

### Session 2025-12-17
- Q: Is the `/chat` API endpoint intended to be publicly accessible, or will it require authentication (e.g., API key, OAuth)? → A: Publicly accessible without authentication.
- Q: What is the desired JSON format for error responses (e.g., API timeouts, retrieval failures, validation errors) from the `/chat` endpoint? → A: `{ "detail": "Error description here", "code": "ERROR_CODE" }`
- Q: Will the FastAPI application need to support Cross-Origin Resource Sharing (CORS) for frontend integration, and if so, what are the allowed origins? → A: Yes, enable CORS for all origins (`*`).
- Q: Should chat session history be persistent across server restarts, or is in-memory storage sufficient for the current phase? → A: In-memory storage is sufficient for the current phase.
- Q: Will the `/chat` API endpoint require rate limiting to prevent abuse or control resource usage? → A: Yes, implement basic rate limiting.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: 90% of book-related questions submitted to the `/chat` endpoint receive accurate, contextually relevant answers based *only* on retrieved book content.
-   **SC-002**: The OpenAI Agent successfully invokes the integrated retrieval tool for 100% of questions identified as potentially related to the book's content.
-   **SC-003**: 100% of questions determined to be outside the book's scope result in a graceful "I don't know" or "out of scope" response.
-   **SC-004**: The average end-to-end response time for the `/chat` endpoint (from request to final agent answer) is less than 5 seconds.
-   **SC-005**: For 100% of responses where content was retrieved, citations (URL and Title) are correctly provided.
