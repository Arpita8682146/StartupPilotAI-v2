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
