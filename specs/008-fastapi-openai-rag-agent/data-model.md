# Data Model: FastAPI OpenAI RAG Agent

**Feature**: 008-fastapi-openai-rag-agent

## Entities

### ChatRequest
Represents an incoming request to the `/chat` endpoint.

| Field | Type | Description |
|-------|------|-------------|
| `user_query` | `str` | User's natural language question. |
| `session_id` | `str` | Unique identifier for the chat session. |

### ChatResponse
Represents the agent's response from the `/chat` endpoint.

| Field | Type | Description |
|-------|------|-------------|
| `answer` | `str` | The agent's generated response. |
| `citations` | `List[Dict[str, str]]` | List of dictionaries, each containing `url` and `title` of the source material. |

### ChatMessage
Represents a single message in a chat conversation, used for history.

| Field | Type | Description |
|-------|------|-------------|
| `role` | `str` | Role of the message sender ("user" or "assistant"). |
| `content` | `str` | The message text. |

### ToolCall
Represents an OpenAI Agent's invocation of an external tool.

| Field | Type | Description |
|-------|------|-------------|
| `tool_name` | `str` | Name of the tool invoked (e.g., "retrieval_tool"). |
| `tool_input` | `Dict[str, Any]` | Parameters passed to the tool (JSON object/dictionary). |
| `tool_output` | `Dict[str, Any]` | Result returned by the tool (JSON object/dictionary). |
