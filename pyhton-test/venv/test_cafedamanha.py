"""
TDD - Test Driven Development (desenvolvimento dirigido a testes)

RED:
 criar o teste e vê a falha 

GREEN:
* criar o codigo e vê o teste passar

REFACTOR:
 melhorar o código

"""

import unittest
from cafedamanha import cafe_da_manha

class TestCafeDaManha(unittest.TestCase):
    def test_cafe_da_manha_assertion_error_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            cafe_da_manha("0")

unittest.main(verbosity=2)            