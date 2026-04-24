import numpy as np

def f(x):
    return x**2

a = 0
b = 2
n = 100

h = (b - a) / n

x = np.linspace(a, b, n+1)

y = f(x)

suma = y[0] + y[n]

for i in range(1, n):
    if i % 2 == 0:
        suma += 2 * y[i]
    else:
        suma += 4 * y[i]

integral = (h/3) * suma

print("Integral aproximada (Simpson):", integral)