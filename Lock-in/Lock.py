import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from lab import mme

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
dVout=mme(Vout/1000,'volt','lab3')*1000
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
pylab.errorbar(n,Vout,dVout,color = 'black',marker = '.',linestyle='')
r=pylab.linspace(-0.5,13,100)
pylab.plot(r,F(r,a0,b0),color = 'black')
chisq=(((F(n,a0,b0)-Vout)/dVout)**2).sum()
ndof=len(Vout)-2
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])
pylab.subplot(212)
pylab.errorbar(n,((F(n,a0,b0)-Vout)/dVout),marker = 'o', color = 'black', linestyle ='')
pylab.ylabel('Scarto normalizzato')
pylab.xlabel('numero lastrine')
pylab.show()
print('a=%f +- %f,b=%f +- %f , cov=%f  chisq=%f'%(a0,da0,b0,db0,pcov[0,1]/(da0*db0),chisq))

##Proviamo a fare in questo modo

n,Vout=pylab.loadtxt(os.path.join(folder,'Dati','Lock_in.txt')).T
dVout=pylab.sqrt((Vout*0.5/100)**2+1)
dVout=mme(Vout/1000,'volt','lab3')*1000
from scipy.optimize import curve_fit
n=n
def F2(x,a2,b2,T2):
    return (T2**x)*a2*pylab.exp(-x*b2)
popt,pcov=curve_fit(F2,n,Vout,p0=[1000,1,0.5],sigma=dVout)
a02,b02,T02=popt
da02,db02,dT02=pylab.sqrt(pcov.diagonal())
print(T02)
r2=pylab.linspace(min(n),max(n),100)
pylab.figure(3)
pylab.title('Tensione di uscita in funzione del numero di lastrine')
pylab.subplot(211)
pylab.ylabel('V$_{out}$ [mV]')
pylab.errorbar(n,Vout,dVout,color = 'black',marker = 'o',linestyle='')
pylab.plot(r2,F2(r2,a02,b02,T02),color = 'blue')
chisq2=(((F2(n,a02,b02,T02)-Vout)/dVout)**2).sum()
ndof=len(Vout)-3
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])
pylab.subplot(212)
pylab.errorbar(n,((F2(n,a02,b02,T02)-Vout)/dVout),marker = 'o', color = 'black', linestyle ='')
pylab.ylabel('Scarto normalizzato')
pylab.xlabel('numero lastrine')
pylab.show()
print('a=%f +- %f,b=%f +- %f, T=%f +- %f   chisq=%f'%(a02,da02,b02,db02,T02,dT02,chisq2))

##Proviamo a fare in quest'altro modo

n,Vout=pylab.loadtxt(os.path.join(folder,'Dati','Lock_in.txt')).T
dVout=pylab.sqrt((Vout*0.5/100)**2+1)
dVout=mme(Vout/1000,'volt','lab3')*1000
from scipy.optimize import curve_fit
n=n
def F3(x,a2,b2,T2,c2):
    return (T2**x)*a2*pylab.exp(-x*b2) + c2
popt,pcov=curve_fit(F3,n,Vout,p0=[1000,1,1,70],sigma=dVout)
a03,b03,T03,c03=popt
da03,db03,dT03,dc03=pylab.sqrt(pcov.diagonal())
r3=pylab.linspace(min(n),max(n),100)
pylab.figure(4)
pylab.title('Tensione di uscita in funzione del numero di lastrine')
pylab.subplot(211)
pylab.ylabel('V$_{out}$ [mV]')
pylab.errorbar(n,Vout,dVout,color = 'black',marker = 'o',linestyle='')
pylab.plot(r2,F3(r3,a03,b03,T03,c03),color = 'blue')
chisq3=(((F3(n,a03,b03,T03,c03)-Vout)/dVout)**2).sum()
ndof=len(Vout)-3
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])
pylab.subplot(212)
pylab.errorbar(n,((F3(n,a03,b03,T03,c03)-Vout)/dVout),marker = 'o', color = 'black', linestyle ='')
pylab.ylabel('Scarto normalizzato')
pylab.xlabel('numero lastrine')
pylab.show()
print('a=%f +- %f,b=%f +- %f, T=%f +- %f, c= %f +- %f   chisq=%f'%(a03,da03,b03,db03,T03,dT03,c03,dc03,chisq3))

##Togliamo T

n,Vout=pylab.loadtxt(os.path.join(folder,'Dati','Lock_in.txt')).T
dVout=pylab.sqrt((Vout*0.5/100)**2+1)
dVout=mme(Vout/1000,'volt','lab3')*1000
from scipy.optimize import curve_fit
n=n
def F4(x,a2,b2,c2):
    return a2*pylab.exp(-x*b2) + c2
popt,pcov=curve_fit(F4,n,Vout,p0=[1000,1,70],sigma=dVout)
a04,b04,c04=popt
da04,db04,dc04=pylab.sqrt(pcov.diagonal())
r4=pylab.linspace(min(n),max(n),100)
pylab.figure(5)
pylab.title('Tensione di uscita in funzione del numero di lastrine')
pylab.subplot(211)
pylab.ylabel('V$_{out}$ [mV]')
pylab.errorbar(n,Vout,dVout,color = 'black',marker = '.',linestyle='')
pylab.plot(r2,F4(r4,a04,b04,c04),color = 'blue')
chisq4=(((F4(n,a04,b04,c04)-Vout)/dVout)**2).sum()
ndof=len(Vout)-3
cov=pcov[0,1]/pylab.sqrt(pcov[0,0]*pcov[1,1])
pylab.subplot(212)
pylab.errorbar(n,((F4(n,a04,b04,c04)-Vout)/dVout),marker = 'o', color = 'black', linestyle ='')
pylab.ylabel('Scarto normalizzato')
pylab.xlabel('numero lastrine')
pylab.show()
print('a=%f +- %f,b=%f +- %f, c=%f +- %f   chisq=%f'%(a04,da04,b04,db04,c04,dc04,chisq4))
print('☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ sab=%f  sac=%f  sbc=%f'%(pcov[0,1]/(da04*db04),pcov[0,2]/(da04*dc04),pcov[1,2]/(db04*dc04)))