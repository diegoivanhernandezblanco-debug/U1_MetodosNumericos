import numpy as np

def f(t, w):
    return -0.5*w

t = 0

w = 10

h = 0.1

for i in range(20):

    w = w + h * f(t, w)

    t = t + h

    print("t = ", t, "w = ", w)