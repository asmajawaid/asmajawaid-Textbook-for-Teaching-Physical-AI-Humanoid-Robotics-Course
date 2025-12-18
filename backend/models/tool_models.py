from typing import Dict, Any
from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    tool_name: str = Field(..., description="Name of the tool invoked (e.g., 'retrieval_tool').")
    tool_input: Dict[str, Any] = Field(..., description="Parameters passed to the tool (JSON object/dictionary).")
    tool_output: Dict[str, Any] = Field(..., description="Result returned by the tool (JSON object/dictionary).")