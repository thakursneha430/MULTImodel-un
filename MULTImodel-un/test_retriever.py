from src.vectorstore.retriever import Retriever


retriever = Retriever()

query = "What is Machine Learning?"

results = retriever.retrieve(
    query=query,
    top_k=3
)

print("=" * 70)
print("QUERY")
print("=" * 70)

print(query)

print()

print("=" * 70)
print("TOP RESULTS")
print("=" * 70)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 50)

    print("Distance :", result["distance"])

    print()

    print(result["text"][:300])

    print()