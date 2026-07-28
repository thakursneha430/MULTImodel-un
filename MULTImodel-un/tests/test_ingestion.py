from pathlib import Path

import pytest

from src.ingestion.document_model import Document
from src.ingestion.file_validator import FileValidator
from src.ingestion.document_router import DocumentRouter
from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.image_loader import ImageLoader
from src.ingestion.text_loader import TextLoader


# ============================================================
# Document Model Tests
# ============================================================

def test_document_model():
    """
    Test the standard Document object.
    """

    document = Document(
        document_id="test-123",
        file_name="sample.txt",
        file_type="text",
        content="Hello World",
        metadata={
            "source": "sample.txt"
        }
    )

    assert document.document_id == "test-123"
    assert document.file_name == "sample.txt"
    assert document.file_type == "text"
    assert document.content == "Hello World"
    assert document.metadata["source"] == "sample.txt"


# ============================================================
# File Validator Tests
# ============================================================

def test_file_validator_valid_file(tmp_path):
    """
    Test that a valid TXT file passes validation.
    """

    test_file = tmp_path / "sample.txt"
    test_file.write_text(
        "This is a test document.",
        encoding="utf-8"
    )

    validator = FileValidator(str(test_file))

    assert validator.validate() is True


def test_file_validator_missing_file(tmp_path):
    """
    Test that a missing file raises FileNotFoundError.
    """

    test_file = tmp_path / "missing.txt"

    validator = FileValidator(str(test_file))

    with pytest.raises(FileNotFoundError):
        validator.validate()


def test_file_validator_unsupported_extension(tmp_path):
    """
    Test that an unsupported file type raises ValueError.
    """

    test_file = tmp_path / "sample.docx"
    test_file.write_text(
        "Test document.",
        encoding="utf-8"
    )

    validator = FileValidator(str(test_file))

    with pytest.raises(ValueError):
        validator.validate()


# ============================================================
# Document Router Tests
# ============================================================

def test_document_router_pdf():
    """
    Test routing for PDF files.
    """

    router = DocumentRouter(
        "data/raw/sample.pdf"
    )

    assert router.get_document_type() == "pdf"
    assert router.get_loader_name() == "PDFLoader"


def test_document_router_image():
    """
    Test routing for image files.
    """

    router = DocumentRouter(
        "data/raw/sample.jpg"
    )

    assert router.get_document_type() == "image"
    assert router.get_loader_name() == "ImageLoader"


def test_document_router_text():
    """
    Test routing for TXT files.
    """

    router = DocumentRouter(
        "data/raw/sample.txt"
    )

    assert router.get_document_type() == "text"
    assert router.get_loader_name() == "TextLoader"


def test_document_router_unsupported():
    """
    Test routing for unsupported file types.
    """

    router = DocumentRouter(
        "data/raw/sample.docx"
    )

    with pytest.raises(ValueError):
        router.get_document_type()


# ============================================================
# Text Loader Tests
# ============================================================

def test_text_loader(tmp_path):
    """
    Test loading a TXT file.
    """

    test_file = tmp_path / "sample.txt"

    test_content = (
        "Artificial Intelligence is powerful.\n"
        "Machine Learning is a subset of AI."
    )

    test_file.write_text(
        test_content,
        encoding="utf-8"
    )

    loader = TextLoader(str(test_file))

    document = loader.load()

    assert isinstance(document, Document)

    assert document.file_name == "sample.txt"

    assert document.file_type == "text"

    assert document.content == test_content

    assert document.metadata["character_count"] == len(
        test_content
    )

    assert document.metadata["line_count"] == 2


# ============================================================
# Image Loader Tests
# ============================================================

def test_image_loader(tmp_path):
    """
    Test loading an image file.
    """

    from PIL import Image

    test_file = tmp_path / "sample.jpg"

    image = Image.new(
        "RGB",
        (100, 100)
    )

    image.save(test_file)

    loader = ImageLoader(str(test_file))

    document = loader.load()

    assert isinstance(document, Document)

    assert document.file_name == "sample.jpg"

    assert document.file_type == "image"

    assert document.metadata["image_format"] == "JPEG"

    assert document.metadata["width"] == 100

    assert document.metadata["height"] == 100


# ============================================================
# PDF Loader Tests
# ============================================================

def test_pdf_loader(tmp_path):
    """
    Test loading a PDF file.
    """

    import fitz

    test_file = tmp_path / "sample.pdf"

    pdf = fitz.open()

    page = pdf.new_page()

    page.insert_text(
        (50, 50),
        "This is a test PDF document."
    )

    pdf.save(test_file)

    pdf.close()

    loader = PDFLoader(str(test_file))

    document = loader.load()

    assert isinstance(document, Document)

    assert document.file_name == "sample.pdf"

    assert document.file_type == "pdf"

    assert document.metadata["page_count"] == 1

    assert "This is a test PDF document." in (
        document.content
    )