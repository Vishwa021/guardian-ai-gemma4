"""
Guardian Service

Acts as the bridge between the API layer
and the AI Coordinator.
"""

from app.agents.coordinator import CoordinatorAgent
from app.models.request import AnalysisRequest
from app.models.final_report import FinalReport
from app.services.file_processor import FileProcessor

class GuardianService:

    def __init__(self):

        self.coordinator = CoordinatorAgent()

    def analyze(
        self,
        request: AnalysisRequest
    ) -> FinalReport:
        """
        Execute the Guardian AI pipeline.
        """

        return self.coordinator.analyze(request)
    
    def analyze(
    self,
    request: AnalysisRequest
):

        request = FileProcessor.process(request)

        return self.coordinator.analyze(request)