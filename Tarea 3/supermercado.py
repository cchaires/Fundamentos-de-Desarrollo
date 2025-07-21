import random

print("Bienvenido al supermercado, si tu número sale mayor a 74 te ganas el 15% de descuento en tu compra, de lo contrario bye y pagas el total. ¡Suerte!")

random_num = random.randint(1, 100)
random_price = random.randint(500, 5000)
discount = 0
if random_num >= 74: 
    print(f"¡Ganaste el 20% de descuento en tu compra total!, tu número al azar fue: {random_num}")
    discount = random_price * 0.2
    
else:
    print(f"Ganaste el 15%, tu número al azar fue: {random_num}")
    discount = random_price * 0.15
    
print(f"El total de tu compra fue de: {random_price}, y el descuento será de: {discount}")