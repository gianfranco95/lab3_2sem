import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab
import scipy
import scipy.special
##Calibrazione sonda
Vout=15 #In volt
dVout=1
#Fattore di amplificazione
A=11.090
dA=0.003
#Fattore di calibrazione della sonda
Q=0.005 #Volt/Gauss
dQ=0.0001

Vh=Vout/A
dVh=pylab.sqrt((dVout/A)**2 + (Vout*dA/(A**2))**2)

B=Vh/Q #Gauss
dB=pylab.sqrt((dVh/Q)**2 + (Vh*dQ/(Q**2))**2)

print('Campo in Gauss = %f +- %f' % (B,dB))

##Altre cose che si possono fare: 
# mappare Bz e fare fit a Bz/Bzmax per ottenere il raggio delle bobine che serve a corregger il campo magnetico per quando si farà il fit circolare per trovare e_m