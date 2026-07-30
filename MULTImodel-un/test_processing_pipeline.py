from src.processing.processing_pipeline import (
    ProcessingPipeline
)

sample_text = """

Artificial Intelligence is changing the world.


Machine Learning enables computers
to learn from data.


Deep Learning is a subset of Machine Learning.


""" * 30

pipeline = ProcessingPipeline()

result = pipeline.process(sample_text)

print("=" * 60)
print("DOCUMENT METADATA")
print("=" * 60)

print(result["metadata"])

print("\n")

print("=" * 60)
print("TOTAL CHUNKS")
print("=" * 60)

print(len(result["chunks"]))

print("\n")

print("=" * 60)
print("FIRST CHUNK")
print("=" * 60)

print(result["chunks"][0]["text"])