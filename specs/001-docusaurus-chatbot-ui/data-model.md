# Data Model: Docusaurus Chatbot UI

**Feature**: 001-docusaurus-chatbot-ui

## Entities

### ChatUIComponent
Represents the interactive chatbot interface within the Docusaurus UI.

| Field | Type | Description |
|-------|------|-------------|
| `isVisible` | `boolean` | Current visibility state of the chatbot UI (e.g., floating button vs. open sidebar). |
| `messages` | `List<ChatMessage>` | Ordered list of messages in the current conversation session. |
| `isLoading` | `boolean` | Indicates if the chatbot is awaiting a response from the backend API. |
| `errorMessage` | `string` | Stores any error message to be displayed to the user. |

### UserMessage
Represents a single message sent by the user to the chatbot.

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique identifier for the message. |
| `text` | `string` | The user's input text. |
| `timestamp` | `datetime` | Time when the message was sent. |

### AgentResponse
Represents the structured response received from the backend API. This directly maps to the `ChatResponse` model from Spec 3.

| Field | Type | Description |
|-------|------|-------------|
| `answer` | `string` | The RAG Agent's generated response (can contain Markdown). |
| `citations` | `List<SourceCitation>` | List of source documents used by the agent. |

### SourceCitation
Represents a single source document cited by the RAG Agent. This directly maps to the `Citation` model from Spec 3.

| Field | Type | Description |
|-------|------|-------------|
| `url` | `string` | URL of the source document within the book's UI. |
| `title` | `string` | Title of the source document. |
