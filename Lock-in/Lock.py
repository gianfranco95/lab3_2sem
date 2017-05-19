import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special

n = numpy.array([0,1,2,3,4,5])
V = numpy.array([1.36,1.10,0.936,0.744,0.644,0.504])
dV = numpy.array([0.04,0.04,0.04,0.015,0.032,0.012])
pylab.figure(1)
pylab.errorbar(n,V,dV,color = 'black', marker = '', linestyle = '')
pylab.title('Uscita del preamplificatore in funzione del numero di lastrine')
pylab.xlabel ('numero lastrine')
pylab.ylabel('V$_{out}$ [V]')
pylab.xlim(-0.5,5.5)
pylab.ylim(0.4,1.5)

n,Vout=pylab.loadtxt(os.path.join(folder,'Dati','Lock_in.txt')).T
dVout=pylab.sqrt((Vout*0.5/100)**2+1)
from scipy.optimize import curve_fit

def F(x,a,b):
    return a*pylab.exp(-x*b)
popt,pcov=curve_fit(F,n,Vout,p0=[1000,1],sigma=dVout)
a0,b0=popt
da0,db0=pylab.sqrt(pcov.diagonal())
pylab.figure(2)
pylab.title('Tensione di uscita in funzione del numero di lastrine')
pylab.subplot(211)
pylab.ylabel('V$_{out}$ [mV]')
pylab.errorbar(n,Vout,dVout,color = 'black',marker = '',linestyle='')
r=pylab.linspace(-0.5,13,100)
pylab.plot(r,F(r,a0,b0),color = 'black')
chisq=(((F(n,a0,b0)-Vout)/dVout)**2).sum()
ndof=len(Vout)-2
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])
pylab.subplot(212)
pylab.errorbar(n,((F(n,a0,b0)-Vout)/dVout),marker = 'o', color = 'black', linestyle ='')
pylab.ylabel('Scarto normalizzato')
pylab.xlabel('numero lastrine')