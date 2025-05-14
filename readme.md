
---

## 🔍 Key Features (Detailed)

### ✅ Upload `.md` or `.pdf` Files  
Just drag and drop them — no preprocessing needed. Both structured (`.md`) and unstructured (`.pdf`) formats are supported.

### ✅ Auto Re-index with `nomic-embed-text`  
New files are split into chunks and embedded locally using Ollama. No cloud embeddings, no API keys.

### ✅ Ask Natural Questions to `mistral`  
The chatbot uses a local LLM (`mistral` or any other Ollama-supported model) to answer contextually grounded questions.

### ✅ Multi-turn Chat with Memory  
It remembers previous questions and builds on them using LangChain's session memory.

### ✅ Source Highlighting for Every Answer  
Each response includes the document name and a snippet for transparency.

### ✅ All on CPU  
Everything runs locally on CPU — perfect for offline setups or private environments.

---

## 🧠 How It Works — Step-by-Step

1. **Upload documents** via Streamlit UI  
2. **Split into chunks & embed** using `nomic-embed-text` (via Ollama)  
3. **Store vectors** in local ChromaDB  
4. **On user question**, retrieve relevant chunks  
5. **Pass context into `mistral`** for answer generation  
6. **Show answer + sources** in a clean, chat-style interface

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
