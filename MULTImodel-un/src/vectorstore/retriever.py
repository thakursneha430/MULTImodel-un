"""
Retriever Module

Performs semantic search on stored document embeddings.
"""

from typing import List, Dict

from src.embeddings.embedding_model import EmbeddingModel
from src.vectorstore.chroma_store import ChromaStore


class Retriever:
    """
    Retrieves the most relevant document chunks.
    """

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_store = ChromaStore()

    def retrieve(
       self,
       query: str,
       top_k: int = 8):
        """
        Retrieve the most relevant chunks.

        Args:
            query: User query.
            top_k: Number of chunks to return.

        Returns:
            List of relevant chunks.
        """

        query_embedding = self.embedding_model.encode(query)

        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        retrieved_chunks = []

        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for chunk_id, document, metadata, distance in zip(
            ids,
            documents,
            metadatas,
            distances
        ):

            retrieved_chunks.append(
                {
                    "chunk_id": chunk_id,
                    "text": document,
                    "metadata": metadata,
                    "distance": distance
                }
            )

        return retrieved_chunks