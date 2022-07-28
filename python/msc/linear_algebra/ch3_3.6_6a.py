from sympy import Matrix

A = Matrix([[2, -1, -4, 13],
            [3, 3, -5, 13],
            [3, -4, 10, -10]])

print(A.rref())
print(A.rank())

A2 = Matrix(
    [[1, 2, 3, 4, 5, 6, 7],
     [8, 9, 10, 11, 12, 13, 14],
     [15, 16, 17, 18, 19, 20, 21],
     [22, 23, 24, 25, 26, 27, 28],
     [29, 30, 31, 32, 33, 34, 35]]
)

print(A2.rref())

print(f"A2 rank: {A2.rank()}")
