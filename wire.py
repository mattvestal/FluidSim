import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d
import time
dat = np.loadtxt('h.dat')
x = np.linspace(0,101,101)
y = np.linspace(0,51,51)
X,Y=np.meshgrid(x,y)
#height = np.loadtxt('eta0.dat')
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_zlim(0,10.02)
#h = ax.plot_wireframe(X,Y,height,color='black')
wframe = None
h = None
tstart = time.time()
n=0
while n<191:
    t = n+1
    ind = np.arange(0,51) + n*51
    lild = []
    for i in ind:
        lild.append(dat[i])
    lild=np.array(lild)
    if wframe:
        ax.collections.remove(wframe)
    Z=lild
    title = ax.set_title('time = '+str(t)+'s',loc='left')
    wframe = ax.plot_wireframe(X, Y, Z, color='blue',alpha=0.5)
    #print(n)
    n=n+1
    plt.pause(0.001)
