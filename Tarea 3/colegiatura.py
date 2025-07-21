import random

materias = {
    "Matemáticas": random.randint(6, 10),
    "Historia": random.randint(6, 10),
    "Ciencias": random.randint(6, 10),
    "Literatura": random.randint(6, 10)
}
costo_materias = random.randint(100, 500)

def calcular_promedio(materias):
    total = sum(materias.values())
    promedio = total / len(materias)
    return promedio

def determinar_descuento(promedio):
    if promedio >= 9:
        print("¡Felicidades! Tienes un descuento del 30% en la colegiatura y no pagas IVA.")
        descuento, iva = 0.3, 0
        return descuento, iva
    else:
        print("No tienes descuento en la colegiatura, pero pagas IVA del 10%.")
        descuento, iva = 0, 0.1
        return descuento, iva

def calcular_costo_final(costo_materias, descuento, iva):
    costo_desc = (costo_materias * len(materias)) * (1 - descuento)
    return costo_desc * (1 + iva)

print("Bienvenido al programa de cálculo de colegiatura")

promedio = calcular_promedio(materias)
print(f"Tu promedio de materias es: {promedio:.2f}")

descuento, iva = determinar_descuento(promedio)

costo_final = calcular_costo_final(costo_materias, descuento, iva)
print(f"El costo de tus materias es: ${costo_materias:.2f}")
print(f"El costo final de tu colegiatura es: ${costo_final:.2f}")