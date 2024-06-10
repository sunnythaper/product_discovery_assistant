from pydantic import BaseModel


class Response(BaseModel):
    question: str
    answer: str | None = None


class Survey(BaseModel):
    responses: list[Response]
