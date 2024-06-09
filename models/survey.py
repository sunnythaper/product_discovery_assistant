from pydantic import BaseModel


class Survey(BaseModel):
    user: str
    need: str
    strategic_goal: str
