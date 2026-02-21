import numpy as np  # Se importa la librería numpy

# Se generan 1000 valores entre 0 y 2
x = np.linspace(0, 2, 1000)
# print(x)  # Muestra todos los valores generados

# Se define la función f(x) = x^2 - 2
f = x**2 - 2

# np.abs(f) calcula el valor absoluto de cada elemento
# np.argmin(...) devuelve el índice del valor más pequeño del arreglo
# Aquí se busca el x donde f(x) está más cerca de 0 (aproximación de la raíz)
x_aprox = x[np.argmin(np.abs(f))]

# print(x_aprox)  # Muestra la aproximación encontrada

# 03/02/26