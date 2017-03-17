import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special
from campo_magnetico import Bz_tot
from importare_dati import importa
##Calibrazione sonda
datafile=['datiB6.txt']
V,d=importa(datafile)
raggio=(31.6-1.9)/2
r=raggio-(d-1.9)



Vout=V/1000 #In volt
dVout=1/1000
#Fattore di amplificazione
A=11.090
dA=0.003
#Fattore di calibrazione della sonda
Q=0.005 #Volt/Gauss
dQ=0.0001

Vh=Vout/A
dVh=pylab.sqrt((dVout/A)**2 + (Vout*dA/(A**2))**2)

B=Vh/Q #Gauss
dB=pylab.sqrt((dVh/Q)**2 + (Vh*dQ/(Q**2))**2)
# print('Campo in Gauss = %f +- %f' % (B,dB))

BT=B*10**(-4)
rm=r*10**(-2)
dBT=dB*10**(-4)

pylab.figure(1)
pylab.plot(rm,BT,'o')
pylab.show()

##Altre cose che si possono fare: 
# mappare Bz e fare fit a Bz/Bzmax per ottenere il raggio delle bobine che serve a corregger il campo magnetico per quando si farà il fit circolare per trovare e_m
N=130
def f(r,r0,A):
    return Bz_tot(A,r0,r,0,1,r0)

from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,rm,BT,pylab.array([0.15,0.]),sigma=dBT,absolute_sigma=True)
r0=popt[0]
A0=popt[1]
dr0,dA0=pylab.sqrt(pcov.diagonal())
cov = pcov[0,1]/(dA0*dr0)
I0=(10**7)*A0/N
dI0=(I0/A0)*dA0
print ('Corrente in Ampere= ',I0,dI0)
print ('raggio = ',r0,dr0)
print ('Covarianza = ',cov)
chisq = (((BT-f(rm,r0,A0))/dBT)**2).sum()
ndof = len(B)-2
print ('Chi quadro/ dof = ',chisq, ndof)
x=pylab.linspace(min(rm),max(rm),1000)
pylab.plot(x,f(x,r0,A0),'-')
pylab.show()