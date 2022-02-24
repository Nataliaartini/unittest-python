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

    def test_cafe_da_manha_retorna_cafe_delicia_se_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "cafezinho diliça"
        for i in entradas:
            with self.subTest(i = i, saida=saida):
                self.assertEqual(cafe_da_manha(i), saida, msg=f"{i} nao retornou {saida}")

    def test_cafe_da_manha_retorna_cafe_soluvel_se_nao_for_multiplo_de_3_e_5(self):
        numeros = (8, 4, 7, 11)
        sai = "café solúvel pra ti"
        for j in numeros:
            with self.subTest(j = j, sai=sai):
                self.assertEqual(cafe_da_manha(j), sai, msg=f"{j} nao retornou {sai}")
  
    def test_cafe_da_manha_retorna_cafezinho_se_for_multiplo_de_3(self):
        numeros = (3, 6, 18, 33)
        sai = "cafézinho"
        for j in numeros:
            with self.subTest(j = j, sai=sai):
                self.assertEqual(cafe_da_manha(j), sai, msg=f"{j} nao retornou {sai}")

    def test_cafe_da_manha_retorna_diliça_se_for_multiplo_de_5(self):
        numeros = (5, 10, 20, 25)
        sai = "diliça"
        for j in numeros:
            with self.subTest(j = j, sai=sai):
                self.assertEqual(cafe_da_manha(j), sai, msg=f"{j} nao retornou {sai}")


unittest.main(verbosity=2)