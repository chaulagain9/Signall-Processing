
"""Sameer Chaulagain
   1001418268(sxc8268)
   CSE 3313
   Homework 05 
   Question no. 05
   
"""
import numpy as np
import matplotlib.pyplot as plt 
import scipy as sc
import soundfile as sf

file=open('shelvingConfig.txt','r').read().splitlines()     #reading from the .txt files
gain=int(file[1])
fc=int(file[2])                                             #cutting frequency
 
data,samplerate=sf.read('P_9_1.wav')                        #reading data and sample from the soundfile
sample_fft=np.fft.fft(data)                                   #finding the fft of the original sample data

N= len(sample_fft)                                              #size of the magnitude of the fft data
plt.subplot(2,1,1)
plt.plot(abs(sample_fft[0:int(N/4)]))
plt.ylim(0,2600)
plt.title("Original FFT Signal.")

#Creating the  the shelving filtered signal .
u=10**(gain/20)
theta=(2*np.pi*fc)/samplerate
y=(1-(4/(1+u))*np.tan(theta/2))/(1+(4/(1+u))*np.tan(theta/2))
a=(1-y)/2

selving_filter=[]                                       #new signal with shelving filter applied
input=0                                                        #the initial input is set to 0.
output=0                                                       #the initial output is set to 0.
for n in range(0,len(data)):
    u_n=a*(data[n]+input)+y*output
    y_n=data[n]+u_n*(u-1)
    input=data[n]
    output=u_n 
    selving_filter.append(y_n)

sf.write('shelvingOutput.wav',selving_filter,22000) 

new_fft=np.fft.fft(selving_filter)
N1=len(sample_fft)
plt.subplot(2,1,2)
plt.plot(abs(new_fft[0:int(N1/4)]))
plt.ylim(0,2600)                            #The maximum amplitude of the original signal is about 2500 therefore setting y-lim to 2600 by adding 100. 
plt.title("Filtered Signal with FFT")


plt.tight_layout()
plt.show()

