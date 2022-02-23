import unittest
from calculadora import soma, subtrai

class TestCalculadora(unittest.TestCase):
    # def fala(self):
    #     print("nao vai axecutar no teste")


    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_e_menos_5_retorna_0(self):
        self.assertEqual(soma(-5, 5), 0)



unittest.main()