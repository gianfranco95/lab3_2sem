import oscillografo
import  os
import pylab as py
import numpy as np
folder = os.path.realpath('.')

filename='prova.csv'
o=oscillografo.OscilloscopeData(os.path.join(folder, 'Dati', filename))

# py.plot(o.T1,o.CH1)
# py.plot(o.T2,o.CH2)
# py.show()

