"""
Main Document Pipeline

Flow:
Upload
    ↓
Ingestion
    ↓
Processing
    ↓
Embedding
    ↓
ChromaDB
"""

from src.ingestion.ingestion_pipeline import IngestionPipeline
from src.processing.processing_pipeline import ProcessingPipeline
from src.embeddings.embedding_pipeline import EmbeddingPipeline
from src.vectorstore.chroma_store import ChromaStore


class DocumentPipeline:
    """
    Orchestrates the complete document processing workflow.
    """

    def __init__(self):

        self.processing_pipeline = ProcessingPipeline()
        self.embedding_pipeline = EmbeddingPipeline()
        self.vector_store = ChromaStore()

    def process(self, file_path: str):

        # ---------------------------------
        # Phase 2 : Document Ingestion
        # ---------------------------------

        ingestion_pipeline = IngestionPipeline(file_path)

        document = ingestion_pipeline.run()

        # ---------------------------------
        # Phase 3 : Document Processing
        # ---------------------------------

        processing_result = self.processing_pipeline.process(
            document.content
        )

        chunks = processing_result["chunks"]

        print(f"Chunks created: {len(chunks)}")

        # ---------------------------------
        # Phase 4 : Embedding Generation
        # ---------------------------------

        embedded_chunks = self.embedding_pipeline.process(
            chunks
        )

        print(f"Embeddings created: {len(embedded_chunks)}")

        # ---------------------------------
        # Phase 5 : Store in ChromaDB
        # ---------------------------------

        try:
            self.vector_store.delete_collection()
        except Exception:
            pass

        self.vector_store = ChromaStore()

        self.vector_store.add_documents(
            embedded_chunks
        )

        print(
            f"Total vectors stored: {self.vector_store.count()}"
        )

        return {
            "document": document,
            "cleaned_text": processing_result["cleaned_text"],
            "chunks": chunks,
            "embedded_chunks": embedded_chunks,
            "metadata": processing_result["metadata"],
            "stored_chunks": self.vector_store.count()
        }