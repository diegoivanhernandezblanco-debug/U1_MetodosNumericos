import numpy as np

def f(x):
    return x**2

a = 0
b = 2   
n = 100

h = (b - a) / n

x = np.linspace(a, b, n+1)

y = f(x)

integral = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])

print ("Integral aproximada (Trapecio):", integral)