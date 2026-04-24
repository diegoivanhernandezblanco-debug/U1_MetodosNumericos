import numpy as np

def f(x):
    return x**3
x = 2
h = 0.001
derivada = (f(x + h) - f(x - h)) / (2 * h)
real = 3*x**2
error = abs(derivada - real)
print("Derivada aproximada:", derivada)
print("Derivada real:", real)
print("Error:", error)