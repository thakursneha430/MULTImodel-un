from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Document:
    """
    Standard representation of a document
    used throughout the ingestion pipeline.
    """

    document_id: str
    file_name: str
    file_type: str
    content: Optional[str] = None
    metadata: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """
        Convert Document object into a dictionary.
        """
        return {
            "document_id": self.document_id,
            "file_name": self.file_name,
            "file_type": self.file_type,
            "content": self.content,
            "metadata": self.metadata,
        }