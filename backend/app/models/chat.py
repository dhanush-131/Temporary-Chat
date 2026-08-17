from pydantic import BaseModel


class ChatMessage(BaseModel):
    type: str
    message: str


    