from util.VisualizeDataset import VisualizeDataset
from Chapter3.OutlierDetection import DistributionBasedOutlierDetection
from Chapter3.OutlierDetection import DistanceBasedOutlierDetection
import copy
import pandas as pd
import numpy as np

# Let is create our visualization class again.
DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sture the index is of the type datetime.
dataset_path = './intermediate_datafiles/'
try:
    dataset = pd.read_csv(dataset_path + 'pmap_chapter2_result.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e


#milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds / 1000

outlier_columns = ['acc_ankle_x', 'acc_ankle_y', 'acc_ankle_z', 'acc_chest_x',
       'acc_chest_y', 'acc_chest_z', 'acc_hand_x', 'acc_hand_y',
       'acc_hand_z', 'gyr_ankle_x', 'gyr_ankle_y', 'gyr_ankle_z',
       'gyr_chest_x', 'gyr_chest_y', 'gyr_chest_z', 'gyr_hand_x',
       'gyr_hand_y', 'gyr_hand_z',
       'mag_ankle_x', 'mag_ankle_y', 'mag_ankle_z', 'mag_chest_x',
       'mag_chest_y', 'mag_chest_z', 'mag_hand_x', 'mag_hand_y',
       'mag_hand_z', 'temp_ankle_temp', 'temp_chest_temp',
       'temp_hand_temp']

OutlierDist = DistanceBasedOutlierDetection()

for col in [c for c in dataset.columns if not 'label' in c]:
    print 'Measurement is now: ' , col
    #dataset = OutlierDistr.chauvenet(dataset, col)

    dataset = OutlierDist.local_outlier_factor(dataset, [col], 'euclidean', 5)
    DataViz.plot_dataset(dataset, [col, 'lof'], ['exact', 'exact'], ['line', 'points'])

    dataset.loc[dataset[col + '_lof'] == True, col] = np.nan
    del dataset[col + '_lof']

dataset.to_csv(dataset_path + 'pmap_chapter3_result_outliers.csv')