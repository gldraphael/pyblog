import os

from dependency_injector import containers, providers


from .data.database import AppDb
from .data.repositories.blogpost_repository import BlogPostRepository

def _endpoint_modules():
    return [
        f'.endpoints.{file[:-3]}'
        for file in os.listdir("./src/pyblog/endpoints")
        if file.endswith('.py') and file not in ['docs.py', 'router.py']
    ]

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=_endpoint_modules())
    db = providers.Singleton(AppDb)

    blogpost_repository = providers.Factory(
        BlogPostRepository,
        db = db
    )


