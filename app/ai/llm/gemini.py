from typing import Type, TypeVar, cast
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings
from .provider import LLMProvider

T = TypeVar("T", bound=BaseModel)


class GeminiProvider(LLMProvider):

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0,
        )

    async def generate_structured(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:

        structured_model = self.model.with_structured_output(response_model)

        response = await structured_model.ainvoke(prompt)

        return cast(T, response)

    async def generate_text(
        self,
        prompt: str,
    ) -> str:

        response = await self.model.ainvoke(prompt)

        return str(response.content)


gemini_provider = GeminiProvider()
