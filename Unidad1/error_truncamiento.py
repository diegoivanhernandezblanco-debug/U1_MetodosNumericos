import math  # Se importa la librería matemática

x = 1  # Valor donde evaluamos

# Aproximación de e^x usando el polinomio de Taylor de orden 2:
# e^x ≈ 1 + x + x^2/2
aprox = 1 + x + (x**2) / 2

# Valor real usando la función exponencial
real = math.exp(x)

# Error absoluto entre el valor real y la aproximación
error = abs(real - aprox)

print("Aprox:", aprox)
print("Real:", real)
print("Error:", error)