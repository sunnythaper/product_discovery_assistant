from pydantic import BaseModel


class Response(BaseModel):
    question: str
    answer: str


class Survey(BaseModel):
    responses: list[Response]
