import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid

# Load environment variables
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Import service (assuming it's in the python path)
from backend.services.agent_service import generate_agent_response
from backend.models.chat_models import ChatResponse, Citation

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FrontendChatRequest(BaseModel):
    query: str

class FrontendChatResponse(BaseModel):
    answer: str
    sources: List[Citation]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI OpenAI RAG Agent!"}

@app.post("/chat", response_model=FrontendChatResponse)
async def chat(request: FrontendChatRequest):
    try:
        # Generate a temporary session ID for this request if we don't track sessions yet
        session_id = str(uuid.uuid4())
        
        # Call the agent service
        agent_response = await generate_agent_response(session_id=session_id, user_query=request.query)
        
        # Map to frontend response format
        return FrontendChatResponse(
            answer=agent_response.answer,
            sources=agent_response.citations or []
        )
    except Exception as e:
        # Log the error (print for now)
        print(f"Error in /chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))
