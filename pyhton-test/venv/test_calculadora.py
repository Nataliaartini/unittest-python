import unittest
from calculadora import soma, subtrai

class TestCalculadora(unittest.TestCase):
    # def fala(self):
    #     print("nao vai axecutar no teste")


    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (20, 30, 50),
            (1, 6.5, 7.5),
            (10, 52, 62),
            (-10, 52, 42),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x,y), saida)

    def test_soma_x_nao_e_int_ou_float(self):
        with self.assertRaises(AssertionError):
            soma("11", 2)

    def test_soma_y_nao_e_int_ou_float(self):
        with self.assertRaises(AssertionError):
            soma(2, "2")


if __name__ == "__main__":
    unittest.main(verbosity=2)