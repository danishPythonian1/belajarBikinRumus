import sympy as sp
import tabulate as tb

x = sp.symbols('x')

def metode_regulaFalsi(function, a, b, tol):
  f = sp.lambdify(x, function)
  fa = f(a)
  fb = f(b)
  
  if fa * fb >= 0:
    return "Tidak mengandung akar"
  c = b - ((fb*(b-a))/(fb-fa))
  fc = f(c)
  
  iterasi = 1
  
  headers = ["iterasi", "a", "b", "c", "fc"]
  data = [[iterasi, a, b, c, fc]]
  
  while abs(fc) > tol:
    if fc < 0 and fa < 0:
      fa = fc
      a = c
    else:
      fb = fc
      b = c
    c = b - ((fb*(b-a))/(fb-fa))
    fc = f(c)
    
    iterasi += 1
    
    data.append([iterasi, a, b, c, fc])
  tabelData = tb.tabulate(data, headers = headers, tablefmt="psql")
  print(tabelData)
  print(f"Nilai c mendekati akar: {c}")
  print(f"Nilai fc: {fc}")
  return ""

# print(metode_regulaFalsi(x**3 - x, -1, 1, 0.0001))

# print(metode_regulaFalsi(x**2 - 3, 1, 2, 0.000001))