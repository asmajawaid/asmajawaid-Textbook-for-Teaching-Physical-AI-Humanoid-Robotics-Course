import React, { useState, useRef, useEffect } from 'react';
import { Send, X } from 'lucide-react';
import styles from './styles.module.css';
import ChatBubble from './ChatBubble';
import { sendMessage } from './api';
import { ChatMessage } from './types';

interface Props {
  onClose: () => void;
}

export default function ChatWindow({ onClose }: Props) {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([
    { 
      id: 'init', 
      role: 'assistant', 
      content: 'Hi! Ask me anything about the Humanoid Robotics book.', 
      timestamp: new Date().toISOString() 
    }
  ]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userMsg: ChatMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const response = await sendMessage(userMsg.content);
      const botMsg: ChatMessage = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: response.answer,
        citations: response.sources,
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (err: any) {
      console.error(err);
      const errorMessage = err.response?.data?.detail || err.message || 'Unknown error';
      const errorMsg: ChatMessage = {
        id: (Date.now() + 1).toString(),
        role: 'system',
        content: `Error: ${errorMessage}. Please check the backend logs.`,
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.chatWindow}>
      <div className={styles.chatHeader}>
        <span>AI Assistant</span>
        <button onClick={onClose} style={{background: 'none', border: 'none', color: 'white', cursor: 'pointer'}}>
          <X size={20} />
        </button>
      </div>
      <div className={styles.messageList}>
        {messages.map(msg => (
          <ChatBubble key={msg.id} message={msg} />
        ))}
        {loading && (
          <div className={`${styles.message} ${styles.botMessage}`}>
            Typing...
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className={styles.inputArea}>
        <input 
          className={styles.input}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && handleSend()}
          placeholder="Type your question..."
          disabled={loading}
          autoFocus
        />
        <button className={styles.sendButton} onClick={handleSend} disabled={loading || !input.trim()}>
          <Send size={18} />
        </button>
      </div>
    </div>
  );
}
