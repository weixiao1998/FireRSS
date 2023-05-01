from peewee import BigAutoField, CharField, FixedCharField

from ..base.db import BaseModel


class User(BaseModel):
    id = BigAutoField()
    name = CharField(max_length=32, unique=True)
    password = FixedCharField(max_length=64)
    type = FixedCharField(max_length=16)
    status = FixedCharField(max_length=16)
