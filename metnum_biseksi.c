#include <stdio.h>
#include "tinyexpr.h"

int main()
{
  // Kamus
  double x, a, b, tol;
  char *persamaan = "x*x + 2*x - 1";

  // Algoritma
  a = 0;
  b = 1;
  tol = 0.0001;
  //Ubah x jadi x matematis
  te_variable vars[] = {{"x", &x}};
  //Mengubah fungsi string menjadi fungsi asli
  te_expr *expr = te_compile(persamaan, vars, 1, 0);

  x = a;
  double fa = te_eval(expr);
  x = b;
  double fb = te_eval(expr);

  if (fa * fb >= 0){
    printf("Tidak mengandung akar");
    return 0;
    
  }
  // int iterasi = 1;

  while ((b - a)/2 > tol){
    double c = (a + b)/2;
    x = c;
    double fc = te_eval(expr);

    if (fc == 0){
      break;
    }
    else if(fc * fa < 0){
      b = c;
      fb = fc;
    } else {
      a = c;
      fa = fc;
    }
    // iterasi += 1;
  }
  printf("Nilai c mendekati akar: %f", (a+b)/2);
  te_free(expr);
  return 0;
}