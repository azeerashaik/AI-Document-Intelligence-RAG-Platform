from fastapi import APIRouter

from backend.app.schemas import ChatRequest

from backend.Services.embedding_service import model
from backend.Services.vector_service import search_embeddings
from backend.Services.llm_service import generate_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    query_embedding = model.encode(
        request.question
    )

    results = search_embeddings(
        query_embedding
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    answer = generate_response(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": documents
    }