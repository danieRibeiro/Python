import unittest
from Ebook.Teste.Exercícios.city_function_two import name_city_country_population


class NameCaseTest(unittest.TestCase):
    """Nome da cidade, país e a população!"""

    def test_city_country(self):
        formatted_name = name_city_country_population('santiago', 'chile', 400000)
        if name_city_country_population(city='santiago', country='chile', population=True):
            self.assertEqual(formatted_name, 'Santiago, Chile - População: 400000')
        elif name_city_country_population(city='santiago', country='chile', population=False):
            self.assertEqual(formatted_name, 'Santiago, Chile.')

        print(formatted_name)


nome = NameCaseTest()
nome.test_city_country()
