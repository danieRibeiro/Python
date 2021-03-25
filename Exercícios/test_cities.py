import unittest
from Ebook.Teste.Exercícios.city_functions import city_country


class NameCaseTest(unittest.TestCase):
    """Testar o nome da cidade"""

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, formatted_name.title())
