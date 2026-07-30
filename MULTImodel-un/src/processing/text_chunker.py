"""
Text Chunking Module

Splits cleaned text into overlapping chunks for
embedding generation and semantic retrieval.
"""

from typing import List
from uuid import uuid4


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100
    ):

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(
        self,
        text: str
    ) -> List[dict]:
        """
        Split text into overlapping chunks.

        Returns:
            List of chunk dictionaries.
        """

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:

            end = min(
                start + self.chunk_size,
                text_length
            )

            chunk = text[start:end].strip()

            if chunk:

                chunks.append(
                    {
                        "chunk_id": str(uuid4()),
                        "chunk_index": len(chunks),
                        "text": chunk,
                        "start": start,
                        "end": end,
                        "length": len(chunk),
                    }
                )

            start += (
                self.chunk_size
                - self.chunk_overlap
            )

        return chunks