# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot

def abstand(x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2+(y2-y1)**2)

def punktmenge(N):
    xi = np.linspace(a,b,N)
    yi = [f(x) for x in xi]
    return [xi, yi]

def bogenlaenge(N):
    [xi,yi] = punktmenge(N)
    s = 0.
    for i in range(N-1):
        s = s + abstand(xi[i],yi[i],xi[i+1],yi[i+1])
    return s

def dump(N,s,e):
    print "{:6d} {:16.8e} {:16.8e}".format(N,s,e)

def dumpHeadline():
    print
    print "{:>6s} {:>17s} {:>16s}".format('N','Bogenlänge s','Fehler e')
    print "----------------------------------------"

def drawPlot(hi,ei):
    fig = pyplot.figure()
    fig.suptitle("sin(x)")
    pyplot.plot(hi,ei,'o-')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlabel('Gitterweite h')
    pyplot.ylabel('Fehler e')
    pyplot.grid()
    
def f(x):
    return np.sin(x)

a = np.double(0)
b = np.double(np.pi)

N = 4096
sref = bogenlaenge(N)


Ni = [2,4,8,16,32,64,128,256,512,1024]
hi = []
ei = []
dumpHeadline()
for N in Ni:
    s = bogenlaenge(N)
    h = (b-a)/(N-1)
    e = np.fabs(s-sref)
    hi.append(h)
    ei.append(e)
    dump(N,s,e)

drawPlot(hi,ei)