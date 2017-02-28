import numpy
import math
import pylab
import scipy
import scipy.special

n=pylab.array([1,2,3])
#Energia in elettronvolt
E=pylab.array([18,36,58])
dE=pylab.array([2,2,1])
pylab.plot(n,E,'o')
pylab.errorbar(n,E,dE,linestyle='')
pylab.show()
##parabola
def f(x,a,b):
    return a*x+ a*b*(x**2)
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,n,E,pylab.array([400.,0.]),sigma=dE,absolute_sigma=True)
a_fit,b_fit=popt
da_fit,db_fit=pylab.sqrt(pcov.diagonal())
ab_cov=pcov[0,1]
ab_norm_cov=ab_cov/(da_fit*db_fit)
print('Fit numerico parabola(errore y)\n a=%f+-%f \n b=%f+-%f  covarianza(normalizzata)=%f(%f)'%(a_fit,da_fit,b_fit,db_fit,ab_cov,ab_norm_cov))
#Chi quadro
chisquare=sum(((E-f(n,a_fit,b_fit))**2)/((dE)**2))
dof=len(E)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
x=pylab.linspace(0,4,1000)
pylab.plot(x,f(x,a_fit,b_fit))
pylab.show()

##retta
def f(x,a):
    return a*x
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,n,E,pylab.array([400.]),sigma=dE,absolute_sigma=True)
a_fit=popt
da_fit=pylab.sqrt(pcov.diagonal())
print('Fit numerico retta (errore y)\n a=%f+-%f '%(a_fit,da_fit))
#Chi quadro
chisquare=sum(((E-f(n,a_fit))**2)/((dE)**2))
dof=len(E)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
x=pylab.linspace(0,4,1000)
pylab.plot(x,f(x,a_fit))
pylab.show()