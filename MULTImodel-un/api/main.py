from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.pipeline.document_pipeline import DocumentPipeline
from src.rag.rag_pipeline import RAGPipeline

app = FastAPI(
    title="Multimodal Document Intelligence API",
    version="1.0.0"
)

# ==========================================
# CORS Configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Directories
# ==========================================

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# Initialize Pipelines
# ==========================================

document_pipeline = DocumentPipeline()
rag_pipeline = RAGPipeline()

# ==========================================
# Request Model
# ==========================================

class QuestionRequest(BaseModel):
    question: str

# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Multimodal Document Intelligence API is running."
    }

# ==========================================
# Upload Endpoint
# ==========================================

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = document_pipeline.process(str(file_path))

        return {
            "message": "Document indexed successfully.",
            "filename": file.filename,
            "stored_chunks": result["stored_chunks"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ==========================================
# Ask Endpoint
# ==========================================

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:

        result = rag_pipeline.ask(request.question)

        return {
            "question": result["question"],
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )