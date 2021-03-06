import  os
folder = os.path.realpath('.')
# from lab import *
import numpy
import math
import pylab
import scipy
import scipy.special

D = (204.5+207.5)/2 #distanza tra schermo e laser su reticolo
dD = (207.5-204.5)/2
d = 0.1

datafile = 'lunghezza_onda.txt'
h,m,dh=pylab.loadtxt(os.path.join(folder, 'Dati', datafile)).T
dh = numpy.sqrt((0.1*numpy.ones(len(h)))**2+(0.5*numpy.ones(len(h)) )**2 )

#modello Y=ax+b; 
#Y=sin(theta_d);  a=-l/d;  x=m;   b=sin(theta_i)
x=m
c=h/D
dc=pylab.sqrt( (dh/D)**2 + ( h*dD/(D**2) )**2 ) 
Y=1/pylab.sqrt(1+(c**2))

dY=dc*c/( (1+c**2)**(3/2))

#fit

def f(x,a,b):
    return a*x+b
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x,Y,pylab.array([400.,0.]),sigma=dY,absolute_sigma=True)
a_fit,b_fit=popt
da_fit,db_fit=pylab.sqrt(pcov.diagonal())
ab_cov=pcov[0,1]
ab_norm_cov=ab_cov/(da_fit*db_fit)
print('Fit numerico (errore y)\n a=%f+-%f \n b=%f+-%f  covarianza(normalizzata)=%f(%f)'%(a_fit,da_fit,b_fit,db_fit,ab_cov,ab_norm_cov))
#Chi quadro
chisquare=sum(((Y-f(x,a_fit,b_fit))**2)/((dY)**2))
dof=len(Y)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.subplot(211)
pylab.ylabel('y')
pylab.xlim(-1,22)
pylab.title('Misura lunghezza onda laser He-Ne')
pylab.grid(color='gray')
pylab.plot(x,Y, 'o')
pylab.plot(x,f(x,a_fit,b_fit), color='black')
pylab.errorbar(x,Y,yerr=dY,xerr=None,linestyle='')
pylab.subplot(212)
pylab.xlim(-1,22)
pylab.title('Residui')
pylab.xlabel(' m')
pylab.plot(x,(Y-f(x,a_fit,b_fit))/dY,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
# pylab.show()

l=-d*a_fit*10**5
dl=d*da_fit*10**5
print('lambda=%f +-%f'%(l,dl))


##tabella in latex
# i=0
# while i<len(h):
#     print('%2.1f & %1.1f & %2.f \\\ '%(h[i],dh[i],m[i]))
#     i=i+1
