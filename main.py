import models
import modules


def app() -> None:
    config = models.Config()
    llm = modules.LLM(config)
    survey = modules.Survey(config, llm)
    discovery = modules.Discovery(config, survey.results, llm)
    report = discovery.report(
        ['strategic_alignment', 'user_need_statement', 'current_state_experience'])
    print(report)


if __name__ == '__main__':
    app()
