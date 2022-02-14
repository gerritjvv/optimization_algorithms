import math

import mpmath
import scipy.integrate as integrate


def f(x):
 return mpmath.sec(x)

def f_a(x):
 return mpmath.sec(x) * mpmath.tan(x)

def f_b(x):
 return mpmath.cos(x)

def f_c(x):
 return mpmath.sec(x)

def f_d(x):
 return mpmath.log(mpmath.cos(x))

if __name__ == "__main__":
 i = integrate.quad(f, 0, 1)
 print(i)
 print(integrate.quad(f_a, 0, 1))
 print(integrate.quad(f_b, 0, 1))
 print(integrate.quad(f_c, 0, 1))
 print(integrate.quad(f_d, 0, 1))
