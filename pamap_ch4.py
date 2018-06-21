from util.VisualizeDataset import VisualizeDataset
from Chapter4.TemporalAbstraction import NumericalAbstraction
from Chapter4.TemporalAbstraction import CategoricalAbstraction
from Chapter4.FrequencyAbstraction import FourierTransformation
from Chapter4.TextAbstraction import TextAbstraction
import copy
import pandas as pd

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
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds/1000

FreqAbs = FourierTransformation()
fs = float(1000)/milliseconds_per_instance

periodic_predictor_cols = ['acc_ankle_x', 'acc_ankle_y', 'acc_ankle_z', 'acc_chest_x',
       'acc_chest_y', 'acc_chest_z', 'acc_hand_x', 'acc_hand_y',
       'acc_hand_z', 'gyr_ankle_x', 'gyr_ankle_y', 'gyr_ankle_z',
       'gyr_chest_x', 'gyr_chest_y', 'gyr_chest_z', 'gyr_hand_x',
       'gyr_hand_y', 'gyr_hand_z',
       'mag_ankle_x', 'mag_ankle_y', 'mag_ankle_z', 'mag_chest_x',
       'mag_chest_y', 'mag_chest_z', 'mag_hand_x', 'mag_hand_y',
       'mag_hand_z']
data_table = FreqAbs.abstract_frequency(copy.deepcopy(dataset), ['gyr_ankle_x'], int(float(10000)/milliseconds_per_instance), fs)

# Spectral analysis.

DataViz.plot_dataset(data_table, ['gyr_ankle_y_max_freq', 'gyr_chest_y_freq_weighted', 'gyr_hand_y_pse', 'label'], ['like', 'like', 'like', 'like'], ['line', 'line', 'line','points'])

dataset = FreqAbs.abstract_frequency(dataset, periodic_predictor_cols, int(float(10000)/milliseconds_per_instance), fs)

# Now we only take a certain percentage of overlap in the windows, otherwise our training examples will be too much alike.

# The percentage of overlap we allow
window_overlap = 0.9
skip_points = int((1-window_overlap) * ws)
dataset = dataset.iloc[::skip_points,:]


#dataset.to_csv(dataset_path + 'chapter4_result.csv')

DataViz.plot_dataset(dataset, ['acc_ankle_x', 'gyr_ankle_x', 'hr_hr', 'temp_ankle_temp', 'mag_ankle_x', 'pca_2', 'pca_1', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like'], ['line', 'line', 'line', 'line', 'line', 'line', 'line', 'points'])

#SECOND PART

window_sizes = [int(float(5000)/milliseconds_per_instance), int(float(0.5*60000)/milliseconds_per_instance), int(float(5*60000)/milliseconds_per_instance)]

NumAbs = NumericalAbstraction()
dataset_copy = copy.deepcopy(dataset)
for ws in window_sizes:
    dataset_copy = NumAbs.abstract_numerical(dataset_copy, ['gyr_ankle_x'], ws, 'slope')
    dataset_copy = NumAbs.abstract_numerical(dataset_copy, ['gyr_ankle_x'], ws, 'mean')

DataViz.plot_dataset(dataset_copy, ['gyr_ankle_x', 'gyr_ankle_x_temp_slope', 'gyr_ankle_x_temp_mean', 'label'], ['exact', 'like', 'like', 'like'], ['line', 'line', 'line', 'points'])

ws = int(float(0.5*60000)/milliseconds_per_instance)
selected_predictor_cols = [c for c in dataset.columns if not 'label' in c]
dataset = NumAbs.abstract_numerical(dataset, selected_predictor_cols, ws, 'slope')
dataset = NumAbs.abstract_numerical(dataset, selected_predictor_cols, ws, 'mean')


CatAbs = CategoricalAbstraction()
dataset = CatAbs.abstract_categorical(dataset, ['label'], ['like'], 0.03, int(float(5*60000)/milliseconds_per_instance), 2)