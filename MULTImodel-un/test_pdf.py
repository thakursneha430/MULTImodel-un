from src.ingestion.pdf_loader import PDFLoader


file_path = "data/raw/sample.pdf"

loader = PDFLoader(file_path)

document = loader.load()

print("=" * 50)
print("PDF TEST")
print("=" * 50)

print("Document ID:", document.document_id)
print("File Name:", document.file_name)
print("File Type:", document.file_type)
print("Page Count:", document.metadata["page_count"])

print("\nExtracted Content:")
print(document.content)