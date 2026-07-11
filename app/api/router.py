from fastapi import APIRouter

from app.features.prescriptions.router import router as prescription_router
from app.features.chat.router import router as chat_router

api_router = APIRouter()

api_router.include_router(prescription_router)
api_router.include_router(chat_router)


@api_router.get("/health")
async def health():
    return {"status": "ok"}


@api_router.get("/")
def baseurl():
    return {"message": "AI for HealthSync"}
