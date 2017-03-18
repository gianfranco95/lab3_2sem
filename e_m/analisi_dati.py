#Analisi
import  os
folder = os.path.realpath('.')
import numpy
import math
import pylab 
import scipy
import scipy.special
import numpy.linalg
from importare_dati import importa
from calibrazione_foto import calibrazione
from fit_luca import e_m
data='fotobis.txt'
i=42
foto=pylab.loadtxt(os.path.join(folder,'Dati',data)).T
tot=0
TOT=0
arr_em=pylab.zeros(len(foto[0]))
arr_dem=pylab.zeros(len(foto[0]))
for t in range(0,len(foto[0])):
    Val,dVal=e_m('calibrazione26_luca.txt',t)
    arr_em[t]=Val
    arr_dem[t]=dVal
    tot=tot+Val/(dVal**2)
    TOT=TOT+(1/dVal**2)
    pylab.figure(99)
    pylab.plot(t,Val,'o',linestyle='')
    pylab.errorbar(t,Val,dVal,linestyle='')
    pylab.show()
    print('e_m=%f +- %f'%(Val,dVal))
em=tot/TOT
print(arr_em)
print(arr_dem)
print('e_m=%f'%(em))
