from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


class UserCreate(User):
    is_adult: bool = False
