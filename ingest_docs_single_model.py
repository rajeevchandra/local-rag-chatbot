from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def ingest():
    loader = DirectoryLoader("./docs", glob="**/*.*", use_multithreading=True)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="rag_docs",
        persist_directory="./db"
    )
    print("✅ Indexing complete. You may now stop the embedding model and run app.py using your LLM.")

if __name__ == "__main__":
    ingest()