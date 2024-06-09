import models


class Survey:
    def __init__(self, config: models.Config):
        self.config = config

    def conduct(self):
        result = models.Survey(
            user=input('Who is the user? '),
            need=input('What is the user need? '),
            strategic_goal=input(
                'What strategic goal does this need align to? ')
        )
        return result
