import axios from 'axios';
import { ChatMessage, Citation } from './types';

// In Docusaurus, use siteConfig.customFields for env vars, or hardcode/fallback
// For this MVP, we'll default to localhost if not found.
const BACKEND_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

interface ChatResponse {
  answer: string;
  sources: Citation[];
}

export const sendMessage = async (query: string): Promise<ChatResponse> => {
  try {
    const response = await api.post<ChatResponse>('/chat', { query });
    return response.data;
  } catch (error) {
    console.error('Chat API Error:', error);
    throw error;
  }
};
