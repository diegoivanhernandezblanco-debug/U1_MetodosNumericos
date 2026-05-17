def f(x,y):    # Define la ecuación diferencial
    return x + y

x = 0          # Valor inicial de x

y = 1          # Condición inicial y(0)=1

h = 0.1        # Tamaño del paso numérico

n = 10         # Número de iteraciones

for i in range(n):   # Ejecuta el método de Euler

    y = y + h*f(x,y)   # Aplica fórmula de Euler

    x = x + h          # Actualiza valor de x

    print("x =",x,", y =",y)