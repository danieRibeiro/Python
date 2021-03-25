import unittest
from Ebook.Teste.Exercícios.Employee import Employee


class TestEmployee(unittest.TestCase, Employee):

    def setUp(self):
        self.employee = Employee('Danilo', 'Júnior', 5000)

    def test_give_default_raise(self):
        valor = self.employee.give_raise()
        self.assertEqual(valor, self.employee.give_raise())

    def test_give_custom_raise(self):
        valor = self.employee.give_raise(2000)
        self.assertEqual(valor, self.employee.give_raise())
