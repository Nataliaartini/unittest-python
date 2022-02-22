def soma(x,y):
    """

    >>> soma(10,20)
    30

    >>> soma("-10", 50)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser um numero natural ou decimal!

    """

    assert isinstance(x, (int, float)), "X precisa ser um numero natural ou decimal!"
    assert isinstance(y, (int, float)), "Y precisa ser um numero natural ou decimal!"
    return x+y


if __name__== "__main__":
    import doctest
    doctest.testmod(verbose=True)
