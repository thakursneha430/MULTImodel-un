from pathlib import Path
from typing import List
import uuid

import fitz

from src.ingestion.document_model import Document


class PDFLoader:
    """
    Loads PDF documents and extracts text page by page.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> Document:
        """
        Load the PDF and return a standardized Document object.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"PDF file not found: {self.file_path}"
            )

        if self.file_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Expected a PDF file, got: "
                f"{self.file_path.suffix}"
            )

        document_id = str(uuid.uuid4())

        pdf_document = fitz.open(self.file_path)

        pages = []
        full_text = []

        for page_number, page in enumerate(pdf_document, start=1):

            page_text = page.get_text("text").strip()

            page_data = {
                "page_number": page_number,
                "text": page_text,
            }

            pages.append(page_data)

            if page_text:
                full_text.append(
                    f"[Page {page_number}]\n{page_text}"
                )

        page_count = len(pdf_document)

        pdf_document.close()

        content = "\n\n".join(full_text)

        metadata = {
            "page_count": page_count,
            "source": self.file_path.name,
            "file_path": str(self.file_path),
            "pages": pages,
        }

        return Document(
            document_id=document_id,
            file_name=self.file_path.name,
            file_type="pdf",
            content=content,
            metadata=metadata,
        )