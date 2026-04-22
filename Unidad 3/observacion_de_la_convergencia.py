import numpy as np

A = np.array([[10, 1, -1],
              [2, 10, 1],
              [2, 3, 10]])

b = np.array([11, 12, 13])

x = np.zeros(3)

tol = 1e-6

for k in range(50):

    x_new = np.zeros(3)

    x_new[0] = (11 + x[1] - x[2]) / 10
    x_new[1] = (12 - 2*x[0] - x[2]) / 10
    x_new[2] = (13 - 2*x[0] - 3*x[1]) / 10

    error = np.linalg.norm(x_new - x)

    print("Iteracion:", k+1, "Solucion:", x_new, "Error:", error)

    if error < tol:
        break

    x = x_new