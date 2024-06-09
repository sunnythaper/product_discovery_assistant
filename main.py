import models
import modules


def app():
    config = models.Config()
    survey = modules.Survey(config).conduct()
    discovery = modules.Discovery(config, survey)
    discovery.user_need_statement()


if __name__ == '__main__':
    app()
