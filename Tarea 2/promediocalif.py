print("¡Bienvenido! ")

items = ["Examen", "Calificación 1", "Calificación 2", "Calificación 3"]
materias = ["Matemáticas", "Física", "Química"]

def leer_notas(materia, items):
    notas = []
    for item in items:
        entrada = input(f"Ingresa calificación de {item} de {materia}: ")
        notas.append(float(entrada))
    return notas

def promedio_ponderado(notas, peso_tareas=0.10, peso_examen=0.80):
    examen, *tareas = notas
    prom_tareas = sum(tareas) / len(tareas)
    return prom_tareas * peso_tareas + examen * peso_examen

calificaciones = { materia: leer_notas(materia, items) for materia in materias }

promedios = {}
for materia, notas in calificaciones.items():
    promedios[materia] = promedio_ponderado(notas)

promedio_general = sum(promedios.values()) / len(promedios)

for materia, prom in promedios.items():
    print(f"Promedio de {materia}: {prom:.2f}")
print(f"Promedio general: {promedio_general:.2f}")