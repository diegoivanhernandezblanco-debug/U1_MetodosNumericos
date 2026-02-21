import numpy as np

# Genera 1000 datos con distribución normal (media 0, desviación 1)
datos_reales = np.random.normal(0, 1, 1000)

# Valor que se sumará a todos los datos (sesgo)
sesgo = 0.5

print(datos_reales)

# Se agrega el sesgo a los datos originales
datos_sesgados = datos_reales + sesgo

print(datos_sesgados)

# Se calcula y muestra la media de ambos conjuntos
print("Media real:", np.mean(datos_reales))
print("Media sesgada:", np.mean(datos_sesgados))