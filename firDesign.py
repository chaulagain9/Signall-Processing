
import csv
import numpy as np 
import matplotlib.pyplot as plt

"""Low Pass Filter"""

fs=2000                                                           #Sampling rate of the data of .csv files. 
csv=np.genfromtxt('data-filtering.csv',delimiter=',')
fc=50                                                             #the cut off frequency
L=21                                                               #Filter length
M=L-1   
plt.figure(1)
plt.subplot(3,1,1)        
plt.plot(csv)
plt.title('original signal')

x=np.arange(2000)
y=[np.cos(2*np.pi*4*(i/fs)) for i in x]
plt.subplot(3,1,2)
plt.plot(x,y)
plt.title('4 Hz Signal')

ft=50/2000                                                        #the normalized cut off frequecny
k=20
temp1=[ ]
for n in range(0,20):
    if n==M/2:
        temp=2*ft
    else:
        temp=(np.sin(2*(np.pi)*ft*(n-M/2)))/(np.pi*(n-M/2))
    temp1.append(temp)

w=np.convolve(csv,temp1)
plt.subplot(3,1,3)
plt.title('application of low pass filter')
plt.plot(w)

plt.tight_layout()


""""The High Pass filter"""
plt.figure(2)
high_fc=280
high_ft=280/2000
temp3=[ ]

splice=csv[:100]

plt.subplot(3,1,1)
plt.plot(splice)
plt.title('original signal')

for m in range(0,20):
    if m==M/2:
        fil=1-2*high_ft
    else:
        fil=(-(np.sin(2*(np.pi)*high_ft*(m-M/2)))/(np.pi*(m-M/2)))
    temp3.append(fil)

high_x=np.arange(100)
high_y=[np.cos(2*np.pi*330*(i/fs)) for i in high_x]
w2=np.convolve(splice,temp3)
spli=w2[0:100]
plt.subplot(3,1,2)
plt.plot(high_x,high_y)
plt.title('330 Hz Signal')

plt.subplot(3,1,3)
plt.plot(spli)
plt.title('application of high pass filter.')


plt.tight_layout()
plt.show()
