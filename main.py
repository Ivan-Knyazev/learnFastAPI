from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates

app = FastAPI()

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
