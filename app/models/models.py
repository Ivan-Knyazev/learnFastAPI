from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    age: int


class UserCreate(User):
    is_adult: bool = False


class Feedback(BaseModel):
    name: str
    message: Optional[str] = None


class FeedbackResponse(BaseModel):
    message: str
