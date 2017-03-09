import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special


D = 45 #distanza tra schermo e laser su reticolo
dD = 20

datafile = 'lunghezza_onda.txt'
rawdata = numpy.loadtxt(os.path.join(folder,'Dati', datafile)).T
h = numpy.empty(len(rawdata[0])/3)
dh =numpy.empty(len(rawdata[0])/3)
x = numpy.empty(len(rawdata[0])/3)
disp= numpy.empty(len(rawdata[0])/3) #dispersione tra i 3 valori misurati da confrontare con dh

#media sulle tre misure fatte
i=0
while i <len(rawdata[0]):
    a=(rawdata[0][i]+rawdata[0][i+1]+rawdata[0][i+2])/3
    h[(1/3)*i]=a
    rawdata[0][i:i+3].sort() 
    disp[(1/3)*i]=rawdata[0][i+2]-rawdata[0][i]
    dh[(1/3)*i]=(rawdata[1][i]+rawdata[1][i+1]+rawdata[1][i+2])/3
    x[(1/3)*i]=rawdata[2][i]
    i=i+3

yr = 4 #posizione del raggio sullo schermo in assenza di reticolo
dyr = 1
y0 = (yr+h[0])/2
dy0 = 0.5*pylab.sqrt(dyr**2+dh[0]**2)
print ('Quota del calibro = ', y0, dy0)

h = h-y0
y = D/pylab.sqrt(D**2+h**2)
dy = pylab.sqrt(((((D**2+h**2)-D)/((D**2+h**2)**(3/2)))*dD)**2+((h*dh)/((D**2+h**2)**(3/2)))**2)

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x,y,pylab.array([400.,0.]),sigma=dy,absolute_sigma=True)
m0=popt[0]
q0=popt[1]
dm0,dq0=pylab.sqrt(pcov.diagonal())
cov = pcov[0,1]/(dm0*dq0)
print ('Pendenza fit = ',m0,dm0)
print ('Intercetta fit = ',q0,dq0)
print ('Covarianza = ',cov)
chisq = (((y-f(x,m0,q0))/dy)**2).sum()
ndof = len(y)-2
print ('Chi quadro/ dof = ',chisq, ndof)

#Grafico
pylab.figure(2)
pylab.subplot(211)
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x,y, 'o')
pylab.errorbar(x,y,yerr=dy,xerr=None,linestyle='')
pylab.plot(x,f(x,m0,q0), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel(' m')
pylab.plot(x,(y-f(x,m0,q0))/dy,'o',linestyle='',markersize = 5)
pylab.legend(loc = 4)
pylab.show()

d = 0.1 #passo reticolare
dd = 0.01
lambda_fit = -m0*d
dlambda_fit = lambda_fit*pylab.sqrt((dm0/m0)**2+(dd/d)**2)
print ('Lunghezza onda dal fit [nm] = ',lambda_fit*10**(7),dlambda_fit*10**(7))