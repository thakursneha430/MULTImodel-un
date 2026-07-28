from pathlib import Path


class DocumentRouter:
    """
    Routes documents to the appropriate document loader
    based on the file extension.
    """

    ROUTE_MAP = {
        ".pdf": "pdf",
        ".png": "image",
        ".jpg": "image",
        ".jpeg": "image",
        ".txt": "text",
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def get_document_type(self) -> str:
        """
        Determine the document type based on file extension.
        """

        extension = self.file_path.suffix.lower()

        if extension not in self.ROUTE_MAP:
            raise ValueError(
                f"Unsupported document extension: {extension}"
            )

        return self.ROUTE_MAP[extension]

    def get_loader_name(self) -> str:
        """
        Return the name of the loader that should process
        the document.
        """

        document_type = self.get_document_type()

        loader_map = {
            "pdf": "PDFLoader",
            "image": "ImageLoader",
            "text": "TextLoader",
        }

        return loader_map[document_type]