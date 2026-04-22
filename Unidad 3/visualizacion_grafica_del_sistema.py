import numpy as np #Importa la biblioteca Numpy para calculos numericos y arreglos
import matplotlib.pyplot as plt # Importa Matploit para graficos

x = np.linspace(-3, 3, 400) 

y1 = np.sqrt(4 - x**2)
y2 = np.sqrt(4 - x**2)

y_line = x - 1

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y_line)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sistemas de ecuaciones no lineales")

plt.grid()
plt.show()