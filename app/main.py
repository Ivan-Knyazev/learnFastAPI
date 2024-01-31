import uvicorn
from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates

from app.models.models import User, UserCreate

app = FastAPI(
    title="FastAPI Learn App",
    description="Is a test app)",
    version="0.1",
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"text": "Hello))"}
    )


@app.post("/calculate")
async def calculate(num1: int = None, num2: int = None, data=Body()):
    result: int = 0
    if len(data) == 2 and "num1" in data and "num2" in data:
        result = data["num1"] + data["num2"]
    else:
        result = num1 + num2
    return {"result": result}


test_user = User(id=1, name="John Doe", age=15)


@app.get("/users")
async def get_test_user():
    return test_user.dict()


@app.post("/user")
async def create_user(user: User) -> UserCreate:
    if user.age < 18:
        return UserCreate(**user.model_dump())
    else:
        return UserCreate(**user.dict(), is_adult=True)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
