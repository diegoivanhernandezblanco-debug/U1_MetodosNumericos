import numpy as np  # Se importa la librería NumPy para usar funciones matemáticas como el coseno

# Definición de la función g(x)
# En este caso, g(x) = cos(x)
def g(x):
    return np.cos(x)

# Valor inicial (semilla) para comenzar el método de punto fijo
x = 0.5

# Tolerancia: criterio de paro.
# El ciclo se detendrá cuando la diferencia entre iteraciones
# sea menor que 1e-6
tolerancia = 1e-6

# Número máximo de iteraciones permitidas
# Esto evita que el programa se quede en un ciclo infinito
max_iter = 100

# Método de iteración de punto fijo
for i in range(max_iter):
    
    # Se calcula el nuevo valor usando la función g(x)
    x_nuevo = g(x)

    # Se verifica el criterio de convergencia:
    # Si la diferencia entre el valor nuevo y el anterior
    # es menor que la tolerancia, se detiene el ciclo
    if abs(x_nuevo - x) < tolerancia:
        break

    # Se actualiza el valor de x para la siguiente iteración
    x = x_nuevo

# Se imprime la raíz aproximada encontrada
print("Raiz aproximada:", x_nuevo)

# Se imprime el número de iteraciones realizadas
print("Iteracciones realizadas:", i+1)