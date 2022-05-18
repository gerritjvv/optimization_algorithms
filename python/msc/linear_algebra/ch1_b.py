import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [2, -1],
    [2, 8],
    [7, 5]
])


print("(AB)_1,1")
print(A[0,:], B[:,0], " = ", np.dot(A[0,:], B[:,0]))

print("(AB)_1,2")
print(A[0,:], B[:,1], " = ", np.dot(A[0,:], B[:,1]))

print("(AB)_2,1")
print(A[1,:], B[:,0], " = ", np.dot(A[1,:], B[:,0]))

print("(AB)_2,2")
print(A[1,:], B[:,1], " = ", np.dot(A[1,:], B[:,1]))

print()
print("AB")
print(np.dot(A, B))
