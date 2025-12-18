# Quickstart: Docusaurus Chatbot UI

## Prerequisites

- Node.js 18+
- Python 3.12+ (for Backend)
- `uv` (for Python dependency management)

## 1. Setup Backend

1.  Navigate to `backend/`.
2.  Install dependencies:
    ```bash
    uv venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    uv pip install -r pyproject.toml # or requirements.txt
    ```
3.  Start the FastAPI server:
    ```bash
    uvicorn main:app --reload --port 8000
    ```
    Ensure the vector database (Qdrant) is accessible as per `backend` config.

## 2. Setup Frontend (Website)

1.  Navigate to `website/`.
2.  Install new dependencies:
    ```bash
    npm install axios react-markdown remark-gfm clsx lucide-react
    ```
3.  Create `.env` file in `website/` (if not exists):
    ```env
    BACKEND_URL=http://localhost:8000
    ```
4.  Start Docusaurus:
    ```bash
    npm start
    ```

## 3. Verify Integration

1.  Open `http://localhost:3000`.
2.  You should see the Chatbot floating button (usually bottom-right).
3.  Click it to open the chat window.
4.  Type "Hello" or a question about the docs.
5.  Verify the typing indicator appears.
6.  Verify the response appears and is formatted correctly.
