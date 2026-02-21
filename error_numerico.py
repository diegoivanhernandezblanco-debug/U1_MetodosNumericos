import math  # Permite usar funciones matemáticas como sqrt, log, trigonometría, etc.

# Valor real de √2
real = math.sqrt(2)

# Valor aproximado
aprox = 1.41

# Error absoluto: diferencia directa entre real y aproximado
error_absoluto = abs(real - aprox)

# Error relativo: error respecto al valor real
error_relativo = error_absoluto / real

print(error_absoluto, error_relativo)

# 03/02/26