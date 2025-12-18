# Backend API Reference: Chat Endpoint

**Feature**: 001-docusaurus-chatbot-ui
**Date**: 2025-12-17
**Purpose**: This document summarizes the key aspects of the `/chat` API endpoint provided by the FastAPI backend (Spec 3), which the Docusaurus frontend will consume. For full details, refer to `specs/008-fastapi-openai-rag-agent/contracts/chat-api.yaml`.

## Endpoint Details

-   **Path**: `/chat`
-   **Method**: `POST`
-   **Summary**: Sends a user query to the conversational agent and receives a response.

## Request Body (`ChatRequest` - from Spec 3)

| Field | Type | Description | Example |
|---|---|---|---|
| `user_query` | `string` | User's natural language question. | `"What is the ROS 2 architecture?"` |
| `session_id` | `string` | Unique identifier for the chat session to maintain context. | `"user123-sessionabc"` |

## Response Body (`ChatResponse` - from Spec 3)

| Field | Type | Description | Example |
|---|---|---|---|
| `answer` | `string` | The agent's generated response to the user query. | `"ROS 2 architecture is based on a graph of nodes that communicate..."` |
| `citations` | `Array<Citation>` | List of source documents used by the agent, including URL and title. | `[{"url": "...", "title": "..."}]` |

### Citation Object (`Citation` - from Spec 3)

| Field | Type | Description | Example |
|---|---|---|---|
| `url` | `string` | URL of the source document. | `"https://example.com/doc"` |
| `title` | `string` | Title of the source document. | `"Example Document Title"` |

## Error Responses (as per clarification in Spec 3)

-   **Format**: `{ "detail": "Error description here", "code": "ERROR_CODE" }`
-   **HTTP Status Codes**: `400` (Invalid Request), `500` (Internal Server Error or Agent Failure)
