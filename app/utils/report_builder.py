"""
Report Builder

Formats multiple AgentResponse objects
into a single report for downstream agents.
"""

from app.models.response import AgentResponse


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