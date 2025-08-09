
CATS = [
    ("Niños",   0, 12),
    ("Jóvenes", 13, 29),
    ("Adultos", 30, 59),
    ("Viejos",  60, 200),
]

def solicitar_persona(i: int) -> tuple[int, float]:
    while True:
        try:
            edad = int(input(f"Persona {i} - Edad: "))
            peso = float(input(f"Persona {i} - Peso (kg): "))
            if edad < 0 or peso <= 0:
                print("Edad/Peso inválidos.")
                continue
            return edad, peso
        except ValueError:
            print("Entrada inválida.")

def indice_categoria(edad: int) -> int:
    for idx, (_, a, b) in enumerate(CATS):
        if a <= edad <= b:
            return idx
    return len(CATS) - 1

def promedios_por_categoria() -> None:
    sumas = [0.0]*len(CATS)
    cuentas = [0]*len(CATS)
    for i in range(1, 51):
        edad, peso = solicitar_persona(i)
        j = indice_categoria(edad)
        sumas[j] += peso
        cuentas[j] += 1
    print("\nPromedios:")
    for (nombre, _, _), s, c in zip(CATS, sumas, cuentas):
        promedio = s / c if c else 0.0
        print(f"{nombre}: {promedio:.2f} kg (n={c})")

print("=== Promedio de peso por categoría (50 personas) ===")
promedios_por_categoria()
