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
#calibrazione q 
lamb=625
dlamb=8
m = numpy.array([50,51,56,85,60])
dm= numpy.array([0,1,1,1,1])
n=numpy.array([9,9,10,15,11]) #numero tacchette lette sul micrometro
dn=numpy.array([1,0,0,0,0])
q= (m*lamb)/(2*n)  #[nanometri]
dq=q*numpy.sqrt(((dm/m)**2 + (dn/n)**2)+(dlamb/lamb)**2)
q01=(q/(dq**2)).sum()
q02=(1/(dq**2)).sum()
q0=q01/q02
dq0=numpy.sqrt(1/q02)
# qqq=(1/5)*q.sum()
# dqqq=(1/5)*dq.sum()
print('calibrazione =%f+-%f'%(q0,dq0))


#Misura lunghezza d'onda mercurio 546 nm
#M numero massimi e minimi contati
#N numero tacchette
M=numpy.array([71,60,75,97,79])
dM =numpy.array([3,3,3,1,1])
N=numpy.array([12,10,12,15,13])
dN=numpy.array([1,1,1,0,0])
l=(2*q*N)/M
dl=l*pylab.sqrt(  (dN/N)**2+(dq0/q0)**2+(dM/M)**2 )
l01 = (l/(dl**2)).sum()
l02 = (1/(dl**2)).sum()
l0 = l01/l02
dl0= numpy.sqrt(1/l02)
# lamdaa=(1/5)*((2*qqq*N)/M).sum()
# dlamdaa=(1/5)*(lamdaa*pylab.sqrt(  (dN/N)**2+(dqqq/qqq)**2+(dM/M)**2 )).sum()
print('lunghezza d onda==%f+-%f'%(l0,dl0))

##tabella in latex
# i=0
# while i<len(m):
#     print('%2.f & %1.f & %2.f & %2.f\\\ '%(M[i],dM[i],10*N[i],10*dN[i]))
#     i=i+1

