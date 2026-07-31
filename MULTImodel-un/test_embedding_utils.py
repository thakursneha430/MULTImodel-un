from src.embeddings.embedding_model import EmbeddingModel
from src.embeddings.embedding_utils import EmbeddingUtils


model = EmbeddingModel()

text1 = "Artificial Intelligence is amazing."

text2 = "Machine Learning is a branch of AI."

embedding1 = model.encode(text1)
embedding2 = model.encode(text2)

print("=" * 60)
print("VECTOR DIMENSION")
print("=" * 60)

print(
    EmbeddingUtils.vector_dimension(
        embedding1
    )
)

print()

print("=" * 60)
print("COSINE SIMILARITY")
print("=" * 60)

print(
    EmbeddingUtils.cosine_similarity(
        embedding1,
        embedding2
    )
)