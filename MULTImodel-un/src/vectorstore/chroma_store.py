"""
ChromaDB Vector Store
"""

from chromadb import PersistentClient


class ChromaStore:

    def __init__(
        self,
        persist_directory: str = "vector_db",
        collection_name: str = "documents"
    ):

        self.client = PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        embedded_chunks
    ):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in embedded_chunks:

            ids.append(chunk["chunk_id"])

            documents.append(chunk["text"])

            embeddings.append(chunk["embedding"])

            metadatas.append(chunk["metadata"])

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(f"Stored {len(ids)} chunks.")

    def count(self):

        return self.collection.count()

    def delete_collection(self):

        self.client.delete_collection("documents")