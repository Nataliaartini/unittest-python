# class Pessoa:
#     __init__
#         nome str
#         sobrenome str
#         dados_obtidos bool

#     API:
#         obter_todos_os_dados -> method
#             OK
#             404

import unittest
from pessoa import Pessoa
from unittest.mock import patch

class TestPessoa(unittest.TestCase):
    #instancia uma pessoa na classe para nao precisar instancia a cada funcao
    def setUp(self):
        self.p1 = Pessoa("Natalia", "Artini")

    def test_pessoa_attr_nome_valor_certo(self):
        self.assertEqual(self.p1.nome, "Natalia")

    def test_pessoa_attr_nome_eh_string(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_valor_certo(self):
        self.assertEqual(self.p1.sobrenome, "Artini")

    def test_pessoa_attr_sobrenome_eh_string(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    #testes da api
    def test_obteve_todos_os_dados(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obteve_todos_os_dados(), "conectado")
            self.assertTrue(self.p1.dados_obtidos)

    def test_nao_obteve_todos_os_dados(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obteve_todos_os_dados(), "ERROR 404")
            self.assertFalse(self.p1.dados_obtidos)

    def test_obteve_todos_os_dados_e_depois_falha(self):
        with patch("requests.get") as fake_request:
            
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obteve_todos_os_dados(), "conectado")
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obteve_todos_os_dados(), "ERROR 404")
            self.assertFalse(self.p1.dados_obtidos)


if __name__ == "__main__":
    unittest.main(verbosity=2)