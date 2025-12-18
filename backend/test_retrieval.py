import os
import time
import cohere
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, Range
from typing import List, Dict, Any

def perform_search(co_client: cohere.Client, qdrant_client: QdrantClient, collection_name: str,
                   query: str, k: int = 3, threshold: float = 0.5):
    start_time = time.time()
    
    if not query.strip(): # Check for empty or whitespace-only queries
        return {"error": "Query cannot be empty.", "latency": 0}

    # 1. Embed the query
    try:
        query_embedding = co_client.embed(
            texts=[query],
            model='embed-english-v3.0',
            input_type='search_query'
        ).embeddings[0]
    except Exception as e:
        return {"error": f"Embedding failed: {e}", "latency": 0}

    # 2. Query Qdrant
    try:
        # Use score_threshold directly in the query_points method
        search_result = qdrant_client.query_points(
            collection_name=collection_name,
            query=query_embedding,
            limit=k,
            score_threshold=threshold,  # Apply threshold here
            with_payload=True
        ).points
    except Exception as e:
        return {"error": f"Qdrant query failed: {e}", "latency": 0}

    latency = time.time() - start_time

    # 3. Format Results
    results = []
    for hit in search_result:
        results.append({
            "score": hit.score,
            "title": hit.payload.get("title", "N/A"),
            "url": hit.payload.get("source_url", "N/A"),
            "text_snippet": hit.payload.get("text", "")[:200]
        })
    
    return {
        "query": query,
        "results": results,
        "latency": latency,
        "filtered_count": len(results)
    }

def main():
    print("Initializing RAG Pipeline Validation...")
    
    # Load environment variables
    load_dotenv()
    
    # T003: Implement environment variable loading
    cohere_api_key = os.environ.get("COHERE_API_KEY")
    qdrant_url = os.environ.get("QDRANT_URL")
    qdrant_api_key = os.environ.get("QDRANT_API_KEY")
    key = os.getenv("OPENAI_API_KEY")

    if not all([cohere_api_key, qdrant_url, qdrant_api_key]):
        print("Error: Missing one or more required environment variables: COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY")
        return

    print("Environment variables loaded successfully.")
    
    # T004: Implement Cohere and Qdrant client initialization and error handling
    try:
        co = cohere.Client(cohere_api_key)
        qdrant_client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
        print("Clients initialized successfully.")
    except Exception as e:
        print(f"Client initialization failed: {e}")
        return

    collection_name = "rag_emabadding"
    
    # T008: Add a predefined set of relevant test queries
    test_queries = [
        "ROS 2 architecture nodes and topics",       # Core technical concept
        "How to simulate sensors in Gazebo?",          # Specific tool usage
        "Reinforcement learning for humanoid walking", # Advanced topic
        "NVIDIA Isaac Sim features",                   # Specific technology
        "",                                            # T014: Edge case: Empty query
        "asdfghjkl",                                   # T014: Edge case: Nonsense query
        "How to bake a chocolate cake",                # T011: Irrelevant query
        "Explain the VLA module data model"            # Specific project topic
    ]

    print(f"\nRunning {len(test_queries)} test queries against collection '{collection_name}'...\n")
    print("="*60)

    for query in test_queries:
        print(f"Query: '{query}'")
        # T010: Use configurable similarity threshold
        # T005, T006, T007, T009 are part of perform_search
        result = perform_search(co, qdrant_client, collection_name, query, k=3, threshold=0.55) 
        
        if "error" in result:
            print(f"  FAILED: {result['error']}")
        else:
            print(f"  Latency: {result['latency']:.4f}s")
            print(f"  Matches Found (Score >= 0.55): {result['filtered_count']}")
            
            if result['filtered_count'] == 0:
                print("  -> No relevant results found above threshold.")
            
            for i, hit in enumerate(result['results']):
                # T012 & T013: Ensure source_url and title are extracted and displayed
                print(f"    {i+1}. [{hit['score']:.4f}] {hit['title']}")
                print(f"       URL: {hit['url']}")
                print(f"       Snippet: {hit['text_snippet']}...")
        
        print("-" * 60)

if __name__ == "__main__":
    main()