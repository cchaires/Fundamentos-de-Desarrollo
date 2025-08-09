
MIN_APROBADO = 60.0

def solicitar_calificacion(i: int) -> float:
    while True:
        try:
            c = float(input(f"  Calificación {i}: "))
            if 0 <= c <= 100:
                return c
            print("Debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida.")

def evaluar_grupo() -> None:
    aprobados = 0
    con_80_o_mas = 0
    for idx in range(1, 11):
        print(f"\nAlumno {idx}:")
        nombre = input("Nombre: ").strip()
        c1 = solicitar_calificacion(1)
        c2 = solicitar_calificacion(2)
        c3 = solicitar_calificacion(3)
        promedio = (c1 + c2 + c3) / 3
        estado = "APROBADO" if promedio >= MIN_APROBADO else "REPROBADO"
        if promedio >= MIN_APROBADO:
            aprobados += 1
        if promedio >= 80:
            con_80_o_mas += 1
        print(f"{nombre} -> [{c1}, {c2}, {c3}] Promedio: {promedio:.2f} -> {estado}")

    print("\n=== Resumen ===")
    print(f"Aprobados: {aprobados}")
    print(f"Con promedio >= 80: {con_80_o_mas}")

print("=== Calificaciones de 10 alumnos ===")
evaluar_grupo()
