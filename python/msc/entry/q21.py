import numpy as np

A = np.array([[1, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 1],
              [0, 0, 0, 0]])

print(A.T)
k = 1
B = np.array([1, -1, k, 3])

print(np.linalg.solve(A, B))
