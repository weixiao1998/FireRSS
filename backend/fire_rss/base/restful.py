from marshmallow import Schema
from marshmallow import fields as mf

from ..base import errors


def resp_schema(schema):
    class ResponseSchema(Schema):
        code = mf.Integer(required=True)
        msg = mf.String(required=True)
        data = mf.Nested(schema)

    return ResponseSchema


def api_resp(data, code=10200, msg="ok"):
    return {
        "code": code,
        "msg": msg,
        "data": data,
    }


def init_error_handler(app):
    @app.errorhandler(errors.BaseError)
    def api_error_handler(err: errors.BaseError):
        resp = api_resp(err.data, err.code, err.msg)
        return resp, getattr(err, "http_code", 409)

    @app.errorhandler(422)
    @app.errorhandler(400)
    def webargs_error_handler(err):
        messages = err.data.get("messages", {})
        return api_error_handler(errors.RequestArgsError(data=messages))
