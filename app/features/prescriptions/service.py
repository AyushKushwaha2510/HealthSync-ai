from .analyzer import prescription_analyzer
from .schemas import Prescription


class PrescriptionService:

    async def analyze(self, prescription: Prescription):
        return await prescription_analyzer.analyze(prescription)


prescription_service = PrescriptionService()