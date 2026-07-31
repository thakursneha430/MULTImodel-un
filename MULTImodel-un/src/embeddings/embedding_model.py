"""
Embedding Model

Loads a SentenceTransformer model and generates
dense vector embeddings for document chunks.
"""

from typing import List

from sentence_transformers import SentenceTransformer

from src.config.embedding_config import EmbeddingConfig


class EmbeddingModel:
    """
    Handles embedding generation using SentenceTransformers.
    """

    def __init__(self):

        self.config = EmbeddingConfig()

        print(f"Loading embedding model: {self.config.MODEL_NAME}")

        self.model = SentenceTransformer(
            self.config.MODEL_NAME,
            device=self.config.DEVICE
        )

        self.model.max_seq_length = (
            self.config.MAX_SEQUENCE_LENGTH
        )

        print("Embedding model loaded successfully.")

    def encode(
        self,
        text: str
    ) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Input text.

        Returns:
            Embedding vector.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=self.config.NORMALIZE_EMBEDDINGS,
            convert_to_numpy=True,
        )

        return embedding.tolist()

    def batch_encode(
        self,
        texts: List[str]
    ) -> List[List[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of input texts.

        Returns:
            List of embedding vectors.
        """

        embeddings = self.model.encode(
            texts,
            batch_size=self.config.BATCH_SIZE,
            normalize_embeddings=self.config.NORMALIZE_EMBEDDINGS,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings.tolist()