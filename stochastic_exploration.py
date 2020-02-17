import numpy
import matplotlib.pyplot as plt

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def func_h(x, y):
    p1 = ((x * numpy.sin(20 * y) + y * numpy.sin(20 * x)) ** 2) * numpy.cosh(x * numpy.sin(10 * x))
    p2 = ((x * numpy.cos(20 * y) - y * numpy.sin(10 * x)) ** 2) * numpy.cosh(y * numpy.cos(20 * y))
    return p1 + p2


if __name__ == "__main__":
    m = 100
    X = numpy.random.uniform(-0.5, 0.5, m)
    Y = numpy.random.uniform(-0.5, 0.5, m)
    h = func_h(X, Y)

    min_idx = numpy.argmin(h)
    print("Min value: {}; Min Index: {}".format(h[min_idx], min_idx))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(X, Y, h, c='g', marker='o')
    ax.scatter(X[min_idx], Y[min_idx], h[min_idx], c='r', marker='^')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('H(X, Y)')

    plt.show()
