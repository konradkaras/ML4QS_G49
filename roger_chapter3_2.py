

from util.VisualizeDataset import VisualizeDataset
from Chapter3.OutlierDetection import DistributionBasedOutlierDetection
from Chapter3.OutlierDetection import DistanceBasedOutlierDetection
import copy
import pandas as pd
from util.VisualizeDataset import VisualizeDataset

import matplotlib.pyplot as plt
import numpy as np

DataViz = VisualizeDataset()


dataset_path = './intermediate_datafiles/'
dataset = pd.read_csv(dataset_path + 'chapter3_result_outliers.csv', index_col=0)

dataset.index = pd.to_datetime(dataset.index)
#Compute the number of milliseconds covered by an instance based on the first two rows
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds / 1000


def impute_interpolate(dataset, col):
    dataset[col] = dataset[col].interpolate()
    # And fill the initial data points if needed:
    dataset[col] = dataset[col].fillna(method='bfill')
    return dataset

#dataset['hr_watch_rate'] = dataset['hr_watch_rate'].values.impute_interpolate(dataset,'hr_watch_rate')
dataset = impute_interpolate(dataset,'hr_watch_rate')
print dataset.isnull().sum()

#dataset['hr_watch_rate'].plot.scatter(x, y, s=None, c=None, **kwds)
#plot.show()

#dataset.columns = ['time','hr_watch_rate']
#dataset.plot(kind='scatter',x='time',y='hr_watch_rate')
#plt.show()

heart = ['hr_watch_rate']
for col in heart:

#dataset = OutlierDist.local_outlier_factor(dataset, [col], 'euclidean', 5)
    #DataViz.plot_dataset(dataset, [col, ''], ['exact','exact'], ['line', 'points'])
    DataViz.plot_dataset(dataset, [col], ['exact','exact'], ['points','points'])