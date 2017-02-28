import oscillografo
import  os
import pylab as py
import numpy as np
folder = os.path.realpath('.')

filename='data626.csv'
o=oscillografo.OscilloscopeData(os.path.join(folder, 'Dati', filename))
o.CH1=o.CH1*10

py.plot(o.CH1,o.CH2,'.')
py.xlabel('$V_a$ [V]')
py.ylabel('$ \propto I_c$')
py.title('$I_c$ vs $V_a$ ')
py.xlim(1,82)
py.show()

##max e min
datafile='maxmin.txt'
rawdata = np.loadtxt(os.path.join(folder, 'Dati', datafile)).T

i=0

py.figure(i)
py.xlabel('$V_e$ [V]')
py.ylabel('$V_a$ [V]')
py.title('valori di $V_a$ vs $V_e$ per primo massimo di $I_c$')
py.errorbar(rawdata[12],rawdata[i],rawdata[i+1],rawdata[13],'o')
i=i+2
py.show()