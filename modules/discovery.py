import models
import modules


class Discovery:
    def __init__(self, config: models.Config, survey: models.Survey):
        self.config = config
        self.survey = survey
        self.llm = modules.LLM(self.config)

    def report(self, prompts: list[str]) -> str:
        report = []
        for prompt in prompts:
            report.append(prompt.replace('_', ' ').title())
            report.append(self.analyze(prompt))
        return '\n\n'.join(report)

    def analyze(self, prompt: str) -> str:
        response = self.llm.prompt(prompt, self.survey.json())
        return response['message']['content']
