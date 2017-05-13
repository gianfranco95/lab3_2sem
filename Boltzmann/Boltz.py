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
R,V,dV=pylab.loadtxt(os.path.join(folder,'Dati','resistenze.txt')).T
R=R*1000
dR=mme(R,'ohm','lab3')
dR=dR
V=V/1000
dV=dV/1000
# dV=mme(V,'volt','lab3')
R=R/1000
dR=dR/1000
pylab.errorbar(R,V,dV,dR,'.',linestyle='')

def ff(R,V0,Rt,Rn2):
    return V0*pylab.sqrt(1 + R/Rt + R**2/Rn2)

popt,pcov=curve_fit(ff,R,V,p0=[0.06,7.780,9.2*(10**3)],sigma=dV)
V0_fit,Rt_fit,Rn2_fit=popt
dV0_fit,dRt_fit,dRn2_fit=pylab.sqrt(pcov.diagonal())
cov_V0_Rt=pcov[0,1]
w=pylab.linspace(min(R),max(R),1000)

pylab.plot(w,ff(w,V0_fit,Rt_fit,Rn2_fit))
pylab.title('Potenziale in udcita in funzione della resistenza')
pylab.xlabel('R [k$\Omega$]')
pylab.ylabel('$V_{rms}$ [V]')
pylab.show()
ndof=len(R)-3
chisq=sum((ff(R,V0_fit,Rt_fit,Rn2_fit)-V)**2/(dV**2))
print('V0=%f+-%f  Rt=%f+-%f   Rn2=%f+-%f  normcov=%f   chisq/ndof=%f/%i'%(V0_fit,dV0_fit,Rt_fit,dRt_fit,Rn2_fit,dRn2_fit,cov_V0_Rt/(dV0_fit*dRt_fit),chisq,ndof))
Rt_fit=Rt_fit*1000
dRt_fit=dRt_fit*1000
Rn2_fit=Rn2_fit*10**6
dRn2_fit=dRn2_fit*10**6
cov_V0_Rt=cov_V0_Rt*1000

Apre=776
dApre=11
Apost=169.95
dApost=Apost/100

A0=Apre*Apost
dA0=pylab.sqrt( (dApre/Apre)**2 + (dApost/Apost)**2)*A0

T=298
dT=3
Df=1534
dDf=160


k=V0_fit**2/(4*Rt_fit*T*(A0**2)*Df)
dk=pylab.sqrt( (2*k*dV0_fit/V0_fit)**2  +(k*dRt_fit/Rt_fit)**2 +(k*dT/T)**2  +  (2*k*dA0/A0)**2  + (k*dDf/Df)**2     +    2*(2*k/V0_fit)*(-k/Rt_fit)*cov_V0_Rt)
print('k=%e+-%e'%(k,dk))