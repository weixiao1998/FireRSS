from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None
