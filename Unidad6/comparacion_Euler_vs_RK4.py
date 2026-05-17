import numpy as np

def f(x,y):
    return x + y

def exacta(x):
    return 2*np.exp(x) - x - 1

h = 0.1

x = 0

y_euler = 1

y_rk4 = 1

for i in range(10):

    # Método de Euler
    y_euler = y_euler + h*f(x,y_euler)

    # Método RK4
    k1 = f(x,y_rk4)

    k2 = f(x+h/2, y_rk4+h*k1/2)

    k3 = f(x+h/2, y_rk4+h*k2/2)

    k4 = f(x+h, y_rk4+h*k3)

    y_rk4 = y_rk4 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    x = x + h

real = exacta(x)

error_euler = abs(real - y_euler)

error_rk4 = abs(real - y_rk4)

print("Exacta:",real)

print("Euler:",y_euler)

print("RK4:",y_rk4)

print("Error Euler:",error_euler)

print("Error RK4:",error_rk4)