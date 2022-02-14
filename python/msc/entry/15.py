import numpy as np
import sympy as s


def f_a(a, b, x):
    return a * np.sin(2 * x) + b * np.cos(2 * x) - (x / 4.0) * np.cos(2 * x)


def f_da(a, b):
    x = s.Symbol('x')
    f = a * s.sin(2 * x) + b * s.cos(2 * x) - (x / 4.0) * s.cos(2 * x)

    f_prime = f.diff(x)
    print(f_prime)

    l = s.lambdify(x, f_prime)
    return l


def f_b(a, b, x):
    return a * np.sin(2 * x) + b * np.cos(2 * x) - (x / 4.0) * np.sin(2 * x)


def f_db(a, b):
    x = s.Symbol('x')
    f = a * s.sin(2 * x) + b * s.cos(2 * x) - (x / 4.0) * s.sin(2 * x)

    f_prime = f.diff(x)
    print(f_prime)

    l = s.lambdify(x, f_prime)
    return l


def f_c(a, b, x):
    return a * np.sin(2 * x) + b * np.cos(2 * x)


def f_dc(a, b):
    x = s.Symbol('x')
    f = a * s.sin(2 * x) + b * s.cos(2 * x)

    f_prime = f.diff(x)
    print(f_prime)

    l = s.lambdify(x, f_prime)
    return l


def f_d(a, b, x):
    return (a + b * x) * np.e ** (-2 * x) - (x / 4.0) * np.cos(2 * x)


def f_dd(a, b):
    x = s.Symbol('x')
    f = (a + b * x) * s.exp(-2 * x) - (x / 4.0) * s.cos(2 * x)

    f_prime = f.diff(x)
    print(f_prime)

    l = s.lambdify(x, f_prime)
    return l


# print(f_a(2, 2, 0))
# # 1
# print(f_b(2, 2, 0))
# # 1
# print(f_c(2, 2, 0))
# # 1
# print(f_d(2, 2, 0))
# 1

print(f_da(1, 1)(0))
print(f_db(1, 1)(0))
print(f_dc(1, 1)(0))
print(f_dd(1, 1)(0))
