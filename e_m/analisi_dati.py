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

V_out=pylab.zeros(len(foto[0])-len(escludere))
W=pylab.zeros(len(foto[0])-len(escludere))
s=0
i=0
while(s<len(foto[0])):
    if(numpy.all(s!= escludere)):
        V_out[i]=foto[1][s]
        W[i]=V_out[i]
        i=i+1
    s=s+1
    
W.sort()

ordine=pylab.zeros(len(foto[0])-len(escludere))
i=0
while(i<len(W)):
    j=int(0)
    while(j<len(W)):
        if(W[i]==V_out[j]):
            ordine[i]= int(j)
        j=j+1
    i=i+1
##
p=0
for t in range(0,len(foto[0])):
    if(esclusione[t]!=1):
        Val,dVal=e_m('calibrazione26_luca.txt',int(ordine[p]))
        arr_em[p]=Val
        arr_dem[p]=dVal
        pylab.figure(99)
        pylab.plot(W[p],Val,'o',linestyle='')
        pylab.errorbar(W[p],Val,dVal,linestyle='')
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
