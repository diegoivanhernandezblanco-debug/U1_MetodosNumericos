# Valor de x
x = 2

# Pequeño cambio en x
dx = 0.01

# Función y = x^2
y = x**2

# Aproximación del error usando la derivada
# Derivada de x^2 es 2x
# El error aproximado es |f'(x)| * dx
dy = abs(2 * x) * dx

print("y:", y)
print("Error aproximado en y:", dy)