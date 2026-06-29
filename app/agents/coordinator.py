"""
Coordinator Agent

Acts as the brain of Guardian AI.
It manages all specialized agents.
"""

from app.agents.vision_agent import VisionAgent
from app.agents.text_agent import TextAgent
from app.agents.fraud_agent import FraudAgent
from app.agents.risk_agent import RiskAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.models.request import AnalysisRequest
from app.models.response import AgentResponse
from app.utils.report_builder import ReportBuilder
from app.models.final_report import FinalReport
from app.utils.report_builder import ReportBuilder
from app.services.pdf_service import PDFService


class CoordinatorAgent:

    def __init__(self):

        # Initialize all agents once
        self.vision_agent = VisionAgent()
        self.text_agent = TextAgent()
        self.fraud_agent = FraudAgent()
        self.risk_agent = RiskAgent()
        self.recommendation_agent = RecommendationAgent()
    
    def status(self):
        """
        Display all registered agents.
        """

        print("\n========== Guardian AI ==========\n")

        print(f"✓ {self.vision_agent.name}")

        print(f"✓ {self.text_agent.name}")

        print(f"✓ {self.fraud_agent.name}")

        print(f"✓ {self.risk_agent.name}")

        print(f"✓ {self.recommendation_agent.name}")

        print("\nCoordinator Ready!\n")
    
    def select_agents(self, request: AnalysisRequest) -> list:
        """
        Decide which specialized agents should analyze the request.
        """

        selected = []

        if request.image_path:
            selected.append(self.vision_agent)

        if request.text:
            selected.append(self.text_agent)
            selected.append(self.fraud_agent)

        return selected
    
    def execute_agents(
    self,
    request: AnalysisRequest
) -> list[AgentResponse]:
        """
        Execute all selected agents and collect their responses.
        """

        selected_agents = self.select_agents(request)

        responses = []

        # if request.pdf_path:

        #     pdf_text = PDFService.extract_text(
        #         request.pdf_path
        #     )

        #     if request.text:
        #         request.text += "\n\n" + pdf_text
        #     else:
        #         request.text = pdf_text

        for agent in selected_agents:

            if agent == self.vision_agent:

                response = agent.analyze_image(
                    image_path=request.image_path
                )

            elif agent == self.text_agent:

                response = agent.analyze_text(
                    request.text
                )

            elif agent == self.fraud_agent:

                response = agent.analyze_fraud(
                    request.text
                )

            else:
                continue

            responses.append(response)

        return responses
    
    def build_report(self, responses):
        """
        Build a combined report from all agent responses.
        """

        return ReportBuilder.combine(responses)
    
    def run_risk_assessment(self, responses):
        """
        Execute the Risk Agent.
        """

        return self.risk_agent.assess_risk(responses)
    
    def generate_recommendations(self, risk_response):
        """
        Generate recommendations based on the risk assessment.
        """

        return self.recommendation_agent.generate_recommendations(
            risk_response
        )
    
    def analyze(self, request):
        """
        Complete Guardian AI workflow.
        """

        # Execute specialist agents
        responses = self.execute_agents(request)

        summary = ReportBuilder.execution_summary(responses)

        # Overall risk
        risk = self.run_risk_assessment(responses)

        # Final recommendations
        recommendations = self.generate_recommendations(risk)

        # Return complete report
        return FinalReport(
    agent_reports=responses,
    risk_assessment=risk,
    recommendations=recommendations,
    execution_summary=summary
)