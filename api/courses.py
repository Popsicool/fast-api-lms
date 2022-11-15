import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"course": {}}

@router.post("/courses")
async def create_course_api():
    return {"course": {}}

@router.get("/courses/{id}")
async def read_course(id:int):
    return {"course": {}}

@router.patch("/courses/{id}")
async def update_course():
    return {"course": {}}

@router.delete("/courses/{id}")
async def delete_course(id:int):
    return {"course": {}}


@router.post("/courses")
async def create_course():
    return {"course": {}}
@router.get("/courses/{id}/sections")
async def read_course_section():
    return {"course": {}}