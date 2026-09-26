from fastapi import APIRouter
from .routes.hello import router as hello_router
from .routes.websocket import router as websocket_router

api_router = APIRouter()
api_router.include_router(hello_router)
api_router.include_router(websocket_router)
