from pathlib import Path
from typing import Dict, List

from paddleocr import PaddleOCR

from src.processing.ocr.image_preprocessor import ImagePreprocessor


class OCREngine:
    """
    OCR engine using PaddleOCR.

    Responsible for:
    1. Preprocessing the input image
    2. Running OCR
    3. Extracting detected text
    4. Extracting confidence scores
    5. Extracting bounding boxes
    """

    def __init__(self, language: str = "en"):
        """
        Initialize the OCR engine.

        Args:
            language: OCR language. Default is English.
        """

        self.language = language

        self.ocr = PaddleOCR(
            lang=self.language
        )

    def extract_text(
        self,
        file_path: str
    ) -> Dict:
        """
        Extract text from an image.

        Args:
            file_path: Path to the input image.

        Returns:
            Dictionary containing extracted text,
            confidence scores, and bounding boxes.
        """

        file_path = Path(file_path)

        # Step 1: Preprocess image
        preprocessor = ImagePreprocessor(
            str(file_path)
        )

        processed_image = preprocessor.preprocess()

        # Step 2: Run OCR
        result = self.ocr.predict(
            processed_image
        )

        extracted_text: List[str] = []
        confidence_scores: List[float] = []
        bounding_boxes: List = []

        # Step 3: Process OCR results
        for page_result in result:

            if not page_result:
                continue

            rec_texts = page_result.get(
                "rec_texts",
                []
            )

            rec_scores = page_result.get(
                "rec_scores",
                []
            )

            rec_boxes = page_result.get(
                "rec_boxes",
                []
            )

            extracted_text.extend(
                rec_texts
            )

            confidence_scores.extend(
                rec_scores
            )

            bounding_boxes.extend(
                rec_boxes
            )

        # Step 4: Combine extracted text
        full_text = "\n".join(
            extracted_text
        )

        return {
            "text": full_text,
            "texts": extracted_text,
            "confidence_scores": confidence_scores,
            "bounding_boxes": bounding_boxes,
        }