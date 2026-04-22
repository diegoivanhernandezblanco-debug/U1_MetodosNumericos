import numpy as np

A = np.array([[10, 1, -1],
              [2, 10, 1],
              [2, 3, 10]])

D = np.diag(np.diag(A))

L = -np.tril(A, -1)

U = -np.triu(A, 1)

T = np.linalg.inv(D).dot(L + U)

eigenvalues = np.linalg.eigvals(T)

rho = max(abs(eigenvalues))

print("Radio espectral:", rho)

if rho < 1:
    print("El metodo converge")
else:
    print("El metodo diverge")