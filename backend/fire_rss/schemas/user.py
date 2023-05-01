from marshmallow import Schema
from marshmallow import fields as mf


class UserSchema(Schema):
    id = mf.Int(dump_only=True)
    name = mf.String(required=True)
    password = mf.String(load_only=True, required=True)


class SearchUserSchema(Schema):
    name = mf.String()
    page_size = mf.Integer(load_default=20)
    page_num = mf.Integer(load_default=1)
