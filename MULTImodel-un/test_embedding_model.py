from src.embeddings.embedding_model import EmbeddingModel


model = EmbeddingModel()

sample_text = """
Artificial Intelligence is transforming the future.
"""

embedding = model.encode(sample_text)

print("=" * 60)
print("EMBEDDING GENERATED")
print("=" * 60)

print("Vector Dimension:", len(embedding))

print()

print("First 10 Values:")

print(embedding[:10])