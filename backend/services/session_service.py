from typing import List, Dict, Optional
from backend.models.chat_models import ChatMessage

class SessionService:
    def __init__(self):
        # In-memory dictionary to store chat histories
        # Key: session_id (str), Value: List of ChatMessage
        self.sessions: Dict[str, List[ChatMessage]] = {}

    def get_session_history(self, session_id: str) -> List[ChatMessage]:
        """
        Retrieves the chat history for a given session ID.
        Returns an empty list if the session does not exist.
        """
        return self.sessions.get(session_id, [])

    def add_message_to_session(self, session_id: str, message: ChatMessage):
        """
        Adds a single chat message to the history of a specified session.
        If the session does not exist, it will be created.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(message)

    def clear_session(self, session_id: str):
        """
        Clears the chat history for a given session ID.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]

session_service = SessionService()
