import os
import re
import chromadb

# Resolve path to the root chroma_db folder dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
root_db_path = os.path.abspath(os.path.join(current_dir, "..", "chroma_db"))

# Persistent database client
client = chromadb.PersistentClient(
    path=root_db_path
)

collection = client.get_or_create_collection(
    name="startup_docs"
)

def store_embeddings(chunks, embeddings):
    """
    Stores text chunks and their embeddings into ChromaDB with unique IDs.
    Args:
        chunks: List of chunk dictionaries [{'text': str, 'page': int, 'source': str, 'chunk_idx': int}]
        embeddings: List or array of embeddings
    """
    if len(chunks) == 0:
        raise Exception("No chunks available to store.")

    if len(embeddings) == 0:
        raise Exception("No embeddings generated.")

    ids = []
    documents = []
    metadatas = []

    for idx, chunk in enumerate(chunks):
        source = chunk["source"]
        page = chunk["page"]
        c_idx = chunk["chunk_idx"]
        
        # Clean file name for standard ASCII ID
        clean_name = re.sub(r'[^a-zA-Z0-9_\-.]', '_', source)
        unique_id = f"{clean_name}_p{page}_c{c_idx}_{idx}"
        
        ids.append(unique_id)
        documents.append(chunk["text"])
        metadatas.append({
            "source": source,
            "page": page,
            "chunk_idx": c_idx
        })

    # Convert embeddings to list of lists if it's a numpy array
    if hasattr(embeddings, "tolist"):
        embeddings_list = embeddings.tolist()
    else:
        embeddings_list = list(embeddings)

    collection.add(
        documents=documents,
        embeddings=embeddings_list,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"Stored {len(chunks)} chunks in vector database.")

def search(query_embedding, n_results=4):
    """
    Queries ChromaDB with a query embedding.
    Returns:
        list: List of dicts containing text, metadata, and score
    """
    if collection.count() == 0:
        return []
        
    if hasattr(query_embedding, "tolist"):
        query_embedding_list = query_embedding.tolist()
    else:
        query_embedding_list = list(query_embedding)

    results = collection.query(
        query_embeddings=[query_embedding_list],
        n_results=min(n_results, collection.count())
    )

    formatted_results = []
    
    # Process results into flat list of dictionaries
    if results and "documents" in results and results["documents"]:
        docs = results["documents"][0]
        metas = results["metadatas"][0] if "metadatas" in results else [{} for _ in docs]
        distances = results["distances"][0] if "distances" in results else [0 for _ in docs]
        ids = results["ids"][0] if "ids" in results else ["" for _ in docs]
        
        for i in range(len(docs)):
            formatted_results.append({
                "id": ids[i],
                "text": docs[i],
                "metadata": metas[i],
                "distance": distances[i]
            })
            
    return formatted_results

def get_stats():
    """
    Returns database statistics such as total chunks and unique documents.
    """
    count = collection.count()
    if count == 0:
        return {
            "chunks": 0,
            "files": 0,
            "filenames": [],
            "file_counts": {}
        }
    
    # Get all metadata
    results = collection.get(include=["metadatas"])
    metadatas = results.get("metadatas", [])
    
    filenames = set()
    file_counts = {}
    for meta in metadatas:
        if meta and "source" in meta:
            source = meta["source"]
            filenames.add(source)
            file_counts[source] = file_counts.get(source, 0) + 1
            
    return {
        "chunks": count,
        "files": len(filenames),
        "filenames": list(filenames),
        "file_counts": file_counts
    }

def clear_db():
    """
    Deletes the current collection and recreates it to clear the database.
    """
    global client, collection
    try:
        client.delete_collection("startup_docs")
    except Exception:
        pass
    collection = client.get_or_create_collection(
        name="startup_docs"
    )
    print("Database cleared successfully.")
