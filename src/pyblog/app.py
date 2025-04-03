from fastapi import FastAPI

from .endpoints.router import router
from .containers import Container

def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_db(conn_str="sqlite://", echo=True)  # todo: read this from config
    api = FastAPI(
        title="pyblog",
        redoc_url="/api"
    )
    api.include_router(router=router, prefix="/api")
    return api

app = create_app()
