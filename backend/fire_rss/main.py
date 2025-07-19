from fastapi import FastAPI

from .routers import api_routers

app = FastAPI()


for router in api_routers:
    app.include_router(router)
