# Q13

import numpy as np
import matplotlib.pyplot as plt


def f_x(a):
    def f(t):
        return a * np.cos(t) ** 3

    return f


def f_dx(a):
    def f(t):
        return a * -3 * np.sin(t) * (np.cos(t) ** 2)

    return f


def f_y(a):
    def f(t):
        return a * np.sin(t) ** 3

    return f


def f_dy(a):
    def f(t):
        return a * 3 * (np.sin(t) ** 2) * (np.cos(t))

    return f


def f_integrand(a):
    y_dy = f_dy(a);
    x_dx = f_dx(a);

    def f(t):
        return np.sqrt(x_dx(t) ** 2 + y_dy(t) ** 2)

    return f


def mc_integrate(f, a, b, n=1000000):
    # Monte Carlo
    vals = np.random.uniform(a, b, n)
    y = np.vectorize(f)(vals)

    y_mean = np.sum(y) / n
    integ = (b - a) * y_mean

    return integ


x = np.linspace(0, np.pi * 2)
y = np.vectorize(f_integrand(1))(x)

plt.plot(x, y)
plt.show()

mc_area = mc_integrate(f_integrand(1), 0, np.pi * 2)
print(f"MC Area: {mc_area}")


# 2 * np.sqrt(3) => 3.4641016151377544
# 3 * np.sqrt(3) => 5.196152422706632
# area is 6.0030577246980386

