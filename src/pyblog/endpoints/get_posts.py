from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from ..containers import Container
from ..data.repositories.blogpost_repository import BlogPostRepository


router = APIRouter()

@router.get("/posts")
@inject
def get_posts(
        blogpost_repository: Annotated[BlogPostRepository, Depends(Provide[Container.blogpost_repository])]):
    return blogpost_repository.get_posts()
