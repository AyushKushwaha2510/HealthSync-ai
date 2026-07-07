from fastapi import APIRouter
from .schemas import Prescription, PrescriptionAnalysis
from .service import prescription_service

router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescription"],
)


@router.post("/analyze")
async def analyze(
    prescription: Prescription,
) -> PrescriptionAnalysis:
    return await prescription_service.analyze(prescription)
