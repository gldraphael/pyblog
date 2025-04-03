from fastapi import APIRouter

from .hello import router as hello_router
from .docs import docs_router
from .get_posts import router as get_posts_router


router = APIRouter()

router.include_router(hello_router)
router.include_router(docs_router)

router.include_router(get_posts_router)
