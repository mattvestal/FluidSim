from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import numpy as np
import os
datu = np.loadtxt('u.dat')
datv = np.loadtxt('v.dat')
datT = np.loadtxt('T.dat')
top = np.loadtxt('topo.dat')
top = top[1:-1, 1:-1]
x = np.linspace(0,251,251)
y = np.linspace(0,101,101)
X,Y=np.meshgrid(x,y)
levels = np.arange(0,2,0.05)

#fig,ax = plt.figure(figsize=(10,6))

images = []
#h = ax.plot_wireframe(X,Y,height,color='black')
plot = None
flow = None
topo = None
h = None
n=0
Rey = []
dim = len(datu)/101

while n<dim:
    fig,ax = plt.subplots(figsize=(10,6))
    ind = np.arange(0,101) + n*101
    Uuse = []
    Vuse = []
    Tuse = []
    for i in ind:
        u = datu[i]
        v = datv[i]
        t = datT[i]
        Uuse.append(u)
        Vuse.append(v)
        Tuse.append(t)
    Uuse = np.array(Uuse)
    Vuse = np.array(Vuse)
    incident = Uuse[:,0]
    inV = np.mean(incident)
    Re = inV*300/(1.3763*10e-5)
    Rey.append(Re)
    #Mre = np.mean(Rey)
    if flow:
        ax.collections=[]
        #ax.collections.remove(flow)
    #title = ax.set_title('Re = '+str(Re)+'      Mean Re = '+str(Mre),loc='left')
    title = ax.set_title('Re = '+str(Re)+'  t = '+str((n+1)*(2-1.98958337))+' days',loc='left')
    flow = ax.contour(X,Y,Tuse,levels)
    topo = ax.contour(X,Y,top)
    im = plt.savefig('plot'+str(n)+'.png')
    images.append('plot'+str(n)+'.png')
    plt.close()


    #print(n)
    n=n+1

frames = []
for i in images:
    new_frame = Image.open(i)
    frames.append(new_frame)
    os.remove(i)

frames[0].save('animated.gif', format='GIF', append_images=frames[1:],save_all=True, loop=0)
