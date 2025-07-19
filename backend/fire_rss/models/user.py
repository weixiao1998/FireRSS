from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True, max_length=32)
    nick_name: str = Field(max_length=32)
    hashed_password: str = Field(max_length=64)
    type: str = Field(max_length=16)
    status: str = Field(max_length=16)
    creat_time: datetime
