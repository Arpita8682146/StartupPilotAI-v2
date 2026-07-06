from embeddings import embed_chunks
from vectorstore import search

def retrieve_context_with_citations(query, n_results=4):
    """
    Retrieves relevant text chunks matching the query along with metadata.
    Args:
        query: User query string
        n_results: Number of chunks to retrieve
    Returns:
        tuple: (context_string, list_of_citations)
               list_of_citations: [{'text': str, 'source': str, 'page': int, 'score': float}]
    """
    # Embed the query
    query_embeddings = embed_chunks([query])
    if len(query_embeddings) == 0:
        return "", []
        
    query_embedding = query_embeddings[0]
    
    # Search in vector store
    results = search(query_embedding, n_results=n_results)
    
    citations = []
    context_parts = []
    
    for idx, res in enumerate(results):
        text = res["text"]
        metadata = res["metadata"]
        source = metadata.get("source", "Unknown Document")
        page = metadata.get("page", 1)
        distance = res["distance"]
        
        # Convert distance to a rough similarity score (Chroma distance is L2/cosine-like depending on setup)
        score = max(0.0, 1.0 - distance)
        
        # Format citation dictionary
        citations.append({
            "text": text,
            "source": source,
            "page": page,
            "score": score
        })
        
        # Build clean context block for Gemini
        context_parts.append(
            f"--- Snippet {idx+1} [Source: {source}, Page: {page}] ---\n{text}"
        )
        
    context_string = "\n\n".join(context_parts)
    return context_string, citations

def retrieve_context(query):
    """
    Backward-compatible single-return context retrieval.
    """
    context_str, _ = retrieve_context_with_citations(query)
    return context_str
