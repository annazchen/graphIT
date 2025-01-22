import matplotlib.pyplot as plt
import numpy as np
from rulerMagv2 import *
import array as arr


#vector addition
def vector_add(V1, V2): 
    Vtotal = V1 + V2
    return Vtotal


#converts any existing array with exclusively numbers into a numpy array
def to_nparray(array):  
    V = np.array([])
    for x in array:
        V.append( float(array[x]))
    return V    

#adds vector to an existing plot according to 2 points, both w/ default val (0,0)   
def create_vector(V1 = np.array([0, 0]), V2 = np.array([0, 0]), plt_color = 'r'): 
    ax.quiver( V1[0], V1[1], V2[0], V2[1], angles = 'xy', scale_units = 'xy', scale = 1,  color  = plt_color)

#shows a single vector NO IDEA IF THIS WORKS LOL
def show_vector(V0, x_low = -2, x_up = 2, y_low = -2, y_up = 2): 
    fig, ax = plt.subplots()
    create_vector(V0)
    ax.set_xlim([x_low, x_up])
    ax.set_ylim([y_low, y_up])
    plt.grid()
    plt.show()
    
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
