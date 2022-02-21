def soma(x,y):
    """

    >>> soma(10,20)
    31

    """


    assert isinstance(x, (int, float)), "X precisa ser um numero natural ou decimal!"
    assert isinstance(y, (int, float)), "Y precisa ser um numero natural ou decimal!"
    return x+y


if __name__== "__main__":
    import doctest
    doctest.testmod()
