import models
import modules


def app() -> None:
    config = models.Config()
    llm = modules.LLM(config)
    template = 'daily_standup'
    survey = modules.Survey(config, llm, template)
    discovery = modules.Discovery(config, survey.results, llm)
    report = discovery.report(template)
    print(report)


if __name__ == '__main__':
    app()
