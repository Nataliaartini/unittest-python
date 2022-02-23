from calculadora import soma, subtrai

try:
    print(soma("98745",4987))
except AssertionError as e:
    print(f"conta inválida: {e}")

try:
    print(subtrai(4937,4987))
except AssertionError as e:
    print(f"conta inválida: {e}")