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
dA = numpy.sqrt(((dVout/Vout)**2+(dVin/Vin)**2))*A
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

def G(x,f2,fi,A):
    return A*(2*math.pi*x)/(pylab.sqrt(f2+((2*math.pi*x) -fi)**2)*pylab.sqrt(f2+((2*math.pi*x)+fi)**2))
popt,pcov=curve_fit(G,f,A,p0=[2000,6400,-1],sigma=dA,)
f2_fit,fi_fit,A_fit=popt
df2_fit,dfi_fit,dA_fit=pylab.sqrt(pcov.diagonal())
w=pylab.logspace(pylab.log10(min(f)),pylab.log10(max(f)),100)
X=pylab.log10(w)
Y=20*pylab.log10(G(w,f2_fit,fi_fit,A_fit))
pylab.plot(X,Y)
pylab.show()


G=G(fi_fit/(2*math.pi),f2_fit,fi_fit,A_fit)
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

print('EnB= %f +- %f [Hz]'%(ENB,dENB))
print('f0= %f +- %f [Hz]'%(fi_fit/(2*math.pi),dfi_fit/(2*math.pi)))
print('centrobanda= %f +-%f'%(G,dG))


