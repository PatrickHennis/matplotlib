import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import art3d

mpl.rcParams['legend.fontsize'] = 10

x = [0, 1]
y = [0, 1]
z = [0, 1]

fig = plt.figure()
ax = fig.gca(projection='3d')

line = ax.plot(x, y, z, label='parametric curve')[0]
art3d.line_2d_to_3d(line)
line.set_data_3d([0,2], [0,2], [0,2])
ax.legend()

plt.show()
