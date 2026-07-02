from embeddings import generate_embeddings
from vectorstore import search


def retrieve_context(question):

    print("Question:", question)

    query_embedding = generate_embeddings(
        [question]
    )[0]

    print("Embedding generated")

    print("Searching database...")

    results = search(
        query_embedding
    )

    print("Search completed")

    print(results)

    docs = results["documents"][0]

    context = "\n".join(
        docs
    )
    

    return context