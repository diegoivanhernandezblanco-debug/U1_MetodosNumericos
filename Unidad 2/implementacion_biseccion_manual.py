def f(x): #Definicion de la funcion a analalizar
    return x**3 - x - 2 #Funcion no lineal

a = 1 #Extremo izquierdo inicial
b = 2 #Extremo derecho inicial
tolerancia = 1e-6 #Error maximo permitido
max_iter = 23 #Numero maximo de iteracciones permitidas

for i in range(max_iter): #Ciclo de iteracciones
    c = (a + b) / 2 #Calculo del punto medio
    fc = f(c) #Evaluacion de la funcion del punto promedio

    if abs(fc) < tolerancia: #Criterio de paro por valor cercano a 0
        break #Terminar ciclo

    if f(a) * f(c) < 0: #Verifica si la raiz esta en el subintervalo izquierdo
        b = c #Actualiza extremo derecho
    else: #En caso contrario
        a = c #Actualiza extremo izquierdo

print("Raiz aproximada:", c) #Muestra la raiz encontrada
print("Iteracciones realizadas:", i+1) #Numero de iteracciones ejecutadas