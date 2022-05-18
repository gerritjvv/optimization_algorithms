import numpy as np
import matplotlib.pyplot as plt

norm = np.linalg.norm


def a():
    """
    45 degrees
    """
    u = np.array([1, 1])
    v = np.array([0, 1])

    origin = np.array([[0, 0], [0, 0]])  # origin point
    plt.quiver(*origin, u, v, color=['r', 'b'], scale=1)
    plt.show()

    print(np.dot(u, v))

    angle = np.degrees(np.arccos((np.dot(u, v)) / (norm(u) * norm(v))))
    print(angle)


def c():
    """
    168.69 degrees
    """
    u = np.array([-2, 3])
    v = np.array([1 / 2, -1 / 2])
    origin = np.array([[0, 0], [0, 0]])  # origin point
    plt.quiver(*origin, u, v, color=['g', 'y'], scale=1)
    plt.show()

    angle = np.degrees(np.arccos((np.dot(u, v) / (norm(u) * norm(v)))))

    print(angle)


def two_a():
    """
    55.902
    """
    u = np.array([-1, 1, 3])
    v = np.array([3, -1, 5])

    d = np.dot(u, v)
    n = norm(u) * norm(v)
    angle = np.degrees(
        np.arccos(d / n)
    )

    origin = [[0, 0, 0], [0, 0, 0]]

    plt.quiver(*origin, u, v, color=['r', 'g', 'b'], scale=1)
    plt.show()
    print(angle)


def two_b():
    """
    90.0
    """
    u = np.array([1, 0, 0])
    v = np.array([0, 0, 15])

    d = np.dot(u, v)
    n = norm(u) * norm(v)
    angle = np.degrees(np.arccos(d / n))

    origin = [[0, 0, 0], [0, 0, 0]]
    plt.quiver(*origin, u, v, color=['r', 'b', 'g'], scale=1)
    plt.show()
    print(angle)


def two_c():
    """
    64.623
    """
    u = np.array([-1, 2, 3])
    v = np.array([np.sqrt(2), 1 / np.sqrt(2), 1])

    d = np.dot(u,v)
    n = norm(u) * norm(v)

    origin = np.zeros((2,3))

    plt.quiver(*origin, u, v, color=['r', 'b', 'g'], scale=1)
    plt.show()

    angle = np.degrees(np.arccos(d/n))
    print(angle)

two_c()
