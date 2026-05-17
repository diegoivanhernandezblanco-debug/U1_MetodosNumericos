import numpy as np

def f(x, y):
    return x + y

x = 0 
y = 1

h = 0.1

for i in range(5):

    y = y + h * f(x, y)

    x = x + h

    print("x = ", x, "y = ", y)