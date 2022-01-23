## PYTHON SCRIPT FOR PLOTTING A TXT FILE
import math
import matplotlib.pyplot as plt
import numpy as np
import random as random

# caricare il file ed estrarre le posizioni dei punti
coord_filename = './coordinates/pos6.txt'
img_filename = './img/orb6.png'
text = np.loadtxt(coord_filename)
X = text[:, 0]
Y = text[:, 1]
Z = text[:, 2]

# plot
fig = plt.figure(figsize=(30, 10))
# ax = fig.add_subplot(111, projection='3d')

# parameters
marker = '.'
marker_size = .33
marker_color = 'black'
marker_edge = 'None'
alpha=1

# piano XY
ax = fig.add_subplot(131)
ax.scatter(X, Y,
        s=marker_size,
        marker=marker,
        color=marker_color,
        edgecolors=marker_edge,
        alpha=alpha)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect(1)
ax.set_xticks([])
ax.set_yticks([])

# piano YZ
ax = fig.add_subplot(132)
ax.scatter(Y,Z,
        s=marker_size,
        marker=marker,
        color=marker_color,
        edgecolors=marker_edge,
        alpha=alpha)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect(1)
ax.set_xticks([])
ax.set_yticks([])

# piano XZ
ax = fig.add_subplot(133)
ax.scatter(Z,X,
        s=marker_size,
        marker=marker,
        color=marker_color,
        edgecolors=marker_edge,
        alpha=alpha)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect(1)
ax.set_xticks([])
ax.set_yticks([])

plt.savefig(img_filename, dpi=600, transparent=True)
