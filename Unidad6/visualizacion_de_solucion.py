import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

x = 0 
y = 1

h = 0.1

x_vals = []
y_vals = []

for i in range(20):

    x_vals.append(x)

    y_vals.append(y)

    y = y + h * f(x, y)

    x = x + h

plt.plot(x_vals,y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO')
plt.grid()
plt.show()