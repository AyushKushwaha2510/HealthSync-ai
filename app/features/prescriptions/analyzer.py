from .schemas import Medicine, MedicineAnalysis, Prescription, PrescriptionAnalysis


class PrescriptionAnalyzer:

    async def analyze(
        self,
        prescription: Prescription,
    ) -> PrescriptionAnalysis:
        """
        Main entry point.
        """

        summary = await self.summarize(prescription)

        medicines = [
            await self.explain_medicine(medicine) for medicine in prescription.medicines
        ]

        warnings = await self.check_interactions(
            prescription.medicines,
        )

        recommendations = await self.generate_recommendations(
            prescription,
        )

        return PrescriptionAnalysis(
            summary=summary,
            medicines=medicines,
            warnings=warnings,
            recommendations=recommendations,
        )

    async def explain_medicine(
        self,
        medicine: Medicine,
    ) -> MedicineAnalysis:
        """
        Explain a single medicine.
        Replace with GPT later.
        """

        return MedicineAnalysis(
            name=medicine.name,
            purpose="Explanation coming soon.",
            dosage=medicine.dosage,
            precautions=[],
            side_effects=[],
        )

    async def check_interactions(
        self,
        medicines: list[Medicine],
    ) -> list[str]:
        """
        Detect medicine interactions.
        Replace with GPT later.
        """

        return []

    async def summarize(
        self,
        prescription: Prescription,
    ) -> str:
        """
        Generate an overall prescription summary.
        Replace with GPT later.
        """

        return "Analysis coming soon."

    async def generate_recommendations(
        self,
        prescription: Prescription,
    ) -> list[str]:
        """
        Lifestyle and precaution recommendations.
        Replace with GPT later.
        """

        return []


prescription_analyzer = PrescriptionAnalyzer()