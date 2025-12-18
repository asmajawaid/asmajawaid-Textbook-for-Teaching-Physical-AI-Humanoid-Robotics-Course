import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import clsx from 'clsx';
import styles from './styles.module.css';
import { ChatMessage } from './types';

interface Props {
  message: ChatMessage;
}

export default function ChatBubble({ message }: Props) {
  const isUser = message.role === 'user';

  return (
    <div className={clsx(styles.message, isUser ? styles.userMessage : styles.botMessage)}>
      <div className={styles.markdownContent}>
        {isUser ? (
          message.content
        ) : (
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {message.content}
          </ReactMarkdown>
        )}
      </div>

      {!isUser && message.citations && message.citations.length > 0 && (
        <div className={styles.citations}>
          <div className={styles.citationHeader}>Sources:</div>
          <ul className={styles.citationList}>
            {message.citations.map((cite, idx) => (
              <li key={idx} className={styles.citationItem}>
                <a 
                  href={cite.url} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className={styles.citationLink}
                >
                  {cite.title || cite.url}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}