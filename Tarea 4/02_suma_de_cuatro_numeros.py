
def solicitar_numero(i: int) -> float:
    while True:
        try:
            return float(input(f"Ingrese el número {i}: "))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def sumar_cuatro() -> float:
    return sum(solicitar_numero(i) for i in range(1, 5))

print("=== Suma de 4 números ===")
print(f"Suma = {sumar_cuatro()}")
