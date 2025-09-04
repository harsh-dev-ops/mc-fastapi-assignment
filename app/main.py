
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import api_router
import warnings


warnings.filterwarnings("ignore")

app = FastAPI(title="Accounts Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", 
                   "http://localhost:3000", 
                   "http://localhost:80"], # Add any other microservice for IPC communication
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router=api_router,
    prefix='/api/v1'
)