
def solicitar_numero(idx: int) -> float:
    while True:
        try:
            return float(input(f"Ingrese el número {idx}: "))
        except ValueError:
            print("Entrada inválida.")

def mayor_de_50() -> float:
    mayor = None
    for i in range(1, 51):
        x = solicitar_numero(i)
        mayor = x if mayor is None or x > mayor else mayor
    return mayor

print("=== Mayor de 50 números ===")
print(f"El mayor es: {mayor_de_50()}")
