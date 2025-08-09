
def solicitar_entero_positivo(msg: str) -> int:
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
            print("Debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida.")

def solicitar_numero(idx: int) -> float:
    while True:
        try:
            return float(input(f"Ingrese el número {idx}: "))
        except ValueError:
            print("Entrada inválida.")

def media_de_numeros() -> float:
    n = solicitar_entero_positivo("¿Cuántos números vas a promediar? ")
    acumulado = 0.0
    for i in range(1, n + 1):
        acumulado += solicitar_numero(i)
    return acumulado / n

print("=== Media aritmética de n números ===")
print(f"Media = {media_de_numeros()}")
