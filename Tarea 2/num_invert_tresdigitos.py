n = int(input("Ingresa un número de tres dígitos: "))
centenas = n // 100
decenas  = (n // 10) % 10
unidades = n % 10
invertido = unidades * 100 + decenas * 10 + centenas
print(f"El número invertido es: {invertido}")
