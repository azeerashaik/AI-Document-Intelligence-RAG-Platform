from fastapi import APIRouter

from app.schemas import ChatRequest

from Services.embedding_service import model
from Services.vector_service import search_embeddings
from Services.llm_service import generate_response

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
