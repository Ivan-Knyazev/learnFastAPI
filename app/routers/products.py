from fastapi import APIRouter, HTTPException
from app.schemas import Product
from app.utils.products import find_product
from app.temp_data.products import sample_products

products_router = APIRouter(
    prefix="/products",
    tags=["Lesson_4"]
)


@products_router.get("/find/{product_id}", response_model=Product)
async def get_product_by_id(product_id: int):
    for product in sample_products:
        if product_id == product["product_id"]:
            return product
    else:
        raise HTTPException(status_code=404, detail="Product not found!")


@products_router.get("/search", response_model=list[Product])
async def get_products(keyword: str, category: str | None = None, limit: int = 10):
    return find_product(keyword, category, limit)
