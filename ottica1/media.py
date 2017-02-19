import  os
folder = os.path.realpath('.')
import numpy as np, pylab, matplotlib.pyplot as plt
from lab import *


#### Parte 1

datafile = 'mercurio.txt'
rawdata = np.loadtxt(os.path.join(folder, 'Dati', datafile)).T
theta=rawdata[0]+(rawdata[1]/60)

theta0=168.71944444
dtheta0=0.03333333
media=np.empty(len(theta)/3)
disp=np.empty(len(theta)/3)

i=0
while i <len(theta):
    a=(theta[i]+theta[i+1]+theta[i+2])/3
    media[(1/3)*i]=a
    theta[i:i+3].sort() 
    disp[(1/3)*i]=theta[i+2]-theta[i]
    i=i+3

theta=media-(theta0*numpy.ones(2))
dtheta=disp +(dtheta0*numpy.ones(2))