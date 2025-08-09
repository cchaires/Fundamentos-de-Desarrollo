
def solicitar_puntos(i: int) -> float:
    while True:
        try:
            return float(input(f"Puntos contaminantes del auto {i}: "))
        except ValueError:
            print("Entrada inválida.")

def estadisticas_contaminacion() -> None:
    valores: list[float] = []
    for i in range(1, 26):
        valores.append(solicitar_puntos(i))
    promedio = sum(valores) / len(valores)
    print(f"Promedio: {promedio:.3f}")
    print(f"Menor: {min(valores)}")
    print(f"Mayor: {max(valores)}")

print("=== Contaminación de 25 automóviles ===")
estadisticas_contaminacion()
