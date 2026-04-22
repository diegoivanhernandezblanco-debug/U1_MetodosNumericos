import numpy as np

X = np.array([[1,1],
              [1,2],
              [1,3],
              [1,4]])

y = np.array([6,5,7,10])

XT = X.T

beta = np.linalg.inv(XT.dot(X)).dot(XT).dot(y)

print("Coeficientes del modelo:", beta)