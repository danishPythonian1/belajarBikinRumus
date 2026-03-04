import sympy as sp
import tabulate as tb

x = sp.symbols('x')

def metode_biseksi(function, a, b, tol):
  data = []
  headers = ["Iterasi", "a", "b", "c", "fc"]
  f = sp.lambdify(x, function)
  fa = f(a)
  fb = f(b)
  
  if fa * fb >= 0:
    return "Tidak mengandung akar"
  
  iterasi = 1
  
  while abs(b - a) > tol:
    c = round((a + b)/2, 10)
    fc = round(f(c), 10)
    
    data.append([iterasi, a, b, c, fc])
    
    if fc < 0 and fa < 0:
      fa = fc
      a = c
    else:
      fb = fc
      b = c
    
    iterasi += 1
  print(tb.tabulate(data, headers = headers, tablefmt="psql"))
  return f"Nilai c mendekati akar: {c}"
        
# aa = metode_biseksi(x**3 - x - 1, 1, 2, 0.000001)

# print(aa)
a = "hello guys"
print(a)


