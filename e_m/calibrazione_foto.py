import pylab as py
import os
import numpy as np
import scipy
import math
from importare_dati import importa
#errore sullo zero y=5  x=4
## x-ay=0   z-by=0
def calibrazione(datafile):
    data=importa(datafile)
    x=data[0]
    y=data[1]
    z_min=-44
    z_max=35
    x0=x[0]
    y0=y[0]
    x=x-x0
    y=y-y0
    y.sort()
    x.sort()
    dy=np.ones(len(data[0]))*3
    dx=np.ones(len(data[0]))*4
    z=np.ones(len(data[0]))
    for i in range(z_min,z_max):
        z[i]=i
    z=z/10
    z.sort()
    
    def f1(x,a):
        return a*x
        
    from scipy.optimize import curve_fit
    popt, pcov=curve_fit(f1,y,x,py.array([400.]),sigma=dx,absolute_sigma=True)
    a_fit=popt
    da_fit=py.sqrt(pcov.diagonal())
    
    popt, pcov=curve_fit(f1,y,x,py.array([400.]),sigma=py.sqrt(dx**2+(a_fit*dy)**2),absolute_sigma=True)
    a_fit=popt
    da_fit=py.sqrt(pcov.diagonal())
    
    popt, pcov=curve_fit(f1,y,z,py.array([400.]),sigma=dy,absolute_sigma=True)
    b_fit=popt
    db_fit=py.sqrt(pcov.diagonal())
    
    # py.figure(10)
    # py.ylabel('x')
    # py.xlabel('y')
    # py.title('calibrazione')
    # py.grid(color='gray')
    # py.plot(y,x, 'o')
    # py.plot(y,f1(y,a_fit), color='black')
    # py.errorbar(y,x,yerr=dx,xerr=dy,linestyle='')
    
    
    # py.figure(20)
    # py.ylabel('z')
    # py.xlabel('y')
    # py.title('calibrazione')
    # py.grid(color='gray')
    # py.plot(y,z, 'o')
    # py.plot(y,f1(y,b_fit), color='black')
    # py.errorbar(y,z,yerr=None,xerr=dy,linestyle='')
    
    tan=b_fit/math.sqrt(1+a_fit**2)
    dtan=math.sqrt((db_fit*tan/b_fit)**2 + (b_fit*a_fit/(math.sqrt(1+a_fit**2)**3))**2)
    
    return  1/tan,dtan/(tan**2)