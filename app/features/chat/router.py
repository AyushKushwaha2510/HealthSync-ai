from fastapi import APIRouter
from app.features.chat.schema import SendMessage
from app.features.chat.service import chat_service

router = APIRouter(prefix="/chat")


@router.post("/send")
async def send(body: SendMessage) -> str:
    print(body.messages)
    return await chat_service.send_message(body.messages)
