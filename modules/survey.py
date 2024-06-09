import models


class Survey:
    def __init__(self, config: models.Config, llm: object, template: str = 'default'):
        self.config = config
        self.template = template
        self.llm = llm
        self.results = self.conduct()

    def conduct(self) -> models.Survey:
        questions = self._get_survey()
        responses = self._ask_questions(questions)
        return models.Survey(responses=responses)

    def _get_survey(self) -> str:
        with open(f'{self.config.surveys_dir}/{self.template}.{self.config.surveys_extension}', 'r') as file:
            return file.read()

    def _ask_questions(self, questions: str) -> list[models.Response]:
        responses = []
        for question in questions.split('\n'):
            answer = input(f'{question}\n')
            responses.append(models.Response(
                question=question, answer=answer))
        return responses
