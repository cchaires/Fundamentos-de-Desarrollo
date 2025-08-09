
def imprimir_alfabeto_desc() -> None:
    for codigo in range(ord('Z'), ord('A') - 1, -1):
        print(chr(codigo))

print("=== Alfabeto descendente ===")
imprimir_alfabeto_desc()
