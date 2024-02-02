from fastapi import APIRouter, Response, Cookie, HTTPException
from datetime import datetime
from hashlib import sha256

from app.schemas import User2
from app.temp_data.users import test_user_2

auth_router = APIRouter(
    prefix="/auth",
    tags=["Lesson_5"]
)


@auth_router.post("/login")
async def login(user: User2, response: Response):
    test_user_2["username"] = user.username
    test_user_2["password"] = user.password
    time_to_expire = str(int(datetime.now().timestamp() + 3600))
    string_to_hash = (test_user_2["username"] + test_user_2["password"]).encode()
    cookie_string = sha256(string_to_hash).hexdigest()
    print(cookie_string)
    response.set_cookie(key="session_token", value=cookie_string, httponly=True,
                        expires=time_to_expire)
    # response.set_cookie(key="expire", value=str(int(datetime.now().timestamp())))
    return {"message": "Cookie was installed!"}


@auth_router.get("/user", response_model=User2)
async def get_user(session_token: str = Cookie()):
    time_now = str(int(datetime.now().timestamp()))
    string_to_hash = (test_user_2["username"] + test_user_2["password"]).encode()
    user_hash = sha256(string_to_hash).hexdigest()
    if session_token == user_hash:
        return test_user_2
    else:
        raise HTTPException(status_code=401, detail="Invalid session token!")
