import numpy as np  # (Aquí realmente no se usa, pero se importa)

x = 3.1415926535  # Número con muchas cifras decimales

# Redondeo a diferentes cantidades de decimales
print(round(x, 2))  # 2 decimales
print(round(x, 4))  # 4 decimales
print(round(x, 6))  # 6 decimales

# Menos cifras --> más error numérico
# Puede tener impacto acumulativo en algoritmos iterativos