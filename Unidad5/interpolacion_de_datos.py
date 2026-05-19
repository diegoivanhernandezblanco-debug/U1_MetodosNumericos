import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2 , 3])
y = np.array([1, 2, 0, 5])

n = len(x)

tabla = np.zeros((n, n))

tabla[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        tabla[i, j] = (tabla[i+1, j-1] - tabla[i, j-1]) / (x[i+j] - x[i])

def newton(x_data, tabla, x_val):
    n = len(x_data)
    resultado = tabla[0, 0]

    producto = 1

    for i in range(1, n):
        producto *= (x_val - x_data[i-1])
        resultado += tabla[0, i] * producto

    return resultado

x_interp = 1.5

y_interp = newton(x, tabla, x_interp)

print("Valor estimado", y_interp)

x_grafica = np.linspace(min(x), max(x), 100)
y_grafica = [newton(x, tabla, punto) for punto in x_grafica]

plt.plot(x_grafica, y_grafica, label="Polinomio interpolado")
plt.scatter(x, y, color="red", label="Datos originales")
plt.scatter(x_interp, y_interp, color="green", label="Valor estimado")
plt.title("Interpolacion de datos")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
