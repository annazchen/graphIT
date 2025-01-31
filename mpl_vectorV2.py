import matplotlib.pyplot as plt
import numpy as np
from rulerMagv2 import vMag
from rulerMagv2 import vDir
from rulerMagv2 import vTyp as new_vTyp
coord_list = ["north", "east", "south", "west"]
mpl_colors = ['b', 'g', 'c', 'm', 'y', 'k', 'w']

def convert_Mag(vMag):
    new_vMag = []
    for i in range(len(vMag)):
        for j in range(len(vMag[i])):
            new_vMag.append(int(vMag[i][j].strip('abcdefghijklmnopqrstuvwxyz'))) 
    return new_vMag

def convert_Dir(vDir):
    new_vDir=[]

    for i in range(len(vDir)):
        for j in range (len(vDir[i])):

            if (vDir[i][j] in coord_list):
                if (vDir[i][j] == "east"):
                    new_vDir.append(0)
                elif (vDir[i][j] == "north"):
                    new_vDir.append(0.5*np.pi)
                elif (vDir[i][j] == "west"):
                    new_vDir.append(np.pi)
                elif (vDir[i][j] == "south"):
                    new_vDir.append(1.5*np.pi)
                else:
                    print("Error")
            #if have units
                #check unit degrees or rad
                #convert degrees to rad if degrees
            #else its like N30ºE
                #convert to rad
    return new_vDir

def convert_toCoords(vMag, vDir):
    x = []
    y = []
    #assumme same length
    if (len(vMag) == len(vDir)):
        for i in range(len(vMag)):
            x.append(vMag[i]*np.cos(vDir[i]))
            y.append(vMag[i]*np.sin(vDir[i]))
    else:
        print ("not same length")
    
    return x, y

def vector_add(x, y):
    x_total = 0
    y_total = 0
    for i in range(len(x)):
        x_total += x[i]
        y_total += y[i]
    return x_total, y_total


def decide_operation(vTyp):
    if ("EIND" in vTyp):
        return "subtract"
    
    #check if theres any normal vectors or weight etc for incline questions
    else:
        return "add"



new_vMag = convert_Mag(vMag)
new_vDir = convert_Dir(vDir)
print(new_vMag)
print(new_vDir)
print(new_vTyp)

if (decide_operation(new_vTyp)=="add"):
    x, y = convert_toCoords(new_vMag, new_vDir)
    print(x)
    print(y)
    x_total, y_total = vector_add(x, y)
    print(x_total)
    print(y_total)
    fig, ax = plt.subplots()
    ax.quiver(0, 0, x_total, y_total, angles = 'xy', scale_units = 'xy', scale = 1,  color  = 'r')
    for i in range(len(x)):
        if (i != 0):
            ax.quiver(x[i-1], y[i-1], x[i], y[i], angles = 'xy', scale_units = 'xy', scale = 1,  color  = mpl_colors[i])
        else: 
            ax.quiver(0, 0, x[i], y[i], angles = 'xy', scale_units = 'xy', scale = 1,  color  = mpl_colors[i])  
 

 
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
plt.grid()
plt.show()