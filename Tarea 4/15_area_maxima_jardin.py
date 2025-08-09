
def area(x: int) -> int:
    return x * (15 - x)

def tabla_y_maximo() -> None:
    print("x  |  Área")
    max_area = None
    x_max = None
    for x in range(10, 16):
        a = area(x)
        print(f"{x:2d} | {a:5d}")
        if max_area is None or a > max_area:
            max_area, x_max = a, x
    print(f"\nEl área máxima es {max_area} (x = {x_max})")

print("=== Área del jardín para x=10..15 ===")
tabla_y_maximo()
