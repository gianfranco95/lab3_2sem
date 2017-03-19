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
#dati da escludere
escludere=pylab.array([5,36,11,40,37,29,28,27,26,12])

foto=pylab.loadtxt(os.path.join(folder,'Dati',data)).T

esclusione=pylab.zeros(len(foto[0]))
r=0
while(r<len(escludere)):
    esclusione[int(escludere[r])]=1
    r=r+1

arr_em=pylab.zeros(len(foto[0])-len(escludere))
arr_dem=pylab.zeros(len(foto[0])-len(escludere))
p=0
for t in range(0,len(foto[0])):
    if(esclusione[t]!=1):
        Val,dVal=e_m('calibrazione26_luca.txt',t)
        arr_em[p]=Val
        arr_dem[p]=dVal
        pylab.figure(99)
        pylab.plot(t,Val,'o',linestyle='')
        pylab.errorbar(t,Val,dVal,linestyle='')
        pylab.show()
        print('e_m=%f +- %f'%(Val,dVal))
        p=p+1
    
em=sum(arr_em/(arr_dem**2))/sum(1/arr_dem**2)
dem=1/math.sqrt(sum(1/(arr_dem**2)))
print(arr_em)
print(arr_dem)
print('e_m=%f+-%f'%(em,dem))
bins=numpy.linspace(min(arr_em),max(arr_em),20)
pylab.figure(100)
pylab.hist(arr_em,bins)
pylab.show()
