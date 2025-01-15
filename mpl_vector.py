import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np



fig = plt.figure()

ax = plt.axes(projection = '3d')
z = 1
x = 2
y = 3

ax.plot3D(x,y,z,'pink')
ax.set_title('3D plot')
plt.show()


