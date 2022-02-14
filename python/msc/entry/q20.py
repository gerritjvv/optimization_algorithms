import numpy as np

A = np.array([[1, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 1],
              [0, 0, 0, 0]])

k = 10
B = np.array([1, -1, k, 3])

print(np.linalg.solve(A, B))
