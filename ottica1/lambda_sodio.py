import  os
folder = os.path.realpath('.')
from lab import *
##Fit lineare di calibrazione(x inverso di lunghezza d'onda; y angoli)
import numpy
import math
import pylab
import scipy
import scipy.special

datafile = 'dati_1.txt'
x,dx,y,dy=pylab.loadtxt(os.path.join(folder, 'Dati', datafile)).T
pylab.figure(1)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y-f(x,m_fit,q_fit))**2)/((dy)**2))
dof=len(y)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(2)
pylab.subplot(211)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')
pylab.plot(x,f(x,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel(' x')
pylab.plot(x,(y-f(x,m_fit,q_fit))/dy,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
## includere errore sulle x
i_max=1000
nano=10**(-10)
iter=0
dy0=dy
for i in range(0,i_max):
    m_prev=m_fit
    q_prev=q_fit
    dy=pylab.sqrt(dy**2+(m_fit*dx)**2)
    popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
    m_fit,q_fit=popt
    dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
    mq_cov=pcov[0,1]
    dy=dy0
    if (abs(m_prev-m_fit)+abs(q_prev-q_fit))<nano:
        break

mq_norm_cov=mq_cov/(dm_fit*dq_fit)

print('Fit numerico (errore x e y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
print('Iterazioni: %i\nStabilizzazione(p-p_prev) = %e'%(i,(abs(m_fit-m_prev)+abs(q_fit-q_prev))))

#Chi quadro
chisquare=sum(((y-f(x,m_fit,q_fit))**2)/(dy**2+(m_fit*dx)**2))
dof=len(y)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))

#Grafico
pylab.figure(3)
pylab.subplot(211)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')
pylab.plot(x,f(x,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel(' x')
pylab.plot(x,(y-f(x,m_fit,q_fit))/dy,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
    
##Determinazione lunghezza d'onda(atteso 589 nm)
theta=56
dtheta=2
L=m_fit/(theta-q_fit)
dL=math.sqrt( (dm_fit/(theta-q_fit))**2 + ((m_fit/((theta-q_fit)**2))**2 )*(dq_fit**2+dtheta**2)+ 2*mq_cov/((theta-q_fit)**2))

print('Lunghezza d onda=%f+-%f'%(L,dL))
