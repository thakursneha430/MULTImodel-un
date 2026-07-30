from src.processing.text_chunker import TextChunker


sample_text = (
    "Artificial Intelligence is transforming industries. "
    * 100
)

chunker = TextChunker(
    chunk_size=300,
    chunk_overlap=50
)

chunks = chunker.chunk_text(
    sample_text
)

print("=" * 60)
print("TOTAL CHUNKS:", len(chunks))
print("=" * 60)

for chunk in chunks:

    print(f"\nChunk {chunk['chunk_index']}")

    print("-" * 40)

    print(chunk["text"][:120])

    print()

    print("Length:", chunk["length"])