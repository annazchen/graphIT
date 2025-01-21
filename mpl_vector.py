import matplotlib.pyplot as plt
import numpy as np
from rulerMagv2 import *
import array as arr



def vector_add()
    
def to_nparray()

def create_vector()
    
def show_vector()
    
    



x1 = int (input("x1?: "))
y1 = int (input("y1?: "))
x2 = int(input("x2?: "))
y2 = int(input("y2?: "))

V1 = np.array([x1, y1])
V2 = np.array([x2, y1])

fig, ax = plt.subplots()
ax.quiver(0, 0, V1[0], V1[1], angles = 'xy', scale_units = 'xy', scale = 1,  color  = 'r')
ax.quiver(V1[0], V2[1], V2[0], V1[1], angles = 'xy', scale_units = 'xy', scale = 1,  color  = 'b')
ax.quiver(0, 0, V1[0] + V2[0], V1[1] + V2[1], angles = 'xy', scale_units = 'xy', scale = 1,  color  = 'g')
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])

plt.grid()
plt.show()
