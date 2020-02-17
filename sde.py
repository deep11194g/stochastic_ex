import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def analytic_solution(mu, sigma, dt, x0):
    t = np.arange(0, 1, dt)
    n = int(1 / dt)
    dwt = np.random.normal(0, np.sqrt(dt), n)
    w = np.cumsum(dwt)
    xt = x0 * np.exp((mu - (sigma ** 2) / 2) * t + sigma * w)
    plt.plot(t, xt)
    plt.xlabel("t")
    plt.ylabel("X(t)")
    plt.show()
    return dwt, xt


def euler_wanyama_solution(mu, sigma, dt, x0, dwt):
    n = int(1 / dt)
    xt = [x0]
    for i in range(1, n):
        xt.append(xt[i - 1] + mu * xt[i - 1] * dt + sigma * xt[i - 1] * dwt[i - 1])
    plt.plot(np.arange(0, 1, dt), xt)
    plt.xlabel("t")
    plt.ylabel("X(t)")
    plt.show()
    return xt


def milstein_solution(mu, sigma, dt, x0, dwt):
    n = int(1 / dt)
    np.random.normal(5, 4)
    xt = [x0]
    d_sigma = sigma
    for i in range(1, n):
        xn = xt[i - 1] + (mu * xt[i - 1] * dt) + (sigma * xt[i - 1] * dwt[i - 1]) + (0.5 * d_sigma * sigma * (
                dwt[i - 1] ** 2 - dt))
        xt.append(xn)
    plt.plot(np.arange(0, 1, dt), xt)
    plt.xlabel("t")
    plt.ylabel("X(t)")
    plt.show()


if __name__ == "__main__":
    mu = 0.3
    sigma = 0.4
    dts = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05]
    x0 = 0.1
    mean_errors = []
    for dt in dts:
        dwt, xt1 = analytic_solution(mu, sigma, dt, x0)
        xt2 = euler_wanyama_solution(mu, sigma, dt, x0, dwt)
        mean_errors.append((np.mean(np.abs(xt1 - xt2))))
    x = np.log(dts)
    y = np.log(mean_errors)
    plt.plot(dts, mean_errors)
    plt.show()
    print(linregress(x, y))
    # milstein_solution(mu, sigma, dt, x0, dwt)
