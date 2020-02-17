import random
import statistics
import numpy as np
import matplotlib.pyplot as plt


def f1_x(x):
    return x * x


def f2_x(x):
    return 10 * x - x * x


def f3_x(x):
    return np.exp(x)


SAMPLE_SIZE = 100
N = 100


def my_monte_carlo():
    sample_xs = []
    sample_ys = []

    expectation_sum = 0

    for _ in range(N):
        for _ in range(SAMPLE_SIZE):
            x = random.normalvariate(5, 4)
            sample_xs.append(x)
            sample_ys.append(f2_x(x))
        expectation = statistics.mean(sample_ys)
        expectation_sum += expectation

    print(expectation_sum / N)


def prof_monte_carlo(a, b, n):
    array_x = np.random.uniform(a, b, n)
    array_f_x = f3_x(array_x)
    exp = (b - a) / n * np.sum(array_f_x)
    var = np.sum((array_f_x - exp) ** 2) / (n - 1) / n
    return exp, var


def sample_plot():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()


sample_plot()