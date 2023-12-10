import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

xymin = 0
xymax = 3
Npts = 50
xv, yv = np.meshgrid(np.linspace(xymin, xymax, Npts), np.linspace(xymin, xymax, Npts))

zv = np.zeros((xv.shape))
for i in range(xv.shape[0]):
    for j in range(xv.shape[1]):
        zv[i,j] = sigmoid(xv[i,j]*yv[i,j])
    
# create figure
fig = plt.figure()
plt.contourf(xv, yv, zv, levels=xv.shape[0], cmap=plt.cm.gist_yarg)
# here's a fancy colormap
# plt.contourf(xv, yv, zv, levels=xv.shape[0], cmap=plt.cm.inferno)
plt.title('using contourf')
plt.colorbar()

fig = plt.figure()
plt.contour(xv, yv, zv, levels=xv.shape[0], cmap=plt.cm.gist_yarg)
plt.title('using contour')
plt.colorbar()

# you should be able to rotate this figure with your mouse
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xv, yv, zv, cmap=plt.cm.gist_yarg)
# how to get a colorbar for a 3d contour?

plt.show()
print()




