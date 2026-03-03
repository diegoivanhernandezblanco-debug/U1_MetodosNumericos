import numpy as np  # Se importa numpy para trabajar con arreglos y funciones matemáticas

# Se generan 1000 valores entre 0 y 2
x = np.linspace(0, 2, 1000)

# Se define la función f(x) = x^2 - 2
f = x**2 - 2

# Se busca el valor de x donde f(x) está más cerca de 0
# np.abs(f) calcula el valor absoluto
# np.argmin(...) devuelve la posición del valor más pequeño
x_aprox = x[np.argmin(np.abs(f))]

# Se imprime la aproximación de la raíz
print(x_aprox)

# 03/02/26