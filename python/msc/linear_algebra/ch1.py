import numpy as np

O = np.zeros((2, 3))

A = np.array([
    [2, -2, 5],
    [0, -1, 7],
])

B = np.array([
    [-1, 3, 7],
    [2, -9, 6],
])

C = np.array([
    [9, 5, 8],
    [-6, -1, 6],
])

print("a) A + B")
print(A + B)
print()

print("b) (A + B) + C")
print((A + B) + C)
print()

print("c) A + (B + C)")
print(A + (B + C))
print()

print("d) B + (C + A)")
print(B + (C + A))
print()

print("e) C + O")
print(C + O)

print("f) B + B + B + B + B")
print(B + B + B + B + B)
print()

print("g) 5B")
print(5 * B)
print()

print("h) C + -C")
print(C + -C)
print()


