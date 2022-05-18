import numpy as np

A = np.array([[2, -5], [-6, 1]])


A_inv = np.linalg.inv(A)
print(A_inv)

b = np.array([3, -1])

print(A_inv.dot(b))