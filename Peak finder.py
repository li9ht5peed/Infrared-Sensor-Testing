# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:56:04 2021

@author: I-Weifeng.Liu
"""

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

#Reading CSV

plt.close('all')
data = pd.read_csv('logs\obs_5cm_s0.txt',';',header=None, names=['x-cor','y-cor','ascan','range'])

#Assigning variables

x_arr = []
y_arr = []

for x_value in data['x-cor']:
    if x_value not in x_arr:
        x_arr.append(x_value)
        
for y_value in data['y-cor']:
    if y_value not in y_arr:
        y_arr.append(y_value)
        
# ascan_arr = np.array(data['ascan'])
range_arr = np.array(data['range'])

#Extracting range array

s = range_arr[1]
x = s[1:-1].split(',')
x = np.array(x)
xs = x.astype(np.float)

#Extracting ascan array + plotting graph

for x_value in x_arr:
    for y_value in y_arr:
        
        f_data = data[(data['x-cor']==x_value) & (data['y-cor']==y_value)]        
        ascan_arr = f_data.ascan

        run_once = 0

        for y in ascan_arr:
            y = y[1:-1].split(",")
            y = np.array(y)
            ys = y.astype(np.float)
    
# Stacking y arrays
    
            if len(ys) != len(xs):
                continue
            else:
                if run_once == 0:
                    array_stack = ys
                    run_once = 1
                else:
                    array_stack = np.row_stack((array_stack,ys))
                    # plt.plot(xs, ys)#, label='Coord = '+str(x_value)+' , '+str(y_value))  

        ys_mean = array_stack.mean(axis=0) 

# Finding amplitude peaks

        peaks = find_peaks(ys_mean, height = (200,20000), threshold=(1), distance=(500))  
        height = peaks[1]['peak_heights'] #list containing the height of the peaks
        peak_pos = ys_mean[peaks[0]]  #list containing the positions of the peaks  

        for i, j in enumerate(ys_mean):
            if j == height:
                a = xs[i]
                b = ys_mean[i]
                print("The coordinate of ", x_value,',',y_value," and average's peak amplitude = \n ", a, b," \n")
        
        plt.figure()
        plt.plot(xs, ys_mean, label='Coord = '+str(x_value)+' , '+str(y_value))
        # plt.scatter(a, b, color = 'r', s = 15, marker = 'x', label = 'Peak')

        plt.title('Grid Sensing')
        plt.ylabel('Amplitude (LSB)', fontsize=10)
        plt.xlabel('Range (mm)', fontsize=10)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(True)
        plt.ylim(0,3000)
        plt.xlim(0,300)
        plt.legend(loc="upper right")
        
        plt.show()



