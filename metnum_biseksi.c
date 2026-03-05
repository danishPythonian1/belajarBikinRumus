#include <stdio.h>
#include "tinyexpr.h"

int main()
{

  double x;
  int a;
  int b;
  float tol;
  char *persamaan = "x*x + 2*x - 1";

  // Untuk bikin x agar bisa dibaca komputer
  te_variable vars[] = {{"x", &x}};

  // Mengcompile fungsi string menjadi fungsi asli
  te_expr *expr = te_compile(persamaan, vars, 1, 0);

  x = 5;
  double hasil = te_eval(expr);
  printf("f(5): %f\n", hasil);

  te_free(expr);
  return 0;
}
