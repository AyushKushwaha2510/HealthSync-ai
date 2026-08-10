from typing import List
from pydantic import BaseModel
from app.features.prescriptions.schemas import PrescriptionAnalysis


class Message(BaseModel):
    role: str
    content: str | PrescriptionAnalysis


class SendMessage(BaseModel):
    messages: List[Message]


class Chat(BaseModel):
    # id:str
    content: str
