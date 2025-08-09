
def solicitar_numero(idx: int) -> float:
    while True:
        try:
            return float(input(f"Ingrese el número {idx}: "))
        except ValueError:
            print("Entrada inválida.")

def medias_positivos_negativos() -> tuple[float, float]:
    suma_pos = suma_neg = 0.0
    cnt_pos = cnt_neg = 0
    for i in range(1, 101):
        x = solicitar_numero(i)
        if x > 0:
            suma_pos += x
            cnt_pos += 1
        elif x < 0:
            suma_neg += x
            cnt_neg += 1
    media_pos = (suma_pos / cnt_pos) if cnt_pos else 0.0
    media_neg = (suma_neg / cnt_neg) if cnt_neg else 0.0
    return media_pos, media_neg

print("=== Medias de positivos y negativos (100 números) ===")
mp, mn = medias_positivos_negativos()
print(f"Media de positivos: {mp}")
print(f"Media de negativos: {mn}")
