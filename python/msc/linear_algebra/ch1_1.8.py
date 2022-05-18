import numpy as np

A = np.array([[1, 2], [-1, 4]])
b = np.array([3, 5])

A_inv = np.linalg.inv(A)

print(A_inv)

X = A_inv.dot(b)

print(X)

x = X[0]
y = X[1]

print(f"{x + 2 * y} == 3")
print(f"{-x + 4 * y} == 5")


print(np.linalg.solve(A, b))
