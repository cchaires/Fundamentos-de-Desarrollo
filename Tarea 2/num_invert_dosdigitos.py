n = int(input("Ingresa un número de dos dígitos: "))
decenas = n // 10
unidades = n % 10
invertido = unidades * 10 + decenas
print(f"El número invertido es: {invertido}")
