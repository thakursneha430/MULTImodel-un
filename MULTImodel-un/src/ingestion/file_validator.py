from pathlib import Path


class FileValidator:
    """
    Validates input documents before they enter
    the document ingestion pipeline.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".txt",
    }

    MAX_FILE_SIZE_MB = 50

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def validate(self) -> bool:
        """
        Run all validation checks.
        """

        self._validate_file_exists()
        self._validate_file_extension()
        self._validate_file_size()

        return True

    def _validate_file_exists(self) -> None:
        """
        Check whether the file exists.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not self.file_path.is_file():
            raise ValueError(
                f"Path is not a valid file: {self.file_path}"
            )

    def _validate_file_extension(self) -> None:
        """
        Check whether the file format is supported.
        """

        extension = self.file_path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}. "
                f"Supported types: {self.SUPPORTED_EXTENSIONS}"
            )

    def _validate_file_size(self) -> None:
        """
        Check whether the file size is within the allowed limit.
        """

        file_size_mb = self.file_path.stat().st_size / (1024 * 1024)

        if file_size_mb > self.MAX_FILE_SIZE_MB:
            raise ValueError(
                f"File size ({file_size_mb:.2f} MB) exceeds "
                f"the maximum allowed size of "
                f"{self.MAX_FILE_SIZE_MB} MB."
            )