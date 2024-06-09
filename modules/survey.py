import models


class Survey:
    def __init__(self, config: models.Config, template: str = 'default'):
        self.config = config
        self.template = template

    def conduct(self):
        questions = self._get_survey()
        responses = []

        for question in questions.split('\n'):
            response = input(f'{question}\n')
            responses.append(models.Response(
                question=question, answer=response))

        return models.Survey(responses=responses)

    def _get_survey(self) -> str:
        with open(f'{self.config.surveys_dir}/{self.template}.{self.config.surveys_extension}', 'r') as file:
            return file.read()
