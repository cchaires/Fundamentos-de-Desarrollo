
V0 = 96

def h(t: int) -> int:
    return V0*t - 5*(t**2)

def imprimir_tabla_altura() -> None:
    print("t (s) | h(t) (m)")
    for t in range(1, 9):
        print(f"{t:>4} | {h(t):>7}")

print("=== Altura de la pelota (t=1..8 s) ===")
imprimir_tabla_altura()
