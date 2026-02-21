from scipy.optimize import minimize  # Se importa la función de optimización

# Definimos la función a minimizar: f(x) = (x - 2)^2
f = lambda x: (x - 2)**2

# Se llama a minimize indicando:
# f  -> función a minimizar
# x0 -> valor inicial (punto de partida)
resultado = minimize(f, x0=0)

# Se imprime el valor de x donde la función alcanza su mínimo
print(resultado.x)

# En IA: ajustes automáticos de parámetros