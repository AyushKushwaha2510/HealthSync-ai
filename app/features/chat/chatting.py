from app.ai.llm.gemini import gemini_provider
from app.ai.llm.provider import LLMProvider
from app.features.chat.prompts import SEND_MESSAGE_PROMPT
from app.features.chat.schema import Chat


class Chatting:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def send_message(self, message: str) -> str:
        """
        Send Message to LLM
        """

        prompt = SEND_MESSAGE_PROMPT.invoke({"message": message})

        res = await self.llm.generate_structured(prompt.to_string(), Chat)

        return res.content


chatting = Chatting(llm=gemini_provider)
