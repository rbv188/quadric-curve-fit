import numpy as np


'''
Generate rotation matrix
input: angles in degree
return: rotation matrix
'''
def rotation_matrix(a,b,c):
    a = 20*3.14/180.0
    b = 30*3.14/180.0
    c = 15*3.14/180.0
    r1 = np.array([[1,0,0],[0,np.cos(a),-np.sin(a)],[0,np.sin(a),np.cos(a)]])
    r2 = np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
    r3 = np.array([[np.cos(c),-np.sin(c),0],[np.sin(c),np.cos(c),0],[0,0,1]])
    R = np.dot(np.dot(r1,r2),r3)
    return R

'''
Generate ellipsoid points
input: angles in degrees(a1,a2,a3)
       axis length (a,b,c)
       center (centerx,centery,centerz)
'''
def ellipsoid_points(a1,a2,a3,a,b,c,centerx,centery,centerz):
    R = rotation_matrix(a1,a2,a3)
    low = -np.pi
    high = np.pi
    f = open('points.txt','w')
    for i in range(100):
        u = np.random.uniform(low=low,high=high,size=None)
        v = np.random.uniform(low=low,high=high,size=None)
        x = a*np.cos(u)*np.cos(v) 
        y = b*np.cos(u)*np.sin(v) 
        z = c*np.sin(u) 
        [xr,yr,zr] = np.dot([x,y,z],R)
        f.write(str(xr + centerx) + " " + str(yr + centery) + " " + str(zr + centerz) + "\n")
    f.close()


'''
Generate hyperboloid points
input: angles in degrees(a1,a2,a3)
       axis length (a,b,c)
       center (centerx,centery,centerz)
'''
def hyperboloid_points(a1,a2,a3,a,b,c,centerx,centery,centerz):
    R = rotation_matrix(a1,a2,a3)
    low = -np.pi
    high = np.pi
    f = open('points.txt','w')
    for i in range(100):
        u = np.random.uniform(low=low,high=high,size=None)
        v = np.random.uniform(low=low,high=high,size=None)
        x = a*np.sqrt(1+u*u)*np.cos(v)
        y = b*np.sqrt(1+u*u)*np.sin(v)
        z = c*u
        [xr,yr,zr] = np.dot([x,y,z],R)
        f.write(str(xr + centerx) + " " + str(yr + centery) + " " + str(zr + centerz) + "\n")
    f.close()


'''
Generate paraboloid points
input: angles in degrees(a1,a2,a3)
       radius and height (a,h)
       center (centerx,centery,centerz)
'''
def paraboloid_points(a1,a2,a3,a,h,centerx,centery,centerz):
    R = rotation_matrix(a1,a2,a3)
    lowv = 0
    highv = 2*np.pi
    lowu = 0
    highu = 30
    f = open('points.txt','w')
    for i in range(100):
        u = np.random.uniform(low=lowu,high=highu,size=None)
        v = np.random.uniform(low=lowv,high=highv,size=None)
        x = a*np.sqrt(float(u/h))*np.cos(v)
        y = a*np.sqrt(float(u/h))*np.sin(v)
        z = u
        [xr,yr,zr] = np.dot([x,y,z],R)
        f.write(str(xr + centerx) + " " + str(yr + centery) + " " + str(zr + centerz) + "\n")
    f.close()


'''
comment out appropriate curves
'''
hyperboloid_points(15,20,30,10,25,10,-6,12,5)
#ellipsoid_points(15,20,30,10,25,10,-6,12,5)
#paraboloid_points(15,20,30,10,25,10,-6,12)
