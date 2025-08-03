import json
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel
from pydantic import Field as PydanticField
from sqlmodel import Field, SQLModel

from fire_rss.base import utils


# SQL Model
class Option(SQLModel, table=True):
    id: int = Field(primary_key=True)
    key: str = Field(unique=True, max_length=128, index=True)
    value: str = Field(max_length=4096)
    description: Optional[str] = Field(default=None, max_length=256)
    create_time: datetime = Field(default_factory=utils.utc_now)
    update_time: datetime = Field(
        default_factory=utils.utc_now, sa_column_kwargs={"onupdate": utils.utc_now}
    )

    def get_value(self) -> Any:
        """Convert JSON string to actual type"""
        try:
            return json.loads(self.value)
        except json.JSONDecodeError:
            return self.value

    def set_value(self, value: Any) -> None:
        """Convert actual type to JSON string for storage"""
        self.value = json.dumps(value)
        self.update_time = datetime.now()


# Pydantic Models
class OptionOut(BaseModel):
    id: int
    key: str
    value: Any
    description: Optional[str]
    create_time: datetime
    update_time: datetime

    class Config:
        arbitrary_types_allowed = True


class OptionCreate(BaseModel):
    key: str = PydanticField(max_length=64)
    value: Any
    description: Optional[str] = PydanticField(default=None, max_length=256)

    class Config:
        arbitrary_types_allowed = True


class OptionUpdate(BaseModel):
    value: Optional[Any] = None
    description: Optional[str] = PydanticField(default=None, max_length=256)

    class Config:
        arbitrary_types_allowed = True
