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

def mappatura(datafile,i):
    V,d=importa(datafile)
    raggio=numpy.ones(len(d))*((31.6-1.9)/2)
    draggio=0.1
    r=raggio-(d-1.9*numpy.ones(len(d)))
    dr=numpy.sqrt(3)*0.1
    
    
    
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
    drm=dr*10**(-2)
    dBT=dB*10**(-4)
    
    #pylab.figure(1)
    #pylab.plot(rm,BT,'o')
    #pylab.show()
    
    #Altre cose che si possono fare: 
    # mappare Bz e fare fit a Bz/Bzmax per ottenere il raggio delle bobine che serve a corregger il campo magnetico per quando si farà il fit circolare per trovare e_m
    N=130
    def f(r,r0,A,d):
        return Bz_tot(A,r0,r,0,1,d)
    
    from scipy.optimize import curve_fit
    popt, pcov=curve_fit(f,rm,BT,pylab.array([0.15,0.,0.15]),sigma=dBT,absolute_sigma=True)
    r0,A0,d0=popt
    dr0,dA0,dd0=pylab.sqrt(pcov.diagonal())
    I0=(10**7)*A0/N
    dI0=(I0/A0)*dA0
    chisq = (((BT-f(rm,r0,A0,d0))/dBT)**2).sum()
    ndof = len(B)-3
    
    
    print ('Corrente in Ampere= %f +- %f ',I0,dI0)
    print ('raggio = %f +- %f ',r0,dr0)
    print ('distanza = %f +- %f ',d0,dd0)
    print ('Chi quadro/ dof = ',chisq, ndof)
    
    
    
    pylab.figure(i) #Grafico con datiB1
    pylab.title('Mappatura campo magnetico')
    pylab.ylabel('Bz [T]')
    pylab.subplot(211)
    pylab.errorbar(rm,BT,dBT,drm,marker='o',color='black',linestyle='')
    x=pylab.linspace(min(rm)*3/2,max(rm)*3/2,1000)
    pylab.plot(x,f(x,r0,A0,d0),'')
    pylab.subplot(212)
    pylab.xlabel('r[m]')
    pylab.ylabel('Scarto normalizzato')
    pylab.errorbar(rm,(BT-f(rm,r0,A0,d0))/dBT, marker = 'o',color = 'black',linestyle='')
    pylab.show()
    
    
    return r0,dr0,abs(d0),dd0,I0,dI0,chisq,ndof

n=6
W=numpy.ndarray(shape=(n,8), dtype=float, order='F')
x=pylab.zeros(n)
R=pylab.zeros(n)
D=pylab.zeros(n)
chi=pylab.zeros(n)
dR=pylab.zeros(n)
dD=pylab.zeros(n)

for i in range(0,n):
    datafile=(['datiB{}.txt'.format(i+1)])
    W[i]=mappatura(datafile,i+1)
for i in range(0,n):
    R[i]=W[i][0]
    dR[i]=W[i][1]
    D[i]=W[i][2]
    dD[i]=W[i][3]
    chi[i]=W[i][6]/W[i][7]
    x[i]=i+1

pylab.figure(200)
pylab.subplot(221)
pylab.plot(x,R,'o')
pylab.errorbar(x,R,yerr=dR,linestyle='')
pylab.subplot(222)
pylab.plot(x,D,'o')
pylab.errorbar(x,D,yerr=dD,linestyle='')
pylab.subplot(212)
pylab.plot(x,chi,'o')
pylab.errorbar(x,chi,yerr=dD,linestyle='')
pylab.show()

r=sum(R/(dR**2))/sum(1/dR**2)
dr=1/math.sqrt(sum(1/(dR**2)))

d=sum(D/(dD**2))/sum(1/dD**2)
dd=1/math.sqrt(sum(1/(dD**2)))

print('distanza = %f +- %f'%(d,dd))
print('raggio = %f +- %f'%(r,dr))


