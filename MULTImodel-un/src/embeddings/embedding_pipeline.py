"""
Embedding Pipeline

This module generates embeddings for processed text chunks.
"""

from typing import Dict, List

from src.embeddings.embedding_model import EmbeddingModel


class EmbeddingPipeline:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self):

        self.embedding_model = EmbeddingModel()

    def process(
        self,
        chunks: List[Dict]
    ) -> List[Dict]:
        """
        Generate embeddings for all chunks.

        Args:
            chunks: List of chunk dictionaries.

        Returns:
            List of chunks with embeddings.
        """

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.embedding_model.batch_encode(
            texts
        )

        embedded_chunks = []

        for chunk, embedding in zip(chunks, embeddings):

            embedded_chunks.append(
                {
                    "chunk_id": chunk["chunk_id"],
                    "chunk_index": chunk["chunk_index"],
                    "text": chunk["text"],
                    "embedding": embedding,
                    "metadata": {
                        "start": chunk["start"],
                        "end": chunk["end"],
                        "length": chunk["length"]
                    }
                }
            )

        return embedded_chunks