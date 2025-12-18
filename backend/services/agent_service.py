from typing import List, Dict, Any, Optional
from openai import OpenAI
from openai.types.beta.threads import Message
import json
from backend.core.config import settings
from backend.models.chat_models import ChatMessage, ChatResponse, Citation
from backend.services.session_service import session_service
from backend.services.retrieval_service import retrieve_context

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Define the tool for the OpenAI agent
retrieval_tool_schema = {
    "type": "function",
    "function": {
        "name": "retrieve_context",
        "description": "Retrieve relevant context from the book to answer user questions. Always use this tool for questions about the book content.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The user's query or a statement to retrieve context for."
                },
                "k": {
                    "type": "integer",
                    "description": "The number of top results to retrieve (default is 3)."
                },
                "threshold": {
                    "type": "number",
                    "description": "The minimum score threshold for retrieved results (default is 0.5)."
                }
            },
            "required": ["query"]
        }
    }
}

async def generate_agent_response(session_id: str, user_query: str) -> ChatResponse:
    """
    Generates a response from the OpenAI agent based on the user's query and session history.
    """
    messages = [] # This will be populated with session history later (T020)
    messages.append({"role": "user", "content": user_query})

    # Step 1: Send user query and tools to the model
    response = client.chat.completions.create(
        model="gpt-4o", # As specified in research.md
        messages=messages,
        tools=[retrieval_tool_schema], # Use the globally defined tool schema
        tool_choice="auto", # Allows the agent to decide whether to call the tool
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    citations = [] # Initialize citations list

    if tool_calls:
        # Step 2: Call the tool
        available_functions = {
            "retrieve_context": retrieve_context,
        }
        messages.append(response_message)  # extend conversation with assistant's reply
        
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            
            # Asynchronous tool call
            tool_response = await function_to_call(
                query=function_args.get("query"),
                k=function_args.get("k", 3),
                threshold=function_args.get("threshold", 0.5)
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(tool_response),
                }
            )
            
            # Extract citations from tool_response
            for item in tool_response:
                citations.append(Citation(url=item['url'], title=item['title']))

        # Step 3: Get a new response from the model where it can see the tool outputs
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        final_answer = second_response.choices[0].message.content
    else:
        final_answer = response_message.content

    return ChatResponse(
        answer=final_answer,
        citations=citations
    )
