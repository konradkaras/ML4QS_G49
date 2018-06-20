import pandas as pd
import numpy as np 

df = pd.read_csv('pamap108_sample10.csv')


### HR

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['hr'] = df['hr'].interpolate()

result.to_csv('pamap_hr.csv')


# ================ HAND ===================

### IMU_HAND TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_hand_temp'].interpolate()

result.to_csv('pamap_imuHand_temp.csv')


### IMU_HAND ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_acc_x_16'].interpolate()
result['y'] = df['imu_hand_acc_y_16'].interpolate()
result['z'] = df['imu_hand_acc_z_16'].interpolate()

result.to_csv('pamap_imuHand_acc.csv')


### IMU_HAND GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_gyr_x'].interpolate()
result['y'] = df['imu_hand_gyr_y'].interpolate()
result['z'] = df['imu_hand_gyr_z'].interpolate()

result.to_csv('pamap_imuHand_gyr.csv')


### IMU_HAND MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_hand_mag_x'].interpolate()
result['y'] = df['imu_hand_mag_y'].interpolate()
result['z'] = df['imu_hand_mag_z'].interpolate()

result.to_csv('pamap_imuHand_mag.csv')


# ================ CHEST ===================

### imu_chest TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_chest_temp'].interpolate()

result.to_csv('pamap_imuChest_temp.csv')


### imu_chest ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_acc_x_16'].interpolate()
result['y'] = df['imu_chest_acc_y_16'].interpolate()
result['z'] = df['imu_chest_acc_z_16'].interpolate()

result.to_csv('pamap_imuChest_acc.csv')


### imu_chest GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_gyr_x'].interpolate()
result['y'] = df['imu_chest_gyr_y'].interpolate()
result['z'] = df['imu_chest_gyr_z'].interpolate()

result.to_csv('pamap_imuChest_gyr.csv')


### imu_chest MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_chest_mag_x'].interpolate()
result['y'] = df['imu_chest_mag_y'].interpolate()
result['z'] = df['imu_chest_mag_z'].interpolate()

result.to_csv('pamap_imuChest_mag.csv')


# =========== ANKLE ===============


### imu_ankle TEMPERATURE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['temp'] = df['imu_ankle_temp'].interpolate()

result.to_csv('pamap_imuAnkle_temp.csv')

### imu_ankle ACCELERATION

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_acc_x_16'].interpolate()
result['y'] = df['imu_ankle_acc_y_16'].interpolate()
result['z'] = df['imu_ankle_acc_z_16'].interpolate()

result.to_csv('pamap_imuAnkle_acc.csv')


### imu_ankle GYROSCOPE

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_gyr_x'].interpolate()
result['y'] = df['imu_ankle_gyr_y'].interpolate()
result['z'] = df['imu_ankle_gyr_z'].interpolate()

result.to_csv('pamap_imuAnkle_gyr.csv')


### imu_ankle MAGNETOMETER

result = pd.DataFrame()

result['timestamp'] = df['timestamp']
result['activity'] = df['activity']

result['x'] = df['imu_ankle_mag_x'].interpolate()
result['y'] = df['imu_ankle_mag_y'].interpolate()
result['z'] = df['imu_ankle_mag_z'].interpolate()

result.to_csv('pamap_imuAnkle_mag.csv')