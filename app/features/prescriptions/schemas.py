from typing import List, Optional
from pydantic import BaseModel


# ==== Input ====
class Medicine(BaseModel):
    name: str
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    duration: Optional[str] = None
    note: Optional[str] = None


class Prescription(BaseModel):
    diagnosis: Optional[str] = None
    symptoms: List[str] = []
    diseases: List[str] = []
    medicines: List[Medicine]
    notes: List[str] = []


# ==== Output ====
class MedicineAnalysis(BaseModel):
    name: str
    purpose: str
    dosage: str | None
    precautions: List[str]
    side_effects: List[str]


class PrescriptionAnalysis(BaseModel):
    summary: str
    medicines: List[MedicineAnalysis]
    warnings: List[str]
    recommendations: List[str]
