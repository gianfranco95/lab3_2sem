##Boltzmann
import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from scipy.optimize import curve_fit
import lab
from lab import mme
R,V=pylab.loadtxt(os.path.join(folder,'Dati','resistenze.txt')).T
R=R*1000
dR=mme(R,'ohm','lab3')
dR=dR
V=V/1000
dV=mme(V,'volt','lab3')
pylab.errorbar(R/1000,V,dV,dR/1000,'.',linestyle='')

def ff(R,V0,Rt,Rn2):
    return V0*pylab.sqrt(1 + R/Rt + R**2/Rn2)

popt,pcov=curve_fit(ff,R,V,sigma=dV,)
V0_fit,Rt_fit,Rn2_fit=popt
dV0_fit,dRt_fit,dRn2_fit=pylab.sqrt(pcov.diagonal())
cov_V0_Rt=pcov[0,1]
w=pylab.linspace(min(R),max(R),1000)

pylab.plot(w/1000,ff(w,V0_fit,Rt_fit,Rn2_fit))
pylab.title('Potenziale in udcita in funzione della resistenza')
pylab.xlabel('R [$\Omega$]')
pylab.ylabel('$V_{rms}$ [V]')
pylab.show()
##
A0=169.95*776
dA0=A0/100
T=303
dT=T/100
Df=976.62
dDf=Df/100
#

k=V0_fit**2/(4*Rt_fit*T*(A0**2)*Df)
dk=pylab.sqrt( (2*k*dV0_fit/V0_fit)**2  +(k*dRt_fit/Rt_fit)**2 +(k*dT/T)**2  +  (2*k*dA0/A0)**2  + (k*dDf/Df)**2     +    2*(2*k/V0_fit)*(-k/Rt_fit)*cov_V0_Rt)
print('k=%f+-%f'%(k,dk))