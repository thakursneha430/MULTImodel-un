from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = input("Ask a question: ")

result = rag.ask(question)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])