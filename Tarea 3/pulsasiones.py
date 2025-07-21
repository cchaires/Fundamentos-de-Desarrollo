HOMBRE_PUL = 210
MUJER_PUL = 220
pulsaciones = 0
edad = 0
sexo = ""

print("Bienvenido al programa de cálculo de pulsaciones")

sexo = input("¿Eres hombre o mujer? (h/m): ").strip().lower()
edad = int(input("¿Cuál es tu edad? "))

if sexo == 'h':
    pulsaciones = (HOMBRE_PUL - edad) / 10
elif sexo == 'm':
    pulsaciones = (MUJER_PUL - edad) / 10
else:
    print("Sexo no reconocido. Por favor, ingresa 'h' para hombre o 'm' para mujer.")
    exit()

print(f"Tu número de pulsaciones es: {pulsaciones}")