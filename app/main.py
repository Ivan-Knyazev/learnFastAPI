import uvicorn
from fastapi import FastAPI, Request, Body, HTTPException
from fastapi.templating import Jinja2Templates

from app.models.models import *

app = FastAPI(
    title="FastAPI Learn App",
    description="Is a test app)",
    version="1.0",
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


@app.post("/user", response_model=UserCheck)
async def create_user(user: User):
    if user.age < 18:
        return UserCheck(**user.model_dump())
    else:
        return UserCheck(**user.dict(), is_adult=True)


feedbacks: list[Feedback] = []


@app.post("/feedback", response_model=FeedbackResponse)
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return FeedbackResponse(message=f"Feedback received. Thank you, {feedback.name}!")


@app.get("/feedback", response_model=list[Feedback])
async def get_all_feedback():
    return feedbacks


@app.post("/create_user", response_model=UserCreate)
async def create_user(user: UserCreate):
    return user


@app.get("/product/{product_id}", response_model=Product)
async def get_product(product_id: int):
    for product in sample_products:
        if product_id == product["product_id"]:
            return product
    else:
        raise HTTPException(status_code=404, detail="Product not found!")


def find_product(keyword: str, category: str | None, limit: int):
    products = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower():
            if category is None or product["category"] == category:
                products.append(product)
    return products[:limit]


@app.get("/products/search", response_model=list[Product])
async def get_product(keyword: str, category: str | None = None, limit: int = 10):
    return find_product(keyword, category, limit)


if __name__ == "__main__":
    uvicorn.run(app)
    # uvicorn.run(app, host="localhost", port=8000, reload=True)
