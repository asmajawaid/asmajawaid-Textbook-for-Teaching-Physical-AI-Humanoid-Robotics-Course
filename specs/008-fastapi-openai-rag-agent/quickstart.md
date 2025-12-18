# Quickstart: FastAPI OpenAI RAG Agent

**Feature**: 008-fastapi-openai-rag-agent

## Purpose

This document provides quick instructions to set up and run the FastAPI backend for the OpenAI RAG conversational agent. It outlines the environment setup, how to start the application, and how to interact with the `/chat` endpoint.

## Prerequisites

-   Python 3.12 or higher installed.
-   `uv` (Ultrafast Python package installer and resolver) installed.
-   Environment variables `OPENAI_API_KEY`, `COHERE_API_KEY`, `QDRANT_URL`, and `QDRANT_API_KEY` configured with appropriate credentials.
-   The Qdrant collection `rag_emabadding` must be populated with data (e.g., by running `backend/main.py` initially).

## Setup

1.  **Navigate to the project root**:
    ```bash
    cd D:\Q4_SirHamzahSyed\Hackathon\humuniod-spec-book
    ```

2.  **Install dependencies**:
    All project dependencies are managed via `uv` and defined in `backend/pyproject.toml`.
    ```bash
    cd backend
    uv pip install .
    cd ..
    ```

## Running the FastAPI Application

To start the FastAPI application locally, use `uvicorn`:

```bash
cd backend
uvicorn main:app --reload
```
This will start the server, typically accessible at `http://127.0.0.1:8000`. The `--reload` flag enables auto-reloading upon code changes, useful for development.

## Interacting with the API

The primary endpoint is `/chat`. You can test it using tools like `curl`, Postman, Insomnia, or directly through the FastAPI interactive documentation (Swagger UI).

### Using Swagger UI (Recommended)

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/docs`. Here you will find an interactive interface to:

1.  **View the `/chat` endpoint**: Expand the POST `/chat` section.
2.  **Try it out**: Click the "Try it out" button.
3.  **Provide Request Body**: Enter a `user_query` and `session_id` (any unique string, e.g., "test_session_1").
    ```json
    {
      "user_query": "What is ROS 2?",
      "session_id": "my_unique_session_id_1"
    }
    ```
4.  **Execute**: Click the "Execute" button to send the request.
5.  **View Response**: Observe the agent's `answer` and any `citations` provided.

### Example `curl` command

Replace `my_unique_session_id_1` and `What is ROS 2?` with your desired values.

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d 
     {
       "user_query": "What is ROS 2 architecture?",
       "session_id": "test_session_1"
     }
```

## Expected Behavior

-   **Book-related questions**: Should receive accurate, concise answers derived from the book content, along with URLs and titles of source pages.
-   **Follow-up questions**: Within the same `session_id`, subsequent questions should maintain context.
-   **Irrelevant questions**: Should trigger a graceful response indicating the agent's inability to answer questions outside its domain.

If results are not satisfactory, refer to the `specs/008-fastapi-openai-rag-agent/spec.md` and `specs/008-fastapi-openai-rag-agent/plan.md` for details on refinement options.
