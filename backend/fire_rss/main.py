from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .base.errors import BaseError
from .routers import api_routers

app = FastAPI()


@app.exception_handler(BaseError)
async def unicorn_exception_handler(request: Request, exc: BaseError):
    return JSONResponse(
        status_code=exc.http_code,
        content={"code": exc.code, "msg": exc.msg, "data": exc.data},
    )


for router in api_routers:
    app.include_router(router)
