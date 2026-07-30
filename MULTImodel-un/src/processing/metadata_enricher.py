"""
Metadata Enrichment Module

Generates useful metadata for processed documents.
"""

import re
from typing import Dict


class MetadataEnricher:
    """
    Generates document metadata.
    """

    def __init__(self):
        pass

    def enrich(self, text: str) -> Dict:
        """
        Generate metadata from text.

        Args:
            text: Cleaned document text.

        Returns:
            Dictionary containing metadata.
        """

        words = re.findall(r"\b\w+\b", text)

        word_count = len(words)

        character_count = len(text)

        line_count = len(text.splitlines())

        paragraph_count = len(
            [
                p
                for p in text.split("\n\n")
                if p.strip()
            ]
        )

        reading_time = max(
            1,
            round(word_count / 200)
        )

        return {
            "word_count": word_count,
            "character_count": character_count,
            "line_count": line_count,
            "paragraph_count": paragraph_count,
            "reading_time_minutes": reading_time,
        }