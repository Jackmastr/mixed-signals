import numpy as np
import matplotlib.pyplot as plt
from ugradio import pico as pco
from ugradio.dft import dft as dft

'''
data = pco.read_socket("2V", 10)
np.save("mixer_80-100",data[1024:2048])
'''
data = np.load("mixer_80-100.npy")
freq,four = dft(data)
fourR = np.real(four)
fourI = np.imag(four)
powsp = np.abs(four)**2

#plt.plot(freq,data, 'k.-')
#plt.plot(freq,fourR, 'b.-')
#plt.plot(freq,fourI, 'r.-')
plt.plot(freq,powsp, 'k.-')
plt.show()
