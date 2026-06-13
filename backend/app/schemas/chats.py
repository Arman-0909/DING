from pydantic import BaseModel


class ChatCreate(BaseModel):
    name: str | None = None
    is_group: bool = False


class ChatResponse(BaseModel):
    id: int
    name: str | None
    is_group: bool

    class Config:
        from_attributes = True