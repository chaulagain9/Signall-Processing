
import numpy as np                                               #importing library numpy.
import csv                                                    #importing library csv to read .csv files. 
import binascii

csv=np.genfromtxt('data-communications.csv',delimiter=',')       #Opens the data-communications.csv file given.
arr_length=len(csv)/10                                           #finding the size of the  data from .csv files and dividing into list of 10 arrays. 
print(type(csv))
print(csv)
arr=np.array_split(csv,arr_length,0)                             #splitting the array into 920 chunks with arrays of 10 elements. 

pulse0 = np.ones( 10 )                                           #code pieces Given. 
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
pulse1 = pulse1/np.linalg.norm(pulse1)
bit=[]                                                         #creating an empty list called bit 
for i in range (0,len(arr)):                                   #running the loop to calculate the dot product of two vectors. 
    y=np.dot(arr[i],pulse0)
    x=np.dot(arr[i],pulse1)
    if y<x:
        a=1
    elif y>x:
        a=0
    bit.append(a)
split=np.array_split(bit,115,0)                                 #splitting the list into 115 pieces with 8 bits each. 
terr=np.concatenate(split)
print(terr)


    

    