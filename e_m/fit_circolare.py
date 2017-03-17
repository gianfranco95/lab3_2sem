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


dati = (['calibrazione31.txt'])
calib = calibrazione(dati)

data='foto.txt'
foto=pylab.loadtxt(os.path.join(folder,'Dati',data)).T

Vacc=foto[1][14]
Icoil=foto[2][14]

datafile=(['cerchio14.txt'])
x0,y0=importa(datafile)
x= (x0- calib[2])/calib[0]      #così x,y e sigma sono in centimetri
y=(y0-calib[2])/calib[0]
x=x*(54.9/64.9)             #correzione proiettiva
y=y*(54.9/64.9)
pylab.figure(2)
pylab.plot(x0,y0,'.')
pylab.plot(x,y,'o')
pylab.show()
sigma= numpy.sqrt( (calib[3]/calib[0])**2 +( y*calib[1]/calib[0] )**2 )
sigma=sum(sigma)/len(y)

def fit(x,y,sigma):
    D=numpy.diag((0,0,0))
    D_inv=numpy.diag((0,0,0))
    E=numpy.zeros(3)
    Q=numpy.zeros(3)
    
    D[0][0]=2*(sum(x))
    D[0][1]=2*(sum(y))
    D[0][2]=len(x)
    D[1][0]=2*(sum((x**2)))
    D[1][1]=2*(sum(x*y))
    D[1][2]=D[0][0]/2
    D[2][0]=D[1][1]
    D[2][1]=2*sum((y**2))
    D[2][2]=D[0][1]/2
    
    E[0]=sum((x**2)+(y**2))
    E[1]=sum((x**3) + x*(y**2))
    E[2]=sum((x**2)*y + y**3)
    
    D_inv= numpy.linalg.inv(D)
    
    def molti(A,b): #prodotto matrice vettore
        for i in range(0,3):
            s=0
            for j in range(0,3):
                s= s+ A[i][j]*b[j]
            x[i]=s
        return x
    
    Q=molti(D_inv,E)
    R=pylab.sqrt(Q[2]+ Q[0]**2 + Q[1]**2)
    # print(R)
    
    #calcolo errori sui parametri
    
    R_x=numpy.zeros(len(x))
    R_y=numpy.zeros(len(x))
    Q_x=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    Q_y=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    E_x=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    E_y=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    D_x=numpy.ndarray(shape=(3,3,len(x)), dtype=float, order='F')
    D_y=numpy.ndarray(shape=(3,3,len(x)), dtype=float, order='F')
    
    
    for i in range(0,len(x)-1):
        E_x[0][i]=2*x[i]
        E_x[1][i]=3*x[i]**2 + y[i]**2
        E_x[2][i]=2*x[i]*y[i]
        E_y[0][i]=2*y[i]
        E_y[1][i]=2*x[i]*y[i]
        E_y[2]=x[i]**2 + 3*y[i]**2
        D_x[0][0][i]=2
        D_x[0][1][i]=0
        D_x[0][2][i]=0
        D_x[1][0][i]=4*x[i]
        D_x[1][1][i]=2*y[i]
        D_x[1][2][i]=1
        D_x[2][0][i]=2*y[i]
        D_x[2][1][i]=0
        D_x[2][2][i]=0
        D_y[0][0][i]=0
        D_y[0][1][i]=2
        D_y[0][2][i]=0
        D_y[1][0][i]=0
        D_y[1][1][i]=2*x[i]
        D_y[1][2][i]=0
        D_y[2][0][i]=2*x[i]
        D_y[2][1][i]=4*y[i]
        D_y[2][2][i]=1
    
    
    W=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    V=numpy.ndarray(shape=(3,len(x)), dtype=float, order='F')
    
    for j in range(0,len(x)-1):
        for i in range(0,3):
            s=0
            t=0
            for k in range(0,3):
                s=s+ D_x[i][k][j]*Q[k]
                t=t+ D_y[i][k][j]*Q[k]
            W[i][j]=s
            V[i][j]=t
    
    for j in range(0,len(x)-1):
        for i in range(0,3):
            s=0
            t=0
            for k in range(0,3):
                s=s + D_inv[i][k]*(E_x[k][j] - W[k][j])
                t=t+ D_inv[i][k]*(E_y[k][j] - V[k][j])
            Q_x[i][j]=s
            Q_y[i][j]=t
    
    for i in range(0,len(x)-1):
        R_x[i]=(1/R)*(2*Q[0]*Q_x[0][i] + 2*Q[1]*Q_x[1][i] + Q_x[2][i])
        R_y[i]=(1/R)*(2*Q[0]*Q_y[0][i] + 2*Q[1]*Q_y[1][i] + Q_y[2][i])
    
    s=0
    t=0
    r=0
    for i in range(0,len(x)-1):
        s= s + Q_x[0][i]**2 + Q_y[0][i]**2 
        t= t + Q_x[1][i]**2 + Q_y[1][i]**2 
        r= r + Q_x[0][i]*Q_x[1][i] +Q_y[0][i]*Q_y[1][i]
    dA=sigma*numpy.sqrt(s)
    dB=sigma*numpy.sqrt(t)
    covAB=sigma*numpy.sqrt(numpy.abs(r))
    dR=sigma*numpy.sqrt( sum(R_y**2 + R_x**2) )
    # print(dR)
        
        ##stima di sigma dai parametri di fit
    # sigma_fit= numpy.sqrt( (sum( ( (x-Q[0])**2 + (y-Q[1])**2 -R**2)**2 ))/(4*R**2*len(x)) )   
    # 
    # dA=sigma_fit*numpy.sqrt(s)
    # dB=sigma_fit*numpy.sqrt(t)
    # covAB=sigma_fit*numpy.sqrt(r)
    # dR=sigma_fit*numpy.sqrt( sum(R_y**2 + R_x**2) )
    
    
    print('R=%f+-%f'%(R,dR))
    print('A=%f+-%f'%(Q[0],dA))
    print('B=%f+-%f'%(Q[1],dB))
    print('cov_normAB=%f'%(covAB/(dA*dB)))
    
    return Q[0],dA,Q[1],dB,covAB/(dA*dB),R,dR
    
    
pop=fit(x,y,sigma)
aa=pylab.linspace(-10,10,1000)
bb=pylab.linspace(-10,10,1000)
pylab.plot(aa, pop[2] + pylab.sqrt(-(aa-pop[0])**2+pop[5]**2))
pylab.plot(aa, pop[2] -pylab.sqrt(-(aa-pop[0])**2+pop[5]**2))
pylab.show()

##calcolo e/m [valore atteso : 1.7588*10^(11) C/Kg]
e_m = 2*Vacc/(10**(-4)*pop[5]**2*(7.8*10**(-4)*Icoil)**2)*10**(-11)
de_m = ( (0.1/Vacc) + 2*(pop[6]/pop[5]) + 2*(0.01/Icoil) )*e_m

print('e_m=%f +- %f'%(e_m,de_m))