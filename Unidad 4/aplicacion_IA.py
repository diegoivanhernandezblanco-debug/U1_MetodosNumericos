import numpy as np

def loss(w):
    return w**2 + 3*w

w = 1.5
h = 0.0001

grad = (loss(w + h) - loss(w - h)) / (2 * h)
real = 2*w + 3

print("Gradiente aproximado:", grad)
print("Gradiente real:", real)