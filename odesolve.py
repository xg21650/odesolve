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
    return x + f(x, t) * h
    pass


def rk4(f, x, t, h):
    k1 = f(x, t)
    k2 = f(x + k1 * h / 2, t + h / 2)
    k3 = f(x + k2 * h / 2, t + h / 2)
    k4 = f(x + k3 * h, t + h)
    return x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    pass


def solveto(f, x0, t0, t1, hmax, method=euler):

    h = hmax
    for i in np.arange(t0, t1, hmax):
        if method == euler:
            if i > t1 - hmax:
                h = t1 - i
            x0 = euler(f, x0, i, h)
            pass

        else:
            if i > t1 - hmax:
                h = t1 - i
            x0 = rk4(f, x0, i, h)
            pass
    return x0
    pass


def odesolve(f, x0, tvals, hmax, method=euler):
    X0 = np.array([x0])
    tvals = np.linspace(0, 1, 5)
    for i in range(0, len(tvals) - 1):
        if method == euler:
            Xt = solveto(f, x0, tvals[i], tvals[i + 1], hmax)
            print(Xt)
        else:
            Xt = solveto(f, X0, tvals[i], tvals[i + 1], hmax, rk4)
        X0 = np.append(X0, [Xt])

    plt.plot(tvals, X0.T)
    # plt.savefig('shm.pdf')
    plt.show()
    pass


def error(f, x0, t0, t1):
    hmax = (t1 - t0) / 100
    x1 = 0
    y1 = 0
    X0 = numpy.array([x1])
    Y0 = numpy.array([y1])
    for i in range(100):
        hmax = (i * hmax) + t0
        x1 = euler(f, x0, t0, hmax)
        y1 = rk4(f, x0, t0, hmax)
        X0 = np.append(x1)
        Y0 = np.append(y1)

    e = 2.718281828459045

    errorEuler = e - solveto(f, X0, t0, t1, hmax)
    errorRK4 = e - solveto(f, X0, t0, t1, hmax, rk4)
    print(errorEuler)
    print(errorRK4)
    if errorEuler < 0:
        errorEuler = -errorEuler
        pass
    elif errorRK4 < 0:
        errorRK4 = -errorRK4
        pass
    plt.plot(errorEuler, color='blue')
    plt.plot(errorRK4, color='orange')
    pass


