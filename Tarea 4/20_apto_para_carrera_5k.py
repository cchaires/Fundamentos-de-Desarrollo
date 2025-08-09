# 10 tiempos (min) de una ruta de 5 km; apto si cumple al menos una condición:
# - en ninguna prueba hace > 16 min
# - en alguna prueba hace < 16 min
# - el promedio es <= 15 min

def solicitar_tiempo(i: int) -> float:
    while True:
        try:
            t = float(input(f"Tiempo del día {i} (min): "))
            if t > 0:
                return t
            print("Debe ser > 0.")
        except ValueError:
            print("Entrada inválida.")

def es_apto(tiempos: list[float]) -> bool:
    condicion1 = max(tiempos) <= 16
    condicion2 = any(t < 16 for t in tiempos)
    condicion3 = (sum(tiempos) / len(tiempos)) <= 15
    return condicion1 or condicion2 or condicion3

def evaluar_atleta() -> None:
    tiempos = [solicitar_tiempo(i) for i in range(1, 11)]
    promedio = sum(tiempos) / len(tiempos)
    apto = es_apto(tiempos)
    print(f"Promedio: {promedio:.2f} min")
    print("Resultado:", "APTO" if apto else "NO APTO")

print("=== Evaluación de atleta para 5 km (10 días) ===")
evaluar_atleta()
