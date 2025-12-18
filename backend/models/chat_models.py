from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class Citation(BaseModel):
    url: str = Field(..., description="URL of the source document.")
    title: str = Field(..., description="Title of the source document.")

class ChatRequest(BaseModel):
    user_query: str = Field(..., description="User's natural language question.")
    session_id: str = Field(..., description="Unique identifier for the chat session to maintain context.")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="The agent's generated response to the user query.")
    citations: Optional[List[Citation]] = Field(None, description="List of source documents used by the agent.")

class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender ('user' or 'assistant').")
    content: str = Field(..., description="The message text.")
