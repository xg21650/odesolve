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


def solveto(f, x1, t1, t2, hmax, method=euler):
    def f(x, t):
        return x

    p = (t2 - t1) / hmax
    for i in np.arange(p):
        t = t1 + i
        print(t)
        if method == euler:
            temp = euler(f, x1, t, hmax)
            print(temp)
        else:
            temp = rk4(f, x1, t, hmax)

    return temp
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass



