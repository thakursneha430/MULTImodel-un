from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Document:
    """
    Standard document object used throughout the
    Multimodal Document Intelligence Platform.
    """

    document_id: str
    file_name: str
    file_type: str
    content: Any
    metadata: Optional[Dict[str, Any]] = None