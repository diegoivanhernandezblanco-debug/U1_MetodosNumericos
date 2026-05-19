import numpy as np

x = np.array([1, 2 , 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

coef = np.polyfit(x, y, 1)

m = coef[0]
b = coef[1]

y_pred = m * x + b

print("pendiente:", m)
print("intercepto:", b)
print("Valores predichos:", y_pred)