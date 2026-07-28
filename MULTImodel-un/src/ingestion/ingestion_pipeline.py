from pathlib import Path

from src.ingestion.document_model import Document
from src.ingestion.file_validator import FileValidator
from src.ingestion.document_router import DocumentRouter
from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.image_loader import ImageLoader
from src.ingestion.text_loader import TextLoader


class IngestionPipeline:
    """
    Main document ingestion pipeline.

    Responsible for:
    1. Validating the input file
    2. Identifying the document type
    3. Selecting the appropriate loader
    4. Loading the document
    5. Returning a standardized Document object
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def run(self) -> Document:
        """
        Execute the complete document ingestion pipeline.
        """

        # Step 1: Validate the file
        validator = FileValidator(
            str(self.file_path)
        )

        validator.validate()

        # Step 2: Identify document type
        router = DocumentRouter(
            str(self.file_path)
        )

        document_type = router.get_document_type()

        # Step 3: Select appropriate loader
        loader = self._get_loader(
            document_type
        )

        # Step 4: Load document
        document = loader.load()

        return document

    def _get_loader(self, document_type: str):
        """
        Return the appropriate loader based on
        the document type.
        """

        loader_map = {
            "pdf": PDFLoader,
            "image": ImageLoader,
            "text": TextLoader,
        }

        if document_type not in loader_map:
            raise ValueError(
                f"No loader available for "
                f"document type: {document_type}"
            )

        loader_class = loader_map[document_type]

        return loader_class(
            str(self.file_path)
        )