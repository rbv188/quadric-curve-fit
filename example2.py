import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import quadrics

if __name__=="__main__":

    data = np.loadtxt('points.txt')

    X = data[:,[0]]
    Y = data[:,[1]]
    Z = data[:,[2]]

    num = len(X)


    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter(X,Y,Z,marker='.',color='r')

    Q = quadrics.quadric_equation(X,Y,Z)

    xmax = np.max(X) + 10
    xmin = np.min(X) - 10
    ymax = np.max(Y) + 10
    ymin = np.min(Y) - 10
    zmax = np.max(Z) + 10
    zmin = np.min(Z) - 10
    
    ax = quadrics.plot_quadric(ax,Q,xmax,xmin,ymax,ymin,zmax,zmin)
    ax.scatter(X,Y,Z,marker='.',color='b')
    plt.show()

