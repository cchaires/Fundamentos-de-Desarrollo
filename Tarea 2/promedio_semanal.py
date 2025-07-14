lun, mie, vie = map(float, input("Ingresa los tiempos de Lunes, Miercoles y Viernes separados de una coma: ").split())
promedio = (lun + mie + vie) / 3
print(f"El promedio del tiempo de la semana fue: {promedio}")
