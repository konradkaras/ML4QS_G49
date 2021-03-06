


dataset_path = './sample_data/'
result_dataset_path = './intermediate_datafiles/'

# Import the relevant classes.

from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
import copy
import os


if not os.path.exists(result_dataset_path):
    print('Creating result directory: ' + result_dataset_path)
    os.makedirs(result_dataset_path)

# Chapter 2: Initial exploration of the dataset.

# Set a granularity (i.e. how big are our discrete time steps). We start very
# coarse grained, namely one measurement per minute, and secondly use four measurements
# per second

granularities = [2000, 2000]
datasets = []

for milliseconds_per_instance in granularities:

    # Create an initial dataset object with the base directory for our data and a granularity
    DataSet = CreateDataset(dataset_path, milliseconds_per_instance)

    # Add the selected measurements to it.

    # We add the accelerometer data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values/
    DataSet.add_numerical_dataset('pamap_imuAnkle_acc.csv', 'timestamp', ['x','y','z'], 'avg', 'acc_ankle_')
    DataSet.add_numerical_dataset('pamap_imuChest_acc.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'acc_chest_')
    DataSet.add_numerical_dataset('pamap_imuHand_acc.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'acc_hand_')


    # We add the gyroscope data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values/
    DataSet.add_numerical_dataset('pamap_imuAnkle_gyr.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'gyr_ankle_')
    DataSet.add_numerical_dataset('pamap_imuChest_gyr.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'gyr_chest_')
    DataSet.add_numerical_dataset('pamap_imuHand_gyr.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'gyr_hand_')

    # We add the heart rate (continuous numerical measurements) and aggregate by averaging again
    DataSet.add_numerical_dataset('pamap_hr.csv', 'timestamp', ['hr'], 'avg', 'hr_')

    # We add the labels provided by the users. These are categorical events that might overlap. We add them
    # as binary attributes (i.e. add a one to the attribute representing the specific value for the label if it
    # occurs within an interval).
    DataSet.add_event_dataset('pamap_labels.csv', 'label_start', 'label_end', 'label', 'binary')

    # We add the amount of light sensed by the phone (continuous numerical measurements) and aggregate by averaging again
    #DataSet.add_numerical_dataset('light_phone.csv', 'timestamp', ['lux'], 'avg', 'light_phone_')

    # We add the magnetometer data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values
    DataSet.add_numerical_dataset('pamap_imuAnkle_mag.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'mag_ankle_')
    DataSet.add_numerical_dataset('pamap_imuChest_mag.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'mag_chest_')
    DataSet.add_numerical_dataset('pamap_imuHand_mag.csv', 'timestamp', ['x', 'y', 'z'], 'avg', 'mag_hand_')
    # We add the pressure sensed by the phone (continuous numerical measurements) and aggregate by averaging again
    DataSet.add_numerical_dataset('pamap_imuAnkle_temp.csv', 'timestamp', ['temp'], 'avg', 'temp_ankle_')
    DataSet.add_numerical_dataset('pamap_imuChest_temp.csv', 'timestamp', ['temp'], 'avg', 'temp_chest_')
    DataSet.add_numerical_dataset('pamap_imuHand_temp.csv', 'timestamp', ['temp'], 'avg', 'temp_hand_')


    #adding labels
    #DataSet.add_numerical_dataset('pamap_imuHand_temp.csv', 'timestamp', ['label'], 'avg', 'label')

    # Get the resulting pandas data table

    dataset = DataSet.data_table

    # Plot the data

    DataViz = VisualizeDataset()

    # Boxplot
    #DataViz.plot_dataset_boxplot(dataset, ['acc_ankle_x','acc_phone_y','acc_phone_z','acc_watch_x','acc_watch_y','acc_watch_z'])

    # Plot all data
    DataViz.plot_dataset_boxplot(dataset, ['mag_ankle_x','mag_ankle_y','mag_ankle_z','mag_chest_x','mag_chest_y','mag_chest_z','mag_hand_x','mag_hand_y','mag_hand_z',])

    DataViz.plot_dataset(dataset, ['acc_', 'gyr_', 'hr', 'temp_', 'mag_', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like'], ['line', 'line', 'line', 'line', 'line', 'points', 'points'])

    # And print a summary of the dataset

    util.print_statistics(dataset)
    datasets.append(copy.deepcopy(dataset))

# And print the table that has been included in the book

util.print_latex_table_statistics_two_datasets(datasets[0], datasets[1])

# Finally, store the last dataset we have generated (250 ms).
#dataset.to_csv(result_dataset_path + 'pmap_chapter2_result.csv')
