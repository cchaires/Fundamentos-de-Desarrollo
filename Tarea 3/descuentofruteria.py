DESCUENTOS = [
    (0.0,    2.0,   0.00),  # 0 a 2 kg: 0%
    (2.01,   5.0,   0.10),  # 2.01 a 5 kg: 10%
    (5.01,  10.0,   0.15),  # 5.01 a 10 kg: 15%
    (10.01, float('inf'), 0.20),  # más de 10.01 kg: 20%
]


def solicitar_kilos() -> float:
    while True:
        try:
            kilos = float(input("Ingresa el número de kilos de manzanas: "))
            if kilos <= 0:
                print("Debe comprar al menos una cantidad positiva de kilos. Intenta de nuevo.")
                continue
            return kilos
        except ValueError:
            print("Entrada inválida. Ingresa un número válido de kilos.")


def solicitar_precio_por_kilo() -> float:
    while True:
        try:
            precio = float(input("Ingresa el precio por kilo de manzanas: $"))
            if precio <= 0:
                print("El precio debe ser mayor a 0. Intenta de nuevo.")
                continue
            return precio
        except ValueError:
            print("Entrada inválida. Ingresa un número válido de precio.")


def determinar_descuento(kilos: float) -> float:
    for minimo, maximo, pct in DESCUENTOS:
        if minimo <= kilos <= maximo:
            return pct
    return 0.0


def calcular_pago(kilos: float, precio: float, descuento: float) -> float:
    subtotal = kilos * precio
    monto_desc = subtotal * descuento
    return subtotal - monto_desc


def main() -> None:
    print("=== Cálculo de pago en frutería con descuento ===")

    kilos = solicitar_kilos()
    precio_kilo = solicitar_precio_por_kilo()
    pct_desc = determinar_descuento(kilos)
    total = calcular_pago(kilos, precio_kilo, pct_desc)
    print(f"\nKilos comprados: {kilos:.2f} kg")
    print(f"Precio por kilo:   ${precio_kilo:.2f}")
    print(f"Descuento:         {pct_desc*100:.0f}%")
    print(f"Total a pagar:     ${total:.2f}")

main()
