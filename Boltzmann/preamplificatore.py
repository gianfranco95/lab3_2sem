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
dA = pylab.sqrt(((dVout/Vout)**2+(dVin/Vin)**2))*A
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
n2=8
m2=11
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

for i in range(0,len(x2)):
    y2[i]=Abode[n2+i]
    dy2[i]=dAbode[n2+i]
    x2[i]=fbode[n2+i]
    dx2[i]=dfbode[n2+i]
    


popt,pcov=curve_fit(f,x1,y1,sigma=dy1)
m1,q1=popt
dm1,dq1=pylab.sqrt(pcov.diagonal())
smq1 =pcov[0,1]

w=pylab.linspace(min(x1*2/3),4.048,10)
pylab.plot(w,f(w,m1,q1))

popt,pcov=curve_fit(f,x2,y2,sigma=dy2)
m2,q2=popt
dm2,dq2=pylab.sqrt(pcov.diagonal())
smq2 = pcov[0,1]

w=pylab.linspace(4.048,max(x2*4/3),10)
pylab.plot(w,f(w,m2,q2))
pylab.title('Risposta del preamplificatore')
pylab.show()
print('m1=%f+-%f dB/decade  q1=%f+-%f dB   normcov=%f'%(m1,dm1,q1,dq1,smq1/(dm1*dq1)))
print('m2=%f+-%fdB/decade  q2=%f+-%f  dB  normcov=%f'%(m2,dm2,q2,dq2,smq2/(dq2*dm2)))
chisq1 = (((f(x1,m1,q1)-y1)/dy1)**2).sum()
chisq2 = (((f(x2,m2,q2)-y2)/dy2)**2).sum()

sm1 =dm1
sq1 =dq1

sm2 =dm2
sq2 = dq2


sx=pylab.sqrt( ((sq1)**2 + (sq2)**2)/(m1-m2)**2 + ((q2-q1)**2) * (((sm1)**2 + (sm2)**2))/(m1-m2)**4  + 2*(q2-q1)*(smq2+smq1)/(m1-m2)**3   )

x=(q2-q1)/(m1-m2)

ft=10**x
dft=(10**x)*sx*math.log(10)
print('ft=%f+-%f Hz'%(ft,dft))