
import numpy as np         
import soundfile as sf

keynumber=np.array([52,52,59,59,61,61,59,59,52,55,56,58,61,56,55,54,61,59,61,59,54,52,52])  
frequency=440*(2**((keynumber-49)/12))                              #apprximate frequency 
t=0.5                                                               #time is 0.5s 
x= 1*np.cos(2*np.pi*frequency*t*(1/8000))    
sf.write('twinkle.wav',x,8000)                                      #creating the sound file 