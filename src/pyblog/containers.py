from dependency_injector import containers, providers

from .data.database import AppDb
from .data.repositories.blogpost_repository import BlogPostRepository


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    db = providers.Singleton(AppDb)

    blogpost_repository = providers.Factory(
        BlogPostRepository,
        db = db
    )


