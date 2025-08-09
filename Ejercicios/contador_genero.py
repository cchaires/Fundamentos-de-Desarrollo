hombres = 0
mujeres = 0
usuarios_validos = 0
intentos_invalidos = 0
edad = {"H": [], "M": []}
print("Ingrese el género de 5 usuarios (H para hombre, M para mujer): ")
while usuarios_validos < 5:
    genero = input(f"Ingrese el género del usuario {usuarios_validos + 1} (H/M): ").strip().upper()
    flag = True
    if genero == "H":
        hombres += 1
        usuarios_validos += 1
        ehombre = input(f"Ingrese la edad del usuario {usuarios_validos} (debe ser un número): ")
        edad["H"].append(ehombre)
    elif genero == "M":
        mujeres += 1
        usuarios_validos += 1
        medad = input(f"Ingrese la edad del usuario {usuarios_validos} (debe ser un número): ")
        edad["M"].append(medad)
    else:
        print("Género no válido. Por favor, ingrese 'H' para hombre o 'M' para mujer.")
        intentos_invalidos += 1

promedio_hombres = sum(int(e) for e in edad["H"]) / len(edad["H"]) if edad["H"] else 0
promedio_mujeres = sum(int(e) for e in edad["M"]) / len(edad["M"]) if edad["M"] else 0
menor_edad_hombres = min(int(e) for e in edad["H"]) if edad["H"] else None
menor_edad_mujeres = min(int(e) for e in edad["M"]) if edad["M"] else None

mayor_edad_hombres = max(int(e) for e in edad["H"]) if edad["H"] else None
mayor_edad_mujeres = max(int(e) for e in edad["M"]) if edad["M"] else None
print(f"Total de hombres: {hombres}, Total de mujeres: {mujeres}, Intentos inválidos: {intentos_invalidos}, Edades de hombres: {edad['H']}, Edades de mujeres: {edad['M']}")
print(f"Promedio de edad de hombres: {promedio_hombres: .2f}, Promedio de edad de mujeres: {promedio_mujeres: .2f}")
print(f"Menor edad de hombres: {menor_edad_hombres}, Menor edad de mujeres: {menor_edad_mujeres}")
print(f"Mayor edad de hombres: {mayor_edad_hombres}, Mayor edad de mujeres: {mayor_edad_mujeres}")