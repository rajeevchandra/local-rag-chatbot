from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainFilter

def get_rag_chain():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(
        persist_directory="./db",
        embedding_function=embeddings,
        collection_name="rag_docs"
    )
    retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 5})

    llm = OllamaLLM(model="mistral")

    prompt = PromptTemplate(
        template="""
        You are an expert software engineer. Use the following context to answer the user's question.
        Only use factual information. If not found, say "I don't know".

        Context:
        {context}

        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    compressor = LLMChainFilter.from_llm(llm=llm)
    retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain