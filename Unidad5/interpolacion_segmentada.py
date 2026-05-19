import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2 , 3])
y = np.array([1, 3, 4, 5])

spline = CubicSpline(x, y)

x_interp = np.linspace(0, 3, 100)

y_interp = spline(x_interp)

print("Valores interpolados:", y_interp)