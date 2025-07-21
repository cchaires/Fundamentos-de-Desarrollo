
print("Bienvenido al programa SAR (Sistema de Ahorro para el Retiro)")

salario = float(input("Ingresa tu salario mensual: "))
porcentaje_empresa = float(input("Ingresa el porcentaje obligatorio que deposita la empresa (sin %): "))

print("\n¿Cómo deseas aportar a tu cuenta SAR?")
print("1. Cuota fija")
print("2. Porcentaje de tu salario")
opcion = input("Selecciona 1 o 2: ").strip()

if opcion == "1":
    aporte_trabajador = float(input("Ingresa la cuota fija mensual que deseas aportar: "))
elif opcion == "2":
    pct = float(input("Ingresa el porcentaje que deseas aportar (sin %): "))
    aporte_trabajador = salario * pct / 100
else:
    print("Opción no válida. Terminando el programa.")
    exit()

aporte_empresa = salario * porcentaje_empresa / 100
total_SAR = aporte_empresa + aporte_trabajador
pago_neto = salario - aporte_trabajador

print("\n===== Resumen de aportaciones =====")
print(f"Aporte de la empresa al SAR:     ${aporte_empresa:.2f}")
print(f"Aporte del trabajador al SAR:    ${aporte_trabajador:.2f}")
print(f"Total depositado en tu cuenta:   ${total_SAR:.2f}")
print(f"Pago mensual neto que recibirás: ${pago_neto:.2f}")
print("===================================")