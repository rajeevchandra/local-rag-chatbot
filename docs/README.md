# 🤖 Local RAG Chatbot with Ollama, LangChain & ChromaDB

Ask questions about your **own Markdown and PDF documents** — 100% locally, with no cloud or API keys required.

Powered by:
- 🧠 [Ollama](https://ollama.com) (Mistral + nomic-embed-text)
- 🧱 [LangChain](https://www.langchain.com)
- 📦 [ChromaDB](https://www.trychroma.com)
- 💬 [Streamlit](https://streamlit.io)

---

## 📸 Demo

![Chatbot UI Screenshot](https://user-images.githubusercontent.com/placeholder/screenshot.png)

---

## 🔍 Features

✅ Upload `.md` and `.pdf` files  
✅ Automatic re-indexing on upload  
✅ RAG pipeline using local embeddings  
✅ Streamlit chatbot interface  
✅ Multi-turn memory (session context)  
✅ Source highlighting and content previews  
✅ Runs on CPU (no GPU required)

---

## 📦 Requirements

- Python 3.10+
- Ollama installed locally (https://ollama.com)
- Models pulled:  
  ```bash
  ollama run mistral
  ollama run nomic-embed-text


🔧 Installation

git clone https://github.com/yourname/local-rag-chatbot.git
cd local-rag-chatbot
pip install -r requirements.txt
pip install "unstructured[pdf]" fpdf

🚀 Run the App

ollama run mistral
streamlit run ui.py

Visit http://localhost:8501 in your browser.

📁 Folder Structure

📦 rag_ollama_advanced
├── ui.py                # Streamlit chatbot interface
├── ingest_docs.py       # Optional standalone ingestion script
├── ingest_docs_single_model.py
├── rag_pipeline.py      # Embeddings + retriever setup
├── requirements.txt
├── docs/                # Place your .md/.pdf files here
│   ├── api_design.md
│   ├── docker_compose.md
│   ├── devops_best_practices.pdf
│   └── ...
└── db/                  # ChromaDB persisted vector store


💡 How It Works (RAG Pipeline)
Load .md and .pdf files into LangChain

Split into chunks using RecursiveCharacterTextSplitter

Generate embeddings with Ollama’s nomic-embed-text

Store embeddings in ChromaDB (./db)

On query, retrieve similar chunks

Inject context into a prompt and send to mistral via Ollama

Display answer + source documents in Streamlit

💬 Example Prompts
"What is a microservice?"
"How does Kubernetes manage pod lifecycle?"
"Give me an example Docker Compose file."
"What are DevOps best practices?"

🔐 Private & Secure
No API keys

No cloud calls

All embeddings and LLM runs locally

Ideal for:

Internal developer docs

Security/compliance handbooks

Offline private AI assistants