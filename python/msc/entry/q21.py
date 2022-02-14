import scipy as sci
import numpy as np

A = np.array([[1, 0, 0], [1, 1, 0], [0, 0, 1]])

B = np.array([[1, 0, 0], [1, -1, 0], [0, 0, 1]])

C = np.array([[1, 0, 1], [1, 0, -1], [0, 1, 0]])

D = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])


# print(np.linalg.norm(A))
# # 2
# print(np.linalg.norm(B))
# # 2
# print(np.linalg.norm(C))
# # 2.236
# print(np.linalg.norm(D))
# 2.449

def dot(r, s):
    print(f"{r} x {s}")
    return np.dot(s.T, r)

# print(dot(A[2], A[1]))
print(dot(D[2], D[1]))
print(dot(D[1], D[0]))
print(dot(D[1], D[1]))
