import models
import modules


def app():
    config = models.Config()
    survey = modules.Survey(config).conduct()
    discovery = modules.Discovery(config, survey)
    discovery.analyze('user_need_statement')
    discovery.analyze('strategic_alignment')


if __name__ == '__main__':
    app()
