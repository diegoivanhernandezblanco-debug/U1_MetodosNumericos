import numpy as np

def L(x):
    return x**3 - 6 * x**2 + 9 * x + 1

def dL(x):
    return 3 * x**2 - 12 * x + 9

def f(x, y):
    return np.exp(-(x**2 + y**2))



def parte_a():
    x = 2
    h = 0.001

    derivada_adelante = (L(x + h) - L(x)) / h
    derivada_central = (L(x + h) - L(x - h)) / (2 * h)
    derivada_real = dL(x)

    error_adelante = abs(derivada_adelante - derivada_real)
    error_central = abs(derivada_central - derivada_real)

    print("PARTE A - Diferenciacion numerica")
    print(f"L({x}) = {L(x):.6f}")
    print(f"Derivada analitica en x = {x}: {derivada_real:.6f}")
    print(f"Diferencia hacia adelante: {derivada_adelante:.6f}")
    print(f"Error hacia adelante: {error_adelante:.10f}")
    print(f"Diferencia central: {derivada_central:.6f}")
    print(f"Error diferencia central: {error_central:.10f}")
    print()

def parte_b():
    a = 0
    b = 3
    n = 100

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = L(x)

    trapecio = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])

    suma_simpson = y[0] + y[n]
    for i in range(1, n):
        if i % 2 == 0:
            suma_simpson += 2 * y[i]
        else:
            suma_simpson += 4 * y[i]
    simpson = (h / 3) * suma_simpson

    integral_real = 9.75

    print("PARTE B - Integracion numerica")
    print(f"Integral real de 0 a 3: {integral_real:.6f}")
    print(f"Metodo del trapecio: {trapecio:.6f}")
    print(f"Error trapecio: {abs(trapecio - integral_real):.10f}")
    print(f"Metodo de Simpson: {simpson:.6f}")
    print(f"Error Simpson: {abs(simpson - integral_real):.10f}")
    print()

def parte_c():
    a = -1
    b = 1
    n = 100

    hx = (b - a) / n
    hy = (b - a) / n
    x_medios = np.linspace(a + hx / 2, b - hx / 2, n)
    y_medios = np.linspace(a + hy / 2, b - hy / 2, n)

    suma_doble = 0.0
    for xi in x_medios:
        for yj in y_medios:
            suma_doble += f(xi, yj)

    integral_doble = suma_doble * hx * hy
    probabilidad_normalizada = integral_doble / np.pi

    print("PARTE C - Integracion multiple")
    print(f"Aproximacion de la integral doble en [-1,1]x[-1,1]: {integral_doble:.6f}")
    print(f"Probabilidad en la region si se normaliza la densidad: {probabilidad_normalizada:.6f}")


parte_a()
parte_b()
parte_c()
