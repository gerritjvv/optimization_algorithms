# From algorithm 3.1
# We end up with 3 points, the range [a,b] and a point c that is f(a) < f(c) < f(b)
import math
from decimal import Decimal
from typing import Tuple, Callable, Any, List


def step_decrease(f: Callable[[Any], Any], x, step=1e-2, step_multiplier=2, iteration_limit=100000000):
    """
    Continues to increment x with x + step till f(x) returns a value that is bigger than the previous value
    i.e
    stop when f(x) > f(x+s)
    step on x + step and for each step expand step with step * step_multiplier.

    We include a iteration_limit to avoid non terminating functions.
    :return (x, the step size at x, steps ran)
    """
    y_prev = f(x)

    for i in range(0, iteration_limit):
        x += step
        y_step = f(x)

        if abs(y_step) > abs(y_prev):
            # we leave the x overstep here because we bracket over the minimum, otherwise we might under shoot it.
            return x, step, i

        y_prev = y_step
        step *= step_multiplier

    return x, step, i


def bracket_minimum(f: Callable[[Any], Any], x=Decimal(0), step=Decimal(1e-2), step_multiplier=2,
                    iteration_limit=100000000):
    y_a = f(x)
    y_b = f(x + step)

    point_a = x

    if y_b > y_a:
        # we need to invert the step direction
        step *= -1
    # else keep step positive, as this decreases the function

    point_b, step_found, steps_run = step_decrease(f, x=x, step=step, step_multiplier=step_multiplier,
                                                   iteration_limit=iteration_limit)

    return (min(point_a, point_b), max(point_a, point_b), step_found, steps_run)


if __name__ == "__main__":
    squared_1 = lambda x: x ** 3 + 2 * x ** 2 + x + 3

    a, b, step_found, steps_run = bracket_minimum(squared_1, x=Decimal(0))

    print(f"""
    Function x**2 + x + 1, Diff: 3x^2 + 2x + 1
    Diff == zero at x = -1/3 
    Function bracket at:
    
    {a}, {b}
    
    steps run: {steps_run}
    final step size: {step_found}
    """)
