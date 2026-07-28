import os
from pathlib import Path


# Project name
PROJECT_NAME = "MULTImodel-un"


# Project directories
directories = [
    "data/raw",
    "data/processed",

    "src",
    "src/ingestion",
    "src/utils",

    "tests",

    "scripts",
]


# Project files
files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    ".env.example",
    "Dockerfile",
    "docker-compose.yml",

    "src/__init__.py",

    "src/ingestion/__init__.py",
    "src/ingestion/file_validator.py",
    "src/ingestion/document_router.py",
    "src/ingestion/pdf_loader.py",
    "src/ingestion/image_loader.py",
    "src/ingestion/text_loader.py",
    "src/ingestion/ingestion_pipeline.py",

    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/exceptions.py",

    "tests/test_ingestion.py",

    "scripts/ingest_documents.py",
]


def create_project_structure():
    """
    Creates the complete project directory structure
    and empty project files.
    """

    project_root = Path(PROJECT_NAME)

    # Create project root directory
    project_root.mkdir(exist_ok=True)

    # Create directories
    for directory in directories:
        directory_path = project_root / directory
        directory_path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        file_path = project_root / file
        file_path.touch(exist_ok=True)

    print("=" * 60)
    print("PROJECT STRUCTURE CREATED SUCCESSFULLY")
    print("=" * 60)
    print(f"Project: {PROJECT_NAME}")
    print(f"Location: {project_root.absolute()}")
    print("=" * 60)


if __name__ == "__main__":
    create_project_structure()