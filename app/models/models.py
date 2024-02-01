from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    age: int


class UserCheck(User):
    is_adult: bool = False


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None = None
    is_subscribed: bool = False


class Feedback(BaseModel):
    name: str
    message: Optional[str] = None


class FeedbackResponse(BaseModel):
    message: str
