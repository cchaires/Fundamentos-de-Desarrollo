llantas = int(input("¿Cuantas llantas deseas llevar? "))
precio = 0
total = 0
if llantas > 5:
    precio = 700
    total = llantas * precio
    print(f"Tu total es: {total: .2f}")
else:
    precio = 800
    total = llantas * precio
    print(f"tu total es: {total: .2f}")
