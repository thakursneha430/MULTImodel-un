"""
Embedding Configuration
"""

from dataclasses import dataclass


@dataclass
class EmbeddingConfig:
    """
    Configuration for embedding generation.
    """

    MODEL_NAME: str = "BAAI/bge-small-en-v1.5"

    DEVICE: str = "cpu"

    BATCH_SIZE: int = 32

    NORMALIZE_EMBEDDINGS: bool = True

    MAX_SEQUENCE_LENGTH: int = 512