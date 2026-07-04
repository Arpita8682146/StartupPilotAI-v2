# StartupPilotAI

## Your AI Co-Founder for Startup Success

StartupPilotAI is an AI-powered platform that helps entrepreneurs understand startup-related documents using Retrieval-Augmented Generation (RAG) and Google Gemini.

Users can upload startup guides, legal agreements, funding schemes, and business documents, then ask questions in natural language. The system retrieves relevant information from the uploaded documents and generates accurate, context-aware answers.

---

## Problem Statement

Entrepreneurs often struggle to understand startup policies, funding opportunities, legal documents, and compliance requirements because the information is spread across multiple lengthy documents.

StartupPilotAI simplifies this process by allowing users to upload documents and receive intelligent, document-based answers instead of manually searching through hundreds of pages.

---

## Features

| Feature | Description |
|---------|-------------|
| PDF Upload | Upload startup-related documents |
| AI Question Answering | Ask questions based on uploaded documents |
| Document Summarization | Generate concise summaries |
| Legal Language Simplification | Explain legal clauses in simple language |
| Startup Readiness Score | Evaluate startup preparedness |
| Funding Recommendation | Suggest suitable funding schemes |
| Missing Document Detection | Identify required documents |
| Startup Roadmap | Generate a personalized roadmap |

---

## Technology Stack

- Python
- Streamlit
- Google Gemini
- ChromaDB
- Sentence Transformers
- PyMuPDF
- Git and GitHub

---

## Architecture

```text
                    User
                      │
                      ▼
         Streamlit Interface
    Upload • Search • Ask • Analyze
                      │
                      ▼
            StartupPilotAI Engine
                      │
      ┌───────────────┴──────────────┐
      │                              │
      ▼                              ▼

Document Processing          Query Processing

PDF Upload                   User Query
     │                           │
     ▼                           ▼

PyMuPDF                 Semantic Search
     │                           │
     ▼                           ▼

Chunking                ChromaDB Retrieval
     │                           │
     ▼                           ▼

Embeddings             Relevant Context
     │                           │
     └──────────────┬────────────┘
                    ▼

              Prompt Builder
                    │
                    ▼

              Google Gemini
                    │
                    ▼

        AI Startup Recommendations

      Funding • Legal • Compliance
      Registration • Roadmaps
      Personalized Guidance
```

## Project Structure

```text
StartupPilotAI/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   └── rag_architecture.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── embeddings/
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   └── gemini_client.py
│
├── assets/
│   ├── logo.png
│   └── screenshots/
│
├── tests/
│   └── test_rag.py
│
├── uploads/
│   └── sample_pdfs/
│
└── venv/

```
Week 1:
## Internship Progress

- Day 1: Implemented PDF loading pipeline using PyMuPDF.
- Day 2: Built a document chunking module for semantic splitting.
- Day 3: Generated embeddings using Sentence Transformers.
- Day 4: Integrated ChromaDB for vector storage.
- Day 5: Implemented semantic similarity search.
- Day 6: Developed context retrieval functionality.
- Day 7: Created a prompt builder for RAG prompts.
