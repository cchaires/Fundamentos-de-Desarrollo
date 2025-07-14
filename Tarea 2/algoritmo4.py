


num = int(input("ingresa el número a invertir \n"))
invertido = ""
if num > 999:
    print("ingresa otro número del rango 1 - 999")
else:
    for onenum in reversed(str(num)):
        invertido += onenum
           
print(invertido)
