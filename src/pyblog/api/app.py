from fastapi import FastAPI

from pyblog.containers import Container


def create_app(container: Container) -> FastAPI:

    db = container.db()
    db.create_db(conn_str="sqlite://", echo=True) # todo: read this from config

    app = FastAPI()

    return app
