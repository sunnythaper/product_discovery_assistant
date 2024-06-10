import models
import modules
import streamlit as st

import modules.llm


class UI:
    def __init__(self, config: models.Config = models.Config()):
        self.config = config
        self.survey = modules.Survey(config)

    def main_page(self):
        self._setup()
        self._basic_questions()
        self._additional_questions()
        self._report()
        self._debug()

    def _setup(self):
        st.title('Setup')
        self.config.survey_template = st.selectbox(
            'Survey', self.survey.templates)

    def _basic_questions(self):
        if self.config.survey_template:
            self.survey.set_questions()
            st.title('Basic Questions')
            self._ask_questions(self.survey.basic_questions.responses)
            self.config.additional_questions = st.button(
                'Generate Additional Questions')

    def _additional_questions(self):
        if self.config.additional_questions:
            self.survey.set_additional_questions()
            st.title('Additional Questions')
            self._ask_questions(self.survey.additional_questions.responses)
            self.config.report = st.button('Generate Report')

    def _ask_questions(self, questions: list[models.Response]):
        for response in questions:
            response.answer = st.text_input(response.question, response.answer)

    def _report(self):
        if self.config.report:
            st.title('Report')

    def _debug(self):
        st.title('Debug')
        st.header('Config')
        st.json(self.config.json(), expanded=False)
        if self.config.survey_template:
            st.header('Basic Survey')
            st.json(self.survey.basic_questions.json(), expanded=False)
        if self.config.additional_questions:
            st.header('Additional Questions Survey')
            st.json(self.survey.additional_questions.json(), expanded=False)
