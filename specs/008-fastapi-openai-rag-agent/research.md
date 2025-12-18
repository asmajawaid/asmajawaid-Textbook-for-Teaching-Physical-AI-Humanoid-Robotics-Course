# Research: FastAPI OpenAI RAG Agent

**Feature**: 008-fastapi-openai-rag-agent
**Date**: 2025-12-17

## Decisions

### 1. Session Management for Chat History
- **Decision**: For the initial prototype/MVP, chat history will be managed using an in-memory dictionary in `session_service.py`, mapping `session_id` (string) to a list of `ChatMessage` objects.
- **Rationale**: This approach is simple to implement and sufficient for demonstrating basic follow-up question capabilities. It avoids introducing external dependencies like Redis or a database for session storage at this stage, accelerating development.
- **Alternatives Considered**:
    -   **Redis**: Would require a Redis instance and more complex integration but offers persistence and scalability. Deferred for future enhancements.
    -   **Database (e.g., PostgreSQL)**: Offers full persistence and querying capabilities but adds significant complexity for schema design and ORM integration. Deferred.

### 2. OpenAI Agent Tool Integration
- **Decision**: The existing Qdrant retrieval logic from `backend/test_retrieval.py` will be wrapped into an asynchronous function that adheres to the OpenAI tool specification. This function will be provided to the `OpenAI` agent for tool calling.
- **Rationale**: Reuses existing, validated retrieval logic and directly leverages the OpenAI SDK's built-in function calling capabilities. Asynchronous execution is crucial for FastAPI's performance.

### 3. FastAPI Error Handling
- **Decision**: Implement custom exception handlers in `main.py` or a dedicated `core/middleware.py` to catch common API errors (e.g., `RequestValidationError`, `HTTPException`) and specific OpenAI/Qdrant client exceptions. Middleware will be used for logging requests and responses.
- **Rationale**: Centralized error handling provides consistent error responses to clients, enhances user experience, and improves maintainability. Logging is critical for debugging and monitoring in production.

### 4. Language Model Selection
- **Decision**: Use `OpenAI GPT-4o` as specified.
- **Rationale**: Provides high-quality responses and is compatible with the OpenAI Agents SDK.

## Open Questions Resolved

-   **Q**: What mechanism for session management?
-   **A**: In-memory dictionary for MVP, designed for easy replacement with Redis/DB later.
-   **Q**: Best practices for integrating OpenAI Agent tools within FastAPI?
-   **A**: Wrap retrieval logic in async functions, use OpenAI SDK's tool definitions, and ensure proper dependency injection.
-   **Q**: FastAPI error handling middleware for API timeouts and custom exceptions?
-   **A**: Custom exception handlers and middleware for logging/specific error types.
