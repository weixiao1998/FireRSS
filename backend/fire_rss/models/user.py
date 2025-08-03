from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel

# const
USER_NAME_REGEX = r"^[a-zA-Z0-9_]{3,32}$"
PASSWORD_REGEX = r'^[a-zA-Z0-9_!@#$%^&*()_+\-=\[\]{}|;:\'",.<>?/]{8,16}$'


# SQL Model
class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True, max_length=32, regex=USER_NAME_REGEX)
    nick_name: str = Field(max_length=32)
    hashed_password: str = Field(max_length=64)
    type: str = Field(max_length=16)
    status: str = Field(max_length=16)
    create_time: datetime


# Pydantic Model
class UserSignUp(BaseModel):
    name: str = Field(min_length=3, max_length=32, regex=USER_NAME_REGEX)
    password: str = Field(min_length=8, max_length=16, regex=PASSWORD_REGEX)


class UserOut(BaseModel):
    id: int
    name: str
    nick_name: str
    type: str
    status: str
    create_time: datetime
