import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

correlation = np.corrcoef(x, y)[0, 1]

print("Coeficiente de correlación:", correlation)