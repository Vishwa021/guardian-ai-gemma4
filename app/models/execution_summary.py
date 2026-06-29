from pydantic import BaseModel


class ExecutionSummary(BaseModel):
    """
    Execution statistics for the Guardian AI pipeline.
    """

    agents_executed: int

    successful_agents: int

    failed_agents: int

    total_input_tokens: int

    total_output_tokens: int

    total_tokens: int

    total_execution_time: float