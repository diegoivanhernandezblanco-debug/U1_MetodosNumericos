import numpy as np

def f(x, y):
    return x + y

a, b = 0 ,1 
c, d = 0 ,1

n = 50 
m = 50

dx = (b - a) / n
dy = (d - c) / m

integral = 0

for i in range(n):
    for j in range(m):

        x = a + i * dx
        y = c + j * dy

        integral += f(x, y) * dx * dy

print("Integral doble aproximada:", integral)