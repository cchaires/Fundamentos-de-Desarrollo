
def solicitar_entero_no_negativo() -> int:
    while True:
        try:
            n = int(input("Ingresa un entero n (>=0): "))
            if n >= 0:
                return n
            print("Debe ser >= 0.")
        except ValueError:
            print("Entrada inválida.")

def factorial(n: int) -> int:
    f = 1
    for k in range(2, n + 1):
        f *= k
    return f

print("=== Factorial de n ===")
n = solicitar_entero_no_negativo()
print(f"factorial {n} es {factorial(n)}")
