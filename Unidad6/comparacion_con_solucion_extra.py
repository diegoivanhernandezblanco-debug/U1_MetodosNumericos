import numpy as np

def f(x,y):
    return x + y

def exacta(x):
    return 2*np.exp(x) - x - 1

x = 0
y = 1
h = 0.1

for i in range(10):

    y = y + h*f(x,y)

    x = x + h

    real = exacta(x)

    error = abs(real-y)

    print("x =",x,
          "Euler =",y,
          "Exacta =",real,
          "Error =",error)