import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special
from importare_dati import importa
#singola bobina
# N numero spire
# r0 raggio bobina
#punto da analizzare in posizione (y0,z0)
datafile=['datiB6.txt']
V,r=importa(datafile)
pylab.figure(3)
pylab.plot(r,V,'o')
pylab.show()

def rx(phi,r0):
    return -r0*pylab.cos(phi)
    
def ry(phi,y0,r0):
    return y0-r0*pylab.sin(phi)

def rz(z0):
    return z0

def dlx(phi,r0):
    return -r0*pylab.sin(phi)
    
def dly(phi,r0):
    return r0*pylab.cos(phi)

def dSz(A,phi,r0,y0,z0):
    return A*(rx(phi,r0)*dly(phi,r0) - ry(phi,y0,r0)*dlx(phi,r0) )/((rx(phi,r0)**2 + ry(phi,y0,r0)**2 + rz(z0)**2)**(3/2))


def dSy(A,phi,r0,y0,z0):
    return A*(rz(z0)*dlx(phi,r0))/((rx(phi,r0)**2 + ry(phi,y0,r0)**2 + rz(z0)**2)**(3/2))
#Formula di Biot-Savart
#costante A= mu0*N*I/(4*pi)
#n numero di iterazioni
#s segno corrente (+1 antiorario)
n=1000
def Bz(A,r0,y0,z0,s):
    S=0
    for i in range(0,n):
        phi = 2*math.pi*i/n
        S=S+dSz(A,phi,r0,y0,z0)*2*math.pi/n
    return S*(-s)

def By(A,r0,y0,z0,s):
    S=0
    for i in range(0,n):
        phi = 2*math.pi*i/n
        S=S+dSy(A,phi,r0,y0,z0)*2*math.pi/n
    return S*(-s)
#due bobine uguali con stessa corrente poste a distanza d tra loro; asse di simmetria è asse z; una si trova a +d/2 e l'altra a -d/2

def Bz_tot(A,r0,y0,z0,s,d):
    return Bz(A,r0,y0,z0+d/2,s) + Bz(A,r0,y0,z0-d/2,s)
def By_tot(A,r0,y0,z0,s,d):
    return By(A,r0,y0,z0+d/2,s) + By(A,r0,y0,z0-d/2,s)
#I nostri casi
A0=10**(-7)*130
r00=0.15
s0=1
d0=r00
z=pylab.linspace(-r00/2,r00/2,100)
pylab.figure(1)
pylab.title('Bz')
pylab.xlabel('z')
pylab.plot(z, Bz_tot(A0,r00,0,z,s0,d0)/Bz_tot(A0,r00,0,0,s0,d0))
pylab.show()

y=pylab.linspace(-r00,r00,100)
pylab.figure(2)
pylab.subplot(211)
pylab.title('Bz')
pylab.xlabel('y')
pylab.plot(y, Bz_tot(A0,r00,y,0,s0,d0)/Bz_tot(A0,r00,0,0,s0,d0))
pylab.subplot(212)
pylab.title('By')
pylab.xlabel('y')
pylab.plot(y, 10**(100)*By_tot(A0,r00,y,-r00/2,s0,d0)/Bz_tot(A0,r00,0,0,s0,d0))
pylab.show()


        