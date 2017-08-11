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
    [tr,[xcenter,ycenter,zcenter]] = quadrics.ellipsoid_to_sphere(Q)

    X -= xcenter
    Y -= ycenter
    Z -= zcenter

    Xt = []
    Yt = []
    Zt = []

    for i in range(0,num):
        temp = np.dot(tr,np.array([[X[i][0]],[Y[i][0]],[Z[i][0]]]))
        Xt.append(temp[0][0])
        Yt.append(temp[1][0])
        Zt.append(temp[2][0])

    ax.scatter(Xt,Yt,Zt,marker='.',color='b')
    plt.show()

    
