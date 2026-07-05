from pdf_loader import load_pdf
from chunking import split_text
from embeddings import embed_chunks
from vectorstore import store_embeddings


def process_pdf(uploaded_file):

    text = load_pdf(uploaded_file)

    print("TEXT LENGTH:", len(text))

    if len(text.strip()) == 0:
        raise Exception(
            "No text extracted from PDF"
        )

    chunks = split_text(text)

    print("CHUNKS:", len(chunks))

    if len(chunks) == 0:
        raise Exception(
            "No chunks created"
        )

    embeddings = embed_chunks(chunks)

    print("EMBEDDINGS:", len(embeddings))

    if len(embeddings) == 0:
        raise Exception(
            "Embeddings are empty"
        )

    store_embeddings(
        chunks,
        embeddings
    )

    print("PDF processed successfully")

    return True
