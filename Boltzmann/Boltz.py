
import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from scipy.optimize import curve_fit
R,V=pylab.loadtxt(os.path.join(folder,'Dati','resistenze.txt')).T
dR=R/1000
dV=V/1000
R=R*1000
V=V/1000
# pylab.plot(R,V,color = 'black',linestyle = '')
pylab.errorbar(R,V,dV,dR,'o',color = 'black',linestyle = '')
pylab.show()

def ff(R,V0,Rt,Rn2):
    return V0*pylab.sqrt(1 + R/Rt + R**2/Rn2)

popt,pcov=curve_fit(ff,R,V,sigma=dV,)
V0_fit,Rt_fit,Rn2_fit=popt
dV0_fit,dRt_fit,dRn2_fit=pylab.sqrt(pcov.diagonal())
w=pylab.linspace(min(R),max(R),1000)

pylab.plot(w,ff(w,V0_fit,Rt_fit,Rn2_fit))
pylab.show()