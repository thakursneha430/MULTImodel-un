from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

print("=" * 60)
print("MULTI-TURN RAG CHAT")
print("=" * 60)
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    result = rag.ask(question)

    print("\nAssistant:")
    print(result["answer"])
    print("\n" + "-" * 60 + "\n")