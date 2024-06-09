import models
import ollama


class LLM:
    def __init__(self, config: models.Config):
        self.config = config

    def prompt(self, system_prompt: str, user_prompt: str) -> str:
        return ollama.chat(
            model=self.config.llm_model,
            messages=[{'role': 'system', 'content': self._get_prompt(system_prompt)},
                      {'role': 'user', 'content': user_prompt}],
            stream=self.config.print_stream
        )

    def _get_prompt(self, name: str) -> str:
        with open(f'{self.config.prompts_dir}/{name}.{self.config.prompts_extension}', 'r') as file:
            return file.read()
