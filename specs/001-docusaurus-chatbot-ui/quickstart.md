# Quickstart: Frontend-Backend Integration

**Feature**: 001-docusaurus-chatbot-ui

## Purpose

This document will provide quick instructions to set up and run the Docusaurus frontend with the FastAPI backend. It will outline the environment setup, how to start both applications, and how to interact with the integrated chatbot.

## Prerequisites

-   Node.js (LTS version)
-   Yarn or npm
-   Python 3.12 or higher
-   `uv` (Ultrafast Python package installer and resolver)
-   FastAPI backend (Spec 3) running locally or accessible via `BACKEND_URL`.

## Setup

1.  **Clone the repository**: (Assumed already done)
2.  **Backend Setup**:
    -   Navigate to the `backend/` directory.
    -   Install Python dependencies (if not already done for Spec 3): `uv pip install .`
    -   Ensure environment variables (`OPENAI_API_KEY`, `COHERE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`) are configured.
    -   Ensure Qdrant collection `rag_emabadding` is populated.
3.  **Frontend Setup**:
    -   Navigate to the `frontend/` directory.
    -   Install Node.js dependencies: `yarn install` or `npm install`
    -   Create a `.env.local` file in the `frontend/` directory with `BACKEND_URL=http://localhost:8000` (or the actual backend URL).

## Running the Applications

1.  **Start FastAPI Backend**:
    ```bash
    cd backend
    uvicorn main:app --reload
    ```
2.  **Start Docusaurus Frontend**:
    ```bash
    cd frontend
    yarn start
    ```
    This will typically open the Docusaurus site at `http://localhost:3000`.

## Interacting with the Chatbot

-   Once both applications are running, navigate to the Docusaurus site in your web browser.
-   Locate the chatbot UI component (e.g., floating action button, sidebar).
-   Type a question related to the book's content into the chatbot input field.
-   Observe the chatbot's response, including any source citations.
-   Click on citations to navigate to relevant book sections.

## Troubleshooting

-   **CORS errors**: Ensure the FastAPI backend is configured to allow requests from the Docusaurus development server.
-   **Backend unreachable**: Verify the `BACKEND_URL` in `.env.local` is correct and the backend is running.
-   **No response from chatbot**: Check backend logs for errors, verify API keys, and ensure Qdrant is populated.
