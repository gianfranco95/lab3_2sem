##preamplificatore
import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
T,dT,Vin,dVin,Vout,dVout=pylab.loadtxt(os.path.join(folder,'Dati','preamp.txt')).T
Vout = Vout*1000
dVout = dVout*1000
A = Vout/Vin
dA = ((dVout/Vout)**2+(dVin/Vin)**2)*A
f=1000/T
df=1000*dT/(T**2)
Abode=20*pylab.log(A)/pylab.log(10)
dAbode=20*dA/(A*pylab.log(10))
fbode=pylab.log10(f)
dfbode=df/(f*pylab.log(10))
pylab.errorbar(fbode,Abode,dAbode,dfbode,color = 'black',linestyle = '')
# pylab.xscale('log')
# pylab.yscale('log')
pylab.xlabel('frequenza [log(Hz)]')
pylab.ylabel('Amplificazione [dB]')

from scipy.optimize import curve_fit

def f(x,m,q):
    return m*x+q
n1=0
m1=4
n2=5
m2=9
x1=pylab.zeros(m1-n1+1)
dx1=pylab.zeros(m1-n1+1)
y1=pylab.zeros(m1-n1+1)
dy1=pylab.zeros(m1-n1+1)

x2=pylab.zeros(m2-n2+1)
dx2=pylab.zeros(m2-n2+1)
y2=pylab.zeros(m2-n2+1)
dy2=pylab.zeros(m2-n2+1)

for i in range(0,len(x1)):
    y1[i]=Abode[n1+i]
    dy1[i]=dAbode[n1+i]
    x1[i]=fbode[n1+i]
    dx1[i]=dfbode[n1+i]

for i in range(1,len(x2)):
    y2[i]=Abode[n2+i]
    dy2[i]=dAbode[n2+i]
    x2[i]=fbode[n2+i]
    dx2[i]=dfbode[n2+i]


popt,pcov=curve_fit(f,x1,y1,sigma=dy1)
m1,q1=popt
dm1,dq1=pylab.sqrt(pcov.diagonal())


w=pylab.linspace(min(x1),max(x1),10)
pylab.plot(w,f(w,m1,q1))
pylab.show()
##
popt,pcov=curve_fit(f,x2,y2,sigma=dy2)
m2,q2=popt
dm2,dq2=pylab.sqrt(pcov.diagonal())


w2=pylab.linspace(min(x2),max(x2),10)
pylab.plot(w2,f(w2,m2,q2))

pylab.show()

##passabanda
import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
T,dT,Vin,dVin,Vout,dVout=pylab.loadtxt(os.path.join(folder,'Dati','passabanda.txt')).T
Vout = Vout*1000
dVout = dVout*1000
A = Vout/Vin
dA = ((dVout/Vout)**2+(dVin/Vin)**2)*A
f=1000/T
df=1000*dT/(T**2)
Abode=20*pylab.log(A)/pylab.log(10)
dAbode=20*dA/(A*pylab.log(10))
fbode=pylab.log10(f)
dfbode=df/(f*pylab.log(10))
pylab.errorbar(fbode,Abode,dAbode,dfbode,color = 'black',linestyle = '')
# pylab.xscale('log')
# pylab.yscale('log')
pylab.xlabel('frequenza [log(Hz)]')
pylab.ylabel('Amplificazione [dB]')

from scipy.optimize import curve_fit

def ff(x,f2,fi,A):
    return A*x/(pylab.sqrt(f2+(x-fi)**2)*pylab.sqrt(f2+(x+fi)**2))
popt,pcov=curve_fit(ff,f,A,p0=[2000,6400,-1],sigma=dA,)
f2_fit,fi_fit,A_fit=popt
df2_fit,dfi_fit,dA_fit=pylab.sqrt(pcov.diagonal())
w=pylab.logspace(pylab.log10(min(f)),pylab.log10(max(f)),100)
X=pylab.log10(w)
Y=20*pylab.log10(ff(w,f2_fit,fi_fit,A_fit))
pylab.plot(X,Y)
pylab.show()

ENB=math.pi*pylab.sqrt(f2_fit)
dENB=math.pi*df2_fit/(2*ENB)
print('EnB= %f +- %f'%(ENB,dENB))

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
R,V=pylab.loadtxt(os.path.join(folder,'Dati','resistenze.txt')).T
R=R
V=V/1000
dR=R/100
dV=V/100
pylab.errorbar(R,V,dV,dR,'o',linestyle='')

def ff(R,V0,Rt,Rn2):
    return V0*pylab.sqrt(1 + R/Rt + R**2/Rn2)

popt,pcov=curve_fit(ff,R,V,sigma=dV,)
V0_fit,Rt_fit,Rn2_fit=popt
dV0_fit,dRt_fit,dRn2_fit=pylab.sqrt(pcov.diagonal())
w=pylab.linspace(min(R),max(R),1000)

pylab.plot(w,ff(w,V0_fit,Rt_fit,Rn2_fit))
pylab.show()





