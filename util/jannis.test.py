from scipy.stats import ks_2samp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# dataset_path = './ /'

crowd= pd.read_csv('/Volumes/Untitled/quant.self/code/datasets/accelerometer_smartwatch.csv')
crowd_x = crowd['x']
crowd_y = crowd['y']
crowd_z = crowd['z']

std_x = np.std(crowd_x)
std_y = np.std(crowd_y)
std_z = np.std(crowd_z)
print ('\n standard deviation of crowdsignal data')
print std_x
print std_y
print std_z

print('\n mean of crowdsignal data')
mean_x = np.mean(crowd_x)
mean_y = np.mean(crowd_y)
mean_z = np.mean(crowd_z)

print mean_x
print mean_y
print mean_z

sample= pd.read_csv('/Users/ioannismilas/PycharmProjects/ML4QS_G49/sample_data/move_acceleration.csv')
sample_x = sample['x']
sample_y = sample['y']
sample_z = sample['z']

std_sampleX = np.std(sample_x)
std_sampleY = np.std(sample_y)
std_sampleZ = np.std(sample_z)

print ('\n standard deviation of sample data')
print std_sampleX
print std_sampleY
print std_sampleZ

mean_sampleX = np.mean(sample_x)
mean_sampleY = np.mean(sample_y)
mean_sampleZ = np.mean(sample_z)

print ('\n mean of sample data')
print mean_sampleX
print mean_sampleY
print mean_sampleZ

#np.random.seed(12345678)
#x = np.random.normal(0, 1, 1000)
#y = np.random.normal(0, 1, 1000)
#z = np.random.normal(1.1, 0.9, 1000)

# test=ks_2samp(sample_y, crowd_y)
# print test

#test1 = ks_2samp(x, z)
#print test1