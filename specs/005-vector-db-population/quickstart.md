# Quickstart: Vector DB Population Script

## Prerequisites

- Python 3.12+
- `uv` installed (`pip install uv` or via installer)
- Cohere API Key
- Qdrant Cloud URL and API Key

## Setup

1. **Navigate to backend**:
   ```bash
   cd backend
   ```

2. **Initialize Environment** (if not already):
   ```bash
   uv init
   uv add cohere qdrant-client requests beautifulsoup4 langchain-text-splitters
   ```

3. **Environment Variables**:
   Create a `.env` file in `backend/` or set variables in your shell:
   ```bash
   export COHERE_API_KEY="your-key"
   export QDRANT_URL="your-url"
   export QDRANT_API_KEY="your-key"
   ```

## Running the Script

Execute the script using `uv`:

```bash
uv run main.py
```

## Verification

Check the output logs for:
- "Successfully connected to Qdrant"
- "Found X URLs"
- "Upserted X chunks"

Go to your Qdrant Cloud Dashboard and verify the collection `rag_emabadding` exists and contains points.
