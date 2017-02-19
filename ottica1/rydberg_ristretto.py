n21=pylab.array([5,5,4,4,3])
n11=pylab.array([2,2,2,2,2])

x= 1/(n1**2) - 1/(n2**2)
x1=1/(n11**2) - 1/(n21**2)
lamb1=pylab.zeros(5)
dlamb1=pylab.zeros(5)
lamb1[0]=(lamb[5]+lamb[0])/2
lamb1[1]=lamb[1]
lamb1[2]=(lamb[2]+lamb[6])/2
lamb1[3]=lamb[3]
lamb1[4]=lamb[4]
dlamb1[0]=(dlamb[5]+dlamb[0])/2
dlamb1[1]=dlamb[1]
dlamb1[2]=(dlamb[2]+dlamb[6])/2
dlamb1[3]=dlamb[3]
dlamb1[4]=dlamb[4]

y1=1/lamb1
dy1=dlamb1/(lamb1**2)

pylab.figure(10)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x1,y1,pylab.array([400.,0.]),sigma=dy1,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n costante_rydberg=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y1-f(x1,m_fit,q_fit))**2)/((dy1)**2))
dof=len(y1)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(20)
pylab.subplot(211)
# pylab.xlim(0.87,0.97)
pylab.ylabel('1/$\lambda$ $[nm^{-1}]$', size = 15)
pylab.title('misura costante di Rydberg')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')
pylab.plot(x1,f(x1,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel('$1/n_1^{2}-1/n_2^{2}$', size = 15)
pylab.plot(x1,(y1-f(x1,m_fit,q_fit))/dy1,'o',linestyle='',markersize = 5)
# pylab.xlim(0.87,0.97)
pylab.legend(loc = 4)
pylab.show()

##Tolgo il verde
n21=pylab.array([5,5,4,3])
n11=pylab.array([2,2,2,2])

x= 1/(n1**2) - 1/(n2**2)
x1=1/(n11**2) - 1/(n21**2)
lamb1=pylab.zeros(4)
dlamb1=pylab.zeros(4)
lamb1[0]=(lamb[5]+lamb[0])/2
lamb1[1]=lamb[1]
lamb1[2]=(lamb[2]+lamb[6])/2
lamb1[3]=lamb[4]

dlamb1[0]=(dlamb[5]+dlamb[0])/2
dlamb1[1]=dlamb[1]
dlamb1[2]=(dlamb[2]+dlamb[6])/2
dlamb1[3]=dlamb[4]


y1=1/lamb1
dy1=dlamb1/(lamb1**2)

pylab.figure(30)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x1,y1,pylab.array([400.,0.]),sigma=dy1,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n costante_rydberg=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y1-f(x1,m_fit,q_fit))**2)/((dy1)**2))
dof=len(y1)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(40)
pylab.subplot(211)
# pylab.xlim(0.87,0.97)
pylab.ylabel('1/$\lambda$ $[nm^{-1}]$', size = 15)
pylab.title('misura costante di Rydberg')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')
pylab.plot(x1,f(x1,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel('$1/n_1^{2}-1/n_2^{2}$', size = 15)
pylab.plot(x1,(y1-f(x1,m_fit,q_fit))/dy1,'o',linestyle='',markersize = 5)
# pylab.xlim(0.87,0.97)
pylab.legend(loc = 4)
pylab.show()

##Tolgo lo sdoppiamento del viola 

n21=pylab.array([5,4,3])
n11=pylab.array([2,2,2])

x= 1/(n1**2) - 1/(n2**2)
x1=1/(n11**2) - 1/(n21**2)
lamb1=pylab.zeros(3)
dlamb1=pylab.zeros(3)
lamb1[0]=((lamb[5]+lamb[0])/2 + lamb[1])/2
lamb1[1]=(lamb[2]+lamb[6])/2
lamb1[2]=lamb[4]

dlamb1[0]=((dlamb[5]+dlamb[0])/2 + dlamb[1])/2
dlamb1[1]=(dlamb[2]+dlamb[6])/2
dlamb1[2]=dlamb[4]


y1=1/lamb1
dy1=dlamb1/(lamb1**2)

pylab.figure(50)
pylab.xlabel(' x')
pylab.ylabel('y')
pylab.title('Data')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')

def f(x,m,q):
    return m*x+q
    
from scipy.optimize import curve_fit
popt, pcov=curve_fit(f,x1,y1,pylab.array([400.,0.]),sigma=dy1,absolute_sigma=True)
m_fit,q_fit=popt
dm_fit,dq_fit=pylab.sqrt(pcov.diagonal())
mq_cov=pcov[0,1]
mq_norm_cov=mq_cov/(dm_fit*dq_fit)
print('Fit numerico (errore y)\n costante_rydberg=%f+-%f \n q=%f+-%f  covarianza(normalizzata)=%f(%f)'%(m_fit,dm_fit,q_fit,dq_fit,mq_cov,mq_norm_cov))
#Chi quadro
chisquare=sum(((y1-f(x1,m_fit,q_fit))**2)/((dy1)**2))
dof=len(y1)-2
pchi = scipy.special.chdtrc(dof,chisquare)
print('Chi quadro/ndof = %f/%f\nprobabilità associata = %f'%(chisquare,dof,pchi))
#Grafico
pylab.figure(60)
pylab.subplot(211)
# pylab.xlim(0.87,0.97)
pylab.ylabel('1/$\lambda$ $[nm^{-1}]$', size = 15)
pylab.title('misura costante di Rydberg')
pylab.grid(color='gray')
pylab.plot(x1,y1, 'o')
pylab.errorbar(x1,y1,yerr=dy1,linestyle='')
pylab.plot(x1,f(x1,m_fit,q_fit), color='black',label = "retta di fit")
pylab.subplot(212)
pylab.title('Residui')
pylab.xlabel('$1/n_1^{2}-1/n_2^{2}$', size = 15)
pylab.plot(x1,(y1-f(x1,m_fit,q_fit))/dy1,'o',linestyle='',markersize = 5)
# pylab.xlim(0.87,0.97)
pylab.legend(loc = 4)
pylab.show()