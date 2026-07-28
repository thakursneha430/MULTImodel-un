from src.ingestion.ingestion_pipeline import IngestionPipeline


def test_document(file_path: str):
    """
    Test the document ingestion pipeline.
    """

    print("=" * 60)
    print("MULTIMODAL DOCUMENT INTELLIGENCE")
    print("DOCUMENT INGESTION PIPELINE")
    print("=" * 60)

    print(f"\nInput File: {file_path}")

    pipeline = IngestionPipeline(
        file_path
    )

    document = pipeline.run()

    print("\n" + "=" * 60)
    print("INGESTION SUCCESSFUL")
    print("=" * 60)

    print("\nDocument ID:")
    print(document.document_id)

    print("\nFile Name:")
    print(document.file_name)

    print("\nFile Type:")
    print(document.file_type)

    print("\nMetadata:")
    print(document.metadata)

    if document.content:
        print("\nExtracted Content:")
        print(document.content[:1000])


if __name__ == "__main__":

    test_document(
        "data/raw/sample.pdf"
    )
from src.ingestion.ingestion_pipeline import IngestionPipeline


def test_document(file_path: str):
    """
    Test the document ingestion pipeline.
    """

    print("=" * 60)
    print("MULTIMODAL DOCUMENT INTELLIGENCE")
    print("DOCUMENT INGESTION PIPELINE")
    print("=" * 60)

    print(f"\nInput File: {file_path}")

    pipeline = IngestionPipeline(file_path)

    document = pipeline.run()

    print("\n" + "=" * 60)
    print("INGESTION SUCCESSFUL")
    print("=" * 60)

    print("\nDocument ID:")
    print(document.document_id)

    print("\nFile Name:")
    print(document.file_name)

    print("\nFile Type:")
    print(document.file_type)

    print("\nMetadata:")
    print(document.metadata)

    if document.content:
        print("\nExtracted Content:")
        print(document.content[:1000])


if __name__ == "__main__":

    # Test Image
    test_document("data/raw/sample.jpg")
from src.ingestion.ingestion_pipeline import IngestionPipeline


def test_document(file_path: str):
    """
    Test the document ingestion pipeline.
    """

    print("=" * 60)
    print("MULTIMODAL DOCUMENT INTELLIGENCE")
    print("DOCUMENT INGESTION PIPELINE")
    print("=" * 60)

    print(f"\nInput File: {file_path}")

    pipeline = IngestionPipeline(file_path)

    document = pipeline.run()

    print("\n" + "=" * 60)
    print("INGESTION SUCCESSFUL")
    print("=" * 60)

    print("\nDocument ID:")
    print(document.document_id)

    print("\nFile Name:")
    print(document.file_name)

    print("\nFile Type:")
    print(document.file_type)

    print("\nMetadata:")
    print(document.metadata)

    if document.content:
        print("\nExtracted Content:")
        print(document.content[:1000])


if __name__ == "__main__":

    # Test Text File
    test_document("data/raw/sample.txt")