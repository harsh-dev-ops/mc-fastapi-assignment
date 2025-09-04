from fastapi import APIRouter
from app.routers import health_check
from app.routers import accounts


api_router = APIRouter()

api_router.include_router(
    router=health_check.router,
    prefix='',
    tags = ['Health Check']
)

api_router.include_router(
    router=accounts.router,
    prefix='',
    tags = ['Accounts']
)