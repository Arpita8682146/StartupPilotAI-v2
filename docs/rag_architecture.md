# RAG Architecture

## StartupPilotAI Pipeline

PDF Documents
↓
PyMuPDF
↓
Text Extraction
↓
Chunking
↓
Sentence Embeddings
↓
ChromaDB
↓
Retriever
↓
Google Gemini
↓
Context-Aware Answer

---

## Workflow

1. User uploads startup documents.
2. PyMuPDF extracts text.
3. Documents are split into chunks.
4. Sentence Transformers generate embeddings.
5. Embeddings are stored in ChromaDB.
6. Relevant chunks are retrieved.
7. Gemini receives retrieved context.
8. Gemini generates grounded responses.

---

## Technologies Used

- PyMuPDF
- Sentence Transformers
- ChromaDB
- Google Gemini
- Streamlit