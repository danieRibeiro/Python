import unittest
from Ebook.Teste.Exercícios.survey import AnonymousSurvey


class TesteAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser usados em todos os métodos de teste."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        # question = 'What language did you first learn to speak?'
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada."""
        question = 'What language did you first learn to speak?.'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            self.my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, self.my_survey.responses)
