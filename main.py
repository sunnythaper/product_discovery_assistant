import models
import modules


def app():
    config = models.Config()
    survey = modules.Survey(config)
    discovery = modules.Discovery(config, survey.results)
    report = discovery.report(['strategic_alignment', 'user_need_statement'])
    print(report)


if __name__ == '__main__':
    app()
