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
lamb=
Dx=m*lamb/2
q=Dx/n
dq=dn*Dx/(n**2)


print('calibrazione =%f+-%f'%(q,dq))

#Misura lunghezza d'onda mercurio 546 nm
#M numero massimi e minimi contati
#N numero tacchette
M=
N=
dN=
l=2*N*q/M
dl=pylab.sqrt(  (dN*l/N)**2 + (dq*l/q)**2 )

print('lunfhezza d onda= %f +- %f'%(l,dl))


