import  os
folder = os.path.realpath('.')
from lab import *
import numpy
import math
import pylab
import scipy
import scipy.special

datafile = 'mercurio.txt'
rawdata = numpy.loadtxt(os.path.join(folder, 'Dati', datafile)).T
theta=rawdata[0]+(rawdata[1]/60)

theta0=168.71944444
dtheta0=0.03333333
media=numpy.empty(len(theta)/3)
disp=numpy.empty(len(theta)/3)

i=0
while i <len(theta):
    a=(theta[i]+theta[i+1]+theta[i+2])/3
    media[(1/3)*i]=a
    theta[i:i+3].sort() 
    disp[(1/3)*i]=theta[i+2]-theta[i]
    i=i+3

theta=media-(theta0*numpy.ones(2))
dtheta=numpy.sqrt(disp**2 +(dtheta0*numpy.ones(2))**2)
#Determinazione del passo reticolare
#misure
a0=theta[0]
da0=dtheta[0]
a1=theta[1]
da1=dtheta[1]
l=546.074 #nm
dl=0.001 #nm
a0=a0*math.pi/180
da0=da0*math.pi/180
a1=a1*math.pi/180
da1=a1*math.pi/180
ti=(math.pi-a0)/2
dti=da0/2
td=math.pi-ti-a1
dtd=pylab.sqrt(dti**2 + da1**2)

d=l/(pylab.sin(ti)-pylab.sin(td))
dd=pylab.sqrt( ((d/l)*dl)**2 + (d*d*pylab.cos(ti)*dti/l)**2 + (d*d*pylab.cos(td)*dtd/l)**2 )
print('Passo reticolare d=%f+-%f'%(d,dd))

#Costante di Rydberg (-1 sta per infinito)
datafile = 'idrogeno.txt'
gradi,primi,n_2,ord=pylab.loadtxt(os.path.join(folder, 'Dati', datafile)).T

alfa=gradi +(primi)/60
media=numpy.empty(len(alfa)/3)
disp=numpy.empty(len(alfa)/3)
ordine=numpy.empty(len(alfa)/3)
n2=numpy.empty(len(alfa)/3)
n1=numpy.ones(len(alfa)/3)
i=0
while i <len(alfa):
    a=(alfa[i]+alfa[i+1]+alfa[i+2])/3
    media[(1/3)*i]=a
    ordine[(1/3)*i]=ord[i]
    n2[(1/3)*i]=n_2[i]
    alfa[i:i+3].sort() 
    disp[(1/3)*i]=alfa[i+2]-alfa[i]
    i=i+3

alfa=media-(theta0*numpy.ones(len(media)))
dalfa=numpy.sqrt(disp**2 +(dtheta0*numpy.ones(len(media)))**2)
# p=pylab.zeros(len(ordine))
# for i in range(0,len(ordine)):
#     if(n2[i]==-1): p[i]=1
#     else: p[i]=0


alfa=alfa*pylab.pi/180
dalfa=dalfa*math.pi/180
teta=pylab.pi-ti-alfa
dteta=pylab.sqrt(dti**2 + dalfa**2)

lamb=(d*(pylab.sin(ti)-pylab.sin(teta)))/ordine
dlamb=pylab.sqrt( (dd*lamb/d)**2 + (d*pylab.cos(ti)*dti)**2 + (d*pylab.cos(teta)*dteta)**2 )/ordine

x= 1/(n1**2) - 1/(n2**2)
y=1/lamb
dy=dlamb/(lamb**2)

pylab.figure(1)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n costante_rydberg=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y-f(x,m_fit,q_fit))**2)/((dy)**2))
dof=len(y)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(2)
pylab.subplot(211)
pylab.xlim(0.87,0.97)
pylab.ylabel('1/$\lambda$ $[nm^{-1}]$')
pylab.title('misura costante di Rydberg')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,linestyle='')
pylab.plot(x,f(x,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel('$\frac{1}{n1^2}-\frac{1}{n2^2}$')
pylab.plot(x,(y-f(x,m_fit,q_fit))/dy,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
pylab.show()
