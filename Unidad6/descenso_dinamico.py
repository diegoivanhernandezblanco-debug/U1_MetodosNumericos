import numpy as np

def f(t,w):
    return -0.3*w

t = 0
w = 5

h = 0.2

n = 20

for i in range(n):

    w = w + h*f(t,w)

    t = t + h

    print("t =",t," w =",w)