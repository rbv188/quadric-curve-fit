# quadric-curve-fit
Python project for 3d quadric curve fitting

The project fits a quadric equation to a set of 3d points using least-squares. The project also includes some examples.

A common application for this is in the calibration of 3 axis magnetometers. Magnetometer readings are logged and an Ellipsoid is fit to the points. A transformation matrix is then calculated to move the points on to a sphere.  

Example 1 is a basic curve fitting script. The data points and the calculated curve is plotted for comparison. 
![Alt text](/images/figure1.png?raw=true)  ![Alt text](/images/figure3.png?raw=true)

Example 2 is for ellipsoid to sphere transformation used in magnetometer calibration. Points in red represent the ellipsoid corresponding to uncalibrated magnetometer readings. Points in blue are the calibrated readings.
![Alt text](/images/figure2.png?raw=true)

points_gen.py is used to generate points in 3d. Ellipsoid, hyperboloid and paraboloid are given in this script. The points are generated using parametric equations of the respective curves. 

