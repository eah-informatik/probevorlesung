# -*- coding: utf-8 -*-

import numpy as np

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

def dump(N,s):
    print "Berechnung der Bogenlänge auf [{:.2f},{:.2f}]".format(a,b)
    print "Approximierte Bogenlänge: s(N={:d}) = {:.8e}".format(N,s)

def f(x):
    return np.sin(x)

a = np.double(0)
b = np.double(np.pi)

N = 4
s = bogenlaenge(N)
dump(N,s)