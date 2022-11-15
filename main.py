from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing student and courses",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Akinola Samson",
        "email": "akinolasamson1234@gmail.com",
    },
    license_info={
        "name": "Popsicool",
    },
)
users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_user():
    return users
@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(id:int = Path(...,
description="The id of the user you want to retrieve", gt=2),
q: str = Query(None, max_length=5)):
    return {"user":users[id], "query":q}
