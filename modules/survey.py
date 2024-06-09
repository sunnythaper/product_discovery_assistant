import models


class Survey:
    def __init__(self, config: models.Config):
        self.config = config

    def conduct(self):
        result = models.Survey(
            user_need=input('What problem or job are we going after? '),
            users_affected=input(
                'Who faces this problem and how important is it to them? '),
            user_current_solution=input(
                'How do they solve these problems today? '),
            strategy_applicability=input(
                'How does this fit into the broader strategy?  '),
            validation=input('How did we validate this? '),
            assumptions=input('What assumptions are we making? '),
            knowledge_gaps=input('What do we not know? ')
        )
        return result
