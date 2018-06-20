##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 2                                               #
#                                                            #
##############################################################


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

granularities = [60000, 1000]
datasets = []

for milliseconds_per_instance in granularities:

    # Create an initial dataset object with the base directory for our data and a granularity
    DataSet = CreateDataset(dataset_path, milliseconds_per_instance)

    # Add the selected measurements to it.

    # We add the accelerometer data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values/
    DataSet.add_numerical_dataset('move_rotation.csv', 'timestamp', ['x','y','z'], 'avg', 'rot_')
    DataSet.add_numerical_dataset('move_acceleration.csv', 'timestamp', ['x','y','z'], 'avg', 'acc_')
    DataSet.add_numerical_dataset('move_magnetic.csv', 'timestamp', ['x','y','z'], 'avg', 'mag_')
    DataSet.add_numerical_dataset('move_gravity.csv', 'timestamp', ['x','y','z'], 'avg', 'gra_')
    DataSet.add_numerical_dataset('move_attitude.csv', 'timestamp', ['yaw','pitch','roll'], 'avg', 'att_')

    DataSet.add_event_dataset('move_label.csv', 'label_start', 'label_end', 'label', 'binary')

    # Get the resulting pandas data table

    dataset = DataSet.data_table

    # Plot the data

    DataViz = VisualizeDataset()

    # Boxplot
    DataViz.plot_dataset_boxplot(dataset, ['acc_x','acc_y','acc_z'])

    # Plot all data
    DataViz.plot_dataset(dataset, ['rot_','acc_','mag_','gra_','att_','label'], ['like','like','like','like','like','like'], ['line','line','line','line','line','points'])

    # And print a summary of the dataset

    util.print_statistics(dataset)
    datasets.append(copy.deepcopy(dataset))

# And print the table that has been included in the book

util.print_latex_table_statistics_two_datasets(datasets[0], datasets[0])


# Finally, store the last dataset we have generated (250 ms).
dataset.to_csv(result_dataset_path + 'kokar_chapter2_result.csv')
