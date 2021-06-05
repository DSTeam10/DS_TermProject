from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# setting show all col
pd.set_option('display.max_columns', None)

data = pd.read_csv('total dataset_cleaned_edit.csv')

# 열 제거
# T00_ID, T00_DATA_CLASS, T01_EDATE은 scaling 대상에서 제외하기 위해서
data = data.iloc[:,3:]

# cleaning data
# Fill missing values with mean column values in the df
data.fillna(data.mean(), inplace=True)

# change data type from object to float
data = data.apply(pd.to_numeric, errors='coerce').fillna(0)

# feature - 혈액 건강 지표
feature_list = ['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0', 'T01_TCHL', 'T01_HDL']
x = data[['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0',
                  'T01_TCHL', 'T01_HDL']]
# target - drink 에 대한 categorical data (FQ)
target_list = ['T01_DRINK', 'T01_TAKFQ', 'T01_RICEFQ', 'T01_WINEFQ', 'T01_BEERFQ', 'T01_HLIQFQ']

# test data set

# function with robust-scaling and knn
# data, feature, target을 param으로 받아서
# train, test set을 분류하기
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

    # 테스트 셋을 통해 예측한 값
    y_predict = knn.predict(x_test)

    # 정답과 예측 데이터셋의 정확도를 matplotlib으로 표현
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

# target list 에 있는 것들 하나씩 scale_knn의 target으로 주기
for idx, target in enumerate(target_list):
    Scaling_KNN(data, feature_list, target, 'robust', 0.2, 3)
