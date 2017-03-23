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

