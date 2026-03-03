# Minimizar f(x) = (x - 3)^2 usando descenso de gradiente

x = 0        # Valor inicial
alpha = 0.1  # Tasa de aprendizaje (qué tan grande es el paso)

for _ in range(20):  
    # Gradiente (derivada) de f(x) = 2(x - 3)
    grad = 2 * (x - 3)
    
    # Regla de actualización: x_nuevo = x - alpha * gradiente
    x = x - alpha * grad

# Valor aproximado del mínimo
print(x)

# 03/02/26