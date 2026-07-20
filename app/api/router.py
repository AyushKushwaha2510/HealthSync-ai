from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.features.prescriptions.router import router as prescription_router
from app.features.chat.router import router as chat_router
from app.lib.database import get_db


api_router = APIRouter()

api_router.include_router(prescription_router)
api_router.include_router(chat_router)


@api_router.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "postgres connected"}


@api_router.get("/")
def baseurl():
    return {"message": "AI for HealthSync"}
