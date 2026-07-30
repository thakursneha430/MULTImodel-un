"""
Processing Pipeline

Clean
↓
Chunk
↓
Metadata
"""

from src.processing.text_cleaner import TextCleaner
from src.processing.text_chunker import TextChunker
from src.processing.metadata_enricher import MetadataEnricher


class ProcessingPipeline:

    def __init__(self):

        self.cleaner = TextCleaner()

        self.chunker = TextChunker(
            chunk_size=500,
            chunk_overlap=100
        )

        self.metadata = MetadataEnricher()

    def process(
        self,
        text: str
    ) -> dict:
        """
        Process a document.

        Returns:
            Dictionary containing cleaned text,
            chunks and metadata.
        """

        cleaned_text = self.cleaner.clean(text)

        chunks = self.chunker.chunk_text(
            cleaned_text
        )

        metadata = self.metadata.enrich(
            cleaned_text
        )

        return {
            "cleaned_text": cleaned_text,
            "chunks": chunks,
            "metadata": metadata,
        }