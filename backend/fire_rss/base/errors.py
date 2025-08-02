class BaseError(Exception):
    code = 10000
    http_code = 409
    msg = "base error"
    data = None

    def __init__(self, data=None) -> None:
        self.data = data
        super().__init__(f"[error] code: {self.code}, msg: {self.msg}, data:{data}")


class RequestArgsError(BaseError):
    code = 10422
    http_code = 422
    msg = "request args invalid"


class UserExistsError(BaseError):
    code = 20100
    msg = "user already exists"
