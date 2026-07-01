import chromadb

client = chromadb.Client()

collection = client.create_collection(
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


def search(query_embedding):

    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=2

    )

    return results