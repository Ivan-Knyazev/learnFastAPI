# import uvicorn
from fastapi import FastAPI

from app.routers import (calculate_router, test_user_router,
                         feedback_router, products_router,
                         auth_router)

app = FastAPI(
    title="FastAPI Learn App",
    description="Is a test app)",
    version="1.1",
)

app.include_router(calculate_router)
app.include_router(test_user_router)
app.include_router(feedback_router)
app.include_router(products_router)
app.include_router(auth_router)

# if __name__ == "__main__":
#     uvicorn.run(app)
#     uvicorn.run(app, host="localhost", port=8000, reload=True)
