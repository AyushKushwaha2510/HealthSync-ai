from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class LLMProvider(ABC):

    @abstractmethod
    async def generate_structured(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:
        """
        Generate structured JSON matching the supplied Pydantic model.
        """
        raise NotImplementedError

    @abstractmethod
    async def generate_text(
        self,
        prompt: str,
    ) -> str:
        """
        Generate plain text.
        """
        raise NotImplementedError
