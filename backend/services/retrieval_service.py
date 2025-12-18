import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, Range
from typing import List, Dict, Any

from backend.core.config import settings

# Initialize clients
co = cohere.Client(settings.COHERE_API_KEY)
qdrant_client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)

async def retrieve_context(query: str, k: int = 3, threshold: float = 0.5) -> List[Dict[str, Any]]:
    """
    Retrieves relevant context from the Qdrant vector database based on a user query.
    This function serves as a tool for the OpenAI agent.

    Args:
        query: The user's query or a statement to retrieve context for.
        k: The number of top results to retrieve from Qdrant.
        threshold: The minimum score threshold for retrieved results.

    Returns:
        A list of dictionaries, where each dictionary represents a retrieved document
        with 'url', 'title', and 'text_snippet'.
    """
    if not query.strip():
        return []

    try:
        query_embedding = co.embed(
            texts=[query],
            model='embed-english-v3.0',
            input_type='search_query'
        ).embeddings[0]
    except Exception as e:
        print(f"Embedding failed: {e}")
        return []

    try:
        search_result = qdrant_client.query_points(
            collection_name="rag_emabadding", # Hardcoded collection name from test_retrieval.py
            query=query_embedding,
            limit=k,
            score_threshold=threshold,
            with_payload=True
        ).points
    except Exception as e:
        print(f"Qdrant query failed: {e}")
        return []

    results = []
    for hit in search_result:
        results.append({
            "score": hit.score, # Keeping score for potential future use or debugging
            "title": hit.payload.get("title", "N/A"),
            "url": hit.payload.get("source_url", "N/A"),
            "text_snippet": hit.payload.get("text", "")
        })
    
    return results
