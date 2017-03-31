import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from scipy.optimize import curve_fit

print('IMPULSO-RESISTENZA')
R,t,dt=pylab.loadtxt(os.path.join(folder,'Dati','Parte_alta_resistenza.txt')).T
dR = pylab.sqrt((0.8*R/100)**2+1)
pylab.figure(1)
pylab.subplot(211)
pylab.title('Durata impulso')
pylab.errorbar(R/1000,t,dt,dR/1000,linestyle='')
pylab.ylabel('$t$ [$\mu$s]')
def f(x,a,b):
    return a*x+b
dT = ((0.115881*dR)**2+dt**2)
popt, pcov=curve_fit(f,R,t,pylab.array([400.,0.]),sigma=dT,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore x,y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((t-f(R,m_fit,q_fit))**2)/((dT)**2))
dof=len(t)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
r = pylab.linspace(0.4,1.2,1000)
pylab.plot(r,f(r*1000,m_fit,q_fit),color = 'black')
pylab.subplot(212)
pylab.xlabel('R [k$\Omega$]')
pylab.ylabel('scarto normalizzato')
pylab.errorbar(R/1000,(t-f(R,m_fit,q_fit))/dT,marker = 'o', color = 'black',linestyle = '')
pylab.show()


print('PERIODO-RESISTENZA')
R,t,dt=pylab.loadtxt(os.path.join(folder,'Dati','Periodo_resistenza.txt')).T
dR = pylab.sqrt((0.8*R/100)**2+1)
dt = dt/2
pylab.figure(2)
pylab.subplot(211)
pylab.title('Periodo')
pylab.errorbar(R/1000,t,dt,dR/1000,linestyle='')
pylab.ylabel('$t$ [$\mu$s]')
def f(x,a,b):
    return a*x+b
dT = ((0.179498*dR)**2+dt**2)
popt, pcov=curve_fit(f,R,t,pylab.array([400.,0.]),sigma=dT,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore x,y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((t-f(R,m_fit,q_fit))**2)/((dT)**2))
dof=len(t)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
r = pylab.linspace(0.4,1.6,1000)
pylab.plot(r,f(r*1000,m_fit,q_fit),color = 'black')
pylab.subplot(212)
pylab.xlabel('R [k$\Omega$]')
pylab.ylabel('scarto normalizzato')
pylab.errorbar(R/1000,(t-f(R,m_fit,q_fit))/dT,marker = 'o', color = 'black',linestyle = '')
pylab.show()