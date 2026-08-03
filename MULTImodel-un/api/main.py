from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException

from src.pipeline.document_pipeline import DocumentPipeline

app = FastAPI(
    title="Multimodal Document Intelligence API",
    version="1.0.0"
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

pipeline = DocumentPipeline()


@app.get("/")
def home():
    return {
        "message": "Multimodal Document Intelligence API is running."
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    try:
        # Save uploaded file
        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Process document
        result = pipeline.process(str(file_path))

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