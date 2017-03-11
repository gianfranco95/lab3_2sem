import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special


datafile = 'Campo_magnetico.txt'
rawdata = numpy.loadtxt(os.path.join(folder, datafile)).T
V = rawdata[0]
dV = rawdata[1]
t = 4
dt = 1
r = rawdata[2]
dr = rawdata[3]
I = rawdata[4]
dI = rawdata[5]
e = 1.6*10**(-19)
n = 4
Bi = (e*n*t*V)/(11.1*I)
dBi = Bi*pylab.sqrt((dt/t)**2+(dV/V)**2+(0.1/11.1)**2+(dI/I)**2)
B = Bi/(7.80*I*(10**(-4)))
dB = B*pylab.sqrt((dBi/Bi)**2+(dI/I)**2)
#Grafico

pylab.figure(1)
pylab.xlabel('r [cm]', size = 22)
pylab.ylabel('Bz/Bzmax', size = 22)
pylab.title('Andamento del campo magnetico', size = 20)
pylab.grid(color='gray')
pylab.errorbar(r,B,dB,dr,linestyle='', color = 'black')
pylab.tight_layout
pylab.minorticks_on
pylab.show()

#PARTE 2

Icoil = 5
dIcoil = 1
Vacc = 4
dVacc = 3

datafile = 'Cerchio.txt'
rawdata = numpy.loadtxt(os.path.join(folder, datafile)).T
x = rawdata[0]
dx = rawdata[1]
y = rawdata[2]
dy = rawdata[3]
a = b = numpy.empty(len(x))
i = 0
for i in range(0,len(x)-1):
    a[i] = (y[i+1]-y[i])/(x[i+1]-x[i])
    b[i] = (y[i+1]+y[i])/2+(1/(2*a[i]))*(x[i+1]+x[i])
xc = yc = numpy.empty(len(a))
i = 0
for i in range(0,len(a)-1):
    xc[i] = a[i]*a[i+1]*(b[i+1]-b[i])/(a[i]-a[i+1])
    yc[i] = (-xc[i]/a[i])+b[i]
i = 0
d = numpy.empty(len(xc))
for i in range(0,math.floor((1/3)*len(xc))):
    print ('Coordinate dei centri')
    print (xc[3*i], yc[3*i])
    d[3*i] = pylab.sqrt((x[3*i]-xc[3*i])**2+(y[3*i]-yc[3*i])**2)
    d[3*i+1] = pylab.sqrt((x[3*i+1]-xc[3*i])**2+(y[3*i+1]-yc[3*i])**2)
    d[3*i+2] = pylab.sqrt((x[3*i+2]-xc[3*i])**2+(y[3*i+2]-yc[3*i])**2)
media=numpy.empty(len(d)/3)
disp=numpy.empty(len(d)/3)
i=0
while i <len(d):
    a=(d[i]+d[i+1]+d[i+2])/3
    media[(1/3)*i]=a
    d[i:i+3].sort()
    disp[(1/3)*i]=d[i+2]-d[i] 
    d=d+3
    
R=media
dR = disp

V = 6.0
dV = 0.1
datafile = 'EM.txt'
rawdata = numpy.loadtxt(os.path.join(folder, datafile)).T
Vacc = rawdata[0]
dVacc = rawdata[1]
Icoil = rawdata[2]
dIcoil = rawdata[3]
Bz = (e*n*t*Vacc)/(11.1*Icoil)
dBz = Bz*pylab.sqrt((dt/t)**2+(dVacc/Vacc)**2+(0.1/11.1)**2+(dIcoil/Icoil)**2)
k = (Bz*R)**2
dk = 2*k*pylab.sqrt((dBz/Bz)**2+(dR/R)**2)

pylab.figure(2)
pylab.xlabel('Vacc [V]', size = 22)
pylab.ylabel('(Bz*R)^2', size = 22)
pylab.title('Elettroni accelerati', size = 20)
pylab.grid(color='gray')
pylab.errorbar(R,k,dk,dr,linestyle='', color = 'black')
pylab.tight_layout
pylab.minorticks_on
pylab.show()