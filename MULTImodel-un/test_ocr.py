from src.processing.ocr.ocr_engine import OCREngine


if __name__ == "__main__":

    image_path = "data/raw/sample.jpg"

    print("=" * 60)
    print("OCR TEST")
    print("=" * 60)

    ocr_engine = OCREngine(
        language="en"
    )

    result = ocr_engine.extract_text(
        image_path
    )

    print("\nExtracted Text:")
    print("-" * 60)

    print(result["text"])

    print("\n" + "=" * 60)
    print("OCR CONFIDENCE SCORES")
    print("=" * 60)

    for score in result["confidence_scores"]:
        print(score)

    print("\n" + "=" * 60)
    print("OCR TEST COMPLETED")
    print("=" * 60)