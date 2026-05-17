import numpy as np

def f(x,y):
    return x + y

x = 0

y = 1

h = 0.1

n = 10

for i in range(n):

    k1 = f(x,y)

    k2 = f(x + h/2, y + h*k1/2)

    k3 = f(x + h/2, y + h*k2/2)

    k4 = f(x + h, y + h*k3)

    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    x = x + h

    print("x =",x," y =",y)