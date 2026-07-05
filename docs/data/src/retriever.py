from embeddings import embed_chunks
from vectorstore import search


def retrieve_context(query):

    query_embedding = embed_chunks([query])[0]

    results = search(query_embedding)

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context