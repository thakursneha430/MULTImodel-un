"""
Text Cleaning Module

This module provides utilities for cleaning and normalizing
raw document text before chunking and embedding.
"""

import re
import unicodedata


class TextCleaner:
    """
    Cleans and normalizes document text.
    """

    def __init__(self):
        pass

    def clean(self, text: str) -> str:
        """
        Execute the complete text cleaning pipeline.

        Args:
            text: Raw extracted text.

        Returns:
            Cleaned text.
        """

        text = self.normalize_unicode(text)
        text = self.remove_extra_spaces(text)
        text = self.remove_extra_newlines(text)
        text = self.remove_tabs(text)
        text = self.strip_lines(text)

        return text.strip()

    def normalize_unicode(self, text: str) -> str:
        """
        Normalize unicode characters.
        """

        return unicodedata.normalize("NFKC", text)

    def remove_extra_spaces(self, text: str) -> str:
        """
        Replace multiple spaces with a single space.
        """

        return re.sub(r"[ ]{2,}", " ", text)

    def remove_extra_newlines(self, text: str) -> str:
        """
        Reduce multiple blank lines to one.
        """

        return re.sub(r"\n{3,}", "\n\n", text)

    def remove_tabs(self, text: str) -> str:
        """
        Replace tabs with spaces.
        """

        return text.replace("\t", " ")

    def strip_lines(self, text: str) -> str:
        """
        Remove leading/trailing whitespace from each line.
        """

        lines = [
            line.strip()
            for line in text.splitlines()
        ]

        return "\n".join(lines)