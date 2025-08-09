def solicitar_entero_positivo(msg: str) -> int:
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
            print("Debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida.")

def solicitar_numero(idx: int) -> float:
    while True:
        try:
            return float(input(f"Ingrese el número {idx}: "))
        except ValueError:
            print("Entrada inválida.")

def sumar_n() -> float:
    n = solicitar_entero_positivo("¿Cuántos números vas a sumar? ")
    total = 0.0
    for i in range(1, n + 1):
        total += solicitar_numero(i)
    return total

print("=== Suma de n números ===")
print(f"Suma total: {sumar_n()}")
