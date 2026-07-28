from src.ingestion.text_loader import TextLoader


file_path = "data/raw/sample.txt"

loader = TextLoader(file_path)

document = loader.load()

print("=" * 50)
print("TEXT FILE TEST")
print("=" * 50)

print("Document ID:", document.document_id)
print("File Name:", document.file_name)
print("File Type:", document.file_type)

print("\nMetadata:")
print(document.metadata)

print("\nContent:")
print(document.content)