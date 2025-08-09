
def suma_cuadrados_1_a_100() -> int:
    return sum(n*n for n in range(1, 101))

print("=== Suma de cuadrados del 1 al 100 ===")
print(f"Resultado: {suma_cuadrados_1_a_100()}")
