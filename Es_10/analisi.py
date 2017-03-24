import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from lab import mme

x,y=pylab.loadtxt(os.path.join(folder,'Dati','Parte1.txt')).T
dx=mme(x,'volt','lab3',sqerr=False)
dy=mme(y,'volt','lab3',sqerr=False)
pylab.figure(1)
pylab.plot(x,y,'.',linestyle='')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')
pylab.xlabel('$V_{in}$ [V]')
pylab.ylabel('$V_{out}$ [V]')
pylab.show()

x1,dx1,y1=pylab.loadtxt(os.path.join(folder,'Dati','correnteingresso.txt')).T
x1=x1/1000
dx1=dx1/1000
dy1=(10**3)*mme(y1*10**(-3),'ampere','lab3',sqerr=False)
pylab.figure(2)
pylab.plot(x1,y1,'.',linestyle='')
pylab.errorbar(x1,y1,yerr=dy1,xerr=dx1,linestyle='')
pylab.xlabel('$V_{in}$ [V]')
pylab.ylabel('$I_{in}$ [mA]')
pylab.show()

