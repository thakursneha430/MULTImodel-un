from pathlib import Path
from typing import Dict
import uuid

from PIL import Image

from src.ingestion.document_model import Document


class ImageLoader:
    """
    Loads image documents and returns a standardized
    Document object.
    """

    SUPPORTED_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> Document:
        """
        Load an image and return a standardized Document object.
        """

        self._validate_file()

        document_id = str(uuid.uuid4())

        with Image.open(self.file_path) as image:

            metadata: Dict = {
                "source": self.file_path.name,
                "file_path": str(self.file_path),
                "image_format": image.format,
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
            }

        return Document(
            document_id=document_id,
            file_name=self.file_path.name,
            file_type="image",
            content=None,
            metadata=metadata,
        )

    def _validate_file(self) -> None:
        """
        Validate the image file before loading.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Image file not found: {self.file_path}"
            )

        if not self.file_path.is_file():
            raise ValueError(
                f"Path is not a valid file: {self.file_path}"
            )

        if self.file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported image format: "
                f"{self.file_path.suffix}"
            )

        try:
            with Image.open(self.file_path) as image:
                image.verify()

        except Exception as e:
            raise ValueError(
                f"Invalid or corrupted image file: "
                f"{self.file_path}"
            ) from e