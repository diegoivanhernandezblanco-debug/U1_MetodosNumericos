import numpy as np

def f(x):
    return x**2

x = np.array([1, 2, 3])
y = f(x)

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

# Comparar valores
x_test = 2.5
valor_interpolado = lagrange(x, y, x_test)
valor_real = f(x_test)
error = abs(valor_interpolado - valor_real)

print("Valor interpolado:", valor_interpolado)
print("Valor real:", valor_real)
print("Error", error)