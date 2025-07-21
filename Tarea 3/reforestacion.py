UMBRAL_M2 = 1_000_000
PORCENTAJES = {
    'grande': {'pino': 0.70, 'oyamel': 0.20, 'cedro': 0.10},
    'pequena': {'pino': 0.50, 'oyamel': 0.30, 'cedro': 0.20},
}

def solicitar_hectareas() -> float:
    while True:
        try:
            valor = float(input("Ingresa la superficie del bosque (hectáreas): "))
            if valor <= 0:
                print("La superficie debe ser mayor a 0. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número válido de hectáreas.")

def determinar_porcentajes(area_m2: float) -> dict:

    if area_m2 > UMBRAL_M2:
        return PORCENTAJES['grande']
    else:
        return PORCENTAJES['pequena']

def calcular_areas(area_m2: float, porcentajes: dict) -> dict:

    areas = {}
    for arbol, pct in porcentajes.items():
        areas[arbol] = area_m2 * pct
    return areas

print("=== Programa de Reforestación SAR Estado de México ===")

hectareas = solicitar_hectareas()
area_m2 = hectareas * 10_000
porcentajes = determinar_porcentajes(area_m2)
areas = calcular_areas(area_m2, porcentajes)

print(f"\nSuperficie total: {hectareas:.2f} ha ({area_m2:,.0f} m²)")
print("Por tipo de árbol a sembrar:")
for arbol, superficie in areas.items():
    hect = superficie / 10_000
    print(f" - {arbol.capitalize():8}: {superficie:,.0f} m² (~{hect:.2f} ha)")