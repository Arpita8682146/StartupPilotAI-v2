import chromadb


# Persistent database
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="startup_docs"
)


def store_embeddings(chunks, embeddings):

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