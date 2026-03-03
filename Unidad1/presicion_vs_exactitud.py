import numpy as np  # Se importa numpy para cálculos numéricos

# Mediciones experimentales
mediciones = np.array([9.8, 9.81, 9.79, 9.80])

# Valor real o teórico
valor_real = 9.81

# Se calcula la media de las mediciones
media = np.mean(mediciones)

# Se calcula el error absoluto respecto al valor real
error = abs(media - valor_real)

print("Media:", media)
print("Error absoluto:", error)

# Alta precisión (baja varianza), buena exactitud