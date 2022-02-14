import math
import random


def geometric_mean(a, b):
    if not (b > 0):
        raise Exception(f"Error {b} must be bigger than zero")

    return math.sqrt(a * b)


def arithmetic_mean(a, b):
    if not (b > 0):
        raise Exception(f"Error {b} must be bigger than zero")

    return (a + b) / 2


def answer_answer_a(a, b):
    m = arithmetic_mean(a, b)
    m2 = 2 * b
    if not math.isclose(m, m2):
        raise Exception(f"Answer a is wrong, a={a}, b={b}, m1={m}, m2={m2}")


def answer_answer_b(a, b):
    m = arithmetic_mean(a, b)
    m2 = 2 * a
    if not math.isclose(m, m2):
        raise Exception(f"Answer b is wrong, a={a}, b={b}, m1={m}, m2={m2}")


def answer_answer_c(a, b):
    m = geometric_mean(a, b)
    m2 = math.sqrt(3) * b

    if a > b and not math.isclose(m, m2):
        raise Exception(f"Answer c is wrong, a={a}, b={b}, m1={m}, m2={m2}")


def gen_a_b(l=100000):
    for i in range(l):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        if a + b == 2 * math.fabs(a-b) and b > 0:
            yield (a,b)


if __name__ == "__main__":

    for a,b in gen_a_b():
        print(f"{a}, {b}")
        answer_answer_c(a, b)
