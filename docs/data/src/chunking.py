import re
def split_text(pages_data, chunk_size=800, chunk_overlap=150):
    """
    Splits text from pages into overlapping chunks, maintaining metadata.
    Args:
        pages_data: List of dicts with keys 'text', 'page', 'source'
        chunk_size: Target size of each chunk in characters
        chunk_overlap: Overlap between consecutive chunks in characters
    Returns:
        List of dicts: [{'text': str, 'page': int, 'source': str, 'chunk_idx': int}]
    """
    all_chunks = []
    
    for page_data in pages_data:
        text = page_data["text"]
        page_num = page_data["page"]
        source = page_data["source"]
        
        start = 0
        chunk_idx = 0
        
        while start < len(text):
            end = start + chunk_size
            
            # Find a boundary to split on, searching back within overlap
            if end < len(text):
                search_area = text[max(start, end - 150):end]
                boundary = re.search(r'[\s\n\.]', search_area[::-1])
                if boundary:
                    end = end - boundary.start()
            
            chunk_text = text[start:end].strip()
            
            if chunk_text:
                all_chunks.append({
                    "text": chunk_text,
                    "page": page_num,
                    "source": source,
                    "chunk_idx": chunk_idx
                })
                chunk_idx += 1
                
            start = end - chunk_overlap
            if start >= len(text) or chunk_overlap <= 0 or end >= len(text):
                break
                
    return all_chunks
from sentence_transformers import SentenceTransformer
# Lazy load model
model = None
def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model
def embed_chunks(chunks):
    """
    Generates embeddings for chunks using sentence-transformers.
    Args:
        chunks: List of chunk dictionaries or strings.
    Returns:
        numpy.ndarray: Embedding vectors.
    """
    if not chunks:
        return []
    
    # Extract text if they are dict objects
    if isinstance(chunks[0], dict):
        texts = [chunk["text"] for chunk in chunks]
    else:
        texts = chunks
        
    transformer_model = get_model()
    embeddings = transformer_model.encode(
        texts,
        convert_to_tensor=False,
        show_progress_bar=False
    )
    return embeddings
