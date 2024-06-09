import models
import modules


def app() -> None:
    config = models.Config()
    llm = modules.LLM(config)
    survey = modules.Survey(config, llm, 'daily_standup')
    discovery = modules.Discovery(config, survey.results, llm)
    report = discovery.report('daily_standup')
    print(report)


if __name__ == '__main__':
    app()
