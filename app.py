from rag_pipeline import get_rag_chain

rag = get_rag_chain()

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    result = rag.invoke(query)

    print("\n📘 Answer:")
    print(result['result'])

    print("\n📚 Sources Used:")
    for doc in result['source_documents']:
        print(f"- {doc.metadata.get('source')}\n  Excerpt: {doc.page_content[:200]}...\n")