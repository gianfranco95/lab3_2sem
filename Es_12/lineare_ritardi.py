import pylab
import numpy
import scipy.optimize

from scipy.optimize import curve_fit
x=pylab.array([1.,2.,3.,4.])
x1=pylab.array([1,2,3,4])
y=pylab.array([14.4, 26, 38, 50])
dy=pylab.array([0.4, 1, 1, 1])

def f(x,a,b):
    return a*x+b

popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
pylab.plot(x1,y,'o')
pylab.errorbar(x1,y,dy,xerr=None,linestyle='')
pylab.plot(x1,f(x1,m_fit,q_fit),linestyle='-')
pylab.title('Ritardo segnale')
pylab.xlabel('N° flip-flop')
pylab.ylabel('Ritardo [ns]')
pylab.show()
#Chi quadro
chisquare=sum(((y-f(x,m_fit,q_fit))**2)/((dy)**2))
dof=len(y)-2
pchi = scipy.special.chdtrc(dof,chisquare)

print('Fit numerico (errore x,y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f) \n chi/ndof= %f/%i'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov,chisquare,dof))
