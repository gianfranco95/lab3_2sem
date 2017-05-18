import pylab
import  os
#folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special

#n,Vout=pylab.loadtxt(os.path.join(folder,'Dati','risposta_frequenza.txt')).T
n,Vout=pylab.loadtxt('C:/Users/Leonardo/Desktop/Lock_in.txt',unpack=True)
dVout=pylab.sqrt((Vout*0.5/100)**2+1)
from scipy.optimize import curve_fit

def F(x,a,b):
    return a*pylab.exp(-x/b)
popt,pcov=curve_fit(F,n,Vout,p0=[1000,1],sigma=dVout)
a0,b0=popt
da0,db0=pylab.sqrt(pcov.diagonal())
pylab.title('Tensione di uscita in funzione del numero di lastrine')
pylab.xlabel('numero lastrine')
pylab.ylabel('V$_{out}$ [mV]')
pylab.errorbar(n,Vout,dVout,color = 'black',marker = '',linestyle='')
r=pylab.linspace(-0.5,13,100)
pylab.plot(r,F(r,a0,b0),color = 'black')
chisq=(((F(n,a0,b0)-Vout)/dVout)**2).sum()
ndof=len(Vout)-2
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])