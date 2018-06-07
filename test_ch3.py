from util.VisualizeDataset import VisualizeDataset
from Chapter3.OutlierDetection import DistributionBasedOutlierDetection
from Chapter3.OutlierDetection import DistanceBasedOutlierDetection
import copy
import pandas as pd
import numpy as np


# Let is create our visualization class again.
DataViz = VisualizeDataset()

dataset_path = './csv-participant-one/'
dataset = pd.read_csv(dataset_path + 'heart_rate_smartwatch.csv', index_col=0)

dataset.index = dataset.index.to_datetime()

