import numpy as np

def f(x, y):
    return np.exp(-(x**2 + y**2))

a, b = -1, 1
c, d = -1, 1

n = 100
m = 100

dx = (b - a) / n
dy = (d - c) / m

integral = 0

for i in range(n):
    for j in range(m):

        x = a + i * dx
        y = c + j * dy

        integral += f(x, y) * dx * dy

print("Probabilidad aproximada:", integral)