import numpy as np
import random
import matplotlib.pyplot as plt


def calculate_points(I_0, N, T, timestep, beta, gamma):
    S = [N - I_0]
    I = [I_0]
    R = [0]
    for i in range(1, T, timestep):
        Sprime = S[-1]
        Iprime = I[-1]
        r = random.uniform(0, 1)
        p = (beta * (S[-1] * I[-1]) / N) * timestep
        p %= 1
        q = gamma * I[-1] * timestep
        q %= 1
        if r < p:
            Sprime -= 1
            Iprime += 1
        elif r < p + q:
            Iprime -= 1
        Rprime = N - Sprime - Iprime
        S.append(Sprime)
        I.append(Iprime)
        R.append(Rprime)
    return (S, I, R)


def average_over_datapoints(I_0, N, T, timestep, beta, gamma):
    Sprime, Iprime, Rprime = calculate_points(I_0, N, T, timestep, beta, gamma)
    for i in range(0, 100):
        S, I, R = calculate_points(I_0, N, T, timestep, beta, gamma)
        np.vstack((Sprime, S))
        np.vstack((Iprime, I))
        np.vstack((Rprime, R))
    S = np.matrix(Sprime).mean(0)
    I = np.matrix(Iprime).mean(0)
    R = np.matrix(Rprime).mean(0)
    return (S, I, R)


N = 2000
I_0 = 15
beta = 0.6
gamma = 0.3
T = 100 * 24 * 60  # 100 days in seconds
timestep = 1
S, I, R = average_over_datapoints(I_0, N, T, timestep, beta, gamma)
Trange = np.arange(0, T, timestep)
plt.plot(Trange, S.tolist()[0], color="b", label="S")
plt.plot(Trange, I.tolist()[0], color="r", label="I")
plt.plot(Trange, R.tolist()[0], color="g", label="R")
plt.legend()
plt.show()
