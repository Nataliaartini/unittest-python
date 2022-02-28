import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obteve_todos_os_dados(self):
        resposta = requests.get("https://google.com")

        if resposta.ok:
            self.dados_obtidos = True
            return "conectado"
        else:
            self.dados_obtidos = False
            return "ERROR 404"
