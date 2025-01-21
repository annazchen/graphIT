import matplotlib.pyplot as plt
import numpy as np

x1 = int (input("x1?: "))
y1 = int (input("y1?: "))
V = np.array([x1,y1])

fig = plt.subplots
ax = plt.subplots
ax.quiver(0, 0, V[0], V[1], angles = 'xy', scale_units = 'xy', scale = 1)
ax.set_xlim([-2.2])
ax.set_ylim([-2,2])

plt.grid()
plt.show()
