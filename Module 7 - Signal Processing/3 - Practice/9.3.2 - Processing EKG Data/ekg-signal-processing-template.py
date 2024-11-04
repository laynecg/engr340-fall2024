import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

#signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath, delimiter=',', skiprows=2)

elapsed_time = signal[:,0]
mlii = signal[:,1]
v1 = signal[:,2]

plt.plot(elapsed_time, mlii, v1, label='EKG Data', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Heartbeat EKG')
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""
signal_magnitude = abs(v1)
weighted_diff = np.diff(signal_magnitude)

plt.plot(weighted_diff, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Voltage Signal after Weighted Differentiation')
plt.show()
## YOUR CODE HERE ##


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
signal_square = np.square(weighted_diff)

plt.plot(signal_square, color='green')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Voltage Signal after Squaring Data')
plt.show()
"""
Step 5: Pass a moving filter over your data
"""
weight = np.ones(25)
moving_filter = np.convolve(signal_square, weight)

plt.plot(moving_filter, color='yellow')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Voltage Signal after Moving Filter')
plt.show()
## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(signal)
plt.show()