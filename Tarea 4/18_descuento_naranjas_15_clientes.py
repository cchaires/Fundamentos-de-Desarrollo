
DESCUENTO = 0.15

def solicitar_precio() -> float:
    while True:
        try:
            p = float(input("Precio por kilo ($): "))
            if p > 0:
                return p
            print("Debe ser > 0.")
        except ValueError:
            print("Entrada inválida.")

def solicitar_kilos(cliente: int) -> float:
    while True:
        try:
            k = float(input(f"Kilos del cliente {cliente}: "))
            if k > 0:
                return k
            print("Debe ser > 0.")
        except ValueError:
            print("Entrada inválida.")

def procesar_ventas() -> None:
    precio = solicitar_precio()
    total_tienda = 0.0
    for i in range(1, 16):
        kilos = solicitar_kilos(i)
        subtotal = kilos * precio
        desc = DESCUENTO if kilos > 10 else 0.0
        pago = subtotal * (1 - desc)
        total_tienda += pago
        print(f"Cliente {i}: kilos={kilos:.2f}, desc={desc*100:.0f}%, paga=${pago:.2f}")
    print(f"\nTotal recibido por la tienda: ${total_tienda:.2f}")

print("=== Venta de naranjas (15 clientes) ===")
procesar_ventas()
