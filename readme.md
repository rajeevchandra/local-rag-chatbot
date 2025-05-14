
---

# 🤖 Local RAG Chatbot with Ollama, LangChain & Chroma

This project is a fully local AI chatbot that lets you ask questions about your own `.md` and `.pdf` documents using a Retrieval-Augmented Generation (RAG) workflow — all running on your laptop.

No cloud APIs. No GPUs. Just open-source tools and your CPU.

---

## 🔍 Features

- 📄 Upload Markdown or PDF files
- 🧠 Embed chunks locally with `nomic-embed-text` via Ollama
- 🔍 Store and search vectors with ChromaDB
- 💬 Ask natural questions using `mistral` or any local Ollama LLM
- 🧵 Chat-style interface with multi-turn memory
- ✅ Private, fast, and runs entirely offline

---

## 📦 Tech Stack

| Tool       | Role                                  |
|------------|----------------------------------------|
| Ollama     | Local LLMs (e.g., mistral) + embeddings |
| LangChain  | Prompt orchestration + memory          |
| ChromaDB   | Local vector store                     |
| Streamlit  | Chatbot UI                             |
| Python     | Backend logic                          |

---

## 🧠 How It Works

1. **Upload** `.md` or `.pdf` documents via the Streamlit UI  
2. **Split** documents into chunks and embed them locally  
3. **Store** embeddings in ChromaDB  
4. **Ask** a question via chat  
5. **Retrieve** similar chunks and pass them to an LLM  
6. **Answer** is generated with context and shown with source snippets

---

## 🚀 Quickstart

```bash
# Clone the repo
git clone https://github.com/your-username/local-rag-chatbot.git
cd local-rag-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt
pip install "unstructured[pdf]" fpdf

# Start Ollama model
ollama run mistral

# Launch the Streamlit chatbot UI
streamlit run ui.py



---

## 🧪 Example Prompts

> "What is a microservice?"  
> "What are DevOps best practices?"  
> "How do Kubernetes pods transition between states?"  
> "Give me a sample Docker Compose file."

---

## 💻 Local Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your-username/local-rag-chatbot.git
cd local-rag-chatbot

# 2. Install dependencies
pip install -r requirements.txt
pip install "unstructured[pdf]" fpdf

# 3. Start LLM with Ollama
ollama run mistral

# 4. Launch the chatbot UI
streamlit run ui.py
