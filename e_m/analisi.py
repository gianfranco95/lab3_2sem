import pylab as py
import os
import numpy as np
folder = os.path.realpath('.')

datafile=(['cerchio.txt','cerchio_1.txt'])    #file di prova

 
data=py.loadtxt(os.path.join(folder,'Dati',datafile[0])).T  #utile solo per trovare numero di colonne in ogni file

data= np.ndarray(shape=(len(data)*len(datafile),len(data[0])), dtype=float, order='F')

i=0
while i< len(datafile):
    if i ==0:
        data[0],data[1]= py.loadtxt(os.path.join(folder,'Dati',datafile[i])).T
        i=i+1
        
    else:
        data[i+1],data[i+2]= py.loadtxt(os.path.join(folder,'Dati',datafile[i])).T
        i=i+1     

#usare data nell'analisi successiva: contiene tutte le colonne di tutti i file importati.


##analisi