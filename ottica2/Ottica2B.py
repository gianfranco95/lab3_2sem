import  os
folder = os.path.realpath('.')
# from lab import *
import numpy
import math
import pylab
import scipy
import scipy.special

#calibrazione
#m numero massimi e minimi contati con il laser
#n numero tacchette
#lambda lunghezza d'onda del laser
#calibrazione q (circa 10 um)
lamb=632.8
m = numpy.array([50,51,56,85,60])
Dx=numpy.array([90,90,100,150,110])
q=(2*Dx*(10**3))/(m*lamb)
dq=q*pylab.sqrt((10/Dx)**2+(1/m)**2)
q01 = (q/(dq**2)).sum()
q02 = (1/(dq**2)).sum()
q0 = q01/q02
dq0 = pylab.sqrt(1/q02)

print('calibrazione =%f+-%f'%(q0,dq0))

#Misura lunghezza d'onda mercurio 546 nm
#M numero massimi e minimi contati
#N numero tacchette
M=numpy.array([71,60,75,97,79])
dM =1
N=numpy.array([120000,100000,120000,150000,130000])
dN=10000
l=(2*N)/(q0*M)
dl=l*pylab.sqrt(  (dN/N)**2+(dq0/q0)**2+(dM/M)**2 )
l01 = (l/(dl**2)).sum()
l02 = (1/(dl**2)).sum()
l0 = l01/l02
dl0 = pylab.sqrt(1/l02)

print('lunghezza d onda= ',l0,dl0)


