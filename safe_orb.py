from tqdm import tqdm
import math
import matplotlib.pyplot as plt
import numpy as np
import random as random


def wavefunction(x, y, z, state):
    R = 0                      # parte radiale
    Y = 0                      # parte angolare
    r = math.sqrt(x*x+y*y+z*z)  # coordinata radiale

    if (state == 1):  # n=1,l=0,m=0
        R = math.exp(-r)
        Y = 1

    elif (state == 2):  # n=2,l=0,m=0
        R = math.exp(-r/2)*(1-r/2)
        Y = 1

    elif (state == 3):  # n=2,l=1,m=0
        R = math.exp(-r/2)*r
        Y = z/r

    elif (state == 4):  # n=2,l=1,m=+-1 R
        R = math.exp(-r/2)*r
        Y = x/r

    elif (state == 5):  # n=2,l=1,m=+-1 I
        R = math.exp(-r/2)*r
        Y = y/r

    elif (state == 6):  # n=3,l=0,m=0
        R = math.exp(-r/3)*(1-2*r/3.0+2*r*r/27.0)/3
        Y = 1

    elif (state == 7):  # n=3,l=1,m=0
        R = math.exp(-r/3)*r*(1-r/6)
        Y = z/r

    elif (state == 8):  # n=3,l=1,m=+-1 R
        R = math.exp(-r/3)*r*(1-r/6)
        Y = x/r

    elif (state == 9):  # n=3,l=1,m=+-1 I
        R = math.exp(-r/3)*r*(1-r/6)
        Y = y/r

    elif (state == 10):  # n=3,l=2,m=0
        R = math.exp(-r/3)*r*r
        Y = (z*z-1)/(r*r)

    elif (state == 11):  # n=3,l=2,m=+-1 R
        R = math.exp(-r/3)*r*r
        Y = x*z/(r*r)

    elif (state == 12):  # n=3,l=2,m=+-1 I
        R = math.exp(-r/3)*r*r
        Y = y*z/(r*r)

    elif (state == 13):  # n=3,l=2,m=+-2 R
        R = math.exp(-r/3)*r*r
        Y = (x*x-y*y)/(r*r)

    elif (state == 14):  # n=3,l=2,m=+-2 I
        R = math.exp(-r/3)*r*r
        Y = x*y/(r*r)

    return(Y*R)

for j in range(14):
    # parametri
    N = int(1e4)      # numero punti (max 10'000)
    L = float(25)     # dimensione del "box" contente l'atomo
    S = int(j+1)      # stato da disegnare

    filename = './coordinates/pos' + str(S) + '.txt'
    file = open(filename, 'w')

    i = 0
    pbar = tqdm(total=N)
    while (i < N):
        x = round((random.uniform(0, 1)-0.5)*L*2, 6)
        y = round((random.uniform(0, 1)-0.5)*L*2, 6)
        z = round((random.uniform(0, 1)-0.5)*L*2, 6)
        psi = round(wavefunction(x, y, z, S), 6)
        rnd = round(random.uniform(0, 1), 6)
        if(rnd <= (psi*psi)):
            file.write('{}'.format(x*0.529)+' '+'{}'.format(y*0.529) +
                       ' '+'{}'.format(z*0.529)+' '+'{}'.format(psi*psi)+'\n')
            i += 1
            pbar.update(1)
    file.close()

    # caricare il file ed estrarre le posizioni dei punti
    text = np.loadtxt(filename)
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

    filename = './img/orb' + str(j+1) + '.png'
    plt.savefig(filename, dpi=600, transparent=True)
    print(filename + ', completed.\n')
