import math


def f(a):
    def f1(x):
        return a / (x * (2 * x + a))

    return f1


a_s = [
    2.0 * (math.e - 1.0),  # converges to 1.382...
    2.0 * (math.e + 1.0),  # converges to 2.01896...
    (1.0 / (2.0 * math.e)) - 2.0,  # converges to -10.7312...,
    0  # converted to 0
]

print(a_s)


def prn(v):
    for i in v:
        print(i)


def last(v):
    last = None
    for i in v:
        last = i
    return last


def partial_sums(f, x, n):
    s = 0
    for i in range(x, n):
        s += f(i)
        yield s

# 1.3821417675375067
# 1.382141922130512
# -10.722068840697396
# -10.731227509883656
# prn(partial_sums(f(a_s[3]), 1, 10))
