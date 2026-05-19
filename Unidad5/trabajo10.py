import numpy as np

x = np.array([ 1, 2, 3, 4, 5])
y = np.array([ 2, 3, 5, 4, 5])

x = np.vstack((x, np.ones(len(x)))).T

XT = x.T
beta = np.linalg.inv(XT.dot(x)).dot(XT).dot(y)

b = beta[0]
m = beta[1]

y_pred = m * x + b

print("Pendiente:", m)
print("Intersección:", b)
print("Prediccion:", y_pred)