from pydantic import BaseModel


class SendMessage(BaseModel):
    message: str


class Chat(BaseModel):
    # id:str
    content: str
