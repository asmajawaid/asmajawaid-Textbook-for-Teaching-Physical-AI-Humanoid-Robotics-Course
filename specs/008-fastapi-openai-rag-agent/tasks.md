# Tasks: FastAPI OpenAI RAG Agent

**Feature**: FastAPI OpenAI RAG Agent
**Branch**: `008-fastapi-openai-rag-agent`
**Date**: 2025-12-17
**Spec**: `specs/008-fastapi-openai-rag-agent/spec.md`

## Summary

This document outlines the tasks required to build a FastAPI backend for an OpenAI RAG conversational agent. The implementation is broken down into phases corresponding to user stories, ensuring a structured approach to integrating API endpoints, agent logic, retrieval tools, and session management.

## Implementation Strategy

The implementation will follow a phased approach, prioritizing core agent functionality (US1), followed by enhancing conversation flow (US2), and robust error handling/boundary conditions (US3 and Polish Phase). This ensures an MVP that can accurately answer book-related questions before scaling up with more complex features.

## Project Structure

The project structure will follow the proposed layout in `plan.md`:

```text
backend/
├── main.py
├── api/
│   └── chat.py
├── services/
│   ├── agent_service.py
│   ├── retrieval_service.py
│   └── session_service.py
├── models/
│   ├── chat_models.py
│   └── tool_models.py
├── core/
│   ├── config.py
│   └── middleware.py
└── tests/
    ├── api/
    ├── services/
    └── integration/
```

## Phase 1: Setup

**Goal**: Establish the basic FastAPI project structure and initial configuration.

- [x] T001 Create `backend/api/` directory.
- [x] T002 Create `backend/services/` directory.
- [x] T003 Create `backend/models/` directory.
- [x] T004 Create `backend/core/` directory.
- [x] T005 Create `backend/tests/` directory.
- [x] T006 Update `backend/pyproject.toml` to include new dependencies: `fastapi`, `uvicorn`, `openai`, `python-dotenv`.
- [x] T007 Create `backend/core/config.py` for environment variable loading (`OPENAI_API_KEY`).
- [x] T008 Create `backend/main.py` with a basic FastAPI application instance.

## Phase 2: Foundational Components

**Goal**: Implement core data models, essential services, and the retrieval tool wrapper.

- [x] T009 Create `backend/models/chat_models.py` for `ChatRequest`, `ChatResponse` (with `Citation`), and `ChatMessage` Pydantic models.
- [x] T010 Create `backend/models/tool_models.py` for `ToolCall` Pydantic model (if specific models are needed for tool representation beyond OpenAI SDK).
- [x] T011 Create `backend/services/retrieval_service.py` to wrap the Qdrant retrieval logic from `backend/test_retrieval.py` into a reusable, asynchronous function that returns structured data (text chunks, URLs, titles). This function will serve as the agent's tool.
- [x] T012 Create `backend/services/session_service.py` with an in-memory dictionary to manage chat session history.
- [x] T013 Create `backend/services/agent_service.py` with a placeholder function for agent initialization and response generation.

## Phase 3: User Story 1 (P1) - Ask a Book-Related Question

**Goal**: Enable the agent to answer questions accurately using book content.

**Independent Test**: Send a specific book-related question to the `/chat` endpoint and verify the response contains accurate information derived from the book, including citations.

- [x] T014 [US1] Integrate `retrieval_service.py` as a function tool into the OpenAI Agent within `backend/services/agent_service.py`.
- [ ] T015 [US1] Configure the OpenAI Agent with the "Book Assistant" System Prompt in `backend/services/agent_service.py`.
- [ ] T016 [US1] Implement the `/chat` POST endpoint in `backend/api/chat.py` to receive `ChatRequest`.
- [ ] T017 [US1] Route `/chat` endpoint requests through `backend/main.py` to the agent logic in `backend/services/agent_service.py`.
- [ ] T018 [US1] Implement agent logic to call the retrieval tool when appropriate and synthesize answers strictly from retrieved context in `backend/services/agent_service.py`.
- [ ] T019 [US1] Ensure the `/chat` endpoint returns the agent's answer and citations in `ChatResponse` format in `backend/api/chat.py`.

## Phase 4: User Story 2 (P2) - Ask a Follow-up Question

**Goal**: Allow for natural, continuous dialogue with context.

**Independent Test**: Send an initial book-related question, then a follow-up question within the same session ID, and verify the response contextually relates to the previous turns.

- [ ] T020 [US2] Implement functionality to retrieve chat history from `session_service.py` and pass it to the OpenAI Agent in `backend/services/agent_service.py`.
- [ ] T021 [US2] Implement functionality to save the current turn's `user_query` and agent `answer` to `session_service.py` for the given `session_id` in `backend/services/agent_service.py`.

## Phase 5: User Story 3 (P2) - Ask an Irrelevant Question

**Goal**: Gracefully handle questions outside the book's scope.

**Independent Test**: Send a question completely unrelated to the book's content to the `/chat` endpoint and verify the agent responds gracefully indicating it cannot answer.

- [ ] T022 [US3] Implement logic for the agent to provide a graceful "I don't know" or "out of scope" response if no relevant information is found by the retrieval tool or if the query is general/unrelated to the book's content in `backend/services/agent_service.py`.

## Final Phase: Polish & Cross-Cutting Concerns

**Goal**: Enhance robustness, logging, and testability.

- [ ] T023 Implement logging for requests, responses, and agent tool calls in `backend/main.py` and `backend/services/agent_service.py`.
- [ ] T024 Create `backend/core/middleware.py` and implement custom error handling middleware for API timeouts (e.g., from OpenAI/Qdrant) and other exceptions. Integrate it into `backend/main.py`.
- [ ] T025 Set up `pytest` in `backend/tests/` for unit tests (e.g., `api/`, `services/`) and integration tests (`integration/`).
- [ ] T026 Update `backend/quickstart.md` to reflect the final API usage and deployment instructions.

## Dependencies

- Phase 1 (Setup) is a prerequisite for all other phases.
- Phase 2 (Foundational Components) is a prerequisite for US1, US2, US3.
- US1 (P1) is foundational for US2 and US3.
- US2 depends on US1.
- US3 depends on US1.
- Final Phase tasks can be integrated throughout but are finalized at the end.

## Parallel Execution Opportunities

- Tasks within Phase 1 (Setup) can be run mostly in parallel (directory creation).
- Tasks within Phase 2 (Foundational Components) related to `models`, `retrieval_service`, and `session_service` can be developed somewhat in parallel once directory structure is set up.
- US2 and US3 can be developed in parallel after US1 is complete.
- Some Final Phase tasks (logging, basic error handling) can start early.

## Independent Test Criteria

- **US1 (Ask a Book-Related Question)**: Send a book-related question to `/chat`, verify accurate response and citations.
- **US2 (Ask a Follow-up Question)**: Send an initial question, then a follow-up with the same `session_id`, verify contextual response.
- **US3 (Ask an Irrelevant Question)**: Send an out-of-scope question, verify graceful "I don't know" response.
