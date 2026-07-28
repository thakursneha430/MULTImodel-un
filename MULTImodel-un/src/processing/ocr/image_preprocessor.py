from pathlib import Path

from PIL import Image, ImageOps


class ImagePreprocessor:
    """
    Preprocess images before sending them to the OCR engine.
    """

    SUPPORTED_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def preprocess(self) -> Image.Image:
        """
        Load and preprocess the image.

        Returns:
            PIL.Image.Image: Preprocessed image.
        """

        self._validate_file()

        # Open image
        image = Image.open(self.file_path)

        # Convert image to RGB
        image = image.convert("RGB")

        # Convert to grayscale
        image = ImageOps.grayscale(image)

        # Auto-adjust image contrast
        image = ImageOps.autocontrast(image)

        return image

    def _validate_file(self) -> None:
        """
        Validate the input image.
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