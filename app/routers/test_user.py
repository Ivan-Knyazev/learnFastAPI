from fastapi import APIRouter
from app.schemas import User, UserCheck, UserCreate
from app.temp_data.user import test_user_1

test_user_router = APIRouter(
    prefix="/test_user",
    tags=["Lesson_2"]
)


@test_user_router.get("/user")
async def get_test_user():
    return test_user_1.dict()


@test_user_router.post("/user", response_model=UserCheck)
async def create_user(user: User):
    if user.age < 18:
        return UserCheck(**user.model_dump())
    else:
        return UserCheck(**user.dict(), is_adult=True)


@test_user_router.post("/create_user", response_model=UserCreate)
async def create_user(user: UserCreate):
    return user
