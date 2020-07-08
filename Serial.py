#!/usr/bin/python3

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

measurement_dur = 5.0  #duration of acceleration measurement in seconds
num_of_accelerometers = 2.0  #number of accelerometers
time_between_measurements = .01  #time in seconds between measurements

ser = serial.Serial('/dev/ttyACM0', 9600)
time_elapsed = 0
arr1 = np.array([])
arr2 = np.array([])

start = time.time()

# read from Arduino
while time_elapsed < measurement_dur:
    input = ser.readline()
    input = input.decode(errors='ignore')
    if "a" in input:
        input = input.replace("a\r\n","")
        arr1 = np.append(arr1,input)
        #print (input.decode("utf-8"))
    if "b" in input:
        input = input.replace("b\r\n","")
        arr2 = np.append(arr2,input)
        #print (input.decode("utf-8"))
    time.sleep(time_between_measurements/num_of_accelerometers)
    time_elapsed = time.time() - start
ser.close()
arr1 = np.delete(arr1,0) #delete first element
arr1 = np.asfarray(arr1,float)
arr1.tofile('dump1.txt',sep='\n',format='%10.3f')

arr2 = np.delete(arr2,0) #delete first element
arr2 = np.asfarray(arr2,float)
arr2.tofile('dump2.txt',sep='\n',format='%10.3f')