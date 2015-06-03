# -*- coding: utf-8 -*-

import numpy as np;
from matplotlib import pyplot as plt;
from matplotlib import animation;
from matplotlib import rc;

fig = plt.figure()
ax1 = plt.axes(xlim=(0,np.pi),ylim=(-1.5,1.5))
ax2 = plt.axes(xlim=(0,np.pi),ylim=(-1.5,1.5))
line, = ax1.plot([],[], lw=2, color='m')
line2, = ax2.plot([],[], lw=2, color='b')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

rc('font', **font)

def abstand(x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2+(y2-y1)**2)

def f(x):
    return np.sin(x)
    
def init():
    line.set_data([],[])
    plt.grid()
    return line, 
    
def animate(N):
    xi = np.linspace(a,b,N)
    yi = np.array([f(x) for x in xi])
    line.set_data(xi,yi)
    line2.set_data(xs,ys)
    plt.title('N = %s' % str(N))
    return line,line2

N=50
Ns=1000
a=0
b=np.pi
xs = np.linspace(a,b,N)
ys = [f(x) for x in xs]

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=20, interval=1000)
                               
anim.save('approx2.gif',writer='imagemagick',fps=1)     

plt.show()  
