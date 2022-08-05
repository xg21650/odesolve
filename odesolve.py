# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py


# Define parameters
import numpy as np
import matplotlib.pyplot as plt


def euler(f, x, t, h):
    return x + f(x, t) * h  # returns a step of the euler method
    pass


def rk4(f, x, t, h):
    k1 = f(x, t)
    k2 = f(x + k1 * h / 2, t + h / 2)
    k3 = f(x + k2 * h / 2, t + h / 2)
    k4 = f(x + k3 * h, t + h)
    return x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)  # returns a step of the rk4 method
    pass


def solveto(f, x0, t0, t1, hmax, method=euler):
    h = hmax
    for i in np.arange(t0, t1, hmax):  # repeats for each equal interval between t0 and t1
        if method == euler:
            if i > t1 - hmax:  # checks if the step size is not divisible by t1
                h = t1 - i  # adjusts h so that the final step size will land on t1
            x0 = euler(f, x0, i, h)  # performs euler method
            pass
        else:
            if i > t1 - hmax:
                h = t1 - i
            x0 = rk4(f, x0, i, h)  # performs rk4 method
            pass
    return x0
    pass


def odesolve(f, x0, tvals, hmax, method=euler):
    X0 = np.array([x0])  # creates an array with starting x0
    for i in range(len(tvals) - 1):  # repeats for each element in tvals
        if method == euler:
            Xt = solveto(f, x0[0], tvals[0], tvals[i + 1], hmax)
            X0 = np.append(X0, [Xt])  # appends new value Xt to the array
        else:
            Xt = solveto(f, x0[0], tvals[0], tvals[i + 1], hmax, rk4)
            X0 = np.append(X0, [Xt])
    plt.plot(tvals, X0.T)
    plt.savefig('shm.pdf')
    plt.show()
    pass
    return X0  # returns the completed array







