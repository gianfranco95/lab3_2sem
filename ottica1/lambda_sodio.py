
# from lab import *
##Fit lineare di calibrazione(x inverso di lunghezza d'onda; y angoli)
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special


datafile = 'calibrazione.txt'
rawdata = numpy.loadtxt(os.path.join(folder, 'Dati', datafile)).T
theta=rawdata[0]+(rawdata[1]/60)

media=numpy.empty(len(theta)/3)
disp=numpy.empty(len(theta)/3)

i=0
while i <len(theta):
    a=(theta[i]+theta[i+1]+theta[i+2])/3
    media[(1/3)*i]=a
    theta[i:i+3].sort() 
    disp[(1/3)*i]=theta[i+2]-theta[i]
    i=i+3
    
y=media
dy=disp
lungh_onda=numpy.array([508.6,643.8,467.8,480.0])
x=1/(lungh_onda)
dlungh=numpy.ones(len(x))*0.1
dx=dlungh/(lungh_onda**2)

pylab.figure(1)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n m=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y-f(x,m_fit,q_fit))**2)/((dy)**2))
dof=len(y)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(2)
pylab.subplot(211)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=dx,linestyle='')
pylab.plot(x,f(x,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel(' x')
pylab.plot(x,(y-f(x,m_fit,q_fit))/dy,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
pylab.show()

    
datafile = 'sodio_giallo.txt'
rawdata = numpy.loadtxt(os.path.join(folder, 'Dati', datafile)).T
angolo=rawdata[0]+rawdata[1]/60
theta=sum(angolo)/(len(angolo))
angolo[0:len(angolo)].sort()
dtheta=(angolo[len(angolo)-1]-angolo[0])/2

L=m_fit/(theta-q_fit)
dL=math.sqrt( (dm_fit/(theta-q_fit))**2 + ((m_fit/((theta-q_fit)**2))**2 )*(dq_fit**2+dtheta**2)+ 2*mq_cov/((theta-q_fit)**2))

print('Lunghezza d onda=%f+-%f'%(L,dL))
