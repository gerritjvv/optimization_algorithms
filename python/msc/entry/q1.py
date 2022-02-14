import random

def f(n):
    """
     f (n) = 2f (n − 1) + 1; f (1) = 3.
    """
    if n == 0:
        return 1

    if n == 1:
        return 3

    return 2 * f(n-1) + 1


def answer(n):
    return 2**(n+1) - 1


if __name__ == "__main__":

    print(f(0))
    print(answer(0))

    for i in range(10000):
        n = random.randint(0, 400)
        y1 = f(n)
        y2 = answer(n)
        if y1 != y2:
            print(f"Incorrect: {n}, y1 = {y1}, y2 = {y2}")
            break