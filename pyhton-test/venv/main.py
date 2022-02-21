from calculadora import soma

try:
    print(soma("98745",4987))
except AssertionError as e:
    print(f"conta inválida: {e}")
