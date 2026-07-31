"""
Embedding Utilities

Helper functions for working with embedding vectors.
"""

from typing import List
import math


class EmbeddingUtils:
    """
    Utility methods for embedding vectors.
    """

    @staticmethod
    def cosine_similarity(
        vector1: List[float],
        vector2: List[float]
    ) -> float:
        """
        Compute cosine similarity between two vectors.
        """

        dot_product = sum(a * b for a, b in zip(vector1, vector2))

        norm1 = math.sqrt(sum(a * a for a in vector1))
        norm2 = math.sqrt(sum(b * b for b in vector2))

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot_product / (norm1 * norm2)

    @staticmethod
    def vector_dimension(
        vector: List[float]
    ) -> int:
        """
        Return vector dimension.
        """

        return len(vector)

    @staticmethod
    def validate_dimension(
        vector1: List[float],
        vector2: List[float]
    ) -> bool:
        """
        Check whether vectors have the same dimension.
        """

        return len(vector1) == len(vector2)