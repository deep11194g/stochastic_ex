import numpy as np
from matplotlib import pyplot as plt


def get_propensities(x):
    """
    Get Propensity vector "a" for a given state "x"

    :param x: State Vector  [D, M, P]
    :return: Propensity Vector
    """
    kD, kM, dM, dP = 0.5, 0.05, 0.1, 0.1
    return np.array([
        kD * x[0],  # a1 = kD * D
        kM * x[1],  # a2 = kM * M
        dM * x[1],  # a3 = kM * M
        dP * x[2],  # a4 = dP * P
    ])


def first_reaction_method(x0, nu, tf):
    """
    Sample Chemical Reaction Network using FRM algorithm

    :param x0: Initial state vector with reactant/product concentration
    :param nu: Reaction Stochiometry matrix
    :param tf: Final time for the reaction to end
    :return: Timesteps and state chain for each reaction occurrence
    """
    x_chain = np.array([x0])  # State chain of reaction; Each column is for a species
    timesteps = [0]  # Cumulative time step for each reaction occurrence
    while timesteps[-1] < tf:
        a_mu = get_propensities(x_chain[-1])
        uni_rand_nos = np.random.uniform(low=0, high=1, size=len(a_mu))
        tau_mu = (1 / a_mu) * np.log(1 / uni_rand_nos)
        next_mu_idx = np.argmin(tau_mu)
        nu_mu = nu[next_mu_idx]
        x_chain = np.vstack([x_chain, x_chain[-1] + nu_mu])
        timesteps.append(timesteps[-1] + tau_mu[next_mu_idx])
    return timesteps, x_chain


def direct_method(x0, nu, tf):
    """
    Sample Chemical Reaction Network using Direct Method algorithm

    :param x0: Initial state vector with reactant/product concentration
    :param nu: Reaction Stochiometry matrix
    :param tf: Final time for the reaction to end
    :return: Timesteps and state chain for each reaction occurrence
    """
    x_chain = np.array([x0])  # State chain of reaction; Each column is for a species
    timesteps = [0]  # Cumulative time step for each reaction occurrence
    while timesteps[-1] < tf:
        a_mu = get_propensities(x_chain[-1])
        a = np.sum(a_mu)
        r1, r2 = np.random.uniform(low=0, high=1, size=2)
        min_mu_idx = np.where((np.cumsum(a_mu) > r1 * a))[0][0]
        tau = np.log(1 / r2) / a
        nu_mu = nu[min_mu_idx]
        x_chain = np.vstack([x_chain, x_chain[-1] + nu_mu])
        timesteps.append(timesteps[-1] + tau)
    return timesteps, x_chain


if __name__ == "__main__":
    sample_nu_minus = np.array([  # Reactant Stochiometry; Each column is for a species
        [1, 0, 0],  # Reaction: D --(kD)--> D + M
        [0, 1, 0],  # Reaction: M --(kM)--> M + P
        [0, 1, 0],  # Reaction: M --(dM)--> {0}
        [0, 0, 1]   # Reaction: P --(dP)--> {0}
    ])
    sample_nu_plus = [  # Product Stochiometry
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]
    sample_nu = sample_nu_plus - sample_nu_minus  # Reaction Stochiometry
    sample_x0 = [10, 10, 10]  # Initial State of Concentration: [D, M, P]
    sample_tf = 100  # Maximum time for reaction

    t, x_chain = direct_method(x0=sample_x0, nu=sample_nu, tf=sample_tf)
    plt.plot(t, x_chain[:, 0], c='g')
    plt.plot(t, x_chain[:, 1], c='b')
    plt.plot(t, x_chain[:, 2], c='r')
    plt.show()
