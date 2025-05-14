from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DocsChangeHandler(FileSystemEventHandler):
    def __init__(self, ingest_function):
        self.ingest_function = ingest_function

    def on_modified(self, event):
        if event.src_path.endswith(".md") or event.src_path.endswith(".pdf"):
            print(f"📄 Detected change in: {event.src_path}")
            self.ingest_function()

def ingest():
    loader = DirectoryLoader("./docs", glob="**/*.*", use_multithreading=True)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="./db")

    vectordb.persist()
    print("✅ Ingestion complete.")

if __name__ == "__main__":
    ingest()
    print("👀 Watching for changes in ./docs...")
    event_handler = DocsChangeHandler(ingest)
    observer = Observer()
    observer.schedule(event_handler, path="./docs", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()