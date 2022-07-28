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

f = 0


def euler(f, x, t, h):
    def f(x, t):
        return x + t

    return x + f(x, t) * h
    pass


def rk4(f, x, t, h):
    def f(x, t):
        return x

    k1 = f(x, t)
    k2 = f(x + k1 * h / 2, t + h / 2)
    k3 = f(x + k2 * h / 2, t + h / 2)
    k4 = f(x + k3 * h, t + h)
    return x + (h / 6) * ((k1 + 2 * k2 + 2 * k3 + k4))
    pass


def solveto(f, x0, t0, t1, hmax, method=euler):
    def f(x, t):
        return x

    t = 0
    t1 += hmax
    for i in np.arange(t0, t1, hmax):
        t += i
        if method == euler:
            # don't know what to do here
            pass
        else:
            # don't know what to do here
            pass
    return x1
    pass


def f(X, t):
    x, y = X
    dxdt = y
    dydt = -x
    return np.array([dxdtm, dydt])


def odesolve(f, X0, t, hmax, method=euler):
    def f(X, t):
        x, y = X
        dxdt = y
        dydt = -x
        return np.array([dxdt, dydt])

    X0 = np.array([dxdt, dydt])
    h =
    t = np.linspace(0, 10, 100)

    Xt = odesolve(f, X0, t, h)

    plt.plot(t, Xt.T)
    plt.savefig('shm.pdf')
    plt.show()

    pass


def error:
    t0 = 0
    t1 = 1
    x0 = 0
    hmax = 0.01

    errorEuler = e - solveto(f, x0.t0, t1, hmax)
    errorRK4 = e - solveto(f, x0.t0, t1, hmax, rk4)
    if errorEuler < 0:
        errorEuler = -errorEuler
        pass
    elif errorRK4 < 0:
        errorRK4 = -errorRK4
        pass
    else:
        pass


