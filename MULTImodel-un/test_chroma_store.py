from src.processing.processing_pipeline import ProcessingPipeline
from src.embeddings.embedding_pipeline import EmbeddingPipeline
from src.vectorstore.chroma_store import ChromaStore


sample_text = """
Artificial Intelligence is changing the world.

Machine Learning enables computers to learn from data.

Deep Learning is a subset of Machine Learning.

Large Language Models are transforming NLP.
""" * 40


print("=" * 60)
print("PROCESSING DOCUMENT")
print("=" * 60)

processing_pipeline = ProcessingPipeline()
processed = processing_pipeline.process(sample_text)


print("=" * 60)
print("GENERATING EMBEDDINGS")
print("=" * 60)

embedding_pipeline = EmbeddingPipeline()
embedded_chunks = embedding_pipeline.process(processed["chunks"])


print("=" * 60)
print("STORING IN CHROMADB")
print("=" * 60)

vector_store = ChromaStore()

vector_store.add_documents(embedded_chunks)

print()

print("Total Stored Chunks:")

print(vector_store.count())