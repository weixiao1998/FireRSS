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


class UnknownError(BaseError):
    code = 90001
    http_code = 400
    msg = "unknown error"


class NetworkError(BaseError):
    code = 90002
    http_code = 400
    msg = "network error"


class UserExistsError(BaseError):
    code = 20100
    msg = "user already exists"


class OptionExistsError(BaseError):
    code = 20200
    msg = "option already exists"


class OptionNotFoundError(BaseError):
    code = 20201
    msg = "option not found"
