from fastapi import APIRouter, Request, Body
from fastapi.templating import Jinja2Templates

calculate_router = APIRouter(
    prefix="",
    tags=["Lesson_1"]
)

templates = Jinja2Templates(directory="templates")


@calculate_router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"text": "Hello))"}
    )


@calculate_router.post("/calculate")
async def calculate(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}
