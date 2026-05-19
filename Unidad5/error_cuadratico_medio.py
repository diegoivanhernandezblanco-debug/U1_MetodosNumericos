import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

coef = np.polyfit(x, y, 1)

y_pred = coef[0]*x + coef[1]

error = np.mean((y - y_pred) ** 2)

print("Error cuadrático medio:", error)