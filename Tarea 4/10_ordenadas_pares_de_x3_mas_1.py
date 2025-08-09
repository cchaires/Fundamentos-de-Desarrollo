
def f(x: int) -> int:
    return x**3 + 1

def imprimir_puntos_pares() -> None:
    for x in range(0, 31):
        y = f(x)
        if y % 2 == 0:
            print(f"x={x}, y={y}")

print("=== Ordenadas pares de y = x^3 + 1 (x=0..30) ===")
imprimir_puntos_pares()
