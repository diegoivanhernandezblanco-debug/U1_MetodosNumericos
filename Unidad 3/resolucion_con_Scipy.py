import numpy as np
from scipy.optimize import fsolve 

def sistema(vars):
    x, y = vars
    f1 = x**2 + y**2 - 4
    f2 = x - y - 1
    return [f1, f2]

sol = fsolve(sistema, [1,1])

print("Solucion aproximada", sol)