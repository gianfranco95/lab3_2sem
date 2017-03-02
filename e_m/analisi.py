import pylab as py
import os
import numpy as np
folder = os.path.realpath('.')

datafile=(['cerchio.txt','cerchio_1.txt'])      #file di prova 

i=0
while i< len(datafile):
    if i ==0:
        data = py.loadtxt(os.path.join(folder,'Dati',datafile[i])).T
        i=i+1
        
    else:
        data=py.append(data,py.loadtxt(os.path.join(folder,'Dati',datafile[i])).T)
        i=i+1     
