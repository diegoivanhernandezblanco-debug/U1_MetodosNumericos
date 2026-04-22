import numpy as np

A = np.array([
    [10, 2, 1],
    [2, 10, 3],
    [1, 3, 10]
], dtype=float)

b = np.array([9, 13, 14], dtype=float)

tol = 1e-6
max_iter = 100

print("= PARTE B - METODO DE JACOBI =")

x = np.zeros(3, dtype=float)

D = np.diag(A)
R = A - np.diagflat(D)

for i in range(max_iter):
    x_nuevo = (b - np.dot(R, x)) / D
    error = np.linalg.norm(x_nuevo - x, np.inf)

    print("Iteracion", i + 1, ": x =", x_nuevo, " error =", error)

    if error < tol:
        break

    x = x_nuevo

print("\nSolucion final:")
print(x_nuevo)
print("Iteraciones totales:", i + 1)
print("Error final:", error)

print("\n= PARTE C - ANALISIS DE CONVERGENCIA =")

D = np.diag(np.diag(A))
L = -np.tril(A, -1)
U = -np.triu(A, 1)

B = np.dot(np.linalg.inv(D), (L + U))
eigenvalores = np.linalg.eigvals(B)
radio_espectral = np.max(np.abs(eigenvalores))

print("Matriz de iteracion B:")
print(B)

print("\nEigenvalores:")
print(eigenvalores)

print("\nRadio espectral:", radio_espectral)

if radio_espectral < 1:
    print("El metodo converge teoricamente porque el radio espectral es menor que 1")
else:
    print("El metodo no converge porque el radio espectral es mayor o igual que 1")

print("\n= PARTE D - APLICACION =")

#Porque facilita que las máquinas puedan resolver,
#problemas complicados sin ayuda constante, manejar mucha información al mismo tiempo 
# y tomar decisiones más rápidas y acertadas, haciendo que todo funcione mejor y con menos fallas
