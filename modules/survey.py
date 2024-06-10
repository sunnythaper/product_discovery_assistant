import models
import modules

from os import listdir
from pydantic import FilePath


class Survey:
    def __init__(self, config: models.Config = models.Config()):
        self.config = config
        self.llm = modules.LLM(config)
        self.templates = self._get_templates(
            self.config.surveys_dir, self.config.surveys_extension)

    def set_questions(self) -> None:
        result = []
        with open(f'{self.config.surveys_dir}/{self.config.survey_template}.{self.config.surveys_extension}', 'r') as template:
            for question in template:
                result.append(models.Response(question=question))
        self.basic_questions = models.Survey(responses=result)

    def set_additional_questions(self) -> None:
        result = []
        questions = self.llm.prompt(
            'additional_questions', self.basic_questions.json())
        for question in questions.split('\n'):
            if question.strip() and '?' in question:
                result.append(models.Response(question=question))
        self.additional_questions = models.Survey(responses=result)

    def _get_templates(self, directory: FilePath, extension: str) -> list[str]:
        result = []
        for file_name in listdir(directory):
            result.append(file_name.replace(f'.{extension}', ''))
        return result
