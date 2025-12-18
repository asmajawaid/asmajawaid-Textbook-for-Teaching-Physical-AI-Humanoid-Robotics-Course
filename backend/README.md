Requirement-2: Integrated RAG Chatbot — Step-by-Step
# Phase 1: Data & Vector Layer (Foundation)

✔ (Aap already complete kar chuki hain, context ke liye list kar raha hoon)

Deploy Docusaurus book on GitHub Pages

Crawl deployed URLs

Clean & chunk content with metadata

Generate embeddings (Cohere)

Store embeddings in Qdrant

# Phase 2: Retrieval Pipeline

✔ (Completed)

Implement vector similarity search

Test retrieval accuracy (query → relevant chunks)

Validate metadata (URL, section, heading)

# Phase 3: Backend Agent (Core Logic)

✔ (Completed)

Setup FastAPI backend

Integrate OpenAI Agents / ChatKit SDK

Connect agent with retrieval pipeline

Implement system prompts + tools

Add “context-restricted answering” logic

# Phase 4: Session & State Management

(Required by spec)

Setup Neon Serverless Postgres

Store:

Chat sessions

Conversation history

Selected-text context (if any)

Link session IDs with user queries

# Phase 5: Selected-Text-Only Q&A (Key Requirement)

(Critical for grading)

Accept selected text from frontend

Override retrieval source:

❌ No Qdrant search

✅ Use only user-selected text

Enforce agent instruction:

“Answer strictly from provided text”

Return grounded answer or “Not found in selection”

# Phase 6: Frontend Integration

(Spec-4)

Embed chatbot UI inside book pages

Connect frontend → FastAPI endpoints

Pass:

User query

Page URL

Selected text (optional)

Display citations / source sections

# Phase 7: Validation & Deployment

Test modes:

Normal RAG (Qdrant)

Selected-text-only

Handle edge cases (no results, empty selection)

Deploy backend

Verify end-to-end flow on live book

Final Deliverables Checklist

✅ Embedded chatbot in book

✅ RAG answers from full book

✅ Answers restricted to selected text

✅ FastAPI backend

✅ OpenAI Agent SDK

✅ Qdrant + Neon integration


# Step 1: uv Install
powershell -c "ircl.exe -L https://astral.sh/uv/install.ps1 | iex" 
# Step 2: Project Folder
uv init backend
cd backend
# Step 3: Zaroori Dependencies Install Karein
uv add fastapi uvicorn cohere qdrant-client openai python-dotenv
(or)
# .Venv 
uv venv
.venv\Scripts\activate
# Step 4: Directory Structure Sahi Karein
backend/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI Entry point
│   ├── engine.py      # RAG/Vector DB logic
│   └── routes.py      # API Endpoints
├── .env               # API Keys (Cohere, Qdrant, etc.)
├── .python-version
└── pyproject.toml
# Step 5: FastAPI Ka Buniyadi Code (main.py)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG Chatbot Backend")

# Frontend se connect karne ke liye CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Local development ke liye
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# Step 6: Server Run Karein
uv run uvicorn app.main:app --reload
# Step 7: Environment Variables (.env)
COHERE_API_KEY=your_key_here
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_key
