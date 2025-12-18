import React, { useState } from 'react';
import { MessageCircle } from 'lucide-react';
import styles from './styles.module.css';
import ChatWindow from './ChatWindow';

export default function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className={styles.chatbotContainer}>
      {isOpen ? (
        <ChatWindow onClose={() => setIsOpen(false)} />
      ) : (
        <button 
          className={styles.toggleButton} 
          onClick={() => setIsOpen(true)}
          aria-label="Open Chat"
        >
          <MessageCircle size={28} />
        </button>
      )}
    </div>
  );
}
