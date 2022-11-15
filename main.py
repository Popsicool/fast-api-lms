from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api.users import router
from api import users, courses, sessions

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sessions.router)




