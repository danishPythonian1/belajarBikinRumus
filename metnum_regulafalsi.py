import sympy as sp
from tabulate import tabulate

x = sp.symbols('x')

def metode_regulaFalsi(expression, a, b, tol):
    f = sp.lambdify(x, expression)
    fa, fb = f(a), f(b)
    
    if fa * fb >= 0:
        return "Error: Tidak ada perubahan tanda di interval [a, b]. Akar mungkin tidak ada."

    iterasi = 0
    data = []
    
    c = a 
    fc = f(c)

    while True:
        # Rumus Regula Falsi
        c_lama = c
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)
        iterasi += 1
        
        lebar_interval = abs(b - a)
        data.append([iterasi, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{fc:.6e}", f"{lebar_interval:.6e}"])

        if abs(fc) < tol or abs(c - c_lama) < tol:
            break

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    headers = ["Iterasi", "a", "b", "c", "f(c)", "Lebar Interval"]
    print(tabulate(data, headers=headers, tablefmt="psql"))
    print(f"\nAkar ditemukan di x = {c}")
    print(f"Nilai f(c) = {fc}")
    return c

# Contoh Penggunaan:
# metode_regulaFalsi(x**3 - 2*x - 5, 2, 3, 0.0001)

# print(metode_regulaFalsi(x**3 - x, -1, 1, 0.0001))

print(metode_regulaFalsi(x**2 - 3, 1, 2, 0.000001))