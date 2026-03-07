import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 100)
y = x**3 - x - 2

plt.axhline(0)
plt.plot(x,y)
plt.title("Funcion f(x) - x^3 - x - 2")
plt.show()