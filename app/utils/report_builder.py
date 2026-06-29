"""
Report Builder

Formats multiple AgentResponse objects
into a single report for downstream agents.
"""

from app.models.response import AgentResponse
from app.models.execution_summary import ExecutionSummary


class ReportBuilder:

    @staticmethod
    def combine(agent_reports: list[AgentResponse]) -> str:
        """
        Convert multiple AgentResponse objects
        into one structured report.
        """

        sections = []

        for report in agent_reports:

            section = f"""
==================================================
Agent Name      : {report.agent_name}
Status          : {report.status}

Summary:
{report.summary}

Confidence      : {report.confidence}

Threat Detected : {report.threat_detected}

Reasoning:
{report.reasoning}

---------------- Metrics ----------------

Input Tokens    : {report.input_tokens}
Output Tokens   : {report.output_tokens}
Total Tokens    : {report.total_tokens}

Response Time   : {report.response_time:.2f} sec
==================================================
"""

            sections.append(section)

        return "\n".join(sections)
    
    @staticmethod
    def execution_summary(agent_reports):

        successful = 0
        failed = 0

        input_tokens = 0
        output_tokens = 0
        total_tokens = 0

        total_time = 0.0

        for report in agent_reports:

            if report.status == "SUCCESS":
                successful += 1
            else:
                failed += 1

            input_tokens += report.input_tokens
            output_tokens += report.output_tokens
            total_tokens += report.total_tokens

            total_time += report.response_time

        return ExecutionSummary(
            agents_executed=len(agent_reports),
            successful_agents=successful,
            failed_agents=failed,
            total_input_tokens=input_tokens,
            total_output_tokens=output_tokens,
            total_tokens=total_tokens,
            total_execution_time=round(total_time, 2)
        )