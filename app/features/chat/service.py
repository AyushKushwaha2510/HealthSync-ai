from app.features.chat.chatting import chatting
from app.features.chat.schema import Chat


class ChatService:
    async def send_message(self, message: str) -> str:
        return await chatting.send_message(message)
    

chat_service = ChatService()
