# 🚀 StartupPilotAI

**Your AI Co-Founder for Startup Success**

StartupPilotAI is an AI-powered platform that helps entrepreneurs understand startup-related documents using **Retrieval-Augmented Generation (RAG)** and **Google Gemini**.

Upload startup guides, legal agreements, funding schemes, and business documents — then ask questions in natural language and get accurate, context-aware answers grounded in your own documents.

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Demo / Screenshots](#-demo--screenshots)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Roadmap](#-roadmap)
- [Development Log](#-development-log)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Problem Statement

Entrepreneurs often struggle to understand startup policies, funding opportunities, legal documents, and compliance requirements because information is scattered across multiple lengthy documents.

**StartupPilotAI** solves this by letting users upload documents and receive intelligent, document-grounded answers — instead of manually digging through hundreds of pages.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Upload** | Upload startup-related documents directly into the platform |
| 🤖 **AI Question Answering** | Ask natural-language questions based on uploaded documents |
| 📝 **Document Summarization** | Generate concise summaries of long documents |
| ⚖️ **Legal Language Simplification** | Explain complex legal clauses in plain, simple language |
| 📊 **Startup Readiness Score** | Evaluate how prepared your startup is with an automated score |
| 💰 **Funding Recommendation** | Get suggestions on funding schemes suited to your startup |
| 🔍 **Missing Document Detection** | Identify required documents you haven't uploaded yet |
| 🗺️ **Startup Roadmap** | Generate a personalized roadmap based on your documents and stage |

---

## 🖼️ Demo / Screenshots

> Add screenshots or a demo GIF here once available.

```
assets/screenshots/
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI Framework | Streamlit |
| LLM | Google Gemini |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| PDF Parsing | PyMuPDF |
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

The full architecture write-up lives in [`docs/rag_architecture.md`](docs/rag_architecture.md).

---

## 📁 Project Structure

```
StartupPilotAI/
│
├── app.py                     # Streamlit entry point
├── requirements.txt           # Python dependencies
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   └── rag_architecture.md    # Detailed RAG architecture notes
│
├── data/
│   ├── raw/                   # Original uploaded documents
│   └── processed/             # Cleaned/chunked text
│
├── embeddings/                # Persisted vector embeddings
│
├── src/
│   ├── pdf_loader.py          # PDF text extraction (PyMuPDF)
│   ├── chunking.py            # Semantic document chunking
│   ├── embeddings.py          # Embedding generation
│   ├── vector_store.py        # ChromaDB integration
│   ├── retrieval.py           # Semantic search & retrieval
│   └── gemini_client.py       # Google Gemini API client
│
├── assets/
│   ├── logo.png
│   └── screenshots/
│
├── tests/
│   └── test_rag.py            # Unit tests for the RAG pipeline
│
├── uploads/
│   └── sample_pdfs/           # Sample documents for testing
│
└── venv/                      # Virtual environment (not committed)
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.9+
- A Google Gemini API key

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

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Run the app

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## 🚀 Usage

1. Launch the app with `streamlit run app.py`.
2. Upload one or more startup-related PDF documents.
3. Wait for the document to be processed, chunked, and embedded.
4. Ask questions in natural language, e.g.:
   - *"What funding schemes am I eligible for?"*
   - *"Summarize the compliance requirements in this document."*
   - *"Explain clause 4.2 in simple terms."*
5. Review AI-generated summaries, readiness scores, and roadmap suggestions.

---

## 🗺️ Roadmap

- [ ] Multi-document cross-referencing
- [ ] Support for DOCX and scanned/OCR PDFs
- [ ] User authentication and saved sessions
- [ ] Export reports (readiness score, roadmap) as PDF
- [ ] Deployment guide (Docker / Streamlit Cloud)

---

## 📅 Development Log

### Week 1

| Day | Progress |
|---|---|
| Day 1 | Implemented PDF loading pipeline using PyMuPDF |
| Day 2 | Built a document chunking module for semantic splitting |
| Day 3 | Generated embeddings using Sentence Transformers |
| Day 4 | Integrated ChromaDB for vector storage |
| Day 5 | Implemented semantic similarity search |
| Day 6 | Developed context retrieval functionality |
| Day 7 | Created a prompt builder for RAG prompts |


