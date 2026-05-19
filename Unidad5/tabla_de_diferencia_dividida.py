import numpy as np

x = np.array([1,2,3])
y = np.array([1,4,9])

n = len(x)

tabla = np.zeros((n,n))
tabla[:,0] = y

for j in range(1,n):
    for i in range(n-j):
        tabla[i,j] = (tabla[i+1,j-1] - tabla[i,j-1]) / (x[i+j] - x[i])

print("Tabla de diferencias divididas:\n" + str(tabla))
