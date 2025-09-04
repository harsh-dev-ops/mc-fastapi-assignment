from fastapi import FastAPI
from app.routers import api_router


app = FastAPI()


app.include_router(
    router=api_router,
    prefix='/api/v1'
)