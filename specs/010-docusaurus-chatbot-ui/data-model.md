# Data Model: Docusaurus RAG Chatbot UI

## Entities

### ChatMessage

Represents a single message in the conversation history.

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` (UUID) | Unique identifier for the message. |
| `role` | `enum` ("user", "assistant", "system") | The sender of the message. |
| `content` | `string` | The text content of the message (Markdown supported for "assistant"). |
| `citations` | `Citation[]` | List of source citations (only for "assistant" role). |
| `timestamp` | `string` (ISO 8601) | Creation time. |

### Citation

Represents a source document used to generate the answer.

| Field | Type | Description |
|-------|------|-------------|
| `title` | `string` | Title of the source page/document. |
| `url` | `string` | URL or relative path to the source documentation. |
| `snippet` | `string` (optional) | A brief excerpt from the source text. |
| `relevance_score` | `number` (optional) | Confidence score from the retrieval system. |

### ChatState (Frontend)

Represents the transient state of the chat widget.

| Field | Type | Description |
|-------|------|-------------|
| `isOpen` | `boolean` | Whether the chat window is visible. |
| `messages` | `ChatMessage[]` | History of the current conversation. |
| `isLoading` | `boolean` | Whether the system is currently generating a response. |
| `error` | `string | null` | Error message if the last request failed. |
