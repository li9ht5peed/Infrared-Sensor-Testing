# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:41:06 2021

@author: I-Weifeng.Liu
"""

import numpy as np
from math import radians
import pandas as pd
import math, copy
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

plt.close('all')

data = pd.read_csv("logs\dist 20 - Copy - Copy.csv",',',header=None, names=['size','angl','ascan'])

angl_arr = []
size_arr = []

for angl_val in data['angl']:
    if angl_val not in angl_arr:
        angl_arr.append(angl_val)
        
for size_val in data['size']:
    if size_val not in size_arr:
        size_arr.append(size_val)
        
data_arr = np.array(data)

theta = np.array(angl_arr)*np.pi/180

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

#finding the biggest amplitude

high_arr = []
for (s,ang,asc) in data_arr:
    high_arr.append(asc)
high_arr = np.array(high_arr)
high = np.partition(high_arr.flatten(), -2)[-1]
        
#append array into new array
for x in size_arr:
    amp_arr = []
    for (s,ang,asc) in data_arr:
        if s != x :
            continue
        else:
            amp_arr.append(asc)
    
    amp_arr = np.array(amp_arr)
    amp_arr[:] = [x / high for x in amp_arr]
    #convert amp to log
    #amp_arr = np.log10(amp_arr)
    ax.plot(theta, amp_arr,label='size='+str(x)+'cm')       
'''
# data5 = data_arr[0:9]
# data10 = data_arr[9:18]
# data15 = data_arr[18:27]
# data20 = data_arr[27:]

#ascan = np.array(data['ascan'])

# ax.plot(theta, data5[:,2] ,label='dist='+str("5"))
# ax.plot(theta, data10[:,2] ,label='dist='+str("10"))
# ax.plot(theta, data15[:,2] ,label='dist='+str("15"))
# ax.plot(theta, data20[:,2] ,label='dist='+str("20"))


# for dist_val in dist_arr:
#     if dist_val == 5:
#         ax.plot(theta, data5[:,2] ,label='dist='+str(dist_val))
#     elif dist_val == 10:
#         ax.plot(theta, data10[:,2] ,label='dist='+str(dist_val))
#     elif dist_val == 15:
#         ax.plot(theta, data15[:,2] ,label='dist='+str(dist_val))
#     else:
#         ax.plot(theta, data20[:,2] ,label='dist='+str(dist_val))

for (d, ang, asc) in data_arr:
    if
    ax.plot(radians(ang), 8000-asc,label='dist='+str(d))

sat_positions = [[1, 1000, 0], [2, 2000, 90], [3, 3000, 180], [4, 4000, 135]]
for (PRN, E, Az) in sat_positions:
    ax.annotate(str(PRN),
                xy=(radians(Az), 8000-E),  # theta, radius
                bbox=dict(boxstyle="round", fc = 'green', alpha = 0.5),
                horizontalalignment='center',
                verticalalignment='center')
 '''   
ax.set_theta_direction("clockwise")
ax.set_title("Amplitude vs Angle")
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_ylim(0,1)
# ax.set_yticks(np.arange(0,8000,2000))
ax.set_theta_offset(1*np.pi)
ax.set_thetagrids(range(0, 181, 45))
ax.legend(loc="upper left", bbox_to_anchor=(1,1))

ax.grid(True)
#ax.set_title("A line plot on a polar axis", va='bottom')
#ax.legend(loc="upper right")
plt.show()

