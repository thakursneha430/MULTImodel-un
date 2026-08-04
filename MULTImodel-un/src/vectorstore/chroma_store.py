"""
ChromaDB Vector Store
"""

from pathlib import Path
from chromadb import PersistentClient


class ChromaStore:

    def __init__(
        self,
        persist_directory: str = None,
        collection_name: str = "documents"
    ):

        # Always use the same database location
        if persist_directory is None:
            BASE_DIR = Path(__file__).resolve().parents[2]
            persist_directory = str(BASE_DIR / "vector_db")

        print(f"Using ChromaDB path: {persist_directory}")

        self.client = PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, embedded_chunks):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in embedded_chunks:

            ids.append(chunk["chunk_id"])
            documents.append(chunk["text"])
            embeddings.append(chunk["embedding"])
            metadatas.append(chunk["metadata"])

        # Avoid duplicate IDs
        existing = set(self.collection.get()["ids"])

        new_ids = []
        new_documents = []
        new_embeddings = []
        new_metadatas = []

        for i in range(len(ids)):
            if ids[i] not in existing:
                new_ids.append(ids[i])
                new_documents.append(documents[i])
                new_embeddings.append(embeddings[i])
                new_metadatas.append(metadatas[i])

        if len(new_ids) > 0:

            self.collection.add(
                ids=new_ids,
                documents=new_documents,
                embeddings=new_embeddings,
                metadatas=new_metadatas
            )

            print(f"Stored {len(new_ids)} chunks.")

        else:

            print("No new chunks to store.")

    def count(self):

        return self.collection.count()

    def delete_collection(self):

        self.client.delete_collection("documents")