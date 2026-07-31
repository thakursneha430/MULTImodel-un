from src.processing.processing_pipeline import ProcessingPipeline
from src.embeddings.embedding_pipeline import EmbeddingPipeline


sample_text = """
Artificial Intelligence is changing the world.

Machine Learning enables computers to learn from data.

Deep Learning is a subset of Machine Learning.

Large Language Models are transforming NLP.
""" * 40


processing_pipeline = ProcessingPipeline()

processed = processing_pipeline.process(
    sample_text
)

embedding_pipeline = EmbeddingPipeline()

embedded_chunks = embedding_pipeline.process(
    processed["chunks"]
)

print("=" * 60)
print("TOTAL CHUNKS")
print("=" * 60)

print(len(embedded_chunks))

print()

print("=" * 60)
print("FIRST EMBEDDED CHUNK")
print("=" * 60)

first = embedded_chunks[0]

print("Chunk ID :", first["chunk_id"])

print("Chunk Index :", first["chunk_index"])

print("Text Length :", len(first["text"]))

print("Embedding Dimension :", len(first["embedding"]))

print()

print("First 10 Embedding Values:")

print(first["embedding"][:10])