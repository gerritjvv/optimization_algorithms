"""
The idea is that we can cancel two numbers a and b using the following:

To make:

a + b = 0

multiply each by the other:

a*b + - b*a = 0

no matter what the value of a or b the equation will always equal 0.

This can be expressed in linear algebra as:

dot( [a b], [-b a]) <-- see how we swapped [a b].

To rotate a vector like that we need to use the following kernel:
[0  -1
 1  0]

Thus dot ( [0 -1; 1 0], [a b] ) = > [-b a]

Then if we do

v = [a b]
dot( dot ( kernel, v), v) => 0

we always get zero.
"""
import numpy as np

a = 2
b = 3

A = np.array([a, b])

kernel = [[0, -1],
          [1, 0]]

print(f"A: {A}")

result = np.dot(kernel, A)

print(f"kernel . A = {result}")

result = np.dot(result, A)

print(f" -kernel . A . A : {result}")
