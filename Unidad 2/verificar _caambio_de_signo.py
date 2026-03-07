import numpy as np #Biblioteca para calculo numerico

def f(x): #Definicion de la funcion matematica
    return x**3 - x - 2 #Expresion algebraica de la funcion

a = 1 #Limite inferior del intervalo
b = 2 #Limite superor del intervalo

fa = f(a) #Evaluacion de la funcion en el extremo izquierdo
fb = f(b) #Evaluacion de la funcion en el extremo derecho

print("f(a):", fa) #Mostrar valor en a
print("f(b):", fb) #Mostrar valor en b

if fa * fb < 0: #Verifica condicion del teorema del valor intermedio
    print("Existe al menos una raiz en el intervalo") #Confirmcion
else:
    print("No se garantiza raiz en el intervalo") #No hay cambio de signo