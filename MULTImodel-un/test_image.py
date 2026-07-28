from src.ingestion.image_loader import ImageLoader


file_path = "data/raw/sample.jpg"

loader = ImageLoader(file_path)

document = loader.load()

print("Document ID:", document.document_id)
print("File Name:", document.file_name)
print("File Type:", document.file_type)
print("Metadata:", document.metadata)