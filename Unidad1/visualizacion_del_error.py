import numpy as np
import matplotlib.pyplot as plt

# Crear valores de x entre -1 y 5
x = np.linspace(-1, 5, 100)

# Función cuadrática f(x) = (x - 2)^2
y = (x - 2)**2

# Graficar la función
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funcion de costo")
plt.show()

#Nota: Visualizar funciones ayuda a enteder la optimizacion en la IA