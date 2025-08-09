print("Pedir numeros al usuario y sumarlos, hasta que el usuario ingrese 0")
suma = 0
contador = 0

n = input("Ingresa un número (0 para terminar): ") 
while n != "0":
    try:
        suma += n
        contador += 1
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")
    
    n = input("Ingresa otro número (0 para terminar): ")

print(f"La suma de los números ingresados es: {suma} y la cantidad de números ingresados es: {contador}")
