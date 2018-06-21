from util.VisualizeDataset import VisualizeDataset
from Chapter4.TemporalAbstraction import NumericalAbstraction
from Chapter4.TemporalAbstraction import CategoricalAbstraction
from Chapter4.FrequencyAbstraction import FourierTransformation
from Chapter4.TextAbstraction import TextAbstraction
import copy
import pandas as pd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import math
import copy
from scipy.stats import norm
from sklearn.decomposition import PCA
from Chapter4.FrequencyAbstraction import FourierTransformation
import re

np.random.seed(0)

# Let us create our visualization class again.
DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sure the index is of the type datetime.
dataset_path = './intermediate_datafiles/'
try:
    dataset = pd.read_csv(dataset_path + 'chapter3_result_final.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e


dataset.index = pd.to_datetime(dataset.index)

# Compute the number of milliseconds covered by an instane based on the first two rows
milliseconds_per_instance = 1000

FreqAbs = FourierTransformation()
fs = float(1000)/milliseconds_per_instance

#periodic_predictor_cols = ['acc_phone_x','acc_phone_y','acc_phone_z','acc_watch_x','acc_watch_y','acc_watch_z','gyr_phone_x','gyr_phone_y',
#                           'gyr_phone_z','gyr_watch_x','gyr_watch_y','gyr_watch_z','mag_phone_x','mag_phone_y','mag_phone_z',
#                           'mag_watch_x','mag_watch_y','mag_watch_z']
#data_table = FreqAbs.abstract_frequency(copy.deepcopy(dataset), ['acc_phone_x'], int(float(10000)/milliseconds_per_instance), fs)


# Figure 4.1

# Sample frequency (Hz)
#fs = 10

fs = float(1000)/milliseconds_per_instance

# Create time points....
a = dataset['acc_phone_x']
df = pd.DataFrame(data=a, columns=list('X'))
df['X'] = a
#df = pd.DataFrame(np.arange(0, 16.1, float(1)/fs), columns=list('X'))
c1 = 3 * np.sin(2 * math.pi * 0.2 * df['X'])
c2 = 2 * np.sin(2 * math.pi * 0.25 * (df['X']-2)) + 5
df['Y'] = c1 + c2

plot.hold(True)
plot.plot(df['X'], df['Y'], 'b-')
plot.legend(['acc_phone_x'], loc=3, fontsize='small')
plot.xlabel('time')
plot.ylabel('$X_{1}$')
#plot.show()

# Figure 4.2

FreqAbs = FourierTransformation()
data_table = FreqAbs.abstract_frequency(copy.deepcopy(df), ['Y'], 40, fs)
# Get the frequencies from the columns....
frequencies = []
values = []
for col in data_table.columns:
    val = re.findall(r'freq_\d+\.\d+_Hz', col)
    if len(val) > 0:
        frequency = float((val[0])[5:len(val)-4])
        frequencies.append(frequency)
        values.append(data_table.ix[data_table.index, col])

fig = plot.figure()
plot.hold(True)
ax1 = fig.add_subplot(111)
#plot.xlim([0, 5])
ax1.plot(frequencies, values, 'b+')
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('$a$')
plot.show()

