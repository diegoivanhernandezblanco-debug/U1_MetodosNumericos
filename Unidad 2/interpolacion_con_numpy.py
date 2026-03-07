import numpy as np #Biblioteca numerica

x_datos = np.array([0,1,2]) #Arreglo con valores conocidos en x
y_datos = np.array([1,3,2]) #Arreglo con valores conocidos en y

coeficientes = np.polyfit(x_datos, y_datos, 2)
polinomio = np.poly1d(coeficientes)

x_eveal = 1.5
y_eval = polinomio(x_eveal)

print("Coeficientes del polinomio: ", coeficientes)
print("Valor interpolado:", y_eval )