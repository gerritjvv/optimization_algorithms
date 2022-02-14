import math
from sympy import *

x = Symbol('x')
f = tan(x) ** 3

y = integrate(f, x)

print(y)


# log(cos(x) + 1/(2*cos(x)**2)

def primitive(x):
    return math.log(math.fabs(math.cos(x))) + 1 / (2.0 * math.cos(x) ** 2)

def ans_a(x):
    return (math.sin(x)**2 * math.tan(x)**2)/4.0

def ans_b(x):
    return math.log(math.fabs(math.cos(x))) - math.tan(x)**2

def ans_c(x):
    return 1/2.0 * math.tan(x)**2 + math.log(math.fabs(math.cos(x)))

def ans_d(x):
    return (math.sin(x)**4)/4


for i in range(0, 100):
    x = i
    print(f"{primitive(x)}, {ans_a(x)}, {ans_b(x)}, {ans_c(x)}, {ans_d(x)}")


