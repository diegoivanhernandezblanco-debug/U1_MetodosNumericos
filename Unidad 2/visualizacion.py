a = 1 #Limite inicial superior
b = 2 #Limite inicial inferior
n = 10 #Numero de iteracciones

error_teorico = (b - a) / (2**n) #Formula del error maximo de biseccion

print("Error maximo despues de", n, "teracciones:", error_teorico) #Mostrar error
