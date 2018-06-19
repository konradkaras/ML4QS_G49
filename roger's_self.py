

from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
import copy
import os

from util.VisualizeDataset import VisualizeDataset
from Chapter3.OutlierDetection import DistributionBasedOutlierDetection
from Chapter3.OutlierDetection import DistanceBasedOutlierDetection
import copy
import pandas as pd
import numpy as np


dataset_path = './sample_data/'
DataViz = VisualizeDataset()
dataset = pd.read_csv(dataset_path + 'pamap108_sample10.csv', index_col=0)

#dataset = dataset.data_table
#dataset.index = pd.to_datetime(dataset.index)

DataViz.plot_dataset(dataset, ['imu_hand_acc_', 'imu_hand_gyr_', 'imu_hand_mag_', 'light_phone_lux', 'imu_hand_temp', 'hr', 'activity'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like'], ['line', 'line', 'line', 'line', 'line', 'line', 'points', 'points'])

util.print_statistics(dataset)
dataset.append(copy.deepcopy(dataset))

util.print_latex_table_statistics_two_datasets(dataset[0], dataset[1])