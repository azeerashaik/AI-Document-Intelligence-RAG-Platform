from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from backend.Services.pdf_service import extract_text
from backend.Services.chunk_service import chunk_text
from backend.Services.embedding_service import generate_embeddings
from backend.Services.vector_service import store_embeddings

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = extract_text(file_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks": len(chunks)
    }