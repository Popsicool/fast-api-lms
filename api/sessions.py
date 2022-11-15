import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

@router.get("/sessions/{id}")
async def read_session():
    return {"course": {}}

@router.get("/sessions/{id}/contest-blocks")
async def read_session_content_block(id:int):
    return {"course": {}}

@router.get("/contest-blocks/{id}")
async def read_content_block():
    return {"course": {}}