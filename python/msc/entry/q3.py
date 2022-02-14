# https://stackoverflow.com/questions/55881078/how-to-know-whether-a-function-is-continuous-with-sympy
from sympy import Symbol, S, limit
# from sympy.calculus.util import continuous_domain
import math

from python.msc.entry.plot import plot


def f1(x):
 if x > 0:
  return x * math.sin(1 / x)
 elif x == 0:
  return 0
 else:
  return -1 * (x / (1 + x ** 2))


def f(value):
 x = Symbol("x")

 if value > 0:
  f = x * math.sin(1 / x)
 elif value == 0:
  f = x * 0
 else:
  f = -1 * (x / (1 + x ** 2))

 return limit(f, x, value).is_real


if __name__ == "__main__":
 print(f(0))

 plot(fs=[f1], x=(-100, 100))
