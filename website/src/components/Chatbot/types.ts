export interface Citation {
  title: string;
  url: string;
  snippet?: string;
  relevance_score?: number;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  citations?: Citation[];
  timestamp: string;
}

export interface ChatState {
  isOpen: boolean;
  messages: ChatMessage[];
  isLoading: boolean;
  error: string | null;
}
