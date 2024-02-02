from app.temp_data.products import sample_products


def find_product(keyword: str, category: str | None, limit: int):
    products = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower():
            if category is None or product["category"] == category:
                products.append(product)
    return products[:limit]
