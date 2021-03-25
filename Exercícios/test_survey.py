import unittest
from Ebook.Teste.Exercícios.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)
