import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time
datu = np.loadtxt('u.dat')
datv = np.loadtxt('v.dat')
datT = np.loadtxt('T.dat')
top = np.loadtxt('topo.dat')
top = top[1:-1, 1:-1]
x = np.linspace(0,151,151)
y = np.linspace(0,51,51)
X,Y=np.meshgrid(x,y)
levels = np.arange(0,2,0.05)
fig,ax = plt.subplots(figsize=(10,6))


#h = ax.plot_wireframe(X,Y,height,color='black')
plot = None
flow = None
topo = None
h = None
n=0
Rey = []
dim = len(datu)/51

while n<dim:

    ind = np.arange(0,51) + n*51
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


    #print(n)
    n=n+1
    plt.pause(0.01)
