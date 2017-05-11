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

n1=1
m1=2
n2=2
m2=5
n3=7
m3=8

x1=pylab.zeros(m1-n1+1)
dx1=pylab.zeros(m1-n1+1)
y1=pylab.zeros(m1-n1+1)
dy1=pylab.zeros(m1-n1+1)

x2=pylab.zeros(m2-n2+1)
dx2=pylab.zeros(m2-n2+1)
y2=pylab.zeros(m2-n2+1)
dy2=pylab.zeros(m2-n2+1)

x3=pylab.zeros(m3-n3+1)
dx3=pylab.zeros(m3-n3+1)
y3=pylab.zeros(m3-n3+1)
dy3=pylab.zeros(m3-n3+1)

for i in range(0,len(x1)):
    x1[i]=Abode[n1+i]
    dx1[i]=dAbode[n1+i]
    y1[i]=fbode[n1+i]
    dy1[i]=dfbode[n1+i]

for i in range(1,len(x2)):
    x2[i]=Abode[n2+i]
    dx2[i]=dAbode[n2+i]
    y2[i]=fbode[n2+i]
    dy2[i]=dfbode[n2+i]
    
for i in range(1,len(x2)):
    x2[i]=Abode[n2+i]
    dx2[i]=dAbode[n2+i]
    y2[i]=fbode[n2+i]
    dy2[i]=dfbode[n2+i]

from scipy.optimize import curve_fit

def f(x,m,q):
    return m*x+q

popt,pcov=curve_fit(f,x3,y3,sigma=dy3)
m,q=popt
dm,dq=pcov(diagonal())


w=pylab.linspace(min(x3),max(x3))
pylab.plot(w,f(w,m,q))


