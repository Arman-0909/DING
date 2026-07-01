from pydantic import BaseModel
from pydantic import field_validator
from datetime import datetime


class MessageCreate(BaseModel):
    chat_id: int
    content: str

    @field_validator("content")
    @classmethod
    def content_length(cls, v):
        if len(v.strip()) < 1:
            raise ValueError(
                "Message cannot be empty."
            )
        if len(v) > 5000:
            raise ValueError(
                "Message cannot exceed 5000 characters."
            )
        return v


class MessageResponse(BaseModel):
    id: int
    chat_id: int
    sender_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True