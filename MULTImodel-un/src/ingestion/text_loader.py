from pathlib import Path
import uuid

from src.ingestion.document_model import Document


class TextLoader:
    """
    Loads text documents and returns a standardized
    Document object.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> Document:
        """
        Load a text file and return a standardized Document object.
        """

        self._validate_file()

        document_id = str(uuid.uuid4())

        try:
            content = self.file_path.read_text(
                encoding="utf-8"
            )

        except UnicodeDecodeError:
            # Fallback for files that are not UTF-8 encoded
            content = self.file_path.read_text(
                encoding="latin-1"
            )

        content = content.strip()

        metadata = {
            "source": self.file_path.name,
            "file_path": str(self.file_path),
            "character_count": len(content),
            "word_count": len(content.split()),
            "line_count": len(content.splitlines()),
        }

        return Document(
            document_id=document_id,
            file_name=self.file_path.name,
            file_type="text",
            content=content,
            metadata=metadata,
        )

    def _validate_file(self) -> None:
        """
        Validate the text file before loading.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Text file not found: {self.file_path}"
            )

        if not self.file_path.is_file():
            raise ValueError(
                f"Path is not a valid file: {self.file_path}"
            )

        if self.file_path.suffix.lower() != ".txt":
            raise ValueError(
                f"Unsupported file type: "
                f"{self.file_path.suffix}. "
                f"Expected a .txt file."
            )