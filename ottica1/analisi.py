import  os
folder = os.path.realpath('.')
import numpy as np, pylab, matplotlib.pyplot as plt
from lab import *


#### Parte 1

datafile = 'dati_1.txt'
rawdata = np.loadtxt(os.path.join(folder, 'Dati', datafile)).T

media=np.empty(len(rawdata)/3)
disp=np.empty(len(rawdata)/3)

i=0
while i <len(rawdata):
    a=(rawdata[i]+rawdata[i+1]+rawdata[i+2])/3
    media[(1/3)*i]=a
    rawdata[i:i+3].sort() 
    disp[(1/3)*i]=rawdata[i+2]-rawdata[i]
    i=i+3
