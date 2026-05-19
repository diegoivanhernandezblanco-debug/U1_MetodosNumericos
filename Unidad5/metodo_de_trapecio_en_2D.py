import numpy as np

def f(x, y):
    return x**2 + y**2

a, b = 0 ,1
c, d = 0 ,1

n = 50
m = 50

x = np.linspace(a, b, n)
y = np.linspace(c, d, m)

dx = (b - a) / (n-1)
dy = (d - c) / (m-1)

integral = 0
for i in range(n):
    for j in range(m):

        peso = 1

        if i == 0 or i == n-1:
            peso *= 0.5
        if j == 0 or j == m-1:
            peso *= 0.5

        integral += peso * f(x[i], y[j])

integral *= dx*dy

print("Integral (Trapecio 2D):", integral)