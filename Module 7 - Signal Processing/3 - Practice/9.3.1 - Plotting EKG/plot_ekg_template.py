from array import array

import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, delimiter=',', skiprows=2)
### Your code here ###

# save each vector as own variable
elapsed_time = data[:,0]
mlii = data[:,1]
v1 = data[:,2]
### Your code here ###

# use matplot lib to generate a single plot
plt.plot(elapsed_time, mlii, v1, label='EKG Data', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Heartbeat EKG')
plt.show()

### Your code here ###