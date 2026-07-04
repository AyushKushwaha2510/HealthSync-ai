from fastapi import APIRouter
from .schemas import Prescription
from .service import prescription_service

router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescription"],
)


@router.post("/analyze")
async def analyze(
    prescription: Prescription,
):
    return await prescription_service.analyze(prescription)
