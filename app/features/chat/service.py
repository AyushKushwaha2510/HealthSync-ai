from typing import List

from app.features.chat.chatting import chatting
from app.features.chat.schema import Message


class ChatService:
     async def send_message(self, messages: List[Message]) -> str:
        return await chatting.send_message(messages)
    

chat_service = ChatService()
