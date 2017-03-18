import pylab as py
import os
import numpy as np
import scipy
from importare_dati import importa

def calibrazione(datafile):
    data=importa(datafile)
    y=data[0]
    y.sort()
    dy=np.ones(len(data[0]))
    x=np.ones(len(data[0]))
    for i in range(-50,41):
        x[i]=i
    x=x/10
    x.sort()
    
    def f(x,a,b):
        return a*x+b
        
    from scipy.optimize import curve_fit
    popt, pcov=curve_fit(f,x,y,py.array([400.,0.]),sigma=dy,absolute_sigma=True)
    a_fit,b_fit=popt
    da_fit,db_fit=py.sqrt(pcov.diagonal())
    ab_cov=pcov[0,1]
    ab_norm_cov=ab_cov/(da_fit*db_fit)
    # print('Fit numerico (errore y)\n a=%f+-%f \n b=%f+-%f  covarianza(normalizzata)=%f(%f)'%(a_fit,da_fit,b_fit,db_fit,ab_cov,ab_norm_cov))
    #Chi quadro
    chisquare=sum(((y-f(x,a_fit,b_fit))**2)/((dy)**2))
    dof=len(y)-2
    pchi = scipy.special.chdtrc(dof,chisquare)
    # print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
    
    py.figure(1)
    py.ylabel('punti[u.a.]')
    py.xlabel('tacche scala[cm]')
    py.title('calibrazione')
    py.grid(color='gray')
    py.plot(x,y, 'o')
    py.plot(x,f(x,a_fit,b_fit), color='black')
    py.errorbar(x,y,yerr=dy,xerr=None,linestyle='')
    py.show()
    a_fit0 = a_fit*(54.9/64.9)
    da_fit0 = a_fit0*py.sqrt((da_fit/a_fit)**2+(0.1/54.9)**2+(0.1/64.9)**2)
    return  157,da_fit0,b_fit,db_fit,ab_cov