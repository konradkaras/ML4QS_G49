import pandas as pd
import numpy as np

df = pd.read_csv('pamap108.csv')

initTimestamp = 1454956105656000000
timestep = 100000000

timestamp_x = np.zeros(len(df))

for i in range(0,len(timestamp_x)):
	print i
	timestamp_x[i] = initTimestamp
	initTimestamp = initTimestamp + timestep

df['timestamp'] = timestamp_x

### HR

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['hr'] = df['hr'].interpolate()

result.to_csv('pamap_hr.csv')

print df['hr'].isnull().sum()

# ================ HAND ===================

### IMU_HAND TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_hand_temp'].interpolate()

df['imu_hand_temp'] = df['imu_hand_temp'].fillna(method='ffill')
print df['imu_hand_temp'].isnull().sum()

result.to_csv('pamap_imuHand_temp.csv')


### IMU_HAND ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_acc_x_16'].interpolate()
result['y'] = df['imu_hand_acc_y_16'].interpolate()
result['z'] = df['imu_hand_acc_z_16'].interpolate()

df['imu_hand_acc_x_16'] = df['imu_hand_acc_x_16'].fillna(method='ffill')
df['imu_hand_acc_y_16'] = df['imu_hand_acc_y_16'].fillna(method='ffill')
df['imu_hand_acc_z_16'] = df['imu_hand_acc_z_16'].fillna(method='ffill')

print df['imu_hand_acc_x_16'].isnull().sum()
print df['imu_hand_acc_y_16'].isnull().sum()
print df['imu_hand_acc_z_16'].isnull().sum()

result.to_csv('pamap_imuHand_acc.csv')


### IMU_HAND GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_gyr_x'].interpolate()
result['y'] = df['imu_hand_gyr_y'].interpolate()
result['z'] = df['imu_hand_gyr_z'].interpolate()

df['imu_hand_gyr_x'] = df['imu_hand_gyr_x'].fillna(method='ffill')
df['imu_hand_gyr_y'] = df['imu_hand_gyr_y'].fillna(method='ffill')
df['imu_hand_gyr_z'] = df['imu_hand_gyr_z'].fillna(method='ffill')

print df['imu_hand_gyr_x'].isnull().sum()
print df['imu_hand_gyr_y'].isnull().sum()
print df['imu_hand_gyr_z'].isnull().sum()

result.to_csv('pamap_imuHand_gyr.csv')


### IMU_HAND MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_mag_x'].interpolate()
result['y'] = df['imu_hand_mag_y'].interpolate()
result['z'] = df['imu_hand_mag_z'].interpolate()

df['imu_hand_mag_x'] = df['imu_hand_mag_x'].fillna(method='ffill')
df['imu_hand_mag_y'] = df['imu_hand_mag_y'].fillna(method='ffill')
df['imu_hand_mag_z'] = df['imu_hand_mag_z'].fillna(method='ffill')

print df['imu_hand_mag_x'].isnull().sum()
print df['imu_hand_mag_y'].isnull().sum()
print df['imu_hand_mag_z'].isnull().sum()

result.to_csv('pamap_imuHand_mag.csv')


# ================ CHEST ===================

### imu_chest TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_chest_temp'].interpolate()

df['imu_chest_temp'] = df['imu_chest_temp'].fillna(method='ffill')
print df['imu_chest_temp'].isnull().sum()

result.to_csv('pamap_imuChest_temp.csv')


### imu_chest ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_acc_x_16'].interpolate()
result['y'] = df['imu_chest_acc_y_16'].interpolate()
result['z'] = df['imu_chest_acc_z_16'].interpolate()

df['imu_chest_acc_x_16'] = df['imu_chest_acc_x_16'].fillna(method='ffill')
df['imu_chest_acc_y_16'] = df['imu_chest_acc_y_16'].fillna(method='ffill')
df['imu_chest_acc_z_16'] = df['imu_chest_acc_z_16'].fillna(method='ffill')

print df['imu_chest_acc_x_16'].isnull().sum()
print df['imu_chest_acc_y_16'].isnull().sum()
print df['imu_chest_acc_z_16'].isnull().sum()

result.to_csv('pamap_imuChest_acc.csv')


### imu_chest GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_gyr_x'].interpolate()
result['y'] = df['imu_chest_gyr_y'].interpolate()
result['z'] = df['imu_chest_gyr_z'].interpolate()

df['imu_chest_gyr_x'] = df['imu_chest_gyr_x'].fillna(method='ffill')
df['imu_chest_gyr_y'] = df['imu_chest_gyr_y'].fillna(method='ffill')
df['imu_chest_gyr_z'] = df['imu_chest_gyr_z'].fillna(method='ffill')

print df['imu_chest_gyr_x'].isnull().sum()
print df['imu_chest_gyr_y'].isnull().sum()
print df['imu_chest_gyr_z'].isnull().sum()


result.to_csv('pamap_imuChest_gyr.csv')


### imu_chest MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_mag_x'].interpolate()
result['y'] = df['imu_chest_mag_y'].interpolate()
result['z'] = df['imu_chest_mag_z'].interpolate()

df['imu_chest_mag_x'] = df['imu_chest_mag_x'].fillna(method='ffill')
df['imu_chest_mag_y'] = df['imu_chest_mag_y'].fillna(method='ffill')
df['imu_chest_mag_z'] = df['imu_chest_mag_z'].fillna(method='ffill')

print df['imu_chest_mag_x'].isnull().sum()
print df['imu_chest_mag_y'].isnull().sum()
print df['imu_chest_mag_z'].isnull().sum()


result.to_csv('pamap_imuChest_mag.csv')


# =========== ANKLE ===============


### imu_ankle TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_ankle_temp'].interpolate()

df['imu_ankle_temp'] = df['imu_ankle_temp'].fillna(method='ffill')
print df['imu_ankle_temp'].isnull().sum()

result.to_csv('pamap_imuAnkle_temp.csv')

### imu_ankle ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_acc_x_16'].interpolate()
result['y'] = df['imu_ankle_acc_y_16'].interpolate()
result['z'] = df['imu_ankle_acc_z_16'].interpolate()

df['imu_ankle_acc_x_16'] = df['imu_ankle_acc_x_16'].fillna(method='ffill')
df['imu_ankle_acc_y_16'] = df['imu_ankle_acc_y_16'].fillna(method='ffill')
df['imu_ankle_acc_z_16'] = df['imu_ankle_acc_z_16'].fillna(method='ffill')

print df['imu_ankle_acc_x_16'].isnull().sum()
print df['imu_ankle_acc_y_16'].isnull().sum()
print df['imu_ankle_acc_z_16'].isnull().sum()

result.to_csv('pamap_imuAnkle_acc.csv')


### imu_ankle GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_gyr_x'].interpolate()
result['y'] = df['imu_ankle_gyr_y'].interpolate()
result['z'] = df['imu_ankle_gyr_z'].interpolate()

df['imu_ankle_gyr_x'] = df['imu_ankle_gyr_x'].fillna(method='ffill')
df['imu_ankle_gyr_y'] = df['imu_ankle_gyr_y'].fillna(method='ffill')
df['imu_ankle_gyr_z'] = df['imu_ankle_gyr_z'].fillna(method='ffill')

print df['imu_ankle_gyr_x'].isnull().sum()
print df['imu_ankle_gyr_y'].isnull().sum()
print df['imu_ankle_gyr_z'].isnull().sum()

result.to_csv('pamap_imuAnkle_gyr.csv')


### imu_ankle MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_mag_x'].interpolate()
result['y'] = df['imu_ankle_mag_y'].interpolate()
result['z'] = df['imu_ankle_mag_z'].interpolate()

df['imu_ankle_mag_x'] = df['imu_ankle_mag_x'].fillna(method='ffill')
df['imu_ankle_mag_y'] = df['imu_ankle_mag_y'].fillna(method='ffill')
df['imu_ankle_mag_z'] = df['imu_ankle_mag_z'].fillna(method='ffill')

print df['imu_ankle_mag_x'].isnull().sum()
print df['imu_ankle_mag_y'].isnull().sum()
print df['imu_ankle_mag_z'].isnull().sum()

result.to_csv('pamap_imuAnkle_mag.csv')




# ------------ PREPARE LABELS -----------

result = pd.DataFrame(columns=['label_start','label_end','label'])

actdict =	{
	0: 'other',
	1: 'lying',
	2: 'sitting',
	3: 'standing',
	4: 'walking',
	5: 'running',
	6: 'cycling',
	7: 'nordic_walking',
	9: 'watching_tv',
	10: 'computer_work',
	11: 'car_driving',
	12: 'ascending_stairs',
	13: 'descending_stairs',
	16: 'vacuum_cleaning',
	17: 'ironing',
	18: 'folding_laundry',
	19: 'house_cleaning',
	20: 'playing_soccer',
	24: 'rope_jumping'
}

#init settings
labelFrom = df['timestamp'][0]
currentLabel = actdict[df['activity'][0]]
resultIndex = 0

#process
for i in range(1,len(df)):
	if df['activity'][i] != df['activity'][i-1]:
		#set new row in result dataframe
		result.loc[resultIndex] = [labelFrom, df['timestamp'][i-1], currentLabel]
		#replace settings
		labelFrom = df['timestamp'][i]
		currentLabel = actdict[df['activity'][i]]
		resultIndex = resultIndex + 1


result.to_csv('pamap_labels.csv')




