from pydantic import BaseModel


class WebSocketMessage(BaseModel):
    chat_id: int
    content: str