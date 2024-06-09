import models


class Survey:
    def __init__(self, config: models.Config, llm: object, template: str):
        self.config = config
        self.template = template
        self.llm = llm
        self.results = self.conduct()

    def conduct(self) -> models.Survey:
        questions = self._get_survey()
        responses = self._ask_questions(questions)
        survey = models.Survey(responses=responses)
        additional_questions = self.llm.prompt(
            'additional_questions', survey.json())
        responses = self._ask_questions(additional_questions)
        survey.responses.extend(responses)
        return survey

    def _get_survey(self) -> str:
        with open(f'{self.config.surveys_dir}/{self.template}.{self.config.surveys_extension}', 'r') as file:
            return file.read()

    def _ask_questions(self, questions: str) -> list[models.Response]:
        responses = []
        questions = self._clean_up_questions(questions)
        for question in questions.split('\n'):
            answer = input(f'\033[1;34m{question}\033[0m\n')
            responses.append(models.Response(
                question=question, answer=answer))
        return responses

    def _clean_up_questions(self, questions: str) -> str:
        cleaned_questions = '\n'.join(line for line in questions.split(
            '\n') if line.strip() and '?' in line)
        return cleaned_questions
