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
rawdata = numpy.loadtxt(os.path.join(folder, datafile)).T
h = rawdata[0]
dh = rawdata[1]
x = rawdata[2]

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
m0,q0=popt
dm0,dq0=pylab.sqrt(pcov.diagonal())
cov = pcov[0,1]/(dm0*dq0)
print ('Pendenza fit = ',m0,dm0)
print ('Intercetta fit = ',q0,dq0)
print ('Covarianza = ',cov)
chisq = (((y-f(x,m0,q0))/dy)**2).sum()
ndof = len(y)-2
print ('Chi quadro/ dof = ',chisq, ndof)

d = 0.1 #passo reticolare
dd = 0.01
lambda_fit = -m0*d
dlambda_fit = lambda_fit*pylab.sqrt((dm0/m0)**2+(dd/d)**2)
print ('Lunghezza onda dal fit [nm] = ',lambda_fit*10**(7),dlambda_fit*10**(7))