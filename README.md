# 🚀 StartupPilotAI

**Your AI Co-Founder for Startup Success**

StartupPilotAI is an AI-powered platform that helps entrepreneurs understand startup-related documents using Retrieval-Augmented Generation (RAG) and Google Gemini.

Upload startup guides, legal agreements, funding schemes, and business documents — then ask questions in natural language and get accurate, context-aware answers grounded in your own documents.



---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#️-tech-stack)
- [Architecture](#️-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#️-getting-started)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Roadmap](#️-roadmap)
- [Development Log](#-development-log)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Problem Statement

Entrepreneurs often struggle to understand startup policies, funding opportunities, legal documents, and compliance requirements because information is scattered across multiple lengthy documents.

StartupPilotAI solves this by letting users upload documents and receive intelligent, document-grounded answers — instead of manually digging through hundreds of pages.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 PDF Upload | Upload startup-related documents directly into the platform |
| 🤖 AI Question Answering | Ask natural-language questions based on uploaded documents |
| 🔍 Cited Answers | Every answer links back to the exact source document, page, and similarity score |
| 💬 Conversational Chat | Multi-turn chat with history-aware context for follow-up questions |
| 📝 Document Summarization | Generate concise summaries of long documents |
| ⚖️ Legal Language Simplifier | Explain complex legal clauses and contract terms in plain language |
| 📊 Startup Readiness Assessment | Evaluate how prepared your startup is with an automated readiness score |
| 💰 Funding Recommendation | Get funding scheme suggestions matched to your stage, industry, and target amount |
| 🗺️ Personalized Roadmap | Generate a milestone-based launch roadmap from your goals and documents |
| 📈 Analytics Dashboard | Visualize indexed documents, chunk counts, and word-count stats |
| 🔐 Bring Your Own API Key | Optionally supply your own Gemini API key from the sidebar |
| ☁️ Cloud Deployed | Live and publicly accessible via Streamlit Community Cloud |

---

## 🖼️ Demo

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI Framework | Streamlit |
| LLM | Google Gemini |
| Vector Database | ChromaDB |
| Embeddings | Google Gemini Embedding API |
| PDF Parsing | PyMuPDF |
| Containerization | Docker |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

## 🏗️ Architecture

```
                          User
                           │
                           ▼
              Streamlit Interface
        Upload • Search • Ask • Analyze
                           │
                           ▼
                StartupPilotAI Engine
                           │
          ┌────────────────┴────────────────┐
          │                                  │
          ▼                                  ▼
  Document Processing               Query Processing
      PDF Upload                       User Query
          │                                  │
          ▼                                  ▼
       PyMuPDF                     Semantic Search
          │                                  │
          ▼                                  ▼
      Chunking                    ChromaDB Retrieval
          │                                  │
          ▼                                  ▼
     Embeddings                   Relevant Context
          │                                  │
          └────────────────┬─────────────────┘
                            ▼
                     Prompt Builder
                            │
                            ▼
                     Google Gemini
                            │
                            ▼
             AI Startup Recommendations
       Funding • Legal • Compliance • Registration
                    Personalized Roadmaps
```

The full architecture write-up lives in `docs/rag_architecture.md`.

---

## 📁 Project Structure

```
StartupPilotAI/
│
├── Dockerfile                 # Container build definition
├── .dockerignore
├── requirements.txt           # Python dependencies
├── README.md
├── LICENSE
├── .gitignore
├── .env                       # Local secrets (not committed)
│
├── docs/
│   ├── rag_architecture.md    # Detailed RAG architecture notes
│   └── data/
│       └── src/
│           ├── app.py             # Streamlit entry point
│           ├── pdf_loader.py      # PDF text extraction (PyMuPDF)
│           ├── chunking.py        # Semantic document chunking
│           ├── embeddings.py      # Embedding generation (Gemini API)
│           ├── vectorstore.py     # ChromaDB integration
│           ├── retriever.py       # Semantic search & retrieval
│           ├── gemini_client.py   # Google Gemini API client
│           ├── advisor.py         # Readiness, funding, roadmap, legal tools
│           └── prompt_builder.py  # RAG prompt construction
│
├── chroma_db/                 # Persisted vector embeddings
│
└── venv/                      # Virtual environment (not committed)
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API key
- Docker (optional, for containerized deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/StartupPilotAI.git
cd StartupPilotAI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```




## 🗺️ Roadmap

- [ ] Multi-document cross-referencing
- [ ] Support for DOCX and scanned/OCR PDFs
- [ ] User authentication and saved sessions
- [ ] Export reports (readiness score, roadmap) as PDF
- [ ] Persistent volume for vector store data in production

---

## 📅 Development Log

## 📅 Week 1 — Foundation & Document Ingestion

- Set up project structure and Python environment (venv, `requirements.txt`).
- Implemented `pdf_loader.py` using PyMuPDF to extract text from uploaded PDFs.
- Built `chunking.py` to split extracted text into overlapping chunks for better context retention.
- Created initial Streamlit UI (`app.py`) for file upload and basic layout.
- Set up Git repository and initial commit structure.

**Outcome:** Working PDF upload and text extraction pipeline with a basic UI shell.

## 📅 Week 2 — RAG Pipeline & AI Integration

- Built `embeddings.py` to generate vector embeddings from text chunks using Gemini.
- Set up `vectorstore.py` with ChromaDB for storing and querying embeddings.
- Implemented `retriever.py` for top-k similarity search on user queries.
- Built `prompt_builder.py` to construct grounded prompts from retrieved context.
- Integrated `gemini_client.py` to connect with the Gemini API for response generation.
- Added `advisor.py` to reframe LLM output into founder-friendly advice.
- Connected all components into `rag_pipeline.py` for end-to-end query handling.

**Outcome:** Fully functional local RAG pipeline — upload a document, ask a question, get a grounded answer.


## 📅 Week 3 — Deployment & Testing

- Wrote `Dockerfile` to containerize the app (Streamlit, ChromaDB, PyMuPDF, Gemini SDK).
- Configured `.streamlit/config.toml` and moved API keys to environment variables via `python-dotenv`.
- Deployed to Streamlit Community Cloud with auto-deploy from GitHub `main`.
- Added unit tests for PDF loading, chunking, retrieval, prompt building, and vector store.
- Fixed PDF parsing edge cases and chunk-overlap bugs affecting retrieval accuracy.
- Finalized `requirements.txt` with pinned dependency versions.

**Outcome:** App live on a public URL, containerized, with core RAG pipeline test coverage.

## 📅 Week 4 — Polish, Documentation & Final Review

- Refined Streamlit UI: improved layout, page config, and sidebar UX.
- Revised and expanded `README.md` for clarity and visual appeal.
- Reviewed and cleaned up code across all modules for consistency.
- Removed unused files and dependencies to streamline the project.
- Conducted end-to-end manual testing across multiple document types (pitch decks, term sheets, reports).
- Verified deployment stability and fixed minor UI/UX bugs on the live app.
- Added MIT License and finalized project documentation.

**Outcome:** Production-ready, publicly deployed StartupPilotAI with polished UI, clean codebase, and complete documentation.
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
