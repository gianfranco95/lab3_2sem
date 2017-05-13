import pylab
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
from lab import mme

T,dT,Vout,dVout=pylab.loadtxt(os.path.join(folder,'Dati','risposta_frequenza.txt')).T
V0in=19/1000
dV0in=5/1000
R1=987
R2=0.994
dR1=mme(R1*1000,'ohm','lab3')/1000
dR2=mme(R2*1000,'ohm','lab3')/1000
Vin=V0in*R2/(R1+R2)
dVin=Vin*pylab.sqrt( (dV0in/V0in)**2 + (dR2/R2)**2 + (dR1**2+dR2**2)/(R1+R2)**2)
A = Vout/Vin
dA = ((dVout/Vout)**2+(dVin/Vin)**2)*A
f=(10**6)/(T)
df=(10**6)*dT/(T**2)
Abode=20*pylab.log(A)/pylab.log(10)
dAbode=20*dA/(A*pylab.log(10))
fbode=pylab.log10(f)
dfbode=df/(f*pylab.log(10))
pylab.figure(1)
pylab.errorbar(fbode,Abode,dAbode,dfbode,color = 'black',linestyle = '')
# pylab.xscale('log')
# pylab.yscale('log')
pylab.xlabel('frequenza [log(Hz)]')
pylab.ylabel('Amplificazione [dB]')

from scipy.optimize import curve_fit

def Gg(x,f2,fi,A0):
    return A0*(2*math.pi*x)/(pylab.sqrt(f2+((2*math.pi*x) -fi)**2)*pylab.sqrt(f2+((2*math.pi*x)+fi)**2))
popt,pcov=curve_fit(Gg,f,A,p0=[2000,6400,76600],sigma=dA)
f2_fit,fi_fit,A_fit=popt
df2_fit,dfi_fit,dA_fit=pylab.sqrt(pcov.diagonal())
w=pylab.logspace(pylab.log10(min(f)),pylab.log10(max(f)),100)
X=pylab.log10(w)
Y=20*pylab.log10(Gg(w,f2_fit,fi_fit,A_fit))
pylab.plot(X,Y)
pylab.title('Risposta del circuito totale')
pylab.show()

G=Gg(fi_fit/(2*math.pi),f2_fit,fi_fit,A_fit)
w=fi_fit
dwi=dfi_fit
wi=fi_fit
wr2=f2_fit
dwr2=df2_fit
cov1=pcov[0,1]
cov2=pcov[0,2]
cov3=pcov[1,2]
dG= numpy.sqrt( (G/A_fit)**2*(dA_fit)**2 + (G*(w-wi)/((w-wi)**2 + wr2) - G*(w+wi)/((w+wi)**2 + wr2))**2*(dwi)**2 + (0.5*G/((w-wi)**2 + wr2) +0.5*G/((w+wi)**2+wr2) )**2*(dwr2)**2 + 2*(G/A_fit)*(G*(w-wi)/((w-wi)**2 + wr2) - G*(w+wi)/((w+wi)**2 + wr2))*cov3+ 2*(G/A_fit)*(0.5*G/((w-wi)**2 + wr2) +0.5*G/((w+wi)**2+wr2) )*cov2 + 2*(0.5*G/((w-wi)**2 + wr2) +0.5*G/((w+wi)**2+wr2) )*(G*(w-wi)/((w-wi)**2 + wr2) - G*(w+wi)/((w+wi)**2 + wr2))*cov1)



ENB=(0.5)*math.sqrt(f2_fit)
dENB=0.5*df2_fit/(2*math.sqrt(f2_fit))
ndof=len(Vout)-3
chisq=sum( ((Gg(f,f2_fit,fi_fit,A_fit)-A)/dA)**2)
print('EnB= %f +- %f [Hz]'%(ENB,dENB))
print('f0= %f +- %f [Hz]'%(fi_fit/(2*math.pi),dfi_fit/(2*math.pi)))
print('Amplificazione centrobanda= %f +-%f'%(G,dG))
print('chisq/ndof= %f/%i'%(chisq,ndof))


Vin20,dVin20,Vout2,dVout2=pylab.loadtxt(os.path.join(folder,'Dati','risposta_ampiezza.txt')).T
Vin2=Vin20*R2/(R1+R2)
dVin2=Vin2*pylab.sqrt( (dVin20/Vin20)**2 + (dR2/R2)**2 + (dR1**2+dR2**2)/(R1+R2)**2)
T0=310 #mus
dT0=8
f=(10**6)/T0
df=dT0*(10**6)/(T0**2)
def f2(x,m,q):
    return m*x+q

popt,pcov=curve_fit(f2,Vin2,Vout2,sigma=dVout2)
m2,q2=popt
dm2,dq2=pylab.sqrt(pcov.diagonal())
smq2 =pcov[0,1]

popt,pcov=curve_fit(f2,Vin2,Vout2,sigma=dVout2)
m2,q2=popt
dm2,dq2=pylab.sqrt(pcov.diagonal())
smq2 =pcov[0,1]


w=pylab.linspace(min(Vin2)*2/3,max(Vin2)*4/3,10)
pylab.figure(2)
pylab.errorbar(Vin2*1000,Vout2/1000,dVout2/1000,dVin2*1000,'.',linestyle='')
pylab.plot(w*1000,f2(w,m2,q2)/1000)
pylab.title('Risposta circuito totale; frequenza %.2f $\pm$ %.2f kHz'%(f/1000,df/1000))
pylab.xlabel('$V_{in}$ [$\mu$V]')
pylab.ylabel('$V_{out}$ [V]')
pylab.show()

chisq2 = (((f2(Vin2,m2,q2)-Vout2)/dVout2)**2).sum()
ndof2=len(Vin2)-2
print('m2=%f+-%f   q2=%f+-%f  mV   normcov=%f   chisq/ndof=%f/%i'%(m2,dm2,q2,dq2,smq2/(dq2*dm2),chisq2,ndof2))
