import numpy as np
import matplotlib.pyplot as plt


#PARTE A
def f(x):
    return x**3 - 4*x - 9

a = 2
b = 3

print("f(a) =", f(a))
print("f(b) =", f(b))

if f(a)*f(b) < 0:
    print("Existe una raíz en [2,3]")
else:
    print("No existe una raíz en [2,3]")


x = np.linspace(1, 4, 100)
y = f(x)

plt.figure()
plt.axhline(0)
plt.plot(x,y,label="f(x)=x^3-4x-9")
plt.title("Gráfica de la función")
plt.show()

#PARTE B
tol = 1e-5
n = 100

for i in range(n):

    c = (a + b) / 2

    if abs(f(c)) < tol or (b - a)/2 < tol:
        break

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

error = (b - a) / (2**n)

print("Raíz aproximada:", c)
print("Número de iteraciones:", i+1)
print("Error teórico máximo:", error)

#PARTE C
def g(x):
    return (9 + 4*x)**(1/3)

x0 = 2.5

for i in range(10):
    x0 = g(x0)

print("Aproximación por punto fijo:", x0)

#PARTE D
x_datos = np.array([2.6, 2.7, 2.8])
y_datos = f(x_datos)

coef = np.polyfit(x_datos, y_datos, 2)
p = np.poly1d(coef)

print("Polinomio interpolante:")
print(p)
raiz = np.roots(p)
print("Raiz de la interpolacion:", raiz)
x_eval = 2.7
print("Evaluación cerca de la raíz:", p(x_eval))
x2 = np.linspace(2, 3, 100)

plt.figure()
plt.plot(x2,f(x2),label="f(x)")
plt.plot(x2,p(x2),label="Interpolación grado 2")
plt.axhline(0)
plt.title("Comparación función vs interpolación")
plt.show() 
