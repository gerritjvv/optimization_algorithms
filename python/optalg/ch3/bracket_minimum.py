"""
From algorithm 3.1

This is my own rewrite of the algorithm to (a) further my own understanding, (b) add better debugging and
make it easier (for me) to read.
"""
from decimal import Decimal
from typing import Callable, Any


def step_decrease(f: Callable[[Any], Any], x, step=1e-2, step_multiplier=2, iteration_limit=100000000):
    """
    Continues to increment x with x + step till f(x) returns a value that is bigger than the previous value
    i.e
    stop when f(x) > f(x+s)
    step on x + step and for each step expand step with step * step_multiplier.

    We include a iteration_limit to avoid non terminating functions.
    :return (a, b, the step size at x, steps ran)
    """
    y_prev = f(x)
    a = x
    b = x

    for i in range(0, iteration_limit):
        b += step
        y_step = f(b)
        if y_step > y_prev:
            # we leave the x overstep here because we bracket over the minimum, otherwise we might under shoot it.
            return a, b, step, i

        a = b
        y_prev = y_step
        step *= step_multiplier

    return a, b, step, i


def bracket_minimum(f: Callable[[Any], Any], x=Decimal(0), step=Decimal(1e-2), step_multiplier=2,
                    iteration_limit=100000000):
    """
    Finds 2 points that contain the local minimum for the function.
    If the function f is convex the local minimum is a global minimum.

    :param f: the single variable function i.e f(x).
    :param x: initial value to start from
    :param step: the step size to start with
    :param step_multiplier: the step is expanded each iteration using step * step_multiplier
    :param iteration_limit: a safe fail to avoid run away functions
    :return: point_a, point_b, y_step found, iterations
    """
    y_a = f(x)
    y_b = f(x + step)

    if y_b > y_a:
        # we need to invert the step direction
        step *= -1
    # else keep step positive, as this decreases the function

    point_a, point_b, step_found, steps_run = step_decrease(f,
                                                            x=x,
                                                            step=step,
                                                            step_multiplier=step_multiplier,
                                                            iteration_limit=iteration_limit)

    return min(point_a, point_b), max(point_a, point_b), step_found, steps_run


if __name__ == "__main__":
    import time

    squared_1 = lambda x: x ** 3 + 2 * x ** 2 + x + 3

    start = time.time() * 1000
    a, b, step_found, steps_run = bracket_minimum(squared_1, x=Decimal(0))
    end = time.time() * 1000

    print(f"""
    Function x^3 + 2x^2 + x + 3, Diff: 3x^2 + 4x + 1
    Diff == zero at x = -1/3 
    Function bracket at:
    
    {a}, {b}
    
    steps run: {steps_run}
    final step size: {step_found}
    Ran: {end - start}ms
    """)
