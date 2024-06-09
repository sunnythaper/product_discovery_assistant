import models


class Discovery:
    def __init__(self, config: models.Config, survey: models.Survey, llm: object):
        self.config = config
        self.survey = survey
        self.llm = llm

    def report(self, template: str) -> str:
        methods = self._get_report(template)
        report = []
        for method in methods.split('\n'):
            report.append(method.replace('_', ' ').title())
            report.append(self.analyze(method))
        return '\n\n'.join(report)

    def analyze(self, prompt: str) -> str:
        response = self.llm.prompt(prompt, self.survey.json())
        return response

    def _get_report(self, name: str) -> str:
        with open(f'{self.config.reports_dir}/{name}.{self.config.reports_extension}', 'r') as file:
            return file.read()
