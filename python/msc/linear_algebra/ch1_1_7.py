import numpy as np


def f1(x, y, z):
    res = x + 3 * y + 2 * z
    return res, res == 5


def f2(x, y, z):
    res = 2 * x + -y + -z
    return res, res == 1


def f3(x, y, z):
    res = -x + 2 * y + z
    return res, res == 3


x = 0.75
y = 3.25
z = -2.75

print(f1(x, y, z))
print(f2(x, y, z))
print(f3(x, y, z))

b = np.array([5, 1, 3])
A = np.array([
    [1, 3, 2],
    [2, -1, -1],
    [-1, 2, 1]
])

sol2 = np.linalg.solve(A, b)
print(sol2)
print(A.dot(sol2))

# Ax = b
# inv(A)x = inv(A)b
# x = inv(A)b

print(np.linalg.inv(A).dot(b))

A2 = np.array([
    [1, 3, 2],
    [0, 3, 1],
    [0, 0, -4]
])

B2 = np.array([5,7,11])

print(np.linalg.solve(A2, B2))