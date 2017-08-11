import numpy as np

'''
Fits a quadric equation to points in 3d space
using least squares fit
input: numpy array of X,Y, and Z points
return: Matrix form of quadric equation
'''
def quadric_equation(X,Y,Z):
    num = len(X)

    matrix = np.hstack((X**2,Y**2,Z**2,2*X*Y,2*X*Z,2*Y*Z,2*X,2*Y,2*Z))
    output = np.ones((num,1))

    [a,b,c,d,e,f,g,h,i] = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(matrix),matrix)),np.transpose(matrix)),output)

    a = -a[0]
    b = -b[0]
    c = -c[0]
    d = -d[0]
    e = -e[0]
    f = -f[0]
    g = -g[0]
    h = -h[0]
    i = -i[0]
    j = 1

    Q = np.array([[a,d,e,g],[d,b,f,h],[e,f,c,i],[g,h,i,j]])
    return Q

'''
Calculates offset and transforamtion matrix
form ellipsoid to sphere
input: quadric equation in matrix form
return: offset and matrix
sphere = (point-offset)*matrix
'''
def ellipsoid_to_sphere(Q):

    e = np.array([[Q[0][0],Q[0][1],Q[0][2]],
                  [Q[1][0],Q[1][1],Q[1][2]],
                  [Q[2][0],Q[2][1],Q[2][2]]])
    
    p3 = np.linalg.matrix_rank(e)
    p4 = np.linalg.matrix_rank(Q)
    temp = np.linalg.det(Q/np.min(Q))

    if (p3==3 and p4==4 and temp<0):
        pqr = np.array([[Q[0][3]],[Q[1][3]],[Q[2][3]]])
        pqr *= float(-1.0)
    
        e_inv = np.linalg.inv(e)
        w,v = np.linalg.eig(e)
        offset = np.dot(e_inv,pqr)
        v_inv = np.linalg.inv(v)

        xcenter = offset[0][0]
        ycenter = offset[1][0]
        zcenter = offset[2][0]

        xlen = 1/np.sqrt(abs(w[0]))
        ylen = 1/np.sqrt(abs(w[1]))
        zlen = 1/np.sqrt(abs(w[2]))

        scale1 = 1.0
        scale2 = float(xlen/ylen)
        scale3 = float(xlen/zlen)

        eigen_val_matrix = np.array([[scale1,0.0,0.0],
                                     [0.0,scale2,0.0],
                                     [0.0,0.0,scale3]])

        tr = np.dot(v,np.dot(eigen_val_matrix,v_inv))
        return [tr,[xcenter,ycenter,zcenter]]
    else:
        print "not real ellipsoid"
        return


'''
Helper function for contour plots
'''
def quadric_surface(Q,x,y,z):
    a = Q[0][0]
    f = Q[0][1]
    h = Q[0][2]
    p = Q[0][3]
    b = Q[1][1]
    g = Q[1][2]
    q = Q[1][3]
    c = Q[2][2]
    r = Q[2][3]
    d = Q[3][3]
    return a*x**2 + b*y**2 + c*z**2 + 2*f*x*y + 2*g*y*z + 2*h*z*x + 2*p*x + 2*q*y + 2*r*z + d 

'''
Plots the quadric equation
input: axis instance
       Quadric equation in matrix form
       max and min values of X,Y,Z points
return: axis instance
'''
def plot_quadric(ax,Q,xmax,xmin,ymax,ymin,zmax,zmin):
    A = np.linspace(xmin, xmax, 100) 
    B = np.linspace(min(xmin,ymin,zmin), max(xmax,ymax,zmax), 10)
    A1,A2 = np.meshgrid(A,A) 

    for z in B: 
        X,Y = A1,A2
        Z = quadric_surface(Q,X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', linewidths=0.5)

    for y in B: 
        X,Z = A1,A2
        Y = quadric_surface(Q,X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', linewidths=0.5)

    for x in B:
        Y,Z = A1,A2
        X = quadric_surface(Q,x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x', linewidths=0.5)

    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)

    return ax

