import numpy as np

x = np.array([0, 1, 2 , 3])
y = np.array([1, 3, 2, 5])

def lagrange(x_data, y_data, x_val):
    n = len(x_data)
    resultado = 0

    for i in range(n):
        L = 1

        for j in range(n):
            if i != j:
                L *= (x_val - x_data[j]) / (x_data[i] - x_data[j])

        resultado += y_data[i] * L

    return resultado

x_interp = 1.5
y_interp = lagrange(x, y, x_interp)
print("Valor estimado", y_interp)

