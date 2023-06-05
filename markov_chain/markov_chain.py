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
        if r < (beta * (S[-1] * I[-1]) / N) * timestep:
            Sprime -= 1
            Iprime += 1
        elif (
            r
            < (beta * (S[-1] * I[-1]) / N) * timestep
            + gamma * I[-1] * timestep
        ):
            Iprime -= 1
        Rprime = N - Sprime - Iprime
        S.append(Sprime)
        I.append(Iprime)
        R.append(Rprime)
    return (S, I, R)


N = 2000
I_0 = 15
beta = 0.6
gamma = 0.3
T = 100 * 24  # 100 days in seconds
timestep = 1
S, I, R = calculate_points(I_0, N, T, timestep, beta, gamma)
Trange = np.arange(0, T, timestep)
plt.plot(Trange, S, color="b")
plt.plot(Trange, I, color="r")
plt.plot(Trange, R, color="g")
plt.show()
