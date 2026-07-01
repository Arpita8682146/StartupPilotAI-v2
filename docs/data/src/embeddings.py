from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)


def generate_embeddings(chunks):

    embeddings = model.encode(
        chunks
    )

    return embeddings


sample_chunks = [

"Startup India supports innovation.",

"Funding schemes help entrepreneurs."

]

vectors = generate_embeddings(
    sample_chunks
)

print(vectors.shape)