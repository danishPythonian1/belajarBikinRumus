import tabulate as tb
import sympy as sp

x = sp.symbols('x')

def metnum_newtonRaphson(function, a, b, tol):
  f = sp.lambdify(x, function)
  dff = sp.diff(function, x)
  df = sp.lambdify(x, dff)
  c1 = (a + b)/2
  
  headers = ["Iterasi", "c1", "c2", "f(c1)", "f(c2)", "Lebar Interval"]
  data = []
  
  iterasi = 1
  while True:
    fc1 = f(c1)
    dfc1 = df(c1)
    
    if dfc1 == 0:
      print("Turunan 0, diberhentikan")
      return None
    
    c2 = c1 - (fc1/dfc1)
    fc2 = f(c2)
    galat = abs(c2 - c1)
    data.append([iterasi, c1, c2, fc1, fc2, galat])
    
    if galat <= tol:
      print(tb.tabulate(data, headers=headers, tablefmt="psql"))
      print(f"\nNilai mendekati akar: {c2}")
      print(f"\nf(c): {fc2}")
      return c2
    iterasi += 1
    c1 = c2
    if iterasi > 100:
      print("Maksimum iterasi tercapai. Metode mungkin divergen.")
      break
    
    
# print(metnum_newtonRaphson(x**2 - 4, 2, 4, 0.00001))