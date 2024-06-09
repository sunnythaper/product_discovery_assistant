import models
import ollama


class Discovery:
    def __init__(self, config: models.Config, survey: models.Survey):
        self.config = config
        self.survey = survey

    def report(self, methods: list[str]) -> str:
        report = []
        for method in methods:
            report.append(method.replace('_', ' ').title())
            report.append(self.analyze(method))
        return '\n\n'.join(report)

    def analyze(self, method: str) -> str:
        response = self._prompt_llm(self._get_prompt(method))
        return str(response['message']['content'])

    def _get_prompt(self, name: str) -> str:
        with open(f'{self.config.prompts_dir}/{name}.{self.config.prompts_extension}', 'r') as file:
            return file.read()

    def _prompt_llm(self, prompt: str) -> str:
        return ollama.chat(
            model=self.config.llm_model,
            messages=[{'role': 'system', 'content': prompt},
                      {'role': 'user', 'content': self.survey.json()}],
            stream=self.config.print_stream
        )
