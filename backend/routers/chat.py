from fastapi import APIRouter

from schemas.chat import ChatRequest, ChatResponse
from Services.langchain_service import get_chat_response

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
def chat_with_ai(request: ChatRequest):
    print(f"Received chat request: Session ID: {request.session_id}, User Message: {request.message}")
    reply = get_chat_response(request.message, session_id=request.session_id)
    print(f"Session ID: {request.session_id}, User Message: {request.message}, AI Reply: {reply}")
    return ChatResponse(reply=reply, session_id=request.session_id)
