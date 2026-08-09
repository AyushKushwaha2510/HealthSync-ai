from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class SendMessage(BaseModel):
    messages: List[Message]


class Chat(BaseModel):
    # id:str
    content: str
