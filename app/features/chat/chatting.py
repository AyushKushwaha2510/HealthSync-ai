from typing import List
from app.ai.llm.gemini import gemini_provider
from app.ai.llm.provider import LLMProvider
from app.features.chat.prompts import SEND_MESSAGE_PROMPT
from app.features.chat.schema import Chat, Message, SendMessage


class Chatting:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def send_message(self, messages: List[Message]) -> str:
        """
        Send Message to LLM
        """

        prompt = SEND_MESSAGE_PROMPT.invoke({"message": messages})

        res = await self.llm.generate_structured(prompt.to_string(), Chat)

        return res.content


chatting = Chatting(llm=gemini_provider)
