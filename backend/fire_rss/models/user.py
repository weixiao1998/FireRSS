from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


# SQL Model
class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True, max_length=32)
    nick_name: str = Field(max_length=32)
    hashed_password: str = Field(max_length=64)
    type: str = Field(max_length=16)
    status: str = Field(max_length=16)
    create_time: datetime


# Pydantic Model
class UserOut(BaseModel):
    id: int
    name: str
    nick_name: str
    type: str
    status: str
    create_time: datetime
