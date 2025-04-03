from dependency_injector import containers, providers

from pyblog.infrastructure.data.database import AppDb
from pyblog.infrastructure.data.repositories.blogpost_repository import BlogPostRepository


class Container(containers.DeclarativeContainer):

    db = providers.Singleton(AppDb)

    blogpost_repository = providers.Factory(
        BlogPostRepository,
        db = db
    )
