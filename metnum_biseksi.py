import sympy as sp
import tabulate as tb

x = sp.symbols('x')

def metode_biseksi(function, a, b, tol):
  data = []
  headers = ["Iterasi", "a", "b", "c", "fc", "Lebar Interval"]
  f = sp.lambdify(x, function)
  fa = f(a)
  fb = f(b)
  
  if fa * fb >= 0:
    return "Tidak mengandung akar"
  
  iterasi = 1
  
  while (b - a)/2 > tol: # pake (b - a) / 2 karena kan kita gatahu secara pasti akar nya ada dimana, nah kita berdiri ditengah, gaperlu kita ngecek dari interval a ke b, lebih baik berdiri di tengah dan memantau dan tangkep akar dari tengah daripada ngecek semua tempat
    c = (a + b)/2
    fc = f(c)
    
    data.append([iterasi, a, b, c, fc, (b-a)])
    if fc == 0:
      break
    elif fa * fc < 0:
      b = c
      fb = fc
    else:
      a = c
      fa = fc
      
    iterasi += 1
  print(tb.tabulate(data, headers = headers, tablefmt="psql"))
  return f"Nilai c mendekati akar: {c}"
        
#aa = metode_biseksi(x**3 - x - 1, 1, 2, 0.000001)

#print(aa)