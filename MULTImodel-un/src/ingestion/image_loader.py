from pathlib import Path
from uuid import uuid4
from PIL import Image

from src.ingestion.document_model import Document


class ImageLoader:
    """
    Loads image metadata.
    OCR will be added in a future version.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> Document:

        image = Image.open(self.file_path)

        metadata = {
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
            "format": image.format,
            "source": self.file_path.name,
        }

        return Document(
            document_id=str(uuid4()),
            file_name=self.file_path.name,
            file_type="image",
            content="",
            metadata=metadata,
        )