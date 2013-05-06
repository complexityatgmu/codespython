'''
Created on Apr 29, 2013

@author: josemagallanes
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from matplotlib import cm

data = np.genfromtxt('test.csv', dtype=[('c','S5'),('x',int),('y',int),('z1',int),('z2',int),('n','S5')],comments='"', delimiter=',')
con_levels = 20
x = data['x']#[1:]
xmin = 0
xmax = x.max() + 5
y = data['y']#[1:]
sample_pts = len(zip(x,y))
ymin = 0
ymax = y.max() + 5
z = data['z2']#[1:]
print x
print y
xi = np.linspace(xmin,xmax,sample_pts)
yi = np.linspace(ymin,ymax,sample_pts)
zi = griddata(x,y,z,xi,yi)
plt.contour(xi,yi,zi,con_levels,linewidths=1)
plt.scatter(x,y,c=z,s=20)

labels = data['c']#[1:]
for label, cx, cy in zip(labels, x, y):
    plt.annotate(
        label, 
        xy = (cx, cy), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',size='xx-small',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'white', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.show()

import scipy.interpolate
# Set up a regular grid of interpolation points
xi, yi = np.meshgrid(xi, yi)
# Interpolate
rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
zi1 = rbf(xi, yi)
plt.imshow(zi1, vmin=z.min(), vmax=z.max(), origin='lower', extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=z)
plt.colorbar()
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.show()
########
from mpl_toolkits.mplot3d.axes3d import Axes3D #@UnusedImport
from math import pi
fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(xi, yi, zi, rstride=4, cstride=4, alpha=0.05)
cset = ax.contour(xi, yi, zi, zdir='z', offset=-pi, cmap=cm.coolwarm) #@UndefinedVariable
cset = ax.contour(xi, yi, zi, zdir='x', offset=-pi, cmap=cm.coolwarm)#@UndefinedVariable
cset = ax.contour(xi, yi, zi, zdir='y', offset=3*pi, cmap=cm.coolwarm)#@UndefinedVariable
plt.show()