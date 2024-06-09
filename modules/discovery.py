import models


class Discovery:
    def __init__(self, config: models.Config, survey: models.Survey, llm: object):
        self.config = config
        self.survey = survey
        self.llm = llm

    def report(self, prompts: list[str]) -> str:
        report = []
        for prompt in prompts:
            report.append(prompt.replace('_', ' ').title())
            report.append(self.analyze(prompt))
        return '\n\n'.join(report)

    def analyze(self, prompt: str) -> str:
        response = self.llm.prompt(prompt, self.survey.json())
        return response['message']['content']
