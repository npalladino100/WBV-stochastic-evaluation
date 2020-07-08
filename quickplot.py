import matplotlib.pyplot as plt
import csv
import numpy as np

x=[]
y=[]
y2=[]

with open('dump1.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[0].strip()))

with open('dump2.txt', 'r') as csvfile:
    plots2= csv.reader(csvfile, delimiter=',')
    for row2 in plots2:
        y2.append(float(row2[0].strip()))


if (len(y)) > (len(y2)):
    y = np.delete(y,-1)

if (len(y)) < (len(y2)):
    y2 = np.delete(y2,-1)
    
x = np.arange(0.0, len(y)/100, 0.01)

plt.plot(x,y,x,y2)

plt.title('Acceleration vs. Time')

plt.xlabel('Time')
plt.ylabel('Acceleration (in G\'s)')

plt.show()

