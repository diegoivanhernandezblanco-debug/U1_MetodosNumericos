import numpy as np

A = np.array([[10,1,-1],
             [2,10,1],
             [2,3,10]])

b = np.array([11,12,13])

x = np.linalg.solve(A,b)

print("Solucion del siistema:", x)

