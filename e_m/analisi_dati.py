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
i=19
Val,dVal=e_m('calibrazione26_luca.txt',i)

print('e_m=%f +- %f'%(Val,dVal))