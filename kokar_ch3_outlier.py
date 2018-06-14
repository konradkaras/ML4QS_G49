##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 3                                               #
#                                                            #
##############################################################

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
    dataset = pd.read_csv(dataset_path + 'chapter2_result.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e

dataset.index = pd.to_datetime(dataset.index)

# Compute the number of milliseconds covered by an instance based on the first two rows
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds / 1000

# Step 1: Let us see whether we have some outliers we would prefer to remove.

# Determine the columns we want to experiment on.
outlier_columns = ['acc_phone_x', 'light_phone_lux']

# Create the outlier classes.
OutlierDistr = DistributionBasedOutlierDetection()
OutlierDist = DistanceBasedOutlierDetection()


for col in outlier_columns:
    print 'Measurement is now: ', col
    # Chauvenet's
    print 'chauvenets start'
    dataset = OutlierDistr.chauvenet(dataset, col)
    print 'chauvenets stop'

    # mixture
    print 'mixture start'
    dataset = OutlierDistr.mixture_model(dataset, col)
    print 'mixture stop'

    # distance-based
    print 'distance start'
    dataset = OutlierDist.simple_distance_based(dataset, [col], 'euclidean', 0.5, 0.99)
    print 'distance stop'

    # lof
    print 'lof start'
    dataset = OutlierDist.local_outlier_factor(dataset, [col], 'euclidean', 10)
    print 'lof stop'

dataset.to_csv(dataset_path + 'kokar_ch3_result_outliers_c10.csv')
