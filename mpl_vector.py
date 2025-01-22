import matplotlib.pyplot as plt
import numpy as np
from rulerMagv2 import *
import array as arr


#vector addition
def vector_add(V1, V2): 
    Vtotal = V1 + V2
    return Vtotal


#converts any existing array with EXCLUSIVELY NUMBERS into a numpy array
def to_nparray(array):  
    V = np.array([])
    return np.array(array, dtype = float)

#adds vector to an existing plot according to 2 points, both w/ default val (0,0)   
def create_vector(V2 = np.array([0, 0]), V1 = np.array([0, 0]), plt_color = 'r'): 
    ax.quiver( V1[0], V1[1], V2[0], V2[1], angles = 'xy', scale_units = 'xy', scale = 1,  color  = plt_color)

#shows a single vector NO IDEA IF THIS WORKS LOL
def show_vector(V0, x_low = -2, x_up = 2, y_low = -2, y_up = 2): 
    fig, ax = plt.subplots()
    create_vector(V0)
    ax.set_xlim([x_low, x_up])
    ax.set_ylim([y_low, y_up])
    plt.grid()
    plt.show()
    
new_vMag = []

for i in range(len(vMag)):
    for j in range(len(vMag[i])):
        new_vMag.append(vMag[i][j].strip('abcdefghijklmnopqrstuvwxyz')) 

print(new_vMag)
np_vMag = to_nparray(new_vMag)
print(np_vMag)

fig, ax = plt.subplots()
create_vector(np_vMag)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

plt.grid()
plt.show()
