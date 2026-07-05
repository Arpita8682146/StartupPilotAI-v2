import os
import chromadb

# Resolve path to the root chroma_db folder dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
root_db_path = os.path.abspath(os.path.join(current_dir, "..", "..", "..", "chroma_db"))

# Persistent database
client = chromadb.PersistentClient(
    path=root_db_path
)

collection = client.get_or_create_collection(
    name="startup_docs"
)


def store_embeddings(chunks, embeddings):

    if len(chunks) == 0:
        raise Exception("No chunks available")

    if len(embeddings) == 0:
        raise Exception("No embeddings generated")

    ids = [str(i) for i in range(len(chunks))]

    collection.add(

        documents=chunks,

        embeddings=embeddings.tolist(),

        ids=ids

    )

    print("Stored Successfully")

    print(
        "Total chunks in database:",
        collection.count()
    )


def search(query_embedding):

    print(
        "Chunks available:",
        collection.count()
    )

    results = collection.query(

        query_embeddings=[

            query_embedding.tolist()

        ],

        n_results=2

    )

    return results