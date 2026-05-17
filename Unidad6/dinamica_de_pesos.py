import numpy as np

def f(t,w):
    return -0.5*w

t = 0

w = 10

h = 0.1

for i in range(20):

    k1 = f(t,w)

    k2 = f(t+h/2, w+h*k1/2)

    k3 = f(t+h/2, w+h*k2/2)

    k4 = f(t+h, w+h*k3)

    w = w + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    t = t + h

    print("t =",t," w =",w)