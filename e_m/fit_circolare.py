import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special
import numpy.linalg
D=numpy.diag((0,0,0))
D_inv=numpy.diag((0,0,0))
E=numpy.zeros(3)
Q=numpy.zeros(3)

D[0][0]=2*(sum(x))
D[0][1]=2*(sum(y))
D[0][2]=len(x)
D[1][0]=2*(sum((x**2)))
D[1][1]=2*(sum(x*y))
D[1][2]=D[0][0]/2
D[2][0]=D[1][1]
D[2][1]=2*sum((y**2))
D[2][2]=D[0][1]/2

E[0]=sum((x**2)+(y**2))
E[1]=sum((x**3) + x*(y**2))
E[2]=sum((x**2)*y + y**3)

D_inv= numpy.linalg.inv(D)

for i in range(0,2):
    s=0
    for j in range(0,2):
        s=s+ D_inv[i][j]*E[j]
    Q[i]=s

R=pylab.sqrt(Q[2]+ Q[0]**2 + Q[1]**2)