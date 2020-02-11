
import matplotlib.pyplot as plt 
import numpy as np
from scipy import ndimage
from PIL import Image


h=np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])                   #Low Pass filter
high_pass=np.array([-1,1])                                              #high Pass filter
plt.figure(1)

"""Low Pass filter Passing through boat.512.tiff"""
picture_boat = Image.open('boat.512.tiff')                  
arr_boat=np.array(picture_boat,dtype=float)
plt.imshow(arr_boat,cmap="gray")
plt.title("Original Unfiltered Image")
row_boat =np.size(arr_boat,0)
column=np.size(arr_boat,1)

plt.figure(2)
result_boat = []
for i in range(0,row_boat,1):
    conv_boat=np.convolve(arr_boat[i],h)
    result_boat=np.append(result_boat,conv_boat)
    b1=np.reshape(result_boat,(-1,len(conv_boat)))

plt.imshow(b1,cmap="gray")
plt.title("Low Filtered Image")

"""high pass filter"""

result_boat_high=[]
for i in range(0,row_boat,1):
    conv_boat_low=np.convolve(arr_boat[i],high_pass)
    result_boat_high=np.append(result_boat_high,conv_boat_low)
    b1_high=np.reshape(result_boat_high,(-1,len(conv_boat_low)))
plt.figure(3)
plt.imshow(b1_high,cmap="gray")
plt.title("High Filtered Image")



plt.figure(4)
"""Low pass Filter Passing through man-5.3.01.tiff"""
picture_man = Image.open('man-5.3.01.tiff')
arr_man=np.array(picture_man,dtype=float)
plt.imshow(arr_man,cmap="gray")
plt.title("Original Unfiltered Image")
row_man =np.size(arr_man,0)
column_man=np.size(arr_man,1)

plt.figure(5)
result_man = []

for i in range(0,row_man,1):
    conv_man=np.convolve(arr_man[i],h)
    result_man=np.append(result_man,conv_man)
    b2=np.reshape(result_man,(-1,len(conv_man)))
plt.imshow(b2,cmap="gray")
plt.title("Low Pass filtered Image")

"""high pass filter"""
plt.figure(6)
result_man_high=[]
for i in range(0,row_man,1):
    conv_man_high=np.convolve(arr_man[i],high_pass)
    result_man_high=np.append(result_man_high,conv_man_high)
    b2_high=np.reshape(result_man_high,(-1,len(conv_man_high)))
plt.imshow(b2_high,cmap="gray")
plt.title("High Pass Filtered Image")

plt.figure(7)
"""Low pass Filter Passing through tank-7.1.07.tiff"""
picture_tank = Image.open('tank-7.1.07.tiff')
arr_tank=np.array(picture_tank,dtype=float)
plt.imshow(arr_tank,cmap="gray")
plt.title("Orginal Uniltered Image")
row_tank =np.size(arr_tank,0)
column_tank=np.size(arr_tank,1)

plt.figure(8)
result_tank = []
for i in range(0,row_tank,1):
    conv_tank=np.convolve(arr_tank[i],h)
    result_tank=np.append(result_tank,conv_tank)
    b3=np.reshape(result_tank,(-1,len(conv_tank)))
plt.imshow(b3,cmap="gray")
plt.title("Low Pass Filtered Image")

"""high pass filter"""
plt.figure(9)
result_tank_high=[]
for i in range(0,row_tank,1):
    conv_tank_high=np.convolve(arr_tank[i],high_pass)
    result_tank_high=np.append(result_tank_high,conv_tank_high)
    b3_high=np.reshape(result_tank_high,(-1,len(conv_tank_high)))
plt.imshow(b3_high,cmap="gray")
plt.title("High Pass Filtered Image")

plt.figure(10)
"""Low pass Filter Passing through clock-5.1.12.tiff"""
picture_clock = Image.open('clock-5.1.12.tiff')
arr_clock=np.array(picture_clock,dtype=float)
plt.imshow(arr_clock,cmap="gray")
plt.title("Original Unfiltered Image")
row_clock =np.size(arr_clock,0)
column_clock=np.size(arr_clock,1)

plt.figure(11)
result_clock = []
for i in range(0,row_clock,1):
    conv_clock=np.convolve(arr_clock[i],h)
    result_clock=np.append(result_clock,conv_clock)
    b4=np.reshape(result_clock,(-1,len(conv_clock)))
plt.imshow(b4,cmap="gray")
plt.title("Low Pass Filtered Image")

"""high pass filter"""
plt.figure(12)
result_clock_high=[]
for i in range(0,row_clock,1):
    conv_clock_high=np.convolve(arr_clock[i],high_pass)
    result_clock_high=np.append(result_clock_high,conv_clock_high)
    b4_high=np.reshape(result_clock_high,(-1,len(conv_clock_high)))
plt.imshow(b4_high,cmap="gray")
plt.title("High Pass Filtered Image")


plt.figure(13)
"""darinGrayNoise.jpg image for median_filter using ndimage"""

prof_img=Image.open('darinGrayNoise.jpg')
arr_prof=np.array(prof_img,dtype=float)
plt.imshow(arr_prof,cmap="gray")
plt.title("Original Unfiltered Image")
row_prof =np.size(arr_prof,0)
column_prof=np.size(arr_prof,1)

plt.figure(14)
result_prof = []
for i in range(0,row_prof,1):
    conv_prof=np.convolve(arr_prof[i],h)
    result_prof=np.append(result_prof,conv_prof)
    b5=np.reshape(result_prof,(-1,len(conv_prof)))
plt.imshow(b5,cmap="gray")
plt.title("Low Filtered Image with noise")

plt.figure(15)
outputImage = ndimage.median_filter(prof_img,5)
plt.imshow(outputImage,cmap="gray")
plt.title("Median Pass Filtered Image")
plt.show()





