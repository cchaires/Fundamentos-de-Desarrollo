
DIAS_MEDICION = 5
UMBRAL_IMECA = 170
DIAS_PARO = 7
PCT_MULTA = 0.50


def solicitar_imecas() -> list[float]:

    imecas = []
    for i in range(1, DIAS_MEDICION + 1):
        while True:
            try:
                valor = float(input(f"Ingresa el valor IMECA del día {i}: "))
                if valor < 0:
                    print("El valor IMECA no puede ser negativo. Intenta de nuevo.")
                    continue
                imecas.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Ingresa un número.")
    return imecas


def calcular_promedio(imecas: list[float]) -> float:

    return sum(imecas) / len(imecas)


def determinar_sancion(promedio: float) -> tuple[bool, float]:

    if promedio > UMBRAL_IMECA:
        print("Promedio IMECA superior a 170: se detendrá la producción por una semana y hay multa del 50%.")
        return True, PCT_MULTA
    else:
        print("Promedio IMECA de 170 o menor: no hay sanción ni multa.")
        return False, 0.0


def calcular_perdida(ganancia_diaria: float, sancion: bool, pct_multa: float) -> float:

    if not sancion:
        return 0.0
    perdida_paro = ganancia_diaria * DIAS_PARO
    multa = ganancia_diaria * pct_multa
    return perdida_paro + multa


print("=== Programa de Control de Contaminación (IMECA) ===")

imecas = solicitar_imecas()
promedio = calcular_promedio(imecas)
print(f"\nPromedio de IMECA en {DIAS_MEDICION} días: {promedio:.2f}")
while True:
        try:
            ganancia = float(input("\nIngresa la ganancia diaria de la fábrica: $"))
            if ganancia < 0:
                print("La ganancia no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
sancion, pct_multa = determinar_sancion(promedio)
perdida_total = calcular_perdida(ganancia, sancion, pct_multa)
print(f"\nPérdida total estimada: ${perdida_total:.2f}")
