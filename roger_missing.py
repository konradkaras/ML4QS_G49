import pandas as pd

dataset_path = './intermediate_datafiles/'
dataset = pd.read_csv(dataset_path + 'kokar_chapter5_result.csv', index_col=0)

dataset = dataset.fillna(0)
print dataset.isnull().sum()

dataset.to_csv(dataset_path + 'kokar_chapter5_result_nofuckingmissingvalues.csv')