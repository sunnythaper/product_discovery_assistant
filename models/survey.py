from pydantic import BaseModel


class Survey(BaseModel):
    user_need: str
    users_affected: str
    user_current_solution: str
    strategy_applicability: str
    validation: str
    assumptions: str
    knowledge_gaps: str
