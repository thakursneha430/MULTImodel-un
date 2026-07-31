from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = "What is Machine Learning?"

answer = rag.ask(question)

print("=" * 70)
print("QUESTION")
print("=" * 70)

print(question)

print()

print("=" * 70)
print("ANSWER")
print("=" * 70)

print(answer)