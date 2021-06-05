from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# setting show all col
pd.set_option('display.max_columns', None)

data = pd.read_csv('total dataset_cleaned_edit.csv')

# Remove column
# T00_ID, T00_DATA_CLASS, and T01_EDATE are to be excluded from scaling
data = data.iloc[:,3:]

# cleaning data
# Fill missing values with mean column values in the df
data.fillna(data.mean(), inplace=True)

# Change data type from object to float
data = data.apply(pd.to_numeric, errors='coerce').fillna(0)

# Change drinking level to frequency
data_drink = data.replace({'T01_DRINK': {1: 0, 2: 1, 3: 2}})

# LIB patient data
# Height ~150cm
H140W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_LIB_mean = H140W40_LIB_mean['T01_DRINK'].mean()
H140W50_LIB_mean = H140W50_LIB_mean['T01_DRINK'].mean()
H140W60_LIB_mean = H140W60_LIB_mean['T01_DRINK'].mean()
H140W70_LIB_mean = H140W70_LIB_mean['T01_DRINK'].mean()
H140W80_LIB_mean = H140W80_LIB_mean['T01_DRINK'].mean()

H150W40_LIB_mean = H150W40_LIB_mean['T01_DRINK'].mean()
H150W50_LIB_mean = H150W50_LIB_mean['T01_DRINK'].mean()
H150W60_LIB_mean = H150W60_LIB_mean['T01_DRINK'].mean()
H150W70_LIB_mean = H150W70_LIB_mean['T01_DRINK'].mean()
H150W80_LIB_mean = H150W80_LIB_mean['T01_DRINK'].mean()

H160W40_LIB_mean = H160W40_LIB_mean['T01_DRINK'].mean()
H160W50_LIB_mean = H160W50_LIB_mean['T01_DRINK'].mean()
H160W60_LIB_mean = H160W60_LIB_mean['T01_DRINK'].mean()
H160W70_LIB_mean = H160W70_LIB_mean['T01_DRINK'].mean()
H160W80_LIB_mean = H160W80_LIB_mean['T01_DRINK'].mean()

H170W40_LIB_mean = H170W40_LIB_mean['T01_DRINK'].mean()
H170W50_LIB_mean = H170W50_LIB_mean['T01_DRINK'].mean()
H170W60_LIB_mean = H170W60_LIB_mean['T01_DRINK'].mean()
H170W70_LIB_mean = H170W70_LIB_mean['T01_DRINK'].mean()
H170W80_LIB_mean = H170W80_LIB_mean['T01_DRINK'].mean()

H180W40_LIB_mean = H180W40_LIB_mean['T01_DRINK'].mean()
H180W50_LIB_mean = H180W50_LIB_mean['T01_DRINK'].mean()
H180W60_LIB_mean = H180W60_LIB_mean['T01_DRINK'].mean()
H180W70_LIB_mean = H180W70_LIB_mean['T01_DRINK'].mean()
H180W80_LIB_mean = H180W80_LIB_mean['T01_DRINK'].mean()


# HTN patient data
# Height ~150cm
H140W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                       & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_HTN_mean = H140W40_HTN_mean['T01_DRINK'].mean()
H140W50_HTN_mean = H140W50_HTN_mean['T01_DRINK'].mean()
H140W60_HTN_mean = H140W60_HTN_mean['T01_DRINK'].mean()
H140W70_HTN_mean = H140W70_HTN_mean['T01_DRINK'].mean()
H140W80_HTN_mean = H140W80_HTN_mean['T01_DRINK'].mean()

H150W40_HTN_mean = H150W40_HTN_mean['T01_DRINK'].mean()
H150W50_HTN_mean = H150W50_HTN_mean['T01_DRINK'].mean()
H150W60_HTN_mean = H150W60_HTN_mean['T01_DRINK'].mean()
H150W70_HTN_mean = H150W70_HTN_mean['T01_DRINK'].mean()
H150W80_HTN_mean = H150W80_HTN_mean['T01_DRINK'].mean()

H160W40_HTN_mean = H160W40_HTN_mean['T01_DRINK'].mean()
H160W50_HTN_mean = H160W50_HTN_mean['T01_DRINK'].mean()
H160W60_HTN_mean = H160W60_HTN_mean['T01_DRINK'].mean()
H160W70_HTN_mean = H160W70_HTN_mean['T01_DRINK'].mean()
H160W80_HTN_mean = H160W80_HTN_mean['T01_DRINK'].mean()

H170W40_HTN_mean = H170W40_HTN_mean['T01_DRINK'].mean()
H170W50_HTN_mean = H170W50_HTN_mean['T01_DRINK'].mean()
H170W60_HTN_mean = H170W60_HTN_mean['T01_DRINK'].mean()
H170W70_HTN_mean = H170W70_HTN_mean['T01_DRINK'].mean()
H170W80_HTN_mean = H170W80_HTN_mean['T01_DRINK'].mean()

H180W40_HTN_mean = H180W40_HTN_mean['T01_DRINK'].mean()
H180W50_HTN_mean = H180W50_HTN_mean['T01_DRINK'].mean()
H180W60_HTN_mean = H180W60_HTN_mean['T01_DRINK'].mean()
H180W70_HTN_mean = H180W70_HTN_mean['T01_DRINK'].mean()
H180W80_HTN_mean = H180W80_HTN_mean['T01_DRINK'].mean()

# DM patient data
# Height ~150cm
H140W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_DM_mean = H140W40_DM_mean['T01_DRINK'].mean()
H140W50_DM_mean = H140W50_DM_mean['T01_DRINK'].mean()
H140W60_DM_mean = H140W60_DM_mean['T01_DRINK'].mean()
H140W70_DM_mean = H140W70_DM_mean['T01_DRINK'].mean()
H140W80_DM_mean = H140W80_DM_mean['T01_DRINK'].mean()

H150W40_DM_mean = H150W40_DM_mean['T01_DRINK'].mean()
H150W50_DM_mean = H150W50_DM_mean['T01_DRINK'].mean()
H150W60_DM_mean = H150W60_DM_mean['T01_DRINK'].mean()
H150W70_DM_mean = H150W70_DM_mean['T01_DRINK'].mean()
H150W80_DM_mean = H150W80_DM_mean['T01_DRINK'].mean()

H160W40_DM_mean = H160W40_DM_mean['T01_DRINK'].mean()
H160W50_DM_mean = H160W50_DM_mean['T01_DRINK'].mean()
H160W60_DM_mean = H160W60_DM_mean['T01_DRINK'].mean()
H160W70_DM_mean = H160W70_DM_mean['T01_DRINK'].mean()
H160W80_DM_mean = H160W80_DM_mean['T01_DRINK'].mean()

H170W40_DM_mean = H170W40_DM_mean['T01_DRINK'].mean()
H170W50_DM_mean = H170W50_DM_mean['T01_DRINK'].mean()
H170W60_DM_mean = H170W60_DM_mean['T01_DRINK'].mean()
H170W70_DM_mean = H170W70_DM_mean['T01_DRINK'].mean()
H170W80_DM_mean = H170W80_DM_mean['T01_DRINK'].mean()

H180W40_DM_mean = H180W40_DM_mean['T01_DRINK'].mean()
H180W50_DM_mean = H180W50_DM_mean['T01_DRINK'].mean()
H180W60_DM_mean = H180W60_DM_mean['T01_DRINK'].mean()
H180W70_DM_mean = H180W70_DM_mean['T01_DRINK'].mean()
H180W80_DM_mean = H180W80_DM_mean['T01_DRINK'].mean()

# LIB patient data result
LIB_result = pd.DataFrame(data = { "~150cm" : [H140W40_LIB_mean, H140W50_LIB_mean, H140W60_LIB_mean, H140W70_LIB_mean, H140W80_LIB_mean],
                           "150cm~160cm" : [H150W40_LIB_mean, H150W50_LIB_mean, H150W60_LIB_mean, H150W70_LIB_mean, H150W80_LIB_mean],
                           "160cm~170cm" : [H160W40_LIB_mean, H160W50_LIB_mean, H160W60_LIB_mean, H160W70_LIB_mean, H160W80_LIB_mean],
                           "170cm~180cm" : [H170W40_LIB_mean, H170W50_LIB_mean, H170W60_LIB_mean, H170W70_LIB_mean, H170W80_LIB_mean],
                           "180cm~" : [H180W40_LIB_mean, H180W50_LIB_mean, H180W60_LIB_mean, H180W70_LIB_mean, H180W80_LIB_mean],})
# Missing data process
LIB_result.fillna(0.0, inplace=True)

# Number of drinks per week
LIB_result = LIB_result * 3.5
LIB_result = LIB_result.round(1)

# Indexing
LIB_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

# HTN patient data result
HTN_result = pd.DataFrame(data = { "~150cm" : [H140W40_HTN_mean, H140W50_HTN_mean, H140W60_HTN_mean, H140W70_HTN_mean, H140W80_HTN_mean],
                           "150cm~160cm" : [H150W40_HTN_mean, H150W50_HTN_mean, H150W60_HTN_mean, H150W70_HTN_mean, H150W80_HTN_mean],
                           "160cm~170cm" : [H160W40_HTN_mean, H160W50_HTN_mean, H160W60_HTN_mean, H160W70_HTN_mean, H160W80_HTN_mean],
                           "170cm~180cm" : [H170W40_HTN_mean, H170W50_HTN_mean, H170W60_HTN_mean, H170W70_HTN_mean, H170W80_HTN_mean],
                           "180cm~" : [H180W40_HTN_mean, H180W50_HTN_mean, H180W60_HTN_mean, H180W70_HTN_mean, H180W80_HTN_mean],})
# Missing data process
HTN_result.fillna(0.0, inplace=True)

# Number of drinks per week
HTN_result = HTN_result * 3.5
HTN_result = HTN_result.round(1)

# Indexing
HTN_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

# DM patient data result
DM_result = pd.DataFrame(data = { "~150cm" : [H140W40_DM_mean, H140W50_DM_mean, H140W60_DM_mean, H140W70_DM_mean, H140W80_DM_mean],
                           "150cm~160cm" : [H150W40_DM_mean, H150W50_DM_mean, H150W60_DM_mean, H150W70_DM_mean, H150W80_DM_mean],
                           "160cm~170cm" : [H160W40_DM_mean, H160W50_DM_mean, H160W60_DM_mean, H160W70_DM_mean, H160W80_DM_mean],
                           "170cm~180cm" : [H170W40_DM_mean, H170W50_DM_mean, H170W60_DM_mean, H170W70_DM_mean, H170W80_DM_mean],
                           "180cm~" : [H180W40_DM_mean, H180W50_DM_mean, H180W60_DM_mean, H180W70_DM_mean, H180W80_DM_mean],})
# Missing data process
DM_result.fillna(0.0, inplace=True)

# Number of drinks per week
DM_result = DM_result * 3.5
DM_result = DM_result.round(1)

# Indexing
DM_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

print("<Drinking frequency according to height and weight of LIB patients>\n")
print(LIB_result, "\n")

print("<Drinking frequency according to height and weight of HTN patients>\n")
print(HTN_result, "\n")

print("<Drinking frequency according to height and weight of DM patients>\n")
print(DM_result, "\n")

# feature - Blood health indicators
feature_list = ['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0', 'T01_TCHL', 'T01_HDL']
x = data[['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0',
                  'T01_TCHL', 'T01_HDL']]
# target - Categorical data for drink (FQ)
target_list = ['T01_DRINK', 'T01_TAKFQ', 'T01_RICEFQ', 'T01_WINEFQ', 'T01_BEERFQ', 'T01_HLIQFQ']

# test data set

# function with robust-scaling and knn
# Receive data, feature, target as param
# Classify train and test sets
def Scaling_KNN(data, feature, target, scaling, test_size, n_neighbors):
    x = data[feature]
    y = data[target]

    # Split the dataset into 4/5 training and 1/5 for testing.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

    # ------------------------------------- Scaling ------------------------------------------------
    # robustScaling
    if scaling == 'robust':
        scaler = preprocessing.RobustScaler()
        scaler.fit(x_train)
        robust_scaled_train = scaler.transform(x_train)
        robust_scaled_test = scaler.transform(x_test)

        # numpy to dataframe
        x_train = pd.DataFrame(robust_scaled_train)
        x_test = pd.DataFrame(robust_scaled_test)

    # standardScaling
    elif scaling == 'standard':
        scaler = preprocessing.StandardScaler()
        scaler.fit(x_train)
        standard_scaled_train = scaler.transform(x_train)
        standard_scaled_test = scaler.transform(x_test)

        # numpy to dataframe
        x_train = pd.DataFrame(standard_scaled_train)
        x_test = pd.DataFrame(standard_scaled_test)

    # minmaxScaling
    elif scaling == 'minmax':
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(x_train)
        minmax_scaled_train = scaler.transform(x_train)
        minmax_scaled_test = scaler.transform(x_test)

        # numpy to dataframe
        x_train = pd.DataFrame(minmax_scaled_train)
        x_test = pd.DataFrame(minmax_scaled_test)

    else:
        print("error occur")
        return 0

    # -------------------------------- KNN --------------------------------
    y_train = y_train.astype('int')
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    knn.fit(x_train, y_train)

    # Values predicted by the test set
    y_predict = knn.predict(x_test)

    # Representation of correct answer and prediction data set accuracy in matplotlib
    # plt.scatter(y_test, y_predict, alpha=0.4)
    # plt.xlabel("Actual health_value")
    # plt.ylabel("Predicted health_value")
    # plt.title("KNN")
    # plt.show()

    # print the accuracy
    print("\n" + target)
    print('KNN Accuracy:')
    print('for train set: ', knn.score(x_train, y_train))
    print('for test set: ', np.mean(y_predict == y_test))

    y_predict = pd.DataFrame(y_predict)

# Assign each one in the target list as the target of scale_knn
for idx, target in enumerate(target_list):
    Scaling_KNN(data, feature_list, target, 'robust', 0.2, 3)
