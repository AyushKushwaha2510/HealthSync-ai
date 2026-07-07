from app.ai.llm.provider import LLMProvider
from app.features.prescriptions.prompts import (
    PRESCRIPTION_ANALYSIS_PROMPT,
)

from .schemas import Medicine, MedicineAnalysis, Prescription, PrescriptionAnalysis
from app.ai.llm.gemini import gemini_provider


class PrescriptionAnalyzer:

    def __init__(self, llm: LLMProvider):
        self.llm = llm

    async def analyze(
        self,
        prescription: Prescription
    ) -> PrescriptionAnalysis:
        """
        Explain whole prescription in only one API call
        """
        
        prompt = PRESCRIPTION_ANALYSIS_PROMPT.invoke(
            {
                "prescription": prescription.model_dump_json()
            }
        )
        print(prompt)

        result = await self.llm.generate_structured(
            prompt.to_string(), 
            PrescriptionAnalysis
        )
        
        return result

    # async def analyze(
    #     self,
    #     prescription: Prescription,
    # ) -> PrescriptionAnalysis:
    #     """
    #     Main entry point.
    #     """

    #     summary = await self.summarize(prescription)

    #     medicines = [
    #         await self.explain_medicine(medicine) for medicine in prescription.medicines
    #     ]

    #     warnings = await self.check_interactions(
    #         prescription.medicines,
    #     )

    #     recommendations = await self.generate_recommendations(
    #         prescription,
    #     )

    #     return PrescriptionAnalysis(
    #         summary=summary,
    #         medicines=medicines,
    #         warnings=warnings,
    #         recommendations=recommendations,
    #     )

    # async def explain_medicine(
    #     self,
    #     medicine: Medicine,
    # ) -> MedicineAnalysis:
    #     """
    #     Explain a single medicine.
    #     Replace with GPT later.
    #     """

    #     prompt = EXPLAIN_MEDICINE_PROMPT.invoke(
    #         {"medicine": medicine.model_dump_json(indent=2)}
    #     )

    #     result = await self.llm.generate_structured(
    #         prompt.to_string(),
    #         MedicineAnalysis,
    #     )

    #     print("result med", result)
    #     return result

    # async def check_interactions(
    #     self,
    #     medicines: list[Medicine],
    # ) -> list[str]:
    #     """
    #     Detect medicine interactions.
    #     Replace with GPT later.
    #     """

    #     return []

    # async def summarize(
    #     self,
    #     prescription: Prescription,
    # ) -> str:
    #     """
    #     Generate an overall prescription summary.
    #     Replace with GPT later.
    #     """

    #     prompt = SUMMARY_PROMPT.invoke({"prescription": prescription.model_dump_json()})

    #     result = await self.llm.generate_structured(
    #         prompt.to_string(), PrescriptionAnalysis
    #     )
    #     print("result summmary", result)
    #     return result.summary

    # async def generate_recommendations(
    #     self,
    #     prescription: Prescription,
    # ) -> list[str]:
    #     """
    #     Lifestyle and precaution recommendations.
    #     Replace with GPT later.
    #     """

    #     return []


prescription_analyzer = PrescriptionAnalyzer(llm=gemini_provider)
