from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
import pandas as pd
from util import util
import copy
import os



dataset_path = './sample_data/'
DataViz = VisualizeDataset()
dataset = pd.read_csv(dataset_path + 'pamap108_sample10.csv', index_col=0)

DataViz.plot_dataset_boxplot(dataset, ['imu_hand_acc_x_16','imu_hand_acc_y_16','imu_hand_acc_z_16','imu_chest_acc_x_16','imu_chest_acc_y_16','imu_chest_acc_z_16', 'imu_ankle_acc_x_16','imu_ankle_acc_y_16','imu_ankle_acc_z_16',])
DataViz.plot_dataset_boxplot(dataset, ['imu_hand_gyr_x','imu_hand_gyr_y','imu_hand_gyr_z','imu_chest_gyr_x','imu_chest_gyr_y','imu_chest_gyr_z', 'imu_ankle_gyr_x','imu_ankle_gyr_y','imu_ankle_gyr_z',])
DataViz.plot_dataset_boxplot(dataset, ['imu_hand_mag_x','imu_hand_mag_y','imu_hand_mag_z','imu_chest_mag_x','imu_chest_mag_y','imu_chest_mag_z', 'imu_ankle_mag_x','imu_ankle_mag_y','imu_ankle_mag_z',])
DataViz.plot_dataset_boxplot(dataset, ['imu_hand_temp','imu_chest_temp','imu_ankle_temp'])
