# TDD - Test Driven Development (desenvolvimento dirigido a testes)
# RED
# -criar o teste e vê a falha 
# GREEN
# -criar o codigo e vê o teste passar
# REFACTOR
# -melhorar o código

import unittest
from cafedamanha import cafe_da_manha

class TestCafeDaManha(unittest.TestCase):
    def test_cafe_da_manha_assertion_error_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            cafe_da_manha("0")

    def test_cafe_da_manha_retorna_cafe_soluvel_se_n_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "cafezinho diliça"
        for i in entradas:
            with self.subTest(i = i, saida=saida):
                self.assertEqual(cafe_da_manha(i), saida, msg=f"{i} nao retornou {saida}")


unittest.main(verbosity=2)            