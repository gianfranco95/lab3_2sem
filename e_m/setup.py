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
datafile1=['datiB1.txt']
datafile2=['datiB2.txt']
datafile3=['datiB3.txt']
datafile4=['datiB4.txt']
datafile5=['datiB5.txt']
datafile6=['datiB6.txt']
V1,d1=importa(datafile1)
V2,d2=importa(datafile2)
V3,d3=importa(datafile3)
V4,d4=importa(datafile4)
V5,d5=importa(datafile5)
V6,d6=importa(datafile6)
d = numpy.array([d1,d2,d3,d4,d5,d6])
V = numpy.array([V1,V2,V3,V4,V5,V6])
raggio=numpy.ones(len(d))*((31.6-1.9)/2)
r=raggio-(d-1.9*numpy.ones(len(d)))



Vout=V/1000 #In volt
dVout=1/1000
#Fattore di amplificazione
A=11.090
dA=0.003
#Fattore di calibrazione della sonda
Q=0.005 #Volt/Gauss
dQ=0.0001

Vh=Vout/A
dVh=((dVout/A)**2 + (Vout*dA/(A**2))**2)**(1/2)

B=Vh/Q #Gauss
dB=((dVh/Q)**2 + (Vh*dQ/(Q**2))**2)**(1/2)
# print('Campo in Gauss = %f +- %f' % (B,dB))

BT=B*10**(-4)
rm=r*10**(-2)
dBT=dB*10**(-4)

#pylab.figure(1)
#pylab.plot(rm,BT,'o')
#pylab.show()

##Altre cose che si possono fare: 
# mappare Bz e fare fit a Bz/Bzmax per ottenere il raggio delle bobine che serve a corregger il campo magnetico per quando si farà il fit circolare per trovare e_m
N=130
def f(r,r0,A):
    return Bz_tot(A,r0,r,0,1,r0)

from scipy.optimize import curve_fit
i = 0
popt=pcov=r0=A0=dr0=dA0=I0=dI0=chisq=ndof=cov=numpy.ones(len(rm))
while i < len(rm):
    popt[i], pcov[i]=curve_fit(f,rm[i],BT[i],pylab.array([0.15,0.]),sigma=dBT[i],absolute_sigma=True)
    r0[i]=popt[i][0]
    A0[i]=popt[i][1]
    dr0[i],dA0[i]=pylab.sqrt(pcov[i].diagonal())
    cov[i] = pcov[i][0,1]/(dA0[i]*dr0[i])
    I0[i]=(10**7)*A0[i]/N
    dI0[i]=(I0[i]/A0[i])*dA0[i]
    chisq[i] = (((BT[i]-f(rm[i],r0[i],A0[i]))/dBT[i])**2).sum()
    ndof[i] = len(B[i])-2
    i = i+1
print ('Corrente in Ampere= ',I0,dI0)
print ('raggio = ',r0,dr0)
print ('Covarianza = ',cov)
print ('Chi quadro/ dof = ',chisq, ndof)
r001=(r0/(dr0**2)).sum()
r002=(1/(dr0**2)).sum()
r00=r001/r002
dr00=numpy.sqrt(1/r002)
print('raggio medio = ',r00,dr00)


pylab.figure(1) #Grafico con datiB1
pylab.title('Mappatura campo magnetico')
pylab.ylabel('Bz [T]')
pylab.subplot(211)
pylab.errorbar(rm[0],BT[0],dBT[0],drm[0],marker='o',color='black')
x=pylab.linspace(min(rm[0]),max(rm[0]),1000)
pylab.plot(x,f(x,r0[0],A0[0]),'-')
pylab.subplot(221)
pylab.xlabel('r[m]')
pylab.ylabel('Scarto normalizzato')
pylab.errorbar(rm[0],(BT[0]-f(rm[0],r0[0],A0[0]))/dBT[0], marker = 'o',color 0 'black')
pylab.show()