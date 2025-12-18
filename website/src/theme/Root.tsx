import React from 'react';
import Chatbot from '../components/Chatbot';

// Global wrapper for Docusaurus
export default function Root({children}: {children: React.ReactNode}) {
  return (
    <>
      {children}
      <Chatbot />
    </>
  );
}