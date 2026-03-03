import numpy as np  # Se importa numpy para trabajar con matrices

# Matriz de coeficientes del sistema
A = np.array([[3, 2],
              [1, 2]])

# Vector de términos independientes
b = np.array([5, 5])

# np.linalg.solve resuelve el sistema A·x = b
x = np.linalg.solve(A, b)

# Solución del sistema
print(x)