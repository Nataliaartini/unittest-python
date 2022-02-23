"""
 recebe um numero inteiro
 verifica se o numero é multiplo de 3 e 5:
    cafezinho diliça
 verifica se é somente multiplo de 3:
    cafezinho
 verifica se é somente multiplo de 5:
    diliça
 verifica se não é multiplo nem de 3 nem de 5:
    café solúvel pra ti
"""

from ast import Assert


def cafe_da_manha(n):
    assert isinstance(n, int), "n deve ser inteiro"