import numpy as np
from matplotlib import pyplot as plt


def f(x):
    p_e = np.exp(-(np.log(x)) ** 2 / 2)
    return p_e / (x * np.sqrt(2 * np.pi))


def get_mh_samples(k, x0):
    samples = [x0]
    for i in range(1, k):
        y_i = np.random.uniform(0, 5)
        ratio = f(y_i) / f(samples[i - 1])
        ro = min(1, ratio)

        u = np.random.uniform(0, 1)
        samples.append(y_i if u < ro else samples[i - 1])
    print(samples)
    return samples


def get_random_walk_mh_samples(k, x0):
    samples = [x0]
    for i in range(1, k):
        efsilon = np.random.normal(0, 0.02)
        y_i = samples[i - 1] + efsilon
        if y_i <= 0:
            samples.append(samples[i - 1])
            continue

        ratio = f(y_i) / f(samples[i - 1])
        ro = min(1, ratio)

        u = np.random.uniform(0, 1)
        samples.append(y_i if u < ro else samples[i - 1])
    return samples


if __name__ == "__main__":
    # chain = get_mh_samples(k=10, x0=5)
    chain = get_random_walk_mh_samples(k=1000, x0=5)
    plt.plot(chain)
    plt.show()
