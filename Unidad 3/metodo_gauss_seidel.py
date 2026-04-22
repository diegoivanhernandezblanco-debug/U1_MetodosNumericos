import numpy as np

x = np.zeros(3)
tol = 1e-6

for k in range(100):
    x_old = x.copy()

    x[0] = (11 - x[1] + x[2]) / 10
    x[1] = (12 - 2*x[0] + x[2]) / 10
    x[2] = (13 - 2*x[0] + 3*x[1]) / 10

    if np.linalg.norm(x - x_old) < tol:
        break

print("Solución:", x)
print("Iteraciones:", k + 1)

