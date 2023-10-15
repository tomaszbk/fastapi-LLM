from fastapi import FastAPI
from loguru import logger

from app.routes import router

app = FastAPI()

app.include_router(router)
