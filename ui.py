import streamlit as st
from rag_pipeline import get_rag_chain
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
import os

st.set_page_config(page_title="Local RAG Q&A", page_icon="📘")

st.title("📘 Ask Your Docs (Local RAG with Ollama + LangChain)")

if "history" not in st.session_state:
    st.session_state.history = []

def reindex_docs():
    with st.spinner("Reading and splitting documents..."):
        loader = DirectoryLoader("./docs", glob="**/*.*", use_multithreading=True)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)

    with st.spinner(f"Embedding {len(chunks)} chunks..."):
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            collection_name="rag_docs",
            persist_directory="./db"
        )
    st.success(f"✅ Re-indexed {len(chunks)} chunks from uploaded documents.")

# File uploader
uploaded_files = st.file_uploader("📄 Upload Markdown or PDF files", type=["md", "pdf"], accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        save_path = os.path.join("docs", file.name)
        with open(save_path, "wb") as f:
            f.write(file.getvalue())
    st.success("Files uploaded.")
    reindex_docs()

# Question input
query = st.text_input("Ask a question:")

if query:
    rag = get_rag_chain()
    with st.spinner("Thinking..."):
        result = rag.invoke(query)

    st.session_state.history.append((query, result))

# Display session memory
for q, r in reversed(st.session_state.history):
    st.markdown(f"#### ❓ {q}")
    st.markdown(f"**📘 Answer:** {r['result']}")

    st.markdown("**📚 Sources:**")
    for doc in r['source_documents']:
        score = doc.metadata.get("score", "N/A")
        snippet = doc.page_content[:300]
        st.markdown(f"- `{doc.metadata.get('source', 'Unknown')}` (score: `{score}`)")
        st.code(snippet + "..." if len(snippet) > 300 else snippet)
    st.markdown("---")