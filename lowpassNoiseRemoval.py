

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt 
from scipy.signal import freqz
import soundfile as sf

data,samplerate=sf.read('P_9_2.wav')

fc=7500                                 #cut-off frequency
L=101                                   #filter length
M=L-1

fs=samplerate
ft=fc/fs
temp1=[ ]
for n in range(0,100):
    if n==M/2:
        temp=2*ft
    else:
        temp=(np.sin(2*(np.pi)*ft*(n-M/2)))/(np.pi*(n-M/2))
    temp1.append(temp)

ham_coff=[ ]
for n in range(0,100):
    ham=0.54-0.46*np.cos((2*np.pi*n)/M)
    ham_coff.append(ham)
h_window=np.multiply(ham_coff,temp1)                    #performing an element-wise multiplication between h[n] and w[n].

conv_h=np.convolve(data,h_window)
x,y=freqz(temp1,1)
plt.plot(x,abs(y),'b',label='Low Pass Filter')
t,u=freqz(h_window,1)

plt.plot(t,abs(u),'r',label='After Applying Hamming Window')
plt.title('Before and After Applying Hamming Window.')
sf.write('cleanMusic.wav',conv_h,22000)
plt.legend()
plt.show()
