import models
import modules


def app() -> None:
    config = models.Config()
    llm = modules.LLM(config)
    survey = modules.Survey(config, llm)
    discovery = modules.Discovery(config, survey.results, llm)
    report = discovery.report('problem_definition')
    print(report)


if __name__ == '__main__':
    app()
