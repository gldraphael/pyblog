from dependency_injector.wiring import inject
from fastapi import APIRouter

from pydantic import BaseModel


class HelloResponse(BaseModel):
    msg: str

router = APIRouter()

@router.get("/hello", response_model=HelloResponse)
@inject
async def index():
    return HelloResponse(msg="Hello!")
